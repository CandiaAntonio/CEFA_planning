# Prompt para Claude Artifact — Tablero Final CEFA 2026

Copia todo lo que está debajo de la línea `---` y pégalo en Claude.ai:

---

Crea un artefacto interactivo en React que sea un tablero de diseño curricular con drag and drop. El syllabus ya está diseñado — quiero visualizarlo y poder hacer ajustes finos arrastrando sesiones.

## ESTRUCTURA DEL CALENDARIO

Curso: "Aplicaciones de IA para Gestión de Portafolios" — CEFA 2026, BCRP
Fechas: 3 al 6 de marzo de 2026 (4 días)
Horario: 09:00–17:00 (Día 4 extiende a 18:00), con almuerzo 12:00–14:00
Bloques: Mañana (09:00–12:00, 3h) y Tarde (14:00–17:00 o 18:00)
Total: 24 horas efectivas

## FUNCIONALIDADES

1. **Drag and Drop**: Cards de sesión arrastrables entre bloques + zona lateral "Banco" para sesiones no asignadas
2. **Campos por sesión**: Título, Duración (0.25h a 3h), Tipo (Teórica/Lab/Demo/Taller/Webinar/Apertura-Cierre), Instructor, Modalidad (Presencial/Remoto), Descripción
3. **Validación**: Mostrar horas usadas/disponibles por bloque. Rojo si se excede.
4. **Vista Syllabus**: Botón "Generar Syllabus" → tabla imprimible (window.print con @media print)
5. **Diseño**: Dark mode profesional. Cards con colores por tipo y badges por instructor.

## COLORES POR TIPO

- Teórica: azul
- Lab 🖥️: verde
- Demo: púrpura
- Taller: naranja
- Webinar remoto: gris-azul
- Apertura/Cierre: dorado

## BADGES POR INSTRUCTOR

- Antonio Candia: 🟢 verde "Presencial"
- Robert Abad: 🟢 verde "Presencial"
- Alfredo Ríos: 🟢 verde "Presencial"
- Speaker FT: 🔵 azul "Remoto"
- Juan J. Ramírez: 🔵 azul "Remoto"

## SESIONES PRE-CARGADAS (ya asignadas a bloques)

### DÍA 1 — Martes 3 marzo — MAÑANA (09:00–12:00)

1. "Apertura del Módulo" — 15min — Apertura — Antonio Candia — Presencial
2. "Macro Investing Framework: Tendencias Seculares, Cíclicas y Tácticas" — 1h15 — Teórica — Antonio Candia — Presencial
3. "Conceptos y Tendencias Globales en IA (Parte 1)" — 1h15 — Teórica — Antonio Candia — Presencial — Desc: Pirámide del conocimiento, historia IA, GenAI, capacidades y desafíos

### DÍA 1 — Martes 3 marzo — TARDE (14:00–17:00)

4. "Monetary Policy & Sovereign Curves" — 1h — Webinar — Speaker FT (TBC) — Remoto
2. "🧪 Lab 1: Prompt Engineering" — 45min — Lab — Antonio Candia — Presencial — Desc: Prompts para analizar comunicados de política monetaria
3. "Inteligencia de Decisión: Fundamentos" — 1h — Teórica — Antonio Candia — Presencial — Desc: Decision Intelligence, sesgos, el humano hackeable

### DÍA 2 — Miércoles 4 marzo — MAÑANA (09:00–12:00)

7. "Conceptos y Tendencias Globales en IA (Parte 2)" — 1h — Teórica — Antonio Candia — Presencial — Desc: IA agéntica, autonomía, Ley de McLau, benchmarks IA vs humanos
2. "De Quants a Copilots: Evolución de la IA en Finanzas" — 1h — Teórica — Antonio Candia — Presencial
3. "Money Market Industry & Trends" — 1h — Teórica — Alfredo Ríos — Presencial

### DÍA 2 — Miércoles 4 marzo — TARDE (14:00–17:00)

10. "US IG Corporate Debt" — 1h — Webinar — Speaker FT (TBC) — Remoto
2. "🧪 Lab 2: AI Coding Assistants" — 45min — Lab — Antonio Candia — Presencial — Desc: Cursor/Copilot para analizar spreads de crédito IG
3. "Demo MAGIC: Agentes Financieros en Acción" — 1h — Demo — Antonio Candia — Presencial

### DÍA 3 — Jueves 5 marzo — MAÑANA (09:00–12:00)

13. "LLMs: Modelos de Lenguaje de Gran Tamaño" — 1h — Teórica — Antonio Candia — Presencial — Desc: Intro ML comprimida + Deep Learning + Transformers + GPT
2. "🧪 Lab 3: Vibe Coding" — 45min — Lab — Antonio Candia — Presencial — Desc: Mini-dashboard de portafolio sin código con Replit/Lovable
3. "US Agency MBS" — 1h — Webinar — Speaker FT (TBC) — Remoto

### DÍA 3 — Jueves 5 marzo — TARDE (14:00–17:00)

16. "Trends in EM Reserve Management" — 1h30 — Teórica — Robert Abad — Presencial — Desc: Diversificación, geopolítica, asset allocation en bancos centrales emergentes
2. "🧪 Lab 4: RAG" — 45min — Lab — Antonio Candia — Presencial — Desc: Chatbot sobre IIF-EY survey usando RAG
3. "Wrap-up Día 3" — 30min — Cierre — Antonio Candia — Presencial

### DÍA 4 — Viernes 6 marzo — MAÑANA (09:00–12:00)

19. "Aplicaciones de IA en Gestión de Portafolios" — 1h — Teórica — Antonio Candia — Presencial — Desc: AIDA framework, estrategia AAA
2. "🧪 Lab 5: Building AI Agents" — 45min — Lab — Antonio Candia — Presencial — Desc: Agente de research financiero con memoria y herramientas
3. "Seguridad y Ética en IA" — 1h — Webinar — Antonio + Juan J. Ramírez — Remoto — Desc: Lavado de IA, antropomorfización, ética en finanzas

### DÍA 4 — Viernes 6 marzo — TARDE (14:00–18:00)

22. "Reserve Portfolio Construction: Putting It All Together" — 2h — Taller — Robert Abad — Presencial — Desc: Taller integrador, construcción de portafolio aplicando todo lo aprendido
2. "🧪 Lab 6: AI Content Generation" — 45min — Lab — Antonio Candia — Presencial — Desc: Presentación ejecutiva para comité de inversión con Gamma/NotebookLM
3. "HumICs + La Singularidad Económica + Cierre" — 1h — Cierre — Antonio Candia — Presencial — Desc: Skills humanos, firma frontera, 3 competencias del futuro, reflexiones finales

## CONTADOR

Mostrar abajo: "24 de 24 horas asignadas" con barra de progreso verde completa.
Desglose: Presencial 20h (83%) | Remoto 4h (17%)
