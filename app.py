import cv2
from ultralytics import YOLO

# Load your model from your Colab train-2/weights folder
model = YOLO('C:/Users/HP/OneDrive/Desktop/YOLO_project/best (3).pt')

# Counting variables
in_count = 0
out_count = 0
counted_ids = set()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # Real-time tracking
    results = model.track(frame, persist=True, conf=0.4)

    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.int().cpu().tolist()
        clss = results[0].boxes.cls.int().cpu().tolist()

        for tid, idx in zip(ids, clss):
            if tid not in counted_ids:
                name = model.names[idx]
                if name == 'human-walk-in':
                    in_count += 1
                    counted_ids.add(tid)
                elif name == 'human-walk-out':
                    out_count += 1
                    counted_ids.add(tid)

    # UI Display
    img = results[0].plot()
    cv2.rectangle(img, (10, 10), (300, 100), (0,0,0), -1)
    cv2.putText(img, f"TOTAL ENTRY COUNT: {in_count}", (20, 40), 2, 1, (0, 255, 0), 2)
    cv2.putText(img, f"TOTAL EXIT COUNT: {out_count}", (20, 80), 2, 1, (0, 0, 255), 2)
    
    cv2.imshow("Entry/Exit Counter", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
