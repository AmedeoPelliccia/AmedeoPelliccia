# Una correlación disciplinada entre teoría de la información y cosmología del Big Bang

**Versión:** v0.5 — *Borrador para discusión*  
*(Refina y reemplaza la cadena `BIT → BOT → NEURONAL BOOM` de las versiones v0.1–v0.2; consolida la corrección de fundamentos de v0.3; añade estructura académica formal en v0.5.)*

**Cambios v0.4 → v0.5 (adiciones estructurales para rigor académico):**
- **Resumen conciso y Abstract bilingüe.** Se incorporan al inicio un Resumen en español y un Abstract en inglés, más breves y orientados a publicación.
- **Introducción ampliada con estado del arte (§1.1).** Se añade una revisión contextualizada de la literatura relevante (Wheeler «it from bit», programa «It from Qubit», decoherencia en cosmología cuántica, formalismo de Page–Wootters, Hipótesis de la Curvatura de Weyl de Penrose) para situar la contribución del documento.
- **Explicitación del blanco (§1.3).** Se define con precisión el objetivo central («blanco») del trabajo: la articulación y defensa disciplinada de la cadena QUBIT₀ → Q-BOT₁ → BITᵢ → QRN como marco conceptual corregido, ontológicamente riguroso y físicamente anclado.
- El cuerpo principal (hipótesis, formalización matemática, secciones filosóficas y apéndices) permanece intacto respecto a la v0.4, salvo ajustes menores de numeración y flujo.

**Cambios v0.3 → v0.4 (cierre del agujero del sistema cerrado):**
- **Auto-decoherencia (§4.4 bis).** Se resuelve cómo decohere un universo *sin afuera*: el estado global, puro y unitario, se factoriza internamente; unos grados de libertad hacen de «sistema» y el resto de «entorno». La flecha Q-BOT → BIT pasa a ser **auto-inducida**.
- **Sección-espina (§4.8) «El universo auto-referencial».** Tres emergencias internas de una sola raíz —clasicidad (auto-decoherencia), tiempo (entrelazamiento, Page–Wootters), hechos/causalidad (partición de la QRN)—. *Nada viene de fuera porque no hay afuera.*
- **Residuo honesto (§7).** El problema de la medida se afina y se añade el de la **factorización preferente** (mereología cuántica, Carroll & Singh); se hace explícito el compromiso hacia unitariedad global / Everett.
- **Rovelli como resonancia (Apéndice B).** Se reconoce la afinidad con la Mecánica Cuántica Relacional **sin adoptar** su tesis de «no hay hechos absolutos»: la QRN conserva un estado global puro que se auto-decoherencia.

**Cambios v0.2 → v0.3 (corrección de fundamentos):**
- **El bit deja de ser el origen.** La cadena se reordena a `QUBIT₀ → Q-BOT₁ → BITᵢ → QRN`. El operador (Q-BOT) **no** aparece después del bit clásico: la dinámica cuántica opera *antes* de que exista un solo bit registrable. El bit es el **primer residuo clásico** de una ejecución cuántica anterior.
- **Cada flecha es ahora una transición física nombrada**, no un mero «y luego»: activación endógena → auto-decoherencia → acumulación de correlaciones.
- **Guardarraíl:** los índices `₀ / ₁ / ᵢ` son **niveles de dependencia, no instantes**. Los cuatro nodos **coexisten**.
- **`QRN` (Quantum Relational Network) sustituye a `NEURONAL BOOM` / `QNN`.** Se evita «neural» porque, en uso técnico, una *Quantum Neural Network* es un objeto **funcional** que entrena y computa; `QRN` afirma sólo lo defendible: una **red relacional**, no una mente que aprende. La versión funcional queda remitida a QCSAA (§7).

**Convención terminológica (vinculante para el repositorio formal).**
- Término fijado: **partición asimétrica de grados de libertad** (la asimetría está en la *partición*, no en el entrelazamiento — para un estado global puro, \( S(\rho_A)=S(\rho_B) \) por la descomposición de Schmidt). Admitido también: *causalidad emergente intra-sistema*.
- Términos **prohibidos** en el texto formal por reintroducir teleología o interioridad psíquica: «supervivencia», «subconsciente», «voluntad», «propósito», y todo antropomorfismo equivalente aplicado al estado primordial. El universo primordial no «quiere» nada: obedece a entrelazamiento y termodinámica cuántica. *(Estas imágenes pueden usarse en divulgación oral, donde el tono señala la metáfora; no en el documento citable.)*

**Estado epistémico:** documento de trabajo. Mezcla deliberadamente tres registros —física establecida, interpretación abierta y metáfora estructural— y los marca como tales en cada punto.

**Lengua:** español (con anclajes notacionales estándar).

---

## Resumen

Se propone una lectura del origen cósmico como la activación endógena de un potencial cuántico, formalizada en la cadena corregida **QUBIT₀ → Q-BOT₁ → BITᵢ → QRN**. El estado primordial no es un bit clásico ni un estado de información o superposición máximas, sino un qubit de **máxima simetría y máxima pureza** (entropía de von Neumann \( S \approx 0 \)), lo que equivale a mínima información diferenciada y máximo potencial de diferenciación. La dinámica cuántica (Q-BOT) opera *antes* de que emerjan, por auto-decoherencia interna, los primeros registros clásicos (BIT); la acumulación de correlaciones produce una red relacional cuántica (QRN). Se enuncian nueve hipótesis, se ofrece formalización matemática por niveles y se identifican cuestiones abiertas, destacando el problema de la factorización preferente. El marco integra resultados establecidos de la decoherencia en cosmología cuántica, el principio de Landauer, la hipótesis de baja entropía inicial de Penrose y el tiempo emergente de Page–Wootters, bajo un compromiso explícito con la unitariedad global del estado cuántico.

## Abstract

This paper proposes reading the cosmic origin as the endogenous activation of a quantum potential, formalized through the corrected chain **QUBIT₀ → Q-BOT₁ → BITᵢ → QRN**. The primordial state is not a classical bit nor a state of maximal information or superposition, but a qubit of **maximal symmetry and maximal purity** (von Neumann entropy \( S \approx 0 \)), equivalent to minimal differentiated information and maximal differentiation potential. Quantum dynamics (Q-BOT) operates *prior* to the emergence, via internal self-decoherence, of the first classical records (BIT); the accumulation of correlations yields a quantum relational network (QRN). Nine hypotheses are stated, a multi-level mathematical formalization is provided, and open questions are identified, notably the preferred factorization problem. The framework integrates established results from decoherence in quantum cosmology, Landauer’s principle, Penrose’s low-entropy initial condition hypothesis, and Page–Wootters emergent time, under an explicit commitment to global unitarity of the quantum state.

---

## 0. Resumen extendido (contenido original v0.4)

