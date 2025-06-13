import cv2  # Import the OpenCV library

# Function to set up and configure the camera
def CameraSetup():
    cap = cv2.VideoCapture(0)  # Open the default camera (usually the built-in webcam)

    # Set video codec to MJPG for better performance and compatibility
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    # Set resolution: width = 960 pixels, height = 640 pixels
    cap.set(3, 960)  # Width
    cap.set(4, 640)  # Height

    print("Camera setup complete.")
    return cap  # Return the camera object

# Function to capture a single frame from the camera
def GetImage(cap):
    ret, image = cap.read()  # 'ret' is True if the frame was successfully read
    if not ret:
        print("Error: Failed to read image from camera.")
        return None
    return image  # Return the captured image frame

# Function to display the image in a window
def ShowImage(img):
    cv2.imshow('image', img)  # Display the image in a window titled "image"

# Example usage
cap = CameraSetup()           # Initialize the camera and get the camera object
image = GetImage(cap)         # Capture a single frame using the camera object

if image is not None:
    ShowImage(image)          # Show the captured image in a window if successful
    cv2.waitKey(1000)         # Wait for 1000 milliseconds (1 second)
    cv2.destroyAllWindows()   # Close all OpenCV-created windows
