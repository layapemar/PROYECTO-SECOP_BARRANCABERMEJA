# Dictamen metodológico final — SECOP II Barrancabermeja (cuadernos 01 a 07)

**Fecha:** 22 de septiembre de 2026 · **Alcance:** cadena completa `notebooks/01…07`, corrida congelada `jbjy-vk9h_20260906_20260911T205559031273Z` (corte de firmas: 4 de septiembre de 2026).

## 1. Veredicto

La metodología es **robusta y defendible**. Nadie puede tumbar las cifras publicadas por un error de cálculo: una recomputación independiente las reprodujo todas. Las críticas que sí eran válidas eran de interpretación (comparar a los alcaldes donde los datos no lo sostienen) y de exposición (tablas públicas con identificadores). Esas críticas se corrigieron en esta versión.

La historia del cuaderno 07 queda **lista para revisión editorial y publicación**, con dos condiciones que ningún código puede cumplir por sí solo:

1. La clasificación profesional / apoyo a la gestión sigue **sin validación manual**, aunque ya tiene una validación interna fuerte. Cuando el objeto dice a la vez "profesionales" y "apoyo a la gestión", se desempata con la profesión u oficio nombrado. Donde la etiqueta y la profesión coinciden en el mismo objeto, concuerdan en el 98,2 % (profesional) y el 99,6 % (apoyo) de los casos. Las cifras por subtipo se publican con cautela y no se usan para comparar gobiernos.
2. Las preguntas marcadas como **"solo expedientes"** no se responden con SECOP: la legalidad de contratos firmados en Ley de Garantías, los contratos simultáneos, los valores extremos y la ESE.

## 2. Cómo se verificó

| Prueba | Qué se hizo | Resultado |
|---|---|---|
| Recomputación independiente | Un verificador escribió su propio código, sin usar el del proyecto, y recalculó 24 cifras clave desde el archivo bruto y la base del 03. | 24 de 24 coinciden. El conteo ingenuo desde el bruto difiere menos de 1,1 %, en la dirección esperada por los filtros. |
| Auditoría adversarial 1 | Un revisor "hostil" (estadística y periodismo de datos) buscó todo lo que pudiera desacreditar el análisis. | 21 observaciones: 2 críticas, 5 altas y el resto medias o bajas. Todas atendidas (sección 3). |
| Auditoría adversarial 2 | Revisión de consistencia entre cada cifra del texto y su tabla, después de las correcciones. | Todas las cifras reproducibles. Se corrigieron 9 detalles de exposición y redacción. |
| Reproducibilidad | Cadena 01→07 ejecutada dos veces desde cero. | 121 archivos de datos, tablas y gráficas idénticos byte a byte. Solo cambian la hora y el entorno de los manifiestos. |
| Controles automáticos | Cada cuaderno bloquea si falla un control crítico. | 01 a 07 sin bloqueos; el 07 pasa 17 de 17 controles. |

**Estado de los cuadernos en su equipo.** En la copia local, el 06 tenía borrado el cuerpo de la función `hallazgo`. Con Run All habría fallado con un error de sintaxis. El 07 tenía textos cortados, porque se separaron cadenas con comas, y se había quitado el gráfico del embudo. Se restauraron los siete cuadernos. Además, el 07 ahora rechaza bloques de texto mal armados, en lugar de cortarlos en silencio.

## 3. Qué se corrigió en esta revisión