Se propone leer el origen cósmico no como una *explosión de información* sino como la **activación de un potencial**: el paso de un estado puro a una dinámica que se ejecuta, y de ahí a registros clásicos y a una red de relaciones. La cadena corregida `QUBIT₀ → Q-BOT₁ → BITᵢ → QRN` nombra ese tránsito —sustrato cuántico → operador → dato emergente → red relacional— y su frase doctrinal, en su forma definitiva, es:

> **El universo no comienza como un bit clásico, sino como un qubit primordial: un estado cuántico puro, simétrico y todavía no diferenciado. La dinámica interna de ese estado actúa como Q-BOT generativo; por decoherencia emergen bits clásicos, y la acumulación de registros, correlaciones y estructuras produce una QRN cosmológica —una red causal-relacional cuántica, no una mente literal—. El bit ya no es el origen: el bit es el primer residuo clásico de una ejecución cuántica anterior.**

El documento defiende que la intuición de fondo es correcta *si y sólo si* se corrigen dos errores recurrentes. **Primero**, el estado primordial **no** es de información máxima ni de superposición máxima, sino de **máxima simetría y máxima pureza** —lo que equivale, por definición, a **mínima información diferenciada**—; lo que sí es máximo al inicio es el **potencial de diferenciación** (el hueco entrópico disponible). **Segundo**, el **orden causal** no es `bit → operador`: la dinámica cuántica precede al dato clásico, que emerge río abajo por decoherencia. Sobre esa base se formulan nueve hipótesis, se ofrece una formalización matemática por niveles, se profundiza el significado filosófico y científico, y se abre una lista de cuestiones para discusión.

---

## 1. Introducción

### 1.1 Estado del arte

La noción de que la realidad física posee un fundamento informacional tiene su formulación clásica en la propuesta de John Archibald Wheeler (1989, 1990). Wheeler sintetizó su visión en la máxima «*it from bit*»: todo ente físico («*it*») deriva en última instancia de respuestas a preguntas sí/no («*bit*»), en un universo participativo donde la observación y el registro desempeñan un papel ontológico constitutivo. Esta idea influyó profundamente en la teoría de la información cuántica, la mecánica cuántica relacional y los enfoques holográficos de la gravedad cuántica. Sin embargo, el marco wheeleriano ha sido objeto de revisiones sustantivas. El programa de investigación «*It from Qubit*» —impulsado, entre otras iniciativas, por la Simons Collaboration on Quantum Fields, Gravity and Information (desde 2015)— enfatiza que el sustrato primordial es cuántico: los *qubits*, y no los bits clásicos, constituyen la base desde la cual emergen el espaciotiempo, las partículas y la geometría (D’Ariano y colaboradores; Harlow, Hayden y equipo). En este enfoque, la información cuántica no es mera descripción, sino herramienta heurística para abordar problemas de gravedad cuántica, agujeros negros y el origen del universo.

En el dominio específico de la cosmología cuántica, la transición desde estados cuánticos puros hacia la apariencia de clasicidad se explica fundamentalmente mediante la **decoherencia**. Los trabajos seminales de Wojciech Zurek sobre einselección y estados puntero, de Claus Kiefer sobre la decoherencia del factor de escala cósmico por acoplamiento a modos inhomogéneos, y de Murray Gell-Mann y James Hartle sobre historias decoherentes, establecen que la clasicidad emerge de interacciones internas sin requerir un observador o entorno externo privilegiado. La noción de **auto-decoherencia** en un universo cerrado —donde la partición «sistema/entorno» se realiza internamente sobre grados de libertad del propio estado global— constituye un desarrollo activo y central para cualquier modelo que aspire a ser consistente con la unitariedad global.

El problema del tiempo en la gravedad cuántica canónica, expresado en la ecuación de Wheeler–DeWitt (\(\hat{H}\Psi = 0\)), ha generado el formalismo de **Page–Wootters** (1983). Según este, el tiempo no es un parámetro externo sino una propiedad relacional que emerge del entrelazamiento entre un subsistema-reloj y el resto del universo; las evoluciones condicionadas recuperan la ecuación de Schrödinger a pesar de la estacionariedad del estado global. Reinterpretaciones gauge-teóricas recientes y experimentos con sistemas entrelazados (por ejemplo, pares de fotones) han aportado apoyo adicional a la idea de un tiempo emergente y relacional.

Por último, la condición de **baja entropía inicial** —requisito indispensable para la existencia de una flecha termodinámica— fue formalizada por Roger Penrose en la **Hipótesis de la Curvatura de Weyl** (1979). Penrose argumenta que el tensor de Weyl debe anularse (o ser extremadamente pequeño) en la singularidad inicial del Big Bang, de modo que la entropía gravitacional sea mínima a pesar de la aparente homogeneidad térmica. Esta hipótesis explica por qué el universo temprano es «especial» y permite la posterior formación de estructura compleja; ha sido extendida al régimen cuántico vinculándola con el vacío adiabático en espacios casi de Sitter.

El presente documento se inscribe en esta tradición consolidada, pero introduce correcciones específicas de orden causal, ontológico y terminológico que lo distinguen de formulaciones previas. En particular, rechaza tanto la primacía del bit clásico como la atribución de «máxima información» al estado inicial, y propone en su lugar una cadena disciplinada que antepone el sustrato cuántico y su dinámica endógena a cualquier registro clásico. La contribución no consiste en postular nuevos mecanismos físicos, sino en articular de manera rigurosa y coherente resultados ya establecidos bajo una única estructura conceptual: la cadena QUBIT₀ → Q-BOT₁ → BITᵢ → QRN.

### 1.2 Qué acierta la intuición y qué dos piedras hay que esquivar

La intuición original —`estado → operador → red`— captura algo real, y conviene decir exactamente *qué*.

Lo que acierta es la **articulación entre estado y dinámica**: la diferencia entre lo que *es el caso* (una configuración) y la *regla* que lo transforma. No es retórica; es una distinción ontológica genuina. Pero la versión primitiva la formulaba como `bit → bot`, y ahí cometía un error de orden que este documento corrige: situaba el operador *después* del bit clásico. El orden correcto antepone el sustrato cuántico y su dinámica al dato clásico (§2c, §4.7). La articulación verdadera es **cuádruple**: sustrato cuántico (QUBIT), operador cuántico (Q-BOT), registro clásico emergente (BIT), red relacional (QRN).

**Primera piedra: la palabra «máxima».** Cada vez que se la coloca junto a «información» o «superposición», migra hacia el extremo equivocado de la flecha del tiempo. Un estado de información máxima —o una superposición máximamente extendida sobre un número enorme de configuraciones— **no** es un comienzo prístino: es un estado **térmico, máximamente mezclado, de entropía máxima**. Es decir, la **muerte térmica**. El final, no el principio. La corrección que sostiene todo el edificio se enuncia en una línea:

