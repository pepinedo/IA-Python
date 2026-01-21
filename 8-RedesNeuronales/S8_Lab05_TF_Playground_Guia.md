# S8 · Lab 05 — TensorFlow Playground (guía de laboratorio + caza de “fantasmas”)

Abre:
https://playground.tensorflow.org/

## Objetivo
Visualizar:
- por qué una sola capa no separa patrones no lineales,
- cómo una capa oculta “dobla” el espacio,
- y cómo demasiada capacidad puede aprender **ruido** (overfitting).

---

## Experimento A — Sin capas ocultas (0 hidden layers)
1. Dataset: **Circle** (o Spiral para más choque).
2. Hidden layers: **0**.
3. Features: `x1`, `x2`.
4. Entrena unos segundos.

### Observa
- La frontera no consigue separar el círculo de forma estable.

### Responde
- ¿Qué estructura falta para “curvar” el espacio?

---

## Experimento B — Una capa oculta pequeña
1. Hidden layers: **1**.
2. Neurons: **3** (o 4).
3. Mantén el mismo dataset.
4. Entrena.

### Observa
- Aparece una separación no lineal.
- El “espacio” se transforma para envolver regiones.

### Responde
- ¿Qué ha aportado la capa oculta?
- ¿Qué significa aquí “aprender representaciones”?

---

## Experimento C — Caza de “fantasmas” (Overfitting)
1. Sube el **ruido** del dataset al máximo (o muy alto).
2. Crea una red grande: **6 capas** con **8 neuronas** cada una.
3. Entrena.

### Observa
- La frontera se vuelve “loca”: intenta rodear puntos individuales de ruido.
- El modelo memoriza irregularidades locales en lugar de aprender estructura general.

### Responde (frase final obligatoria)
Escribe esta frase y complétala con tu interpretación:

> “He aprendido que más capacidad no siempre es mejor modelo, sino más riesgo de aprender ________.”

---

## Cierre
Este laboratorio conecta con el contrato profesional:
- más capacidad = más potencia,
- pero también más riesgo,
- y más necesidad de validación/regularización (sesiones siguientes).


---

## Evidencias que debes capturar (para tu entrega)
- Una captura del **Experimento A** (0 capas) donde se vea que la frontera no separa bien.
- Una captura del **Experimento B** (1 capa, 3 neuronas) donde se vea que ya hay separación no lineal.
- Una captura del **Experimento C** (ruido alto + red grande) donde se vea la frontera “nerviosa/loca”.

## Errores comunes (y cómo corregirlos)
- “No veo overfitting”: sube el ruido y aumenta capas/neuronas; entrena más tiempo.
- “La frontera no cambia”: asegúrate de que el entrenamiento está corriendo (botón play) y que no estás en pausa.
- “Me separa incluso con 0 capas”: cambia el dataset a **Circle** o **Spiral** y aumenta el ruido un poco.

## Cierre (1 frase obligatoria)
Escribe en tu entrega:
- Qué ganaste al aumentar capacidad (qué pudo aprender),
- y qué riesgo apareció (qué empezó a memorizar).
