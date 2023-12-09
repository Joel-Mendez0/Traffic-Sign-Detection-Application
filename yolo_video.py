from ultralytics import YOLO
import cv2
import math
import pytesseract
import time

def video_detection(path_x):
    video_capture = path_x
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    target_width = 640
    target_height = 480

    scale_x = target_width / frame_width
    scale_y = target_height / frame_height

    model = YOLO("best.pt")
    classNames = ['Speed Limit', 'Stop']
    
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (target_width, target_height))
        results = model(img, stream=True, conf = 0.85)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]

                c2 = x1 + t_size[0], y1 - t_size[1] - 3

                if class_name == 'Speed Limit':
                    # Make the bounding box around the OCR region blue
                    color = (255, 0, 0)  # Blue

                    # Crop the region within the bounding box for OCR
                    roi = img[y1:y2, x1:x2]

                    # Perform OCR on the cropped region
                    speed_limit_text = pytesseract.image_to_string(roi, config='--psm 8')

                    # Filter out non-numeric characters
                    speed_limit_text = ''.join(filter(str.isdigit, speed_limit_text))

                    # Get the bounding box coordinates for the OCR region
                    (text_width, text_height), baseline = cv2.getTextSize(speed_limit_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                    text_box_x1, text_box_y1 = x1, y1 - 30
                    text_box_x2, text_box_y2 = x1 + text_width + 4, y1 - 30 - text_height - 4

                    # Draw the bounding box around the OCR region with increased thickness
                    cv2.rectangle(img, (text_box_x1, text_box_y1), (text_box_x2, text_box_y2), color, 2)

                    # Print the recognized speed limit text in the terminal
                    print(f"Recognized Speed Limit: {speed_limit_text}")

                    # Draw the OCR result on the image with increased font size
                    cv2.putText(img, speed_limit_text, (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                elif class_name == "Stop":
                    color = (20, 20, 20)

                if conf > 0.8:
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
                    
                time.sleep(0.1) 

        yield img

    cv2.destroyAllWindows()