$$\text{máxima simetría} \;=\; \text{máxima pureza} \;=\; \text{mínima información diferenciada}.$$

No son magnitudes en tensión: son **la misma cosa vista de dos lados**. Un estado perfectamente simétrico no tiene rasgos que registrar; por eso es, *a la vez*, pobre en información y bajo en entropía. La «máxima» que la intuición busca existe —pero se llama máxima *simetría*, no máxima *información*.

**Segunda piedra: el bit como origen.** Es el error que da nombre a esta versión. El bit clásico —el hecho definido, registrable, almacenable— no está al principio; **emerge**. Antes de que haya un solo registro ya hay dinámica cuántica operando. Poner el bit primero invierte la causalidad. El origen es un **qubit**, y su dinámica (el Q-BOT) corre *antes* de producir el primer dato.

### 1.3 El blanco de este trabajo

El **blanco** —es decir, el objetivo principal y el foco disciplinario— de este documento es articular, formalizar y defender la cadena conceptual **QUBIT₀ → Q-BOT₁ → BITᵢ → QRN** como el marco más preciso, ontológicamente coherente y físicamente anclado disponible para describir el tránsito desde el estado primordial cuántico hasta la emergencia de clasicidad, tiempo y orden causal en un universo cerrado y auto-referencial.

Este blanco implica tres compromisos explícitos:

1. **Corrección del orden causal**: la dinámica cuántica (Q-BOT) precede y genera los registros clásicos (BIT); el bit no es el origen, sino el primer residuo clásico de una ejecución cuántica anterior.
2. **Rechazo de superlativos mal ubicados**: el estado inicial se caracteriza por máxima simetría y pureza (mínima información diferenciada), no por máxima información o máxima superposición (que corresponden al régimen térmico final).
3. **Prudencia interpretativa**: la red resultante se denomina **QRN** (Quantum *Relational* Network) —topología de correlaciones causales— y no se le atribuye sin justificación adicional el carácter funcional de una Quantum Neural Network (QNN) que computa o aprende. La versión funcional queda remitida a investigaciones específicas de agencia sentiente.

El documento no aspira a resolver el problema de la medida ni a derivar la factorización preferente; aspira a ofrecer un marco conceptual riguroso, libre de teleología y antropomorfismo, que integre de manera coherente la física establecida de la decoherencia, la termodinámica de la información y la gravedad cuántica canónica, y que identifique con honestidad los residuos que permanecen abiertos.

---

## 2. El reencuadre fundacional

Tres reencuadres convierten la intuición en una hipótesis discutible en lugar de una afirmación físicamente excesiva.

**(a) El comienzo es pobre en datos, no rico.** «Compresión máxima» significa *descripción corta*. Un estado liso, homogéneo y simétrico se especifica con poquísimos parámetros. El universo arranca **pobre de información y rico de reglas**; la complejidad no está escrita en la condición inicial, se *genera* a partir del operador.

**(b) Lo uniforme es lo raro (Penrose).** En cuanto la gravedad entra en juego, la intuición termodinámica ordinaria se invierte. Un plasma caliente y homogéneo *parece* desordenado, pero **gravitacionalmente es un estado de baja entropía**, porque la gravedad «quiere» agrumar: la suavidad inicial es la condición especial e improbable. Esta es la *Hipótesis de la Curvatura de Weyl* de Penrose: el pasado bajo en entropía no es un accidente menor, es la dotación que hace posible toda la historia posterior.

**(c) El sustrato es cuántico, y la dinámica precede al dato (it from qubit).** La formulación de Wheeler —*it from bit*, todo deriva de respuestas sí/no— se corrige hoy a **it from qubit**: el sustrato es cuántico. Y aquí está la corrección de orden que define la v0.3. La cadena no es `bit → operador`; es:

$$\text{QUBIT (sustrato)} \;\to\; \text{Q-BOT (dinámica)} \;\to\; \text{BIT (registro)} \;\to\; \text{QRN (red)}.$$

El **bit clásico no está al principio: emerge** por decoherencia, y antes de que exista hace falta que el operador cuántico ya esté corriendo sobre el estado puro. La dinámica es **primaria**; el dato clásico aparece **río abajo**. Dicho en una línea: *el bit es el primer residuo clásico de una ejecución cuántica anterior.*

---

## 3. Formulación de hipótesis

Se enuncian como proposiciones, marcando para cada una su grado de compromiso.

**H1 — Estado primordial como máxima simetría, no máxima información.**  
El estado inicial (QUBIT₀) es de máxima simetría y máxima pureza (entropía de von Neumann \( S \approx 0 \)), lo que equivale a *mínima* información diferenciada. La «compresión» del origen es pobreza de datos, no abundancia.  
*Compromiso: físico estándar (lectura de baja entropía inicial).*

**H2 — Primacía del operador sobre el dato.**  
La riqueza del universo no reside en la información del estado inicial sino en las leyes dinámicas (el Q-BOT). La complejidad se genera, no se almacena. En su forma fuerte (§4.6 bis): el potencial de diferenciación es propiedad del **par** \((\Psi_0,\hat{O})\), no del estado solo — sin operador no trivial, la simetría no diferencia nada.  
*Compromiso: físico estándar, con lectura informacional.*

**H3 — Orden causal corregido: qubit y dinámica antes que bit (it from qubit).**  
La unidad primordial es un grado de libertad **cuántico** (QUBIT₀), no un bit clásico. Su **dinámica** (Q-BOT₁) opera *antes* de que exista cualquier registro. Los **bits clásicos** (BITᵢ) **emergen** por decoherencia, río abajo. Corolario doctrinal: *el bit no es el origen, sino el primer residuo clásico de una ejecución cuántica anterior.*  
*Compromiso: interpretación bien apoyada (decoherencia + cosmología inflacionaria).*

**H4 — Activación endógena, sin input externo.**  
La transición potencial → ejecución (QUBIT → Q-BOT) no requiere agente externo. La inestabilidad es intrínseca: la incertidumbre cuántica impide que un estado «se quede quieto», y la ruptura es espontánea. El operador no se *carga* desde fuera; está latente y se activa por sí mismo.  
*Compromiso: físico estándar (ruptura espontánea de simetría, fluctuación de vacío).*

**H5 — Diferenciación sin selección.**  
El paso a la multiplicidad de hechos clásicos (Q-BOT → BIT) ocurre por **decoherencia** —pérdida de coherencia mutua entre ramas, cada una con registros autoconsistentes— y **no** por selección o proyección de una rama. No hace falta árbitro.  
*Compromiso: la decoherencia es física establecida; «sin selección» es elección interpretativa (ver §6 y §7).*

