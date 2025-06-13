from ultralytics import YOLO
import cv2

image = cv2.imread("test.png")  # Load an image from a file (for testing purposes)

def LoadModel(model_path="yolo11s.pt"):
    model = YOLO(model_path)
    print(f"Model successfully loaded from {model_path}")
    return model

def GetResult(model, source):
    results = model.predict(source)
    result = results[0]
    return result

def ObtainData(result):
    for box in result.boxes:
        x, y, w, h = box.xywh[0] 
        x, y, w, h = int(x), int(y), int(w), int(h)
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        print(f"Box: x={x}, y={y}, w={w}, h={h}, Confidence: {conf:.2f}, Class: {cls}")

model = LoadModel()
result = GetResult(model, image)
ObtainData(result)

annotated = result.plot()
cv2.imshow('image', annotated)
cv2.waitKey(10000)
cv2.destroyAllWindows()

