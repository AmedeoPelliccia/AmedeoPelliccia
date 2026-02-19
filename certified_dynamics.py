import numpy as np
import json
from enum import Enum, auto
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Callable, List, Dict, Tuple, Optional

# ==========================================
# 1. ESTRUCTURAS DE DATOS Y ESTADOS
# ==========================================

class AdmissibilityStatus(Enum):
    FULLY_ADMISSIBLE = "FULLY_ADMISSIBLE"
    MIXED_BOUNDARY = "MIXED_BOUNDARY"
    INADMISSIBLE = "INADMISSIBLE"
    CONDITIONAL_PENDING = "CONDITIONAL_PENDING"

@dataclass
class EvidenceGate:
    """Requisito documental para aprobar una transición condicional."""
    gate_id: str
    description: str
    standard_ref: str
    required_trl: int
    is_fulfilled: bool = False
    evidence_uri: Optional[str] = None
    timestamp: Optional[str] = None
    
    def fulfill(self, uri: str):
        self.is_fulfilled = True
        self.evidence_uri = uri
        self.timestamp = datetime.now().isoformat()

# ==========================================
# 2. RESTRICCIONES DINÁMICAS Y NÚCLEO
# ==========================================

class TimeVaryingConstraint:
    """Restricción que evoluciona con el tiempo: g(x, t) <= 0."""
    def __init__(self, name: str, base_fn: Callable[[np.ndarray], float], 
                 evolution_fn: Callable[[float], float] = lambda t: 1.0):
        self.name = name
        self.base_fn = base_fn
        self.evolution_fn = evolution_fn  # Por defecto no cambia en el tiempo

    def evaluate(self, x: np.ndarray, t: float) -> float:
        return self.base_fn(x) * self.evolution_fn(t)

class InvariantCore:
    """El denominador común mínimo (C) con restricciones temporales."""
    def __init__(self, sys_id: str, authority: str, purpose: str):
        self.sys_id = sys_id
        self.authority = authority
        self.purpose = purpose
        self.constraints: List[TimeVaryingConstraint] = []

    def add_constraint(self, constraint: TimeVaryingConstraint):
        self.constraints.append(constraint)

class System:
    """M_i = C ⊕ E_i"""
    def __init__(self, core: InvariantCore):
        self.core = core
        self.state: np.ndarray = np.zeros(0)

    def set_state(self, initial_state: np.ndarray):
        self.state = initial_state

# ==========================================
# 3. ESPACIO ADMISIBLE Y TRAZABILIDAD
# ==========================================

class CertifiedAdmissibleSpace:
    """Evalúa la admisibilidad en el tiempo t, gestiona gates y log de auditoría."""
    def __init__(self, fail_closed: bool = True):
        self.fail_closed = fail_closed
        self.evidence_gates: Dict[int, EvidenceGate] = {}
        self.audit_log: List[Dict] = []
        self.current_time: float = 0.0

    def register_gate(self, constraint_idx: int, gate: EvidenceGate):
        """Vincula el índice de una restricción a un requisito de evidencia."""
        self.evidence_gates[constraint_idx] = gate

    def step_time(self, delta_t: float):
        self.current_time += delta_t

    def evaluate_state(self, state: np.ndarray, core: InvariantCore) -> Tuple[AdmissibilityStatus, str]:
        """Evalúa el estado actual y genera el registro de auditoría."""
        violations = []
        conditional_gates = []
        
        for idx, constraint in enumerate(core.constraints):
            # Evaluamos la restricción en el tiempo actual
            val = constraint.evaluate(state, self.current_time)
            
            if val > 0: # Restricción violada
                violations.append(constraint.name)
                
                # Comprobar si hay un salvoconducto (Evidence Gate)
                if idx in self.evidence_gates:
                    gate = self.evidence_gates[idx]
                    if gate.is_fulfilled:
                        conditional_gates.append(f"GATE-{gate.gate_id}: PASSED")
                    else:
                        conditional_gates.append(f"GATE-{gate.gate_id}: PENDING")
        
        # Lógica de resolución
        if not violations:
            status = AdmissibilityStatus.FULLY_ADMISSIBLE
            reason = "All constraints satisfied."
        elif self.fail_closed and len(violations) == len(core.constraints) and not conditional_gates:
            status = AdmissibilityStatus.INADMISSIBLE
            reason = f"Fail-Closed: Critical violations in {violations}."
        elif conditional_gates and all("PASSED" in g for g in conditional_gates):
            status = AdmissibilityStatus.FULLY_ADMISSIBLE
            reason = "Conditional approval granted via valid evidence gates."
        elif conditional_gates:
            status = AdmissibilityStatus.CONDITIONAL_PENDING
            reason = f"Pending documentation: {conditional_gates}."
        else:
            status = AdmissibilityStatus.MIXED_BOUNDARY
            reason = f"Partial violations in {violations}, no evidence gates available."

        # Registrar trazabilidad
        self._log_audit(core.sys_id, state, status, reason, violations)
        return status, reason

    def _log_audit(self, sys_id: str, state: np.ndarray, status: AdmissibilityStatus, reason: str, violations: List[str]):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "simulation_time": self.current_time,
            "system_id": sys_id,
            "state_vector": state.tolist(), # Convertimos numpy a lista para JSON
            "status": status.value,
            "reason": reason,
            "violations": violations
        }
        self.audit_log.append(log_entry)

    # ==========================================
    # 4. SERIALIZACIÓN JSON
    # ==========================================
    def export_audit_log(self, filepath: str = "audit_log.json"):
        with open(filepath, 'w') as f:
            json.dump(self.audit_log, f, indent=4)
        print(f"[Export] Audit log saved to {filepath}")

    def export_evidence_gates(self, filepath: str = "evidence_gates.json"):
        # Serializa el diccionario de Dataclasses a JSON
        gates_dict = {str(idx): asdict(gate) for idx, gate in self.evidence_gates.items()}
        with open(filepath, 'w') as f:
            json.dump(gates_dict, f, indent=4)
        print(f"[Export] Evidence gates saved to {filepath}")