**H6 — Ejecución = flecha del tiempo, con presupuesto.**  
«Ejectuar» información es un proceso físico (principio de Landauer). La ejecución cósmica —formación de registros, decoherencia, formación de estructura— **es** aumento de entropía y, por tanto, **es** la flecha del tiempo, costeada por la baja entropía inicial de H1.  
*Compromiso: Landauer es físico estándar; su identificación con «la flecha del tiempo cósmica» es lectura razonada.*

**H7 — Tiempo emergente.**  
En el nivel más fundamental (ecuación de Wheeler–DeWitt, \(\hat{H}\Psi = 0\)) el estado es **atemporal**. El tiempo no es el escenario donde el operador se ejecuta; **emerge con la ejecución**, de las correlaciones internas del estado.  
*Compromiso: marco teórico serio pero no confirmado experimentalmente.*

**H8 — Complejidad transitoria.**  
La complejidad es no-monótona: mínima al inicio (simetría), mínima al final (muerte térmica), **máxima en el intervalo intermedio**. La QRN cósmica es una **fase**, no un destino; el operador corre cuesta abajo y agota su combustible.  
*Compromiso: cualitativamente robusto; depende de una definición rigurosa de «complejidad».*

**H9 — Umbral de agencia: QRN (relacional) frente a QNN (funcional).**  
Llamar a la red cósmica una **red relacional** (QRN) es defendible: nombra una topología de nodos, filamentos y correlaciones causales. Llamarla **red neuronal** (QNN, en su sentido técnico) es un compromiso mayor y no ganado, porque una *Quantum Neural Network* es un objeto **funcional** —entrena parámetros, optimiza una pérdida, **aprende**—. Afirmar que el cosmos *computa* o *aprende* cruza de la metáfora a una tesis fuerte. Este documento se queda en QRN; la versión QNN-funcional se remite a su territorio propio (§7).  
*Compromiso: la versión relacional (QRN) es lícita; la versión neural-funcional (QNN) es especulativa y debe declararse como tal.*

---

## 4. Formalización matemática (por niveles)

> **Advertencia de honestidad.** No existe un único formalismo unificado del origen cósmico. Lo que sigue son piezas reales que viven en **niveles distintos** y no encajan todavía en una sola ecuación. Se presentan ordenadas, no soldadas.

### 4.1 El estado primordial QUBIT₀: \(\Psi_0[\Phi]\)

El estado fundamental de un campo cuántico no es una configuración definida, sino una **superposición** sobre todas las configuraciones del campo \(\Phi\). Para un campo libre es una funcional gaussiana:

$$\Psi_0[\Phi] \;\propto\; \exp\!\left(-\tfrac{1}{2}\int \Phi(\mathbf{x})\,K(\mathbf{x},\mathbf{y})\,\Phi(\mathbf{y})\;d\mathbf{x}\,d\mathbf{y}\right).$$

Punto clave: \(\Psi_0\) es el estado de **mínima incertidumbre** —el más quieto, coherente y simétrico posible—. Por eso H1 no es una paradoja: el estado más «extendido» en sentido de simetría es el más *pobre* en información diferenciada.

**Matiz conceptual decisivo.** *Potencial* ≠ *superposición*. El estado \(\Psi_0\) está **completamente definido** —no tiene nada de potencial—. Lo que está *en potencia* no es el estado cuántico, son los **desenlaces clásicos**: los hechos definidos aún no existen porque aún no hay base preferida ni ha corrido la decoherencia. \(\Psi_0\) es actual y pleno; lo pendiente son las **ramas clásicas** (los futuros BITᵢ) que de él se diferenciarán.

### 4.2 Pureza y entropía: por qué «mínima información»

La entropía de von Neumann de un estado \(\rho\):

$$S(\rho) = -k_B \,\mathrm{Tr}\!\left(\rho \ln \rho\right).$$

- Estado **puro** (como \(\rho_0 = |\Psi_0\rangle\langle\Psi_0|\)): \(S = 0\). Máxima pureza, mínima información diferenciada.
- Estado **máximamente mezclado**: \(S = S_{\max}\). Esto es lo térmico, lo de equilibrio — **el final, no el principio**.

Aquí se cierra el círculo de §1–§2: «máxima superposición repartida» \(\Rightarrow\) máximamente mezclado \(\Rightarrow\) entropía máxima \(\Rightarrow\) muerte térmica. El comienzo es lo contrario: \(S \to 0\).

### 4.3 Atemporalidad: la ecuación de Wheeler–DeWitt

Para la «función de onda del universo» \(\Psi\) —funcional de la 3-geometría \(h_{ij}\) y los campos \(\phi\), en el espíritu de la propuesta sin frontera de Hartle–Hawking, \(\Psi[h_{ij}, \phi]\)— la dinámica cuántica de la gravedad da:

$$\hat{H}\,\Psi = 0.$$

Obsérvese lo que **no** aparece: no hay \(\partial/\partial t\). El estado del universo es, a este nivel, **atemporal** (el «problema del tiempo»). El tiempo no es un fondo dado: **emerge** de las correlaciones internas de un \(\Psi\) sin tiempo. El mecanismo explícito es el de **Page–Wootters**: se elige un subsistema-**reloj** \(C\) y se lo entrelaza con el resto \(R\); aunque el estado global \(|\Psi\rangle\) es estacionario (\(\hat H|\Psi\rangle=0\)), el estado de \(R\) *condicionado* a que el reloj marque \(t\),

$$|\psi_R(t)\rangle \;=\; \langle t|_C\,|\Psi\rangle,$$

**sí** evoluciona, y recupera la ecuación de Schrödinger en \(t\). El tiempo no fluye «por fuera»: es una **lectura relacional** del entrelazamiento entre dos partes del universo. Esto afila H6–H7 —«la información empieza a operar» **no** presupone un reloj de fondo, la ejecución y el tiempo emergen *a la vez*— y prefigura la sección-espina (§4.8): el tiempo es la primera de tres cosas que el universo extrae de sus propias relaciones internas.

### 4.4 La flecha Q-BOT → BIT: diferenciación por decoherencia (sin selección)

Esta es la transición que **produce los bits clásicos** — y la única que lo hace. Dada una división sistema–entorno, el estado reducido del sistema se obtiene trazando el entorno:

$$\rho_S = \mathrm{Tr}_E\,|\Psi\rangle\langle\Psi|.$$

La interacción con el entorno **suprime los términos no diagonales** de \(\rho_S\) en la base de *estados puntero* (einselección, en la línea de Zurek):

$$\rho_S \;\xrightarrow{\;\text{decoherencia}\;}\; \sum_i p_i \,|i\rangle\langle i|.$$

