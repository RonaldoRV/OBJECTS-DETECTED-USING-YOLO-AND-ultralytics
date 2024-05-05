from ultralytics import YOLO
from enum import Enum

# Enum for different model types
class ModelType(Enum):
    YOLOv8n = 'yolov8n.pt'
    YOLOv8s = 'yolov8s.pt'
    YOLOv8x = 'yolov8x.pt'

# Enum for different camera indices
class Camera(Enum):
    LOGI_1 = '0'
    LAPTOP = '1'
    LOGI_2 = '2'

# Determine available cameras and choose a valid index
def find_available_cameras():
    import cv2
    index = 0
    available_cameras = []
    while True:
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()
        else:
            break
        index += 1
    return available_cameras

# Function to run live object detection with error handling
def liveObjDetection(modelType: ModelType, cameraIndex='0'):
    try:
        model = YOLO(modelType.value)
        # Ensure the specified camera index is valid
        if int(cameraIndex) not in find_available_cameras():
            raise ConnectionError(f"Camera {cameraIndex} is not available.")
        
        model.predict(source=cameraIndex, show=True)
    except Exception as e:
        print(f"Error: Could not open camera {cameraIndex}. {e}")

# Entry point of the script
if __name__ == '__main__':
    # Get valid camera indices
    available_cameras = find_available_cameras()
    
    # Choose a valid camera index (use 0 if only one camera exists)
    camera_index = str(available_cameras[0]) if available_cameras else '0'

    # Run live object detection with a valid camera index
    #liveObjDetection(ModelType.YOLOv8x, cameraIndex=camera_index)
    liveObjDetection(ModelType.YOLOv8n)