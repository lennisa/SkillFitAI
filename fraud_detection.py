import cv2
import numpy as np
from PIL import Image

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

def detect_fraud(image):

    img = Image.open(image)

    frame = np.array(img)

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        1.1,
        4
    )

    fraud_flags = []

    behavior_signals = []



   

    if len(faces) == 0:

        fraud_flags.append(
            "No face detected"
        )

    elif len(faces) > 1:

        fraud_flags.append(
            "Multiple faces detected"
        )

    else:

        fraud_flags.append(
            "Face verification passed"
        )




    if len(faces) == 1:

        x, y, w, h = faces[0]

        face_area = w * h

        if face_area < 50000:

            behavior_signals.append(
                "Candidate appears far from camera"
            )

        else:

            behavior_signals.append(
                "Candidate attention maintained"
            )

        center_x = x + (w / 2)

        frame_center = frame.shape[1] / 2

        if abs(center_x - frame_center) > 120:

            behavior_signals.append(
                "Frequent off-center positioning detected"
            )

        else:

            behavior_signals.append(
                "Face positioning stable"
            )



    return fraud_flags, behavior_signals