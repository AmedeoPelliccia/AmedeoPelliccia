import numpy as np
import json
from enum import Enum
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Callable, List, Dict, Tuple, Optional

# ==========================================
# 1. DATA STRUCTURES AND STATES
# ==========================================

class AdmissibilityStatus(Enum):
    FULLY_ADMISSIBLE = "FULLY_ADMISSIBLE"
    MIXED_BOUNDARY = "MIXED_BOUNDARY"
    INADMISSIBLE = "INADMISSIBLE"
    CONDITIONAL_PENDING = "CONDITIONAL_PENDING"

@dataclass
class EvidenceGate:
    """Documentary requirement to approve a conditional transition."""
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
# 2. DYNAMIC CONSTRAINTS AND CORE
# ==========================================

class TimeVaryingConstraint:
    """Constraint that evolves over time: g(x, t) <= 0."""
    def __init__(self, name: str, base_fn: Callable[[np.ndarray], float], 
                 evolution_fn: Callable[[float], float] = lambda t: 1.0):
        self.name = name
        self.base_fn = base_fn
        self.evolution_fn = evolution_fn  # By default does not change over time

    def evaluate(self, x: np.ndarray, t: float) -> float:
        return self.base_fn(x) * self.evolution_fn(t)

class InvariantCore:
    """The minimum common denominator (C) with temporal constraints."""
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
        if not isinstance(initial_state, np.ndarray):
            initial_state = np.asarray(initial_state)
        if initial_state.ndim == 0:
            raise ValueError("State must be at least 1-dimensional.")
        self.state = initial_state

# ==========================================
# 3. ADMISSIBLE SPACE AND TRACEABILITY
# ==========================================

class CertifiedAdmissibleSpace:
    """Evaluates admissibility at time t, manages gates and audit log."""
    def __init__(self, fail_closed: bool = True):
        self.fail_closed = fail_closed
        self.evidence_gates: Dict[int, EvidenceGate] = {}
        self.audit_log: List[Dict] = []
        self.current_time: float = 0.0

    def register_gate(self, constraint_idx: int, gate: EvidenceGate):
        """Links the index of a constraint to an evidence requirement."""
        self.evidence_gates[constraint_idx] = gate

    def fulfill_gate(self, constraint_idx: int, uri: str):
        """Fulfill an evidence gate for a given constraint index."""
        if constraint_idx not in self.evidence_gates:
            raise KeyError(f"No evidence gate registered for constraint index {constraint_idx}.")
        self.evidence_gates[constraint_idx].fulfill(uri)

    def step_time(self, delta_t: float):
        self.current_time += delta_t

    def evaluate_state(self, state: np.ndarray, core: InvariantCore) -> Tuple[AdmissibilityStatus, str]:
        """Evaluates the current state and generates the audit log."""
        violations = []
        conditional_gates = []
        ungated_violations = []
        
        for idx, constraint in enumerate(core.constraints):
            # Evaluate the constraint at the current time
            val = constraint.evaluate(state, self.current_time)
            
            if val > 0: # Constraint violated
                violations.append(constraint.name)
                
                # Check if there is a safe-conduct pass (Evidence Gate)
                if idx in self.evidence_gates:
                    gate = self.evidence_gates[idx]
                    if gate.is_fulfilled:
                        conditional_gates.append(f"GATE-{gate.gate_id}: PASSED")
                    else:
                        conditional_gates.append(f"GATE-{gate.gate_id}: PENDING")
                else:
                    ungated_violations.append(constraint.name)
        
        # Resolution logic
        if not violations:
            status = AdmissibilityStatus.FULLY_ADMISSIBLE
            reason = "All constraints satisfied."
        elif self.fail_closed and len(violations) == len(core.constraints) and not conditional_gates:
            status = AdmissibilityStatus.INADMISSIBLE
            reason = f"Fail-Closed: Critical violations in {violations}."
        elif ungated_violations:
            status = AdmissibilityStatus.MIXED_BOUNDARY
            reason = f"Partial violations in {ungated_violations}, no evidence gates available."
        elif conditional_gates and all("PASSED" in g for g in conditional_gates):
            status = AdmissibilityStatus.FULLY_ADMISSIBLE
            reason = "Conditional approval granted via valid evidence gates."
        elif conditional_gates:
            status = AdmissibilityStatus.CONDITIONAL_PENDING
            reason = f"Pending documentation: {conditional_gates}."
        else:
            status = AdmissibilityStatus.MIXED_BOUNDARY
            reason = f"Partial violations in {violations}, no evidence gates available."

        # Register traceability
        self._log_audit(core.sys_id, state, status, reason, violations)
        return status, reason

    def _log_audit(self, sys_id: str, state: np.ndarray, status: AdmissibilityStatus, reason: str, violations: List[str]):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "simulation_time": self.current_time,
            "system_id": sys_id,
            "state_vector": state.tolist(), # Convert numpy array to list for JSON
            "status": status.value,
            "reason": reason,
            "violations": violations
        }
        self.audit_log.append(log_entry)

    # ==========================================
    # 4. JSON SERIALIZATION
    # ==========================================
    def export_audit_log(self, filepath: str = "audit_log.json"):
        try:
            with open(filepath, 'w') as f:
                json.dump(self.audit_log, f, indent=4)
            print(f"[Export] Audit log saved to {filepath}")
        except IOError as e:
            print(f"[Export] Failed to save audit log to {filepath}: {e}")

    def export_evidence_gates(self, filepath: str = "evidence_gates.json"):
        # Serialize the dictionary of Dataclasses to JSON
        gates_dict = {str(idx): asdict(gate) for idx, gate in self.evidence_gates.items()}
        try:
            with open(filepath, 'w') as f:
                json.dump(gates_dict, f, indent=4)
            print(f"[Export] Evidence gates saved to {filepath}")
        except IOError as e:
            print(f"[Export] Failed to save evidence gates to {filepath}: {e}")

