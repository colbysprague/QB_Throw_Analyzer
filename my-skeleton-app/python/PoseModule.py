import cv2
import mediapipe as mp
import time
import math
import pprint


class PoseDetector:
    def __init__(self, subjectHeight = 180, mode = False, upBody = False, smooth=True, detectionCon = True, trackCon = 0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

        self.subjectHeight = subjectHeight

        self.maxHandPosY = None
        self.waitingForRelease = False
        self.ballThrown = False
        self.frames_below_eye = 0
        self.ballTucked = False
        self.waitingForRelease = False
        self.frames_close_together = 0
        self.frame_count = 0
        self.releaseHeight = None

        self.throwInProgress = False
        self.throwData = {
            "throwingArmAngle": [], 
            "releaseArmAngle": None, 
            "throwingLeftLegAngle": [], 
            "throwingRightLegAngle": [], 
            "shoulderTilt": None, 
            "framesDuringThrow": None, 
        }

        self.throwSession = []

    def calcReleaseHeight(self):
    
        x1, y1 = self.lmList[16][1:]
        print("before", x1)
        x2, y2 = self.lmList[12][1:]

        x1 = x2


        given_cm = self.subjectHeight / 4
        given_px = self.findDistance(11, 12)
        target_px = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        # Calculate the corresponding value of x
        x = (given_cm * target_px) / given_px

        releaseHeightCm = self.subjectHeight + x - 20 + 17 

        print(releaseHeightCm)

        return int(releaseHeightCm)



    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        #print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw=True):
        self.lmList= []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, p1, p2, p3, draw = True): 
        # get the landmarks
        x1, y1 =  self.lmList[p1][1:]
        x2, y2 =  self.lmList[p2][1:]
        x3, y3 =  self.lmList[p3][1:]

        # calc the angle
        angle = math.degrees(
            math.atan2(y3 - y2, x3 - x2 - math.atan2(y1-y2, x1-x2))
            )
        
        if angle < 0: 
            angle += 360
            angle = 360 - angle

        return int(angle)

    def findDistance(self, p1, p2):
        """ Returns the distance between two coordinates """
        x1, y1 =  self.lmList[p1][1:]
        x2, y2 =  self.lmList[p2][1:]

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return distance
    
    def calcShoulderTilt(self, l_shoulder=11, r_shoulder=12):
            x1, y1 = self.lmList[l_shoulder][1:]
            x2, y2 = self.lmList[r_shoulder][1:]

            x3, y3 = (x1, y2)

            angle = math.degrees(
                math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)
            )
            # Ensure the angle is always less than 90 degrees
            angle = abs(angle)

            return int(angle)


    def determinePoint(self, img, p1, frames_to_wait=3):
        x1, y1 = self.lmList[p1][1:]
        _, handHeight = self.lmList[p1][1:]
        _, eyeHeight = self.lmList[5][1::]

        if handHeight < eyeHeight:
            self.waitingForRelease = True
            cv2.putText(img, "Waiting for Release!", (x1 + 50, y1 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        if self.waitingForRelease:
            if self.maxHandPosY is None:
                self.maxHandPosY = handHeight
            elif self.maxHandPosY < handHeight:
                self.maxHandPosY = handHeight
                self.frames_below_eye = 0  # Reset the counter
            elif self.maxHandPosY > handHeight:
                self.frames_below_eye += 1

                if self.frames_below_eye >= frames_to_wait:
                    self.throwInProgress = False
                    self.ballThrown = True
                    self.waitingForRelease = False  # Reset for the next throw

        if not self.throwInProgress and self.ballThrown:
            cv2.putText(img, "Ball Thrown", (150, 200), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    def drawCore(self, img, l_shoulder = 11, r_shouler = 12, l_hip = 23, r_hip = 24): 
        x1, y1 =  self.lmList[l_shoulder][1:]
        x2, y2 =  self.lmList[r_shouler][1:]
        x3, y3 =  self.lmList[l_hip][1:]
        x4, y4 =  self.lmList[r_hip][1:]
        
        # draw lines
        # TOP: R to L Shoulder
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
        # RIGHT: R Shoulder to R Hip
        cv2.line(img, (x2, y2), (x4, y4), (255, 255, 255), 3)
        # LEFT: L Shoulder to L Hip
        cv2.line(img, (x1, y1), (x3, y3), (255, 255, 255), 3)
        # BOTTOM: L Hip to R Hip
        cv2.line(img, (x3, y3), (x4, y4), (255, 255, 255), 3)

        # draw circles
        cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x3, y3), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x4, y4), 5, (255, 0, 0), cv2.FILLED)

    def detectFootballThrow(
            self,
            img,
            # l_shoulder = 11, 
            r_shoulder = 12, 
            r_elbow = 14,
            r_hand = 16,
            # l_hip = 23,
            r_hip = 24, 
            r_knee = 26, 
            r_ankle = 28, 
            l_hip = 23, 
            l_knee = 25, 
            l_ankle = 27, 

            # l_hand = 15, 
            ):
        
        # find distance between R Hand and R Shoulder to determine if throw is starting
        distance = self.findDistance(r_hand, r_shoulder)

        if not self.ballThrown:
            if distance > 20 and distance < 100: 
                self.ballTucked = True

            if distance < 30 and not self.throwInProgress and not self.ballThrown: 
                self.throwInProgress = True
                self.ballTucked = False

            # determine throw start and end
            _, handHeight = self.lmList[r_hand][1:]
            _, eyeHeight = self.lmList[5][1:]
            frames_to_wait = 3 #frames to wait before accepting value

            if handHeight < eyeHeight:
                self.waitingForRelease = True
                # cv2.putText(img, "Waiting for Release!", (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            if self.waitingForRelease:
                
                if self.maxHandPosY is None:
                    self.maxHandPosY = handHeight
                elif self.maxHandPosY < handHeight:
                    self.maxHandPosY = handHeight
                    self.frames_below_eye = 0  # Reset the counter
                elif self.maxHandPosY > handHeight:
                    self.frames_below_eye += 1

                    if self.frames_below_eye >= frames_to_wait:
                        # cv2.putText(img, "Ball Thrown!", (200, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                        self.throwInProgress = False
                        self.ballThrown = True
                        self.waitingForRelease = False  # Reset for the next throw
                        self.throwData["shoulderTilt"] = self.calcShoulderTilt()
                        self.throwData["releaseHeight"] = self.calcReleaseHeight()
                        # print("Assigning Release Height!", self.calcReleaseHeight())
                        # self.releaseHeight = self.calcReleaseHeight()
                        # print("release Height: ", self.releaseHeight)

            # record data about the throw
            if self.throwInProgress:   

                self.frame_count += 1
                self.throwData["framesDuringThrow"] = self.frame_count
                self.throwData["throwingArmAngle"].append(self.findAngle(r_shoulder, r_elbow, r_hand))
                self.throwData["throwingLeftLegAngle"].append(self.findAngle(l_hip, l_knee, l_ankle))
                self.throwData["throwingRightLegAngle"].append(self.findAngle(r_hip, r_knee, r_ankle))
                self.throwData["releaseArmAngle"] = self.throwData["throwingArmAngle"][-1]

            elif self.ballThrown: 
                return self.throwData
        
    
def main():
    ...
#     cap = cv2.VideoCapture('videos/a.mp4')
#     pTime = 0
#     detector = PoseDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findPose(img)
#         lmList = detector.getPosition(img)
#         print(lmList)

#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime

#         cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)


if __name__ == "__main__":
    main()