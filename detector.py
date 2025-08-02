import cv2
from ultralytics import YOLO

# Activamos la cámara
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Cargamos el modelo entrenado
model = YOLO('best.pt')

while True:
    ret, frame = cap.read()

    # Realizamos la predicción
    results = model.predict(source=frame, imgsz=640, conf=0.5, verbose=False)

    # Dibujamos resultados
    annotated_frame = frame.copy()
    if len(results) > 0:
        annotated_frame = results[0].plot()

    cv2.imshow("Deteccion de contaminantes", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()