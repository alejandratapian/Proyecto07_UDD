# Análisis de Opiniones de Google Play Store usando Inteligencia Artificial

Este proyecto utiliza análisis de sentimientos en reseñas de Google Play Store para predecir el sentimiento de un usuario sobre una app. Se entrena un modelo de Machine Learning que, al recibir una reseña, devuelve una predicción del sentimiento (positivo, negativo, neutral) junto con la polaridad y subjetividad de dicha reseña.

### 1. **Introducción:**
   - **Objetivo del Proyecto:** 
     "El proyecto tiene como objetivo desarrollar un modelo que pueda predecir el sentimiento de las reseñas de usuarios en la tienda de aplicaciones de Google Play. Esto significa que, al recibir una reseña, el modelo puede decirnos si es positiva, negativa o neutra."
   
   - **Problema:**
     "Las reseñas de los usuarios son valiosas para las empresas porque muestran lo que los clientes piensan de sus productos. Sin embargo, muchas veces es difícil para una empresa revisar miles de comentarios manualmente para detectar tendencias o problemas específicos."

   - **Solución Propuesta:** 
     "Se ha creado un sistema automatizado que puede leer las reseñas de forma automática y clasificarlas según su sentimiento, ayudando a las empresas a analizar grandes volúmenes de opiniones de clientes rápidamente."

### 2. **Descripción del Modelo:**
   - **¿Qué es un modelo de procesamiento de lenguaje natural?**
     "Es un tipo de inteligencia artificial que ayuda a las computadoras a entender y trabajar con el lenguaje humano. En este caso, el modelo 'lee' los comentarios y entiende si las palabras usadas son más comunes en opiniones positivas, neutras o negativas."

   - **Modelos Utilizados:**
     "Se utilizó un modelo llamado **Regresión Logística**. Este tipo de modelo trata de encontrar patrones en los datos para hacer predicciones. Después de ajustar el modelo con diferentes configuraciones (hiperparámetros), se mejoró su capacidad para clasificar correctamente las reseñas."
     

   - **Ajuste de Hiperparámetros:**
     "Se utilizó **Grid Search** para ajustar los hiperparámetros del modelo **Random Forest**, el cual es un modelo basado en árboles de decisión, donde múltiples árboles colaboran para mejorar la precisión. Random Forest es especialmente útil para capturar relaciones no lineales en los datos. “
“Grid Search es un proceso exhaustivo que prueba varias combinaciones de configuraciones de parámetros para encontrar la que ofrece el mejor rendimiento. En este caso, se ajustaron parámetros como el número de árboles (`n_estimators`) y la profundidad de los mismos (`max_depth`). El ajuste con Grid Search permitió mejorar el **accuracy** del modelo de 0.82 a 0.87."

### 3. **Datos y Limpieza:**
   - **¿Qué datos se usaron?**
     "El modelo fue entrenado con reseñas de la Google Play Store, cada una acompañada por una etiqueta que indica si el sentimiento era positivo, negativo o neutro."

   - **Limpieza de datos:**
     "Antes de entrenar el modelo, se procesaron los datos para eliminar cualquier información innecesaria o ruido (como puntuaciones o símbolos). También se balancearon los datos para asegurar que el modelo tuviera una cantidad equitativa de ejemplos positivos, neutros y negativos."

### 4. **Resultados y Métricas:**
   - **Precisión del Modelo:**
     "La precisión del modelo fue evaluada usando varias métricas, incluidas **Exactitud (Accuracy)** y **F1-Score**. El modelo de regresión logística alcanzó una precisión del 82%, mientras que el modelo Random Forest, con ajuste de hiperparámetros, mejoró la precisión hasta el 87%. El F1-Score también reflejó mejoras significativas, especialmente en la clasificación de reseñas negativas."

   - **Curvas de Rendimiento:**
     "Se generaron gráficos que muestran cómo el modelo mejora con más datos de entrenamiento y cómo se desempeña en nuevos datos no vistos durante el entrenamiento."

   - **Pruebas del Modelo:**
     "Se probó el modelo con frases de ejemplo como 'I love this game!' (Me encanta este juego), 'It's okay, nothing special.' (Está bien, nada especial), y 'I can't stand this app!' (¡No soporto esta aplicación!)."


### 5. **Ajustes y Mejoras:**
   - **Ajuste de Hiperparámetros:**
     "Se utilizó Grid Search para optimizar los parámetros del modelo de Regresión Logística. Los mejores parámetros obtenidos fueron `C`=10 y `solver`='liblinear', lo que mejoró notablemente el rendimiento del modelo."

   - **Ensamblaje de Modelos:**
     "Además, se implementó un modelo ensamblado mediante un **Voting Classifier**, que combina la Regresión Logística ajustada con un modelo de **Random Forest**. Esta técnica permite que ambos modelos 'voten' sobre la clasificación final, generando una predicción más robusta. Se utilizó votación 'soft' para tomar en cuenta las probabilidades de cada modelo en lugar de simplemente contar los votos. Tras entrenar y ajustar el ensemble, los resultados demostraron una mejora en la precisión general en comparación con los modelos individuales.

### 6. **Conclusión:**
   - "Este proyecto demuestra cómo la inteligencia artificial puede ayudar a las empresas a analizar rápidamente grandes cantidades de opiniones de usuarios. La automatización del análisis de sentimiento puede ahorrar tiempo y recursos, permitiendo a las empresas mejorar sus productos y servicios basándose en los comentarios de los clientes."

   - **Próximos Pasos:**
     "Se puede mejorar el sistema obteniendo más datos o afinando aún más el modelo, así como considerar desbalances en los datos que podrían afectar la precisión para casos menos representados (como comentarios neutrales). También se podría explorar el uso de otros modelos más complejos como redes neuronales para mejorar aún más la precisión."