| Observación | Gravedad | Corrección |
|---|---|---|
| P10 afirmaba que a la misma persona "no se le recortó", pero el 47 % perdió poder de compra y el 04 muestra −12,6 % entre 2022 y 2026. | Crítica | P10 presenta los dos diseños y concluye que el resultado depende del intervalo de tiempo. No se atribuye nada a un gobierno. |
| P09 y la prueba de estrés publicaban la comparación real Alfonso → Jonathan, que el 06 marca como no publicable. | Crítica | P09 da pesos de cada año por periodo y la serie real por año. La comparación real entre gobiernos y sus columnas salieron de las tablas públicas. Se añadió la sensibilidad al clasificador en apoyo. |
| P06: "con Jonathan se renueva a más personas" era un efecto de composición, porque 2022 fue año de Ley de Garantías. | Alta | Ahora se presenta por año de terminación (40 % a 75 % a 90 días). No se comparan gobiernos. El Q04 del 06 pasó a no publicable. |
| Conteos en Ley de Garantías tratados de forma asimétrica (2022 oculto, 2026 publicado). | Alta | Ambos se publican como dato descriptivo, con las excepciones del art. 33 citadas. La legalidad queda como pregunta para los expedientes. |
| Archivos públicos con id de contrato y URL de SECOP (pares multientidad, detalle de Ley de Garantías, extremos, solapes, conteos por día). | Alta | Movidos a `uso_interno_verificacion/`. El control de privacidad del 07 revisa ahora las carpetas públicas del 05, 06 y 07. |
| Se afirmaba "verificado en el 01" aunque la consulta a SECOP I puede fallar por conexión. | Alta | Los textos cambian según el resultado real de la verificación. Se eliminó la ventana del año 2 (abril a diciembre de 2021), que empieza en el mes de migración a SECOP II. |
| "El cambio de gobierno renovó a la mayoría" decía lo contrario del dato (40 %). | Alta | "El nuevo gobierno volvió a contratar a 4 de cada 10". |
| Atribuciones causales ("porque", "por diseño", "el primer año se planea…"). | Media | Reescritas como coincidencias. Un control bloquea si reaparecen. |
| El estado "terminado" se leía como terminación anticipada. | Media | Renombrado. Ya no se usa como filtro de robustez: depende de la antigüedad del contrato. |
| P12 (15 %) incluía registros de la ESE aún sin confirmar. | Media | El titular usa solo CPS confirmados. La ESE va aparte. |
| Fuentes débiles para el salario mínimo 2026 y el fin de la veda. | Media | Decreto 1469 de 2025 y Decreto transitorio 0159 de 2026; Registraduría para la segunda vuelta del 21 de junio de 2026. |
| Filas que ubicaban un contrato (duración, mes y subtipo). | Media | Solo se publican conteos por banda de duración. |
| Detalles: cifras fijas en el texto ("939", "2.600"), fines de semana filtrados, picos de años parciales, "Ana" mezclando años. | Baja | Todo se calcula en el código. |
| Cerca del 8 % de los CPS de la Alcaldía (2.154) quedaba "ambiguo" aunque el objeto nombraba la profesión ("como arquitecto", "como comunicadora social"). Lo detectó la revisión de la plantilla manual. | Media | El 03 desempata por la profesión u oficio nombrado, con la regla del Decreto 1082 de 2015: profesión universitaria es Profesional; técnico, tecnólogo, auxiliar, formador o instructor es Apoyo. Se resolvieron 2.196 contratos y quedan 272 ambiguos (0,2 % a 1,0 % por año). La etiqueta original se conserva en `subtipo_literal`. |

## 4. Por qué la metodología se sostiene

- **Universo correcto.** La Alcaldía se identifica por su NIT. Las entidades autónomas (Concejo, Personería, Contraloría, Hospital Regional) nunca se suman al alcalde.
- **Identidad sólida.** Cada persona es su documento, no su nombre. Las exclusiones por identidad son del 0,1 %.
- **Cálculos verificados.** La unión de intervalos, la duración inclusiva, los episodios, la serie diaria (cuadra con el valor prorrateado al 0,1 %), el índice de Gini, la retención y el Kaplan–Meier se revisaron y recalcularon por separado.
- **Sesgos tratados de forma explícita:**
  - censura en las renovaciones, con un seguimiento igual de 365 días;
  - inflación, con el IPC del DANE y el salario mínimo;
  - etapa del mandato, con una ventana comparable;
  - años parciales, que se marcan;
  - días adicionados, con una prueba empírica que muestra que ya están en la fecha final.
- **Publicación por reglas.** Cada hallazgo tiene nivel de evidencia y estado, y dice "qué no significa". Lo que depende de la ventana se publica como rango. Lo que requiere documentos va como pregunta.
- **Trazabilidad.** Hay huellas sha256 de cada archivo, manifiestos por etapa y ejecución determinista. El dato bruto nunca se modifica.

## 5. Límites que SECOP no permite eliminar (y cómo se manejan)

