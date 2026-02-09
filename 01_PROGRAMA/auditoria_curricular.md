# 🔎 Agente 3 — Auditoría de Solapamiento Curricular

> **Análisis de solapamientos entre el módulo de IA (27h) y los 16 cursos restantes del programa CEFA 2026**

---

## Metodología

Se analizó cada sesión del Ultimate Syllabus actual contra los 16 cursos del programa CEFA 2026 listados en `programa_cefa_2026.xlsx`. El análisis identifica:

- 🔴 **Solapamiento alto**: Contenido que el otro curso probablemente cubre en profundidad
- 🟡 **Solapamiento medio**: Hay intersección temática pero se puede diferenciar el ángulo
- 🟢 **Sin solapamiento**: Tema único del módulo de IA

---

## Matriz de Solapamiento

### Sesiones del Módulo de IA vs. Otros Cursos

| Sesión del Módulo IA | Curso CEFA que solapa | Nivel | Diagnóstico | Recomendación |
|---|---|---|---|---|
| **Macro Investing Framework** (1h15) | *Macroeconomía Monetaria* (24h) | 🟡 Medio | Macro framework es estándar en macroeconomía monetaria | **Reencuadrar**: No enseñar macro — usar como puente: "Cómo la IA cambia el análisis macro" |
| **Monetary Policy & Sovereign Curves** (webinar FT, 1h) | *Macroeconomía Monetaria* (24h), *Modelos de Tasa de Interés* (27h) | 🔴 Alto | Política monetaria y curvas soberanas son el corazón de estos dos cursos | **Redirigir**: Pedir al speaker FT que enfoque en "Cómo la IA está transformando el análisis de política monetaria y curvas" |
| **Labs con Python** (Labs 2, 4) | *Analítica de Datos: Python* (18h) | 🟡 Medio | Los alumnos ya saben Python cuando llegan al módulo de IA (el curso de Python es antes) | **Aprovechar**: Dar por sentado que saben basics de Python. Los labs deben usar Python como vehículo, no enseñarlo |
| **US IG Corporate Debt** (webinar FT, 1h) | *Renta Fija* (24h), *Ingeniería Financiera* (27h) | 🔴 Alto | IG debt es tema central de Renta Fija | **Redirigir**: Pedir al speaker FT que enfoque en "IA en credit analysis" o "AI-driven IG screening" |
| **US Agency MBS** (webinar FT, 1h) | *Renta Fija* (24h), *Estrategias de Renta Fija* (9h) | 🔴 Alto | MBS es tema central de Renta Fija | **Redirigir**: Enfoque en "AI-powered prepayment modeling" o "ML in MBS valuation" |
| **Money Market Industry & Trends** (Alfredo, 1h) | *Operaciones Monetarias* (24h) | 🟡 Medio | Money markets se cubre en operaciones monetarias | **Diferenciar**: Enfocar en FinTech y AI trends en money markets, no en instrumentos básicos |
| **Reserve Portfolio Construction** (Robert, 2h) | *Gestión de Reservas: SAA y EDR* (18h), *Juego de Negociación* (24h), *Estrategias RF* (9h) | 🔴 Alto | Construcción de portafolios de reservas es exactamente lo que cubren ~51h de otros cursos | **Reencuadrar urgente**: Robert debe enfocarse en "AI-Augmented Reserve Portfolio Construction" — cómo la IA cambia el proceso, no el proceso en sí |
| **Trends in EM Reserve Management** (Robert, 1h30) | *Gestión de Reservas: SAA y EDR* (18h) | 🟡 Medio | Tendencias en EM overlaps con SAA general | **Diferenciar**: Focus en AI adoption trends entre bancos centrales emergentes, no en tendencias de asignación |
| **Decision Intelligence** (1h) | *Riesgos Financieros* (18h) | 🟢 Bajo | Decision Intelligence es un enfoque de IA, no de riesgo tradicional | **OK**: Mantener como está |
| **Conceptos y Tendencias IA** (2h15) | — | 🟢 Ninguno | Único del módulo | **OK** |
| **De Quants a Copilots** (1h) | *Analítica de Datos: Econometría* (18h) | 🟢 Bajo | Quants son diferente a econometría | **OK**: Mencionar la evolución, no enseñar quant methods |
| **LLMs** (1h) | — | 🟢 Ninguno | Único del módulo | **OK** |
| **AI Labs 1-6** (4h30) | *Analítica de Datos: Python* (18h) | 🟡 Medio | Labs usan código pero no enseñan programación | **OK si**: Los labs asumen Python como herramienta, no como aprendizaje |
| **Seguridad y Ética en IA** (1h) | — | 🟢 Ninguno | Único del módulo | **OK** |
| **Aplicaciones de IA en Portafolios** (1h) | *Tópicos de Portafolios* (12h) | 🟡 Medio | Portafolios se cubre ampliamente | **Diferenciar**: Solo aplicaciones IA, no teoría de portafolios |
| **HumICs + Cierre** (1h) | — | 🟢 Ninguno | Único del módulo | **OK** |

