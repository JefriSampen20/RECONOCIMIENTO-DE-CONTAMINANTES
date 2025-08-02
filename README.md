# Proyecto de Detección de Contaminantes en frutas
Somos estudiantes de la Universidad Nacional de Piura, de la Escuela Profesional de Ingeniería Electrónica y Telecomunicaciones. En este proyecto desarrollamos un sistema de visión por computadora enfocado en la detección de contaminantes, utilizando técnicas de autoetiquetado, procesamiento de imágenes, y entrenamiento de modelos de detección basados en inteligencia artificial.

# Descripción general del proyecto

El objetivo principal fue detectar y clasificar tres tipos diferentes de contaminantes presentes en distintos entornos. Para ello, trabajamos con un total de 300 imágenes, distribuidas en tres etiquetas principales (100 imágenes por clase), las cuales fueron procesadas y anotadas en el formato YOLOv8.

# Autoetiquetado con Grounding DINO

Con el fin de reducir el tiempo invertido en la anotación manual, implementamos un sistema de autoetiquetado semiautomático utilizando el modelo Grounding DINO. Este modelo permite generar cajas delimitadoras (bounding boxes) precisas a partir de descripciones en lenguaje natural.

Grounding DINO combina un componente visual y uno lingüístico en una sola arquitectura. Está compuesto por:

- Una red vision-language multimodal, que utiliza un Vision Transformer (ViT) para la parte visual y un Transformer para la parte textual.

- Un método de refinamiento iterativo, que mejora progresivamente las predicciones del modelo, logrando mayor precisión y coherencia en los resultados.

Gracias a este enfoque, pudimos:

- Generar automáticamente las bounding boxes para cada contaminante en las imágenes.

- Asignar etiquetas correspondientes según los tipos de contaminantes definidos previamente.

- Acelerar el proceso de etiquetado, manteniendo la calidad de los datos de entrenamiento.

# Procesamiento de Imágenes

Antes del entrenamiento del modelo, cada imagen fue sometida a un preprocesamiento, con el objetivo de normalizar su formato y asegurar consistencia en el dataset. Las operaciones aplicadas fueron:

- Corrección automática de orientación de los píxeles.

- Redimensionamiento de todas las imágenes a una resolución fija de 640 × 640 píxeles, ajustando las proporciones mediante estiramiento.

# Aumento de Datos (Data Augmentation)

Para aumentar la cantidad y variedad del conjunto de datos, se aplicaron técnicas de aumento automático, generando tres versiones adicionales por cada imagen original. Estas técnicas incluyeron:

- Rotaciones aleatorias de 0°, 90° (sentido horario y antihorario).

- Rotaciones adicionales entre –15° y +15°.

- Aplicación de desenfoque gaussiano aleatorio, entre 0 y 1 píxeles.

Este conjunto enriquecido de datos permitió entrenar modelos más robustos, capaces de reconocer los contaminantes en distintas condiciones de luz, orientación y enfoque.

# Anotaciones

Todas las anotaciones generadas fueron estructuradas en el formato YOLOv8, lo que facilitó el entrenamiento del modelo utilizando herramientas modernas y eficientes de detección de objetos.

# Librerías utilizadas

Durante el desarrollo del proyecto, se emplearon las siguientes librerías y herramientas principales en el entorno Python:

- torch – para manejo de modelos basados en PyTorch.

- opencv-python – para lectura, visualización y manipulación de imágenes.

- numpy – para operaciones matriciales y procesamiento de datos.

- matplotlib – para visualización de resultados y análisis gráfico.

- PIL (Pillow) – para operaciones de carga y transformación de imágenes.

- transformers – para usar modelos de lenguaje preentrenados, útiles en la etapa lingüística de Grounding DINO.

- GroundingDINO – librería base del modelo vision-language utilizado para el autoetiquetado.

- ultralytics – para la implementación y entrenamiento con el modelo YOLOv8.

- pycocotools – para la conversión y manipulación de formatos de anotación (COCO, si es necesario).

- tqdm – para visualizar barras de progreso durante procesos largos.

# Procedimientos de instalación y configuración

A continuación, se describen los pasos básicos para instalar y configurar el entorno del proyecto:

## 1. Crear entorno virtual (opcional pero recomendado)

    python -m venv venv
    source venv/bin/activate   # En Linux/macOS
    venv\Scripts\activate.bat  # En Windows

## 2. Clonar los repositorios necesarios

git clone https://github.com/IDEA-Research/GroundingDINO.git
cd GroundingDINO

## 3. Instalar dependencias principales

    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install opencv-python numpy matplotlib pillow transformers
    pip install -e .  # para instalar GroundingDINO como paquete local

## 4. Instalar Ultralytics (YOLOv8)

    pip install ultralytics

## 5. Instalar otras utilidades

    pip install pycocotools tqdm

Nota: Asegúrate de tener Python 3.8 o superior y una versión de CUDA compatible si planeas usar GPU. Puedes verificar la compatibilidad en la página oficial de PyTorch.

# Autores

- AREVALO MENDOZA ALESSANDRO MIGUEL
- GONZALES ALVARADO SEBASTIAN ANTONY
- SAMPEN CHANCAFE JEFFERSON ARMANDO

# Licencia

Este proyecto está bajo la licencia MIT. Puedes usar, modificar y distribuir este código con fines educativos y de investigación, siempre que se otorgue el debido crédito.

# Créditos

* Universidad Nacional de Piura

* Escuela Profesional de Ingeniería Electrónica y Telecomunicaciones

* IDEA Research (GroundingDINO)

Ultralytics (YOLOv8)
