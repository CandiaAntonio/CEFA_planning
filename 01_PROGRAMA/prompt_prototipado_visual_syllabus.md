# Prompt para Prototipado Visual del Syllabus — CEFA 2026

> **Instrucción**: Copia todo el contenido de abajo y pégalo en tu herramienta de Claude Code para prototipar visualmente el syllabus.

---

## PROMPT

Necesito diseñar visualmente el **Ultimate Syllabus** para un módulo de 4 días. Genera una interfaz interactiva tipo calendario/timeline donde pueda arrastrar, reordenar y ajustar las sesiones. A continuación están todos los datos del módulo.

### CONSTRAINTS

- **Fechas**: Martes 3 – Viernes 6 de marzo de 2026
- **Horario**: 09:00–17:00 TODOS los días (no excepción)
- **Almuerzo**: 12:00–14:00 (fijo, no negociable)
- **Bloques por día**: Mañana 09:00–12:00 (3h) + Tarde 14:00–17:00 (3h) = 6h/día
- **Total**: 24h programadas + 3h evento alumni = 27h módulo
- **Pausas**: 15 min entre sesiones (flexible)
- **Regla**: Todos los días abren y cierran con instructor presencial (🟢)

### SESIONES DISPONIBLES (pool para ubicar en el calendario)

#### Sesiones de Antonio Candia (FLAR) — 🟢 Presencial — ~10h total

| ID | Sesión | Duración | Notas |
|----|--------|----------|-------|
| AC1 | Apertura del Módulo | 15m | Siempre Día 1, 09:00 |
| AC2 | Conceptos y Tendencias Globales en IA (Parte 1) | 1h | Fundamentos IA, historia, GenAI |
| AC3 | Conceptos y Tendencias Globales en IA (Parte 2) | 1h | IA agéntica, autonomía, futuros |
| AC4 | Inteligencia de Decisión | 30m–1h | Sesgos cognitivos, humano hackeable |
| AC5 | De Quants a Copilots | 1h | Evolución IA en finanzas |
| AC6 | LLMs: Modelos de Lenguaje | 1h | Deep learning, transformers, GPT |
| AC7 | HumICs + Singularidad + Cierre | 30m–1h | Cierre magistral. Siempre último bloque del Día 4 |
| LAB1 | 🧪 Prompt Engineering | 45m | Prompts para comunicados de política monetaria |
| LAB2 | 🧪 AI Coding Assistants | 45m | Script Python con Cursor/Copilot |
| LAB3 | 🧪 Vibe Coding | 45m | Dashboard sin código, Replit/Lovable |
| LAB4 | 🧪 RAG | 30–45m | Chatbot sobre docs de reservas |
| LAB5 | 🧪 Building AI Agents | 45m | Agente de research financiero |
| LAB6 | 🧪 AI Content Generation | 45m | Presentación ejecutiva con Gamma |

#### Sesiones FT — Ordenadas por complejidad progresiva

| ID | Sesión | Speaker | Modalidad | Duración |
|----|--------|---------|-----------|----------|
| FT1 | Money Market Industry & Trends | Alfredo Rios | 🟢 Presencial | 1h |
| FT2 | Monetary Policy & Sovereign Curves | Nick Mastroianni, CFA | 🔵 Webinar | 1h |
| FT3 | US IG Corporate Debt | James So, CFA | 🔵 Webinar | 1h |
| FT4 | US Agency MBS | Elliott Neumayer | 🔵 Webinar | 1h |
| FT5 | Commodities in Reserve Portfolios | Steve Land | 🔵 Webinar | 1h |
| FT6 | ESG Considerations in CB Portfolios | Brishni Mukhopadhyay, CFA | 🔵 Webinar | 1h |
| FT7 | Trends in EM Reserve Management | Robert Abad | 🟢 Presencial | 1h30 |
| FT8 | Soft Skills for Reserve Mgmt Teams | Alejandro Vargas | 🔵 Webinar | 1h |

#### Sesiones colaborativas

| ID | Sesión | Speakers | Modalidad | Duración |
|----|--------|----------|-----------|----------|
| COL1 | Seguridad y Ética en IA | Antonio + Juan J. Ramírez | 🔵 Remoto | 1h |
| COL2 | Reserve Portfolio Construction: Putting It All Together | Robert Abad + Antonio | 🟢 Presencial | 2h–2h30 |

#### Evento

| ID | Sesión | Día | Hora | Duración |
|----|--------|-----|------|----------|
| EVT | 🥂 CEFA Connect (cóctel alumni) | Día 3 (Jueves 5) | 18:30–21:30 | 3h |

### DESIGN RULES

1. **Progresión FT**: FT1→FT2→FT3→FT4→FT5→FT6→FT7→FT8 (simple→complejo)
2. **Progresión Labs**: LAB1→LAB2→LAB3→LAB4→LAB5→LAB6 (básico→avanzado)
3. **Labs conectan con teoría**: cada lab idealmente sigue a una sesión teórica relacionada
4. **No webinars consecutivos** si es posible
5. **Robert Abad presencial**: FT7 y COL2 deben estar el mismo día o días consecutivos
6. **Day 4 cierra con AC7 (HumICs)**: siempre el último bloque

### CURRENT v2 LAYOUT (punto de partida)

```
DÍA 1 (Mar): AC1→AC2→break→FT1→AC4→lunch→FT2→LAB1→break→AC5
DÍA 2 (Mié): AC3→FT3→FT4→lunch→LAB2→cierre [TERMINA 15:00 ⚠️ CAMBIAR A 17:00]
DÍA 3 (Jue): AC6→LAB3→break→FT5→lunch→FT6→FT7→LAB4 → EVT 18:30
DÍA 4 (Vie): FT8→LAB5→break→COL1→lunch→COL2+LAB6→AC7
```

### WHAT I NEED

- Interfaz visual tipo **grilla** con 4 columnas (días) y filas de 30 min
- Bloques de colores por tipo: 🟢 presencial, 🔵 webinar, 🧪 lab, ⬜ pausa
- Poder **drag-and-drop** o reubicar sesiones
- **Timer** que muestre horas usadas vs disponibles por día
- Verificación automática de constraints (horario, speaker, no webinars consecutivos)
- **El Día 2 necesita ~2h más de contenido** para ir de 15:00 a 17:00

### OPCIONES PARA LLENAR DÍA 2 (15:00–17:00)

Opciones a considerar para las 2 horas extra del Día 2:

- Mover alguna sesión de otro día que esté sobrecargado
- Extender el Lab 2 a 1h (de 45m)
- Agregar una sesión teórica de Antonio (AC4 o AC5 si no están en el Día 1)
- Incluir un Q&A / workshop session post-lab