---

## Resumen de Riesgo de Solapamiento

```
🔴 Alto (requiere reencuadre)    : 4 sesiones (5h)
🟡 Medio (requiere diferenciación): 6 sesiones (7h15)
🟢 Bajo/Ninguno (OK)              : 6 sesiones (~11h45)
```

---

## Zona de Mayor Riesgo: Sesiones de Franklin Templeton

Las 8 sesiones de FT se incluyen en orden de complejidad de asset class. Las que concentran mayor riesgo de solapamiento:

- **Monetary Policy & Sovereign Curves** → solapa con 51h de otros cursos (Macro + Modelos de Tasa)
- **US IG Corporate Debt** → solapa con 51h de otros cursos (Renta Fija + Ing. Financiera)
- **US Agency MBS** → solapa con 33h de otros cursos (Renta Fija + Estrategias RF)
- **Commodities in Reserve Portfolios** → solapa parcialmente con Gestión de Reservas (51h)
- **ESG Considerations** → tema nuevo, bajo riesgo de solapamiento
- **Soft Skills** → tema nuevo, bajo riesgo de solapamiento

### Decisión: Todas las sesiones FT se mantienen sin cambios

> [!IMPORTANT]
> **Las 8 sesiones de Franklin Templeton NO pueden ser modificadas.** Mantienen sus títulos y contenido original:
>
> 1. **Money Market Industry & Trends** (Alfredo Ríos, presencial, Día 1)
> 2. **Monetary Policy and Its Impact on Sovereign Curves** (TBC webinar, Día 1)
> 3. **US Investment Grade (IG) Corporate Debt** (TBC webinar, Día 2)
> 4. **US Agency Mortgage-Backed Securities (MBS)** (TBC webinar, Día 2)
> 5. **Commodities in Reserve Portfolios** (TBC webinar, Día 3)
> 6. **ESG Considerations in Central Bank Portfolios** (TBC webinar, Día 3)
> 7. **Trends in EM Reserve Management** (Robert Abad, presencial, Día 3)
> 8. **Soft Skills for Reserve Management Teams** (TBC webinar, Día 4)
>
> El solapamiento temático con otros cursos es mitigado por la **perspectiva global de Franklin Templeton** y el contexto del módulo de IA que les da un posicionamiento diferenciado.

---

## Zona de Mayor Riesgo: Sesión de Robert Abad

La sesión "Reserve Portfolio Construction: Putting It All Together" (comprimida a 1h30) tiene riesgo de solapamiento por volumen: hay **51 horas** de cursos relacionados con gestión de reservas en el programa.

### Nota sobre Robert Abad

> [!NOTE]
> El título de la sesión se mantiene como **"Reserve Portfolio Construction: Putting It All Together"**. Robert debe tener en cuenta que los alumnos ya habrán completado 51h de gestión de reservas, por lo que el taller integrador tiene mayor valor cuando conecta lo aprendido previamente con las herramientas de IA vistas en el módulo.

---

## Mapa de Sinergias (Oportunidades)

| El módulo de IA puede COMPLEMENTAR | Cómo |
|---|---|
| *Analítica de Datos: Python* (18h) | Los labs del módulo IA son la "graduación" del curso de Python — aplican Python a problemas reales con IA |
| *Tópicos de Portafolios* (12h) | El taller de Robert muestra el "siguiente nivel" de portfolio management |
| *Riesgos Financieros* (18h) | La sesión de ética/seguridad en IA introduce riesgos que NO son financieros tradicionales (IA hallucination, bias, etc.) |
| *Gestión de Reservas: Juego de Negociación* (24h) | Los labs de AI Agents (Lab 5) complementan la perspectiva de negociación con agentes autónomos |

---

## Recomendaciones Finales para el Agente 4 (Diseñador del Syllabus)

1. **Las sesiones FT se mantienen sin cambios** — aportan perspectiva global complementaria
2. **Briefar a Robert Abad**: Los alumnos tienen 51h de reservas — su valor agregado está en la integración
3. **No reemplazar MAGIC**: Se elimina sin sustitución — el Día 2 termina a las 16:00, dando tiempo de consolidación
4. **Asumir Python como pre-requisito**: 18h de Python antes del módulo significa que pueden codear
5. **No enseñar conceptos financieros básicos**: Renta fija, derivados, macro — todo cubierto antes
6. **El módulo de IA debe ser la CÚSPIDE tecnológica del programa**: Todo lo previo es la base sobre la que se construye