# ==========================================
# 5. WILL DYNAMICS
# ==========================================

class VoluntadDynamics:
    """Advances the system toward the projected objective in the admissible space.

    The `objective_gradient` callable must accept the current system state
    (a NumPy array) and return a NumPy array of the *same shape* representing
    the gradient direction.
    """
    def __init__(self, objective_gradient: Callable[[np.ndarray], np.ndarray], space: CertifiedAdmissibleSpace):
        self.grad_J = objective_gradient
        self.space = space
        
    def step(self, system: System, step_size: float = 0.1) -> Tuple[np.ndarray, AdmissibilityStatus]:
        direction = self.grad_J(system.state)
        # Ensure direction is a NumPy array and has the same shape as the state
        if not isinstance(direction, np.ndarray):
            direction = np.asarray(direction)
        if direction.shape != system.state.shape:
            raise ValueError(
                f"objective_gradient must return an array with shape {system.state.shape}, "
                f"but got {direction.shape}."
            )
        proposed_state = system.state + (step_size * direction)
        
        status, _ = self.space.evaluate_state(proposed_state, system.core)
        
        # Only apply the state if it is fully admissible
        if status == AdmissibilityStatus.FULLY_ADMISSIBLE:
            system.state = proposed_state

        # Mark whether the proposed state was actually applied
        if self.space.audit_log:
            self.space.audit_log[-1]["applied"] = (status == AdmissibilityStatus.FULLY_ADMISSIBLE)
            
        return system.state, status

# ==========================================
# QUICK TEST (MAIN)
# ==========================================
if __name__ == "__main__":
    # 1. Configure System
    core = InvariantCore("AERO-EVTOL-1", "EASA", "Urban Air Mobility")
    
    # Dynamic Constraint: Noise limit becomes stricter over time (t)
    # x[0] = Noise (dB). Base limit 80 dB, reduced by 1 dB per simulated "year" (t).
    noise_constraint = TimeVaryingConstraint(
        name="Noise_Limit_CS23",
        base_fn=lambda x: x[0] - 80, 
        evolution_fn=lambda t: 1.0 - (0.0125 * t) 
    )
    core.add_constraint(noise_constraint)
    
    sys = System(core)
    sys.set_state(np.array([79.0])) # Starts at 79 dB (Admissible at t=0)

    # 2. Configure Space and Gates
    space = CertifiedAdmissibleSpace(fail_closed=True)
    
    # Add a Gate to constraint 0 (Noise) to allow exceeding the limit
    # if an acoustic mitigation report is presented.
    gate = EvidenceGate("G-NOISE-01", "Acoustic Mitigation Report", "AMC-20", 6)
    space.register_gate(0, gate)
    
    dynamics = VoluntadDynamics(lambda x: np.array([0.5]), space) # Tendency to increase noise

    # 3. Simulation
    print(f"Initial State: {sys.state[0]} dB")
    for year in range(3):
        space.step_time(1.0) # Advance 1 year
        new_state, status = dynamics.step(sys, step_size=1.0)
        print(f"Year {year+1} | State: {new_state[0]:.1f} dB | Status: {status.value}")
        
        # In year 2, upload evidence to unlock the constraint
        if year == 1:
            print(">>> Uploading documentary evidence...")
            space.fulfill_gate(0, "uri://dpp/reports/acoustics_v1.pdf")

    # 4. Export
    space.export_audit_log()
    space.export_evidence_gates()
