# -*- coding:utf-8*-
import cv2
import string, random
import numpy as np

video_path = "F:\PaperInsightTool\images_to_gif\we_are_young.mp4"


def read_video(video_path):
    capture = cv2.VideoCapture(video_path)
    return  capture


def reszize(img, fx=0.6, fy=0.5):
    """ 图片缩放"""
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)


def img2gray_bgr(img):
    """ 彩色图片转3通道灰色图片 """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)



capture = None
if capture is None:
    capture = read_video(video_path)



while (capture.isOpened()):
    ret, frame = capture.read()
    if not ret:
        break
    reszie_factor = 0.6
    frame = reszize(frame, fx=reszie_factor, fy=reszie_factor) ## 缩放

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    flip = cv2.flip(frame, 0)
    met1 = np.hstack((frame, gray)) ## 水平合并

    met2 = np.hstack((flip, hsv))
    met = np.vstack([met1, met2]) ## 垂直合并

    cv2.imshow('result', met)

    key = cv2.waitKey(delay=1)

    #  # esc键退出
    if 0xFF & cv2.waitKey(30) == 27:
        break
    if key == ord('q'):
        break


cv2.destroyAllWindows()
capture.release()







# import cv2
# import mediapipe as mp
# import time
# mpPose = mp.solutions.pose
#
# pose = mpPose.Pose()
# mpDraw = mp.solutions.drawing_utils
#
# cap = cv2.VideoCapture(video_path)
# pTime = 0
# while True:
#     success, img = cap.read()
#
#     try:
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = pose.process(imgRGB)
#
#         fps = 30
#         w, h = 640, 480
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         videoWriter = cv2.VideoWriter("1.mp4", fourcc, fps, (w, h))
#
#         if results.pose_landmarks:
#             mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
#             for id, lm in enumerate(results.pose_landmarks.landmark):
#                 h, w,c = img.shape
#                 cx, cy = int(lm.x*w), int(lm.y*h)
#                 cv2.circle(img, (cx, cy), 1, (255,0,0), cv2.FILLED)
#                 cTime = time.time()
#
#                 fps = 1/(cTime-pTime)
#                 pTime = cTime
#                 cv2.putText(img, str(int(fps)), (50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 5)
#                 cv2.imshow("Image", img)
#
#                 # videoWriter.write(img)
#
#                 cv2.waitKey(1)
#
#         videoWriter.release()
#
#     except Exception as ee:
#         print(ee)
#         break







