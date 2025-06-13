# Raspberry Pi tutorial

# Vytvoření

# Získání fotky z Kamery

Instalace potřebné knihovny:

```bash
pip install opencv-python
```

Ukázka programu :

```python
import cv2  # Import the OpenCV library 

# Function to set up the camera
def CameraSetup():
    cap = cv2.VideoCapture(0)  # Open the default camera (0 = built-in webcam)

    # Set video format to MJPG (better performance than default)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

    # Set the width and height of the video frame
    cap.set(3, 960)  # Width
    cap.set(4, 640)  # Height

    print("Camera setup complete.")
    return cap

# Function to capture a frame from the camera
def GetImage(cap = cap):
    ret, image = cap.read()  # 'ret' is a success flag; 'image' is the captured frame
    return image

# Function to display an image in a window
def ShowImage(img):
    cv2.imshow('image', img)  # Show the image in a new window

# Example usage
cap = CameraSetup()       # Initialize the camera
image = GetImage()        # Capture a frame
ShowImage(image)          # Display the frame
cv2.waitKey(1000)         # Wait 1000 ms (1 second) before closing the window
cv2.destroyAllWindows()   # Close all OpenCV windows
```

Důležité části:

| Klíčová část | Vysvětlení |
| --- | --- |
| `cv2.VideoCapture(0)` | Otevírá kameru. Číslo může být 0, 1, 2… podle počtu zařízení. |
| `cv2.CAP_PROP_FOURCC` | Nastavuje formát videa (MJPG má často lepší výkon než výchozí YUY2). |
| `cap.set(3, 960)` / `cap.set(4, 640)` | Nastavení rozlišení obrazu – můžeš přizpůsobit dle potřeby. |
| `cv2.imshow(...)` | Otevře nové okno s náhledem obrázku. |
| `cv2.waitKey(...)` | Počká určený čas v milisekundách, nebo na stisk klávesy (např. `cv2.waitKey(0)`). |
| `cv2.destroyAllWindows()` | Zajistí, že po skončení programu se nezasekne GUI OpenCV. |
| `global cap` | Umožní proměnnou `cap` sdílet mezi funkcemi.  |

---

# Použití AI modelu

Instalace potřebné knihovny:

```bash
pip install ultralytics
```

Ukázka programu:

```python
from ultralytics import YOLO  # Import the YOLO class from the Ultralytics library
import cv2  # Import OpenCV for image handling and display

image = cv2.imread("test.png")  # Load an image from a file (for testing purposes)

# Function to load a YOLOv11 model
def LoadModel(model_path="yolo11s.pt"):
    model = YOLO(model_path)  # Load the model from the given path
    print(f"Model successfully loaded from {model_path}")
    return model

# Function to perform object detection on a given source
def GetResult(model, source):
    results = model.predict(source)  # Predict on the input (image, video, etc.)
    result = results[0]  # Take the first result (usually only one for static image)
    return result

# Function to extract and print bounding box data
def ObtainData(result):
    for box in result.boxes:
        x, y, w, h = box.xywh[0]  # Get box center x, y, width, height
        x, y, w, h = int(x), int(y), int(w), int(h)  # Convert to integers
        conf = float(box.conf[0])  # Get confidence score
        cls = int(box.cls[0])  # Get class ID
        print(f"Box: x={x}, y={y}, w={w}, h={h}, Confidence: {conf:.2f}, Class: {cls}")

# Load model
model = LoadModel()

# Run detection on the input image
result = GetResult(model, image)

# Print bounding box data
ObtainData(result)

# Show annotated image with bounding boxes
annotated = result.plot()  # Draw boxes and labels on a copy of the image
cv2.imshow('image', annotated)  # Display the annotated image
cv2.waitKey(10000)  # Wait for 10 seconds
cv2.destroyAllWindows()  # Close all OpenCV windows
```

Důležité části:

| Klíčová část | **Vysvětlení** |
| --- | --- |
| `YOLO(model_path)` | Načte YOLOv11 model z `.pt` souboru (např. `yolo11s.pt`). |
| `model.predict(source)` | Spustí detekci na vstupním obrázku nebo videu, vrací seznam výsledků. |
| `results[0]` | Vezme první výsledek (u obrázku je vždy jeden). |
| `result.boxes` | Obsahuje detekované objekty (bounding boxy, konfidence, třídy atd.). |
| `box.xywh[0]` | Souřadnice boxu: x (střed), y (střed), šířka, výška. |
| `int(x), int(y), ...` | Zaokrouhlení hodnot pro snadný výstup nebo zobrazení. |
| `box.conf[0]` | Důvěra v detekci (pravděpodobnost, že je to správná třída). |
| `box.cls[0]` | ID detekované třídy (např. 0 = člověk, 16 = pes – záleží na modelu). |
| `result.plot()` | Vrací kopii obrázku s vykreslenými boxy a názvy tříd. |
| `cv2.imshow(...)` | Zobrazí obrázek v novém okně. |
| `cv2.waitKey(...)` | Počká zadaný počet ms, jinak se okno okamžitě zavře. |
| `cv2.destroyAllWindows()` | Zavře všechna okna vytvořená OpenCV. |

---