Cada \(|i\rangle\langle i|\) estabilizado es un **BITᵢ**: un registro clásico, una rama autoconsistente. Esto explica la **diferenciación** de H5. Lo que la decoherencia **no** hace por sí sola es *seleccionar* un único resultado observado; ese paso adicional es interpretación-dependiente (ver §6). Por eso H5 distingue con cuidado *diferenciar* (no necesita árbitro) de *seleccionar* (lo necesitaría).

Caso concreto y hermoso: las fluctuaciones del fondo cósmico de microondas son **fluctuaciones cuánticas del vacío** estiradas por la inflación hasta escalas super-horizonte, donde **decoheren** en perturbaciones de densidad clásicas — las semillas de toda la estructura. Es decir: el tránsito **QUBIT → BIT** (sustrato cuántico → registro clásico), observado en el cielo.

### 4.4 bis Auto-decoherencia: el universo como su propio entorno

Hay una objeción estándar que el §4.4, tal como está, deja abierta — y conviene cerrarla, porque es el mayor agujero teórico del modelo. La decoherencia se define por la interacción de un sistema con un **entorno** externo. Pero si el universo es el sistema **total**, *no tiene afuera*: su evolución es **puramente unitaria**, \(|\Psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\Psi_0\rangle\), y un estado puro que evoluciona unitariamente **nunca pierde coherencia globalmente**. ¿De dónde sale entonces la decoherencia?

La respuesta —estándar en cosmología cuántica— es que el universo **se decoherencia a sí mismo**. Al no haber entorno externo, el estado global se **factoriza internamente**: una parte de sus grados de libertad actúa como «sistema» y el resto como «entorno». La traza parcial del §4.4 no se toma sobre un afuera, sino sobre **otros grados de libertad del propio universo**:

$$\rho_{\text{sis}} = \mathrm{Tr}_{\text{resto}}\,|\Psi\rangle\langle\Psi|.$$

El estado global sigue siendo puro y unitario; lo que decohere es el **estado reducido** de cada parte respecto a las demás. Tres anclajes concretos:

