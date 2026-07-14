import cv2
import os

from yolov4_code_simple import detection

det = detection()

path = "input"
imgDir = os.listdir(path)
saveFol = "output"

for imgName in imgDir:
    final_fol = os.path.join(path, imgName)
    img = cv2.imread(final_fol)
    if img is None:
        print(f"Skipping {imgName}: could not read image.")
        continue
    img = det.getdetection(img)

    os.makedirs(saveFol, exist_ok=True)
    final_save = os.path.join(saveFol, imgName)
    cv2.imwrite(final_save, img)
    print(f"Saved: {final_save}")