# ==========================================
# 5. DINÁMICA DE LA VOLUNTAD
# ==========================================

class VoluntadDynamics:
    """Avanza el sistema hacia el objetivo proyectado en el espacio admisible."""
    def __init__(self, objective_gradient: Callable[[np.ndarray], np.ndarray], space: CertifiedAdmissibleSpace):
        self.grad_J = objective_gradient
        self.space = space
        
    def step(self, system: System, step_size: float = 0.1) -> Tuple[np.ndarray, AdmissibilityStatus]:
        direction = self.grad_J(system.state)
        proposed_state = system.state + (step_size * direction)
        
        status, _ = self.space.evaluate_state(proposed_state, system.core)
        
        # Solo aplicamos el estado si es totalmente admisible
        if status == AdmissibilityStatus.FULLY_ADMISSIBLE:
            system.state = proposed_state
            
        return system.state, status

# ==========================================
# PRUEBA RÁPIDA (MAIN)
# ==========================================
if __name__ == "__main__":
    # 1. Configurar Sistema
    core = InvariantCore("AERO-EVTOL-1", "EASA", "Urban Air Mobility")
    
    # Restricción Dinámica: Límite de ruido se vuelve más estricto con el tiempo (t)
    # x[0] = Ruido (dB). Límite base 80 dB, se reduce 1 dB por cada "año" (t) simulado.
    noise_constraint = TimeVaryingConstraint(
        name="Noise_Limit_CS23",
        base_fn=lambda x: x[0] - 80, 
        evolution_fn=lambda t: 1.0 - (0.0125 * t) 
    )
    core.add_constraint(noise_constraint)
    
    sys = System(core)
    sys.set_state(np.array([79.0])) # Inicia en 79 dB (Admisible en t=0)

    # 2. Configurar Espacio y Gates
    space = CertifiedAdmissibleSpace(fail_closed=True)
    
    # Añadimos un Gate a la restricción 0 (Ruido) para permitir exceder el límite 
    # si se presenta un informe de mitigación acústica.
    gate = EvidenceGate("G-NOISE-01", "Acoustic Mitigation Report", "AMC-20", 6)
    space.register_gate(0, gate)
    
    dynamics = VoluntadDynamics(lambda x: np.array([0.5]), space) # Tendencia a aumentar ruido

    # 3. Simulación
    print(f"Estado Inicial: {sys.state[0]} dB")
    for year in range(3):
        space.step_time(1.0) # Avanza 1 año
        new_state, status = dynamics.step(sys, step_size=1.0)
        print(f"Año {year+1} | Estado: {new_state[0]:.1f} dB | Status: {status.value}")
        
        # En el año 2, subimos la evidencia para desbloquear la restricción
        if year == 1:
            print(">>> Subiendo evidencia documental...")
            space.evidence_gates[0].fulfill("uri://dpp/reports/acoustics_v1.pdf")

    # 4. Exportar
    space.export_audit_log()
    space.export_evidence_gates()
