import cv2
import os
import numpy as np


def blur(frame, x, y, w, h):
    try:
        blur_roi = frame[round(y):round(y + h), round(x):round(x + w)]
        blurred = cv2.GaussianBlur(blur_roi, (31, 31), 100)
        frame[round(y):round(y + h), round(x):round(x + w)] = blurred
    except Exception as e:
        print(f'Error in blur: {e}')
    return frame

class detection:
    def __init__(self):
        pass
    def Model(self):
        error,model,classes=None,None,None
        try:
            model_path = "yolov4_weights/yolov4.weights"
            model_config = "yolov4_weights/yolov4.cfg"
            Model_class = "yolov4_weights/obj.names"
            with open(Model_class, 'r') as f:
                classes = f.read().splitlines()
            net = cv2.dnn.readNetFromDarknet(model_config,model_path)
            model = cv2.dnn_DetectionModel(net)
            model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
        except Exception as e:
            print(e)
            error=e
        return error,model,classes
    
        
    def getdetection(self,image=None):
        Count=0
        result_image=None
        error=None

        try:
            img=image.copy()
            error,model,classes=self.Model()

 
            classIds, scores, boxes = model.detect(img, confThreshold=0.4, nmsThreshold=0.4)
            detection="no"

            # print(classIds, scores, boxes, "check")
            print(boxes,'==========')
            for (classId, score, box) in zip(classIds, scores, boxes):
                # print(text = '%s: %.2f' % (classes[0], score))
                # print(classId[0], classId[1], "0,1")
                # print("hi")
                # print(classId, score, box, "1st")
                # if classId != 0:
                #     continue
                # print(classId, score, box)
                # print("check")
                # cv2.imshow(img)
                # cv2.waitKey(0)

                if int(classId) == 0:
                    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                            color=(0, 0, 0), thickness=2)
                    text = '%s: %.2f' % (classes[classId], score)
                    cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0, 0, 0), thickness=2)
                elif int(classId) == 1:
                    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                            color=(0, 255, 0), thickness=2)
                else:
                    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                            color=(255, 0, 0), thickness=2)
                    text = '%s: %.2f' % (classes[classId], score)
                    cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0, 0, 0), thickness=2)

            # Count=len(classIds)
            result_image=img
        except Exception as e:
            print(e)
        return result_image
    

# getdetection("img.png")