- **Kiefer (cosmología cuántica):** el grado de libertad **macroscópico** —el factor de escala del universo, su geometría global— decohere precisamente por su acoplamiento a la multitud de **modos inhomogéneos microscópicos** (las fluctuaciones cuánticas). Lo micro «mide» a lo macro. Lo grande se vuelve clásico porque lo pequeño lo observa.
- **Gell-Mann & Hartle (historias decoherentes):** ni siquiera hace falta una partición sistema/entorno fija. Se trabaja con **historias de grano grueso** y un *funcional de decoherencia* \(D(h,h')\); las historias cuyas interferencias se anulan, \(D(h,h')\approx 0\) para \(h\neq h'\), adquieren probabilidades clásicas. La clasicidad es una propiedad de **conjuntos de historias**, no de una frontera espacial.
- **Zurek (einselección):** el mismo mecanismo de estados puntero del §4.4, aplicado a particiones internas.

**Reencuadre de la flecha.** Con esto, la flecha `Q-BOT → BIT` no es decoherencia *contra un afuera* sino **auto-decoherencia por partición asimétrica de grados de libertad**: el operador fragmenta la simetría original, las fracciones resultantes se entrelazan, y esa interacción interna hace «saltar» los primeros BITs clásicos. La causalidad no viene de fuera: es **causalidad emergente intra-sistema**.

**El residuo honesto (no desaparece, se reubica).** La auto-decoherencia cierra el agujero del «no hay entorno», pero no lo disuelve del todo: lo convierte en una pregunta **más pequeña y con nombre**. En un universo cerrado con un solo espacio de Hilbert y un Hamiltoniano, *qué* partición cuenta como sistema y cuál como entorno **no viene dado** — la estructura de producto tensorial \(\mathcal{H} = \mathcal{H}_{\text{sis}}\otimes\mathcal{H}_{\text{resto}}\) es una **elección**. Es el «problema de la factorización preferente», y se retoma en §7.

### 4.5 La flecha del tiempo es física: principio de Landauer

Procesar información cuesta. Borrar un bit (operación lógicamente irreversible) disipa al menos:

$$E \;\ge\; k_B T \ln 2.$$

Consecuencia para H6: la «ejecución» cósmica —formar registros, decoherer, estructurar— es **operación irreversible** y por tanto **aumento de entropía**. La flecha del tiempo *es* el operador ejecutándose; y se paga con un presupuesto:

$$\frac{dS}{dt} \ge 0, \qquad \text{con } S(t_{\text{inicial}}) \approx 0.$$

«La información empieza a operar» se vuelve **literal**: operar *es* gastar la dotación inicial de baja entropía.

**Identidad clave (potencial = presupuesto).** Esto fija el sentido físico de «potencial máximo de diferenciación». El potencial no es un superlativo retórico: es el **hueco entrópico disponible**,

$$\Delta S \;=\; S_{\max} - S_0, \qquad S_0 \approx 0 \;\Rightarrow\; \Delta S \;\text{máximo}.$$

Y ese hueco es **la misma magnitud** que el presupuesto que la ejecución consume. Es decir: *potencial máximo de diferenciación* (lectura informacional) y *combustible que costea la flecha del tiempo* (lectura termodinámica) son **una sola cantidad medida de dos formas**. Aquí «máximo» queda anclado a un número, en lugar de flotar — que es justamente lo que fallaba en «información máxima» o «superposición máxima».

### 4.6 El arco de complejidad (H8)

La entropía crece monótonamente, pero la **complejidad** (estructura, organización) es **no-monótona**:

$$\underbrace{\text{orden}}_{\text{simple, } S\approx 0} \;\longrightarrow\; \underbrace{\text{complejidad}}_{\text{estructura, vida, mente}} \;\longrightarrow\; \underbrace{\text{muerte térmica}}_{\text{simple, } S = S_{\max}}.$$

El máximo está **en el medio**. Vivimos en la ventana en que la ejecución todavía es rica. La QRN cósmica no es el destino del operador; es el **intervalo** en que su carrera produce estructura antes de agotar el combustible.

### 4.6 bis El potencial no es del estado solo, sino del par (estado, operador)

Hay una precisión que da dientes a H2 y sentido fuerte a la flecha `QUBIT → Q-BOT`. El potencial de diferenciación **no es intrínseco a \(\Psi_0\)**. Un estado de máxima simetría sometido a un operador *trivial* —sin inestabilidades, sin dinámica— **no diferencia nada**: se queda liso para siempre. El potencial vive en el **par**

$$\big(\,\Psi_0,\ \hat{O}\,\big), \qquad \text{no en } \Psi_0 \text{ aislado.}$$

Formulación operativa:

$$\text{potencial efectivo de diferenciación} \;=\; \Delta S(\Psi_0)\ \textbf{ condicionado a }\ \hat{O}\ \text{no trivial}.$$

El QUBIT no «tiene» potencial por sí mismo; lo tiene **porque hay un Q-BOT que lo lee**. La diferenciabilidad del estado puro sólo se actualiza porque existe una dinámica para la que ese estado es alimento. Estrictamente: el potencial del qubit es su potencial *según el operador*. Lejos de debilitar el esquema, esto explica por qué `QUBIT → Q-BOT` es una flecha y no una identidad — el estado y la regla son piezas distintas, y la creación es su **acoplamiento**.

### 4.7 Cadena corregida (forma canónica del documento)

$$
\boxed{
\begin{array}{l}
\textbf{QUBIT}_0 \;=\; \text{estado cuántico primordial} \;(\Psi_0[\Phi]) \\[2pt]
\qquad\quad\;\; =\; \text{máxima simetría / máxima pureza} \;(S\approx 0) \\[2pt]
\qquad\quad\;\; =\; \text{mínima información clásica diferenciada} \\[2pt]
\qquad\quad\;\; =\; \text{potencial máximo de diferenciación } (\Delta S \text{ máximo}) \\[6pt]
\quad\big\downarrow\;\; \textsf{[activación endógena: incertidumbre, ruptura espontánea]} \\[6pt]
\textbf{Q-BOT}_1 \;=\; \text{operador cuántico generativo} \;(\hat{O},\;\hat{H}) \\[2pt]
\qquad\quad\;\; =\; \text{dinámica primordial, regla de evolución} \\[2pt]
\qquad\quad\;\; =\; \text{información en ejecución, aún no clásica} \\[6pt]
\quad\big\downarrow\;\; \textsf{[auto-decoherencia: partición asimétrica de grados de libertad]} \\[6pt]
\textbf{BIT}_i \;=\; \text{hecho clásico emergente, registro decoherido} \\[2pt]
\qquad\;\; =\; \text{rama estable / correlación observable} \\[2pt]
\qquad\;\; =\; \text{información ya diferenciada (residuo clásico)} \\[6pt]
\quad\big\downarrow\;\; \textsf{[acumulación de correlaciones y estructura]} \\[6pt]
\textbf{QRN} \;=\; \text{red relacional cuántica, causal-relacional} \\[2pt]
\qquad\;\; =\; \text{expansión de correlaciones, campos, materia, geometría} \\[2pt]
\qquad\;\; =\; \text{fase transitoria de complejidad cósmica}
\end{array}
}
$$

**Guardarraíl 1 — los índices son niveles, no tiempos; los nodos coexisten.** Los subíndices `₀ / ₁ / ᵢ` **no** marcan instantes en un reloj. La decoherencia no es un evento único y fechado: es **continua y distribuida**, ocurre sin cesar y a ritmos distintos según el grado de libertad. Por eso \(\text{BIT}_i\) indexa **registros** (uno por cada hecho que decohere), no momentos. Y \(\text{Q-BOT}_1\) **no «termina»** cuando empiezan los bits: sigue corriendo *debajo* de toda la cadena. Los cuatro nodos **coexisten** —el sustrato cuántico nunca deja de estar ahí, el operador nunca deja de operar—. Lo que la flecha ordena es **dependencia lógica**, no **sucesión temporal**.

**Guardarraíl 2 — QRN ≠ QNN.** `QRN` (Quantum **Relational** Network) nombra una **topología de relaciones**: nodos, filamentos, correlaciones causales (la morfología de la telaraña cósmica). `QNN` (Quantum **Neural** Network) es, en uso técnico, un objeto **funcional**: entrena parámetros y aprende. Este documento afirma sólo lo primero. Sostener lo segundo —que el cosmos *computa* o *aprende*— no es una nota al pie de este texto: es otra tesis, con su propia carga de prueba (§7).

### 4.8 El universo auto-referencial: una sola raíz, tres emergencias

Las tres piezas no triviales del modelo —la auto-decoherencia (§4.4 bis), el tiempo de Page–Wootters (§4.3) y la red relacional (QRN)— descansan sobre **un único movimiento**, y conviene verlo junto porque es la columna vertebral conceptual del documento.

El universo **no tiene afuera**. No hay entorno externo, ni reloj externo, ni observador externo, ni hechos definidos «desde fuera». Por tanto **todo** lo que parece dado tiene que **generarse desde dentro**, como relación entre subsistemas del propio estado global. Tres emergencias, una sola raíz:

| Qué emerge | Desde dónde (interno) | Mecanismo |
|---|---|---|
| **Clasicidad** (los BITs) | unos grados de libertad miden a otros | auto-decoherencia (Kiefer, Gell-Mann–Hartle, Zurek) |
| **Tiempo** | un subsistema-reloj entrelazado con el resto | Page–Wootters |
| **Hechos / causalidad** | la partición que teje la red de correlaciones | QRN (partición asimétrica) |

La frase que lo sintetiza:

> **Nada viene de fuera, porque no hay afuera.** La clasicidad, el tiempo y la causalidad no son escenario; son **lecturas relacionales internas** de un estado global puro que se auto-diferencia.

Esto es lo que «red relacional» buscaba nombrar desde el principio. La QRN no es una metáfora de adorno colgada al final de la cadena: es la **estructura** que hace posible que un universo sin exterior tenga, aun así, hechos, tiempo y orden causal. El Q-BOT fragmenta la simetría; las fracciones se entrelazan; de ese entrelazamiento interno se leen —simultáneamente y sin árbitro externo— lo clásico, lo temporal y lo causal. Un sistema **auto-referencial** en el sentido estricto: su única referencia es él mismo, partido.

---

## 5. Profundización filosófica

**La ontología estado/dinámica: estar contenido frente a operar.** El núcleo filosófico de la propuesta es una distinción modal: entre lo que *es el caso* (configuración) y lo que *hace que algo cambie* (regla). La tesis fuerte —y defendible— es que la **creación no es la aparición de un contenido nuevo**, sino el **paso de la contención a la operación**. El origen no añade un objeto al inventario del mundo; activa una dinámica. Esto desplaza la pregunta clásica «¿por qué hay algo en vez de nada?» hacia «¿por qué la regla empieza a correr?» — y H4 responde que no hace falta que «empiece» en sentido de un primer empujón externo: la quietud perfecta es, cuánticamente, imposible. La inestabilidad está dentro.

**El bit como residuo, no como origen.** La corrección de fundamentos de esta versión tiene una lectura filosófica precisa: lo definido, lo clasificable, lo que podemos *registrar y nombrar* no es el punto de partida del mundo, sino su **sedimento**. Primero hay potencial cuántico y dinámica; el hecho clásico —el bit— es lo que *queda depositado* cuando esa dinámica decohere. Invertir esto (poner el bit primero) es la tentación clásica: tomar el residuo por la fuente. El qubit es la fuente; el bit, la huella. Dicho de otro modo: **la clasicidad no es el estado natural del mundo, sino su sedimento forzado** — tener un valor definido, «ser un bit», es la **excepción costosa** (cuesta decoherencia, cuesta entropía), no la regla. Lo fluido y no-diferenciado es lo primero; lo binario y definido es lo que la auto-decoherencia *impone*.

**Información: ¿ontología o descripción?** *It from bit / it from qubit* sugiere que la información tiene **prioridad ontológica** —que lo físico *deriva* de lo informacional—. Es una posición seria pero no obligada. La lectura mínima y más segura es **descriptiva**: la información es nuestro mejor lenguaje para hablar de distinciones, correlaciones y registros, sin afirmar que el mundo «esté hecho de» bits. El documento adopta la lectura descriptiva como suelo, y señala la ontológica como puerta abierta, no como tesis asumida.

**El problema del seleccionador.** Aquí está el punto filosófico más delicado, y donde la versión primitiva de la metáfora se traicionaba a sí misma. Hablar de un input que «selecciona o proyecta una rama» es lenguaje de **colapso**, y reintroduce justo lo que H4 quería expulsar: un **seleccionador**. ¿Quién proyecta? Si de verdad se quiere que *nada entre desde fuera*, la lectura por **decoherencia** lo regala: nada selecciona ninguna rama; las ramas simplemente pierden coherencia mutua. La **diferenciación** no necesita árbitro; la **selección** sí. Quedarse en diferenciar sin seleccionar es lo coherente con un origen endógeno — y deja el residuo honesto: *por qué observamos un único resultado* sigue sin estar resuelto (§7).

**La cuestión QRN / QNN (H9).** «Red» es el término que más connotación no ganada arrastra, y por eso esta versión separa con cuidado dos siglas. **QRN — red relacional cuántica** es lo defendible: la semejanza con una red es **morfológica** (nodos, filamentos, correlaciones), no funcional. Existe literatura que compara la **telaraña cósmica** con redes neuronales por su estructura, pero es parecido de *forma*, no de *función*: la red cósmica no computa ni aprende en ningún sentido sustantivo. **QNN — red neuronal cuántica** sería la versión funcional —una arquitectura que entrena y optimiza—, y afirmarla del cosmos es un compromiso mucho mayor, perteneciente al territorio de la **agencia sentiente** y su gobernanza. Conviene saber que ahí se cruza una frontera: de la metáfora a una tesis fuerte. Es una puerta aparte, no un sinónimo poético. *(Nota de marco, opcional: dentro de tu Q+ATLANTIDE1000 la versión QNN-funcional pertenecería a la banda **QCSAA 900–999**, específicamente al rango de **Agencia Sentiente Cuántica** y al de **Gobernanza y Ética**; lo dejo como sugerencia de ubicación, no como asignación canónica —esa es tu decisión.)*

---

## 6. Lectura científica prudente: qué es cada cosa

El valor de la propuesta depende de **no confundir registros**. Esta tabla separa lo establecido, lo interpretativo y lo metafórico.

| Afirmación | Estatus | Nota |
|---|---|---|
| El estado fundamental de un campo es una superposición de mínima incertidumbre (QUBIT₀) | **Física establecida** | Vacío gaussiano \(\Psi_0[\Phi]\). |
| Baja entropía gravitacional al inicio; la uniformidad es lo improbable | **Física establecida** (lectura de Penrose) | Hipótesis de Curvatura de Weyl. |
| El dato clásico (BIT) emerge por decoherencia, río abajo de la dinámica cuántica | **Física establecida** | Decoherencia + cosmología inflacionaria. |
| Las estructuras del CMB son fluctuaciones cuánticas decoheridas | **Física establecida** | Tránsito QUBIT → BIT observado. |
| Borrar información cuesta \(k_B T \ln 2\) | **Física establecida** | Principio de Landauer. |
| El sustrato es cuántico, no clásico (it from qubit) | **Interpretación bien apoyada** | Frente a *it from bit* clásico. |
| Tiempo emergente; \(\hat{H}\Psi = 0\) atemporal | **Marco teórico serio, no confirmado** | Wheeler–DeWitt; problema del tiempo. |
| Diferenciación **sin** selección de rama | **Interpretación-dependiente** | Decoherencia sí; el «sin selección» depende de §7. |
| La complejidad es transitoria, máxima en el medio | **Cualitativo robusto** | Requiere definición rigurosa de complejidad. |
| La red cósmica es una **QRN** (relacional) | **Metáfora morfológica** | Topología, no función. |
| La red cósmica es una **QNN** (neural, computa/aprende) | **Tesis fuerte, no asumida aquí** | Territorio QCSAA (§7, H9). |
| «El universo es un qubit / es información» | **Metáfora / programa de investigación** | Útil como heurística, no como hecho. |

---

## 7. Invitación a la discusión: cuestiones abiertas

Estas son las costuras donde el documento se sabe incompleto. Se ofrecen como agenda, no como retórica.

1. **El problema de la medida.** La decoherencia explica la *apariencia* de clasicidad, pero **por qué se observa un único resultado** sigue abierto: ¿muchos-mundos (todas las ramas reales, ninguna selección) o teorías de colapso físico (una dinámica adicional que selecciona)? Conviene hacer explícito el compromiso del modelo: la **auto-decoherencia** del §4.4 bis —apariencia de clasicidad *dentro* de un estado global puro y unitario— es la imagen **everettiana**, y por tanto **refuerza H5** (diferenciación, no selección). El documento se inclina, pues, hacia unitariedad global sin colapso; queda el residuo honesto de por qué *este* observador ve *esta* rama, que ninguna interpretación cierra sin coste.

2. **El problema de la factorización preferente.** Es el residuo que la auto-decoherencia *reubica* en lugar de disolver (§4.4 bis). En un universo cerrado con un solo \(\mathcal{H}\) y un \(\hat{H}\), la partición \(\mathcal{H} = \mathcal{H}_{\text{sis}}\otimes\mathcal{H}_{\text{resto}}\) que distingue «sistema» de «entorno» **no viene dada**: hay infinitas factorizaciones posibles, y casi todas no producen clasicidad. ¿Qué selecciona la factorización «correcta»? Hay un programa vivo —la **mereología cuántica** de **Carroll & Singh**— que intenta *derivar* la partición de la estructura del Hamiltoniano (localidad, interacciones de bajo orden, cuasi-clasicidad), en vez de postularla. Si ese programa tiene éxito, la QRN ganaría su pieza más fundamental: no sólo *cómo* decohere un universo cerrado, sino *por qué se parte como se parte*. Si no, la partición sigue siendo un input no explicado.

3. **¿Es \(\Psi_0[\Phi]\) fundamental o emergente?** Escribir \(\Psi_0[\Phi]\) como *el* estado del QUBIT₀ primordial es la aspiración correcta, no un hecho. Cerca de \(t = 0\) puede que ni «campo» ni «estado» sobrevivan como nociones, y por debajo el propio campo podría emerger de una estructura de **entrelazamiento** (espaciotiempo tejido desde correlaciones). \(\Psi_0[\Phi]\) es un **nivel intermedio**: mejor que bits clásicos, todavía no el fondo. ¿Cuál es el fondo?

4. **El estatus de la baja entropía inicial.** ¿Es una **ley**, una **condición de frontera**, un **efecto de selección** (antrópico/observacional) o un **hecho bruto**? De la respuesta depende si H1–H2 describen una necesidad o una contingencia.

5. **¿Puede definirse rigurosamente «complejidad»?** H8 es intuitivamente fuerte pero necesita una medida no trivial que efectivamente alcance su máximo *entre* dos simplicidades, y que sea independiente del observador.

6. **Información: ¿ontología o descripción?** ¿Hay razón sustantiva para conceder prioridad ontológica a la información (it from qubit fuerte), o la lectura descriptiva es suficiente y más honesta?

7. **El umbral QRN → QNN (la puerta a QCSAA).** ¿Bajo qué condiciones —si alguna— una red **relacional** (QRN) dejaría de ser morfología para volverse **funcional** (QNN): computar, optimizar, aprender? ¿Qué criterio distinguiría una red que *parece* mente de una que *opera como* mente? Esta es la pregunta que conecta el documento con la gobernanza de la agencia sentiente, y la que —de responderse afirmativamente— cambiaría la categoría del documento.

---

## Apéndice A — Glosario notacional

| Símbolo | Lectura |
|---|---|
| **QUBIT₀** \(= \Psi_0[\Phi]\) | Estado cuántico primordial: puro, simétrico, indiferenciado |
| **Q-BOT₁** \(= \hat{O},\ \hat{H}\) | Operador cuántico generativo; dinámica / regla de evolución |
| **BITᵢ** | Registro clásico emergente (rama decoherida); residuo clásico |
| **QRN** | Quantum Relational Network: red causal-relacional (morfológica) |
| **QNN** | Quantum Neural Network: red **funcional** que entrena/computa (no asumida aquí) |
| \(\Phi,\ \phi\) | Campo cuántico (configuración) |
| \(\rho\) | Operador densidad (estado, puro o mezclado) |
| \(S(\rho) = -k_B\,\mathrm{Tr}(\rho\ln\rho)\) | Entropía de von Neumann |
| \(\Delta S = S_{\max}-S_0\) | Hueco entrópico = potencial de diferenciación = presupuesto |
| \(\hat{H}\Psi = 0\) | Ecuación de Wheeler–DeWitt (restricción hamiltoniana) |
| \(\rho_S = \mathrm{Tr}_E\,|\Psi\rangle\langle\Psi|\) | Estado reducido del sistema (traza sobre el entorno) |
| \(\rho_{\text{sis}} = \mathrm{Tr}_{\text{resto}}\,|\Psi\rangle\langle\Psi|\) | Auto-decoherencia: traza sobre *otros grados de libertad del propio universo* |
| \(\ $ \mathcal{H} = \mathcal{H}_{\text{sis}}\otimes\mathcal{H}_{\text{resto}} $\) | Factorización (partición asimétrica); su elección es el problema abierto del §7.2 |
| \(|\psi_R(t)\rangle = \langle t|_C|\Psi\rangle\) | Estado de \(R\) condicionado al reloj \(C\) (tiempo de Page–Wootters) |
| \(E \ge k_B T \ln 2\) | Cota de Landauer para borrado de un bit |
| \(k_B,\ T\) | Constante de Boltzmann, temperatura |

## Apéndice B — Anclajes (para lectura ulterior)

Los nombres y programas con los que dialoga este documento, sin pretensión de cita formal:

- **J. A. Wheeler** — *it from bit*; participación del observador.
- **R. Penrose** — Hipótesis de la Curvatura de Weyl; baja entropía gravitacional inicial.
- **R. Landauer** — coste termodinámico del borrado de información.
- **J. Hartle & S. Hawking** — propuesta sin frontera; función de onda del universo.
- **B. DeWitt** — ecuación de Wheeler–DeWitt; cuantización de la gravedad.
- **W. Zurek** — decoherencia, einselección, estados puntero.
- **C. Kiefer** — decoherencia en cosmología cuántica; el factor de escala decohere por los modos inhomogéneos (la flecha Q-BOT → BIT en un universo cerrado).
- **M. Gell-Mann & J. Hartle** — historias decoherentes; funcional de decoherencia; clasicidad sin frontera sistema/entorno fija.
- **Page & Wootters** — tiempo emergente del entrelazamiento entre un subsistema-reloj y el resto (§4.3).
- **S. Carroll & A. Singh** — mereología cuántica; intento de *derivar* la factorización preferente del Hamiltoniano (§7, cuestión 2).
- **it from qubit** — programa de espaciotiempo emergente desde entrelazamiento.
- *Comparación morfológica telaraña cósmica / redes* — analogía de estructura, no de función (frontera QRN / QNN, H9).

**Resonancia epistemológica — Mecánica Cuántica Relacional (C. Rovelli).** La QRN comparte con la RQM de Rovelli una intuición profunda: que el mundo clásico es, en su raíz, una **red de relaciones** entre sistemas, no una colección de propiedades absolutas. Esa afinidad es real y conviene reconocerla. Pero la QRN **no adopta** la tesis fuerte de la RQM —que *no existen hechos absolutos*, que todo estado es relativo a un observador-sistema—. La QRN mantiene su premisa fundacional: un **estado global puro y unitario** (a lo Everett / Carroll) que se **auto-decoherencia** mediante una **partición asimétrica de grados de libertad** (§4.4 bis). En otras palabras, la QRN toma de Rovelli la *estructura relacional* sin comprar su *anti-realismo de los hechos*: las relaciones emergen *dentro* de un estado global que sí es, él mismo, un hecho. Es una resonancia, no una identidad.

---

*Fin del borrador v0.5. Documento abierto: las nueve hipótesis y las siete cuestiones del §7 están planteadas para ser atacadas, no defendidas. La corrección de fundamentos de v0.3 —el bit como residuo y no como origen— y el cierre de v0.4 —la auto-decoherencia de un universo sin afuera— son las piezas que conviene poner a prueba primero. El residuo más profundo que queda abierto es la **factorización preferente** (§7, cuestión 2): por qué el universo se parte como se parte.*

*Las adiciones de v0.5 (abstract, estado del arte y explicitación del blanco) tienen como propósito facilitar la discusión académica y la eventual preparación para publicación o revisión por pares, sin alterar el contenido conceptual del borrador anterior.*