| Límite | Manejo |
|---|---|
| La vigencia pactada no son días trabajados; una terminación anticipada no registrada infla la duración. | Se dice en cada hallazgo. La prueba de estrés recalcula sin prórrogas. |
| El subtipo profesional / apoyo sale del texto del contrato; tiene validación interna (98 % de concordancia) pero no manual. | Cautela en P09, P10 y P11; sensibilidad con los contratos ambiguos. No se comparan gobiernos por subtipo. |
| Cada entidad empezó a publicar en SECOP II en una fecha distinta. | No se comparan gobiernos en las otras entidades. Se informa el primer mes de publicación regular de cada una. |
| La fecha de firma de SECOP puede no ser la de suscripción. | Los conteos de Ley de Garantías se publican sin conclusión legal. |
| Un solo periodo por alcalde. | Ningún patrón (obra al final del gobierno, rotación) se generaliza. |
| Los contratos de 2026 siguen en ejecución. | Se marca en prórrogas, valor pagado y retención de 2025 a 2026. |

## 6. Conclusiones finales que se pueden publicar

Estas conclusiones cumplen a la vez tres condiciones: se reprodujeron de forma independiente, pasaron la prueba de estrés y no atribuyen causas.

1. **Muchos contratos, poca plata.** Entre el 92 % y el 95 % de los contratos de la Alcaldía son CPS, pero se llevan entre el 13 % y el 31 % del valor firmado cada año.
2. **Contratos cortos, personas que encadenan.** Un CPS dura unos 3 a 4 meses. Aun así, entre el 28 % y el 39 % de las personas suma 7 meses o más al año encadenando contratos.
3. **Cada enero la contratación se apaga.** El 15 de enero de 2022 a 2025 había entre 1 y 4 personas con CPS vigente. En 2026 había 757, porque las firmas empezaron el 5 de enero.
4. **Mes y medio de espera típica.** Quien renueva espera una mediana de unos 47 días. Cuántos renuevan depende más del año (40 % a 75 % antes de 90 días) que del gobierno.
5. **Oleadas que coinciden con el calendario electoral.**
   - En junio de 2023 se firmaron 2.187 CPS en 30 días, antes de las restricciones territoriales; en julio a octubre, casi ninguno.
   - En enero de 2026 se firmaron 3.039 antes de la veda, y el 42 % se prorrogó después.
   - SECOP registra 938 CPS con fecha de firma dentro de la prohibición de 2022 y 2 en la de 2026. Esto es un dato, no una conclusión legal.
6. **El cambio de gobierno.** El nuevo gobierno volvió a contratar a 4 de cada 10 contratistas del anterior. Dentro de un mismo gobierno repite entre el 57 % y el 79 % de un año a otro; en el cambio, el 30 %.
7. **Honorarios.** En pesos de cada año suben. Descontando la inflación, la mediana profesional pasó de 5,1 a 4,2 millones entre 2021 y 2026, y de 3,8 a 2,3 salarios mínimos. La erosión empezó antes del cambio de gobierno y no se atribuye a un alcalde.
8. **Sin concentración extrema del dinero de CPS.** El 10 % con más valor reúne entre el 25 % y el 28 % del total.
9. **Obra y convenios.** La obra pública firmada se concentró en 2022 y 2023; en 2024 fue mínima. La contratación directa de lo que no son CPS subió al 41 % del valor en 2025, sobre todo por contratos con entidades públicas.

**Lo que no se puede afirmar:**
- que un alcalde pague más o menos;
- que un alcalde renueve más;
- que las tandas tengan fines electorales;
- que hubo infracciones a la Ley de Garantías;
- que repetir sea favoritismo o salir sea despido.

## 7. Recomendaciones antes de publicar

1. Ejecutar los siete cuadernos en orden con **Restart & Run All**, sin editarlos. Si hay que cambiar algo, cambiarlo en el cuaderno y volver a ejecutar desde esa etapa.
2. Diligenciar la plantilla `datos/referencias/03_revision_manual_cps.csv` (417 contratos) para validar el subtipo, y volver a ejecutar desde el 03. Solo se llenan `decision_cps_manual`, `subtipo_manual`, `revisor` y `fecha_revision`. La columna `subtipo_cps` de la plantilla es la de su fecha de creación; el 03 compara con la clasificación vigente. Con 60 o más revisados por subtipo y una precisión de 90 % o más, el estado pasa a VALIDADA.
3. Pedir a la Alcaldía, mediante derecho de petición, los expedientes de las preguntas abiertas: CPS firmados en la veda de 2022, contratos interadministrativos de diciembre de 2025 a enero de 2026, prórrogas de enero de 2026, extremos y simultáneos.
4. Publicar `historia_ciudadana.html`, que es autocontenida. Las carpetas `uso_interno_verificacion/` **no se publican**.
