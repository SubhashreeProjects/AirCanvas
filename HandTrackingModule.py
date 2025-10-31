import cv2
import mediapipe as mp 


class HandTracker:
    def __init__(self, mode=False, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=self.mode,
                                          max_num_hands=1,
                                          min_detection_confidence=self.detection_confidence,
                                          min_tracking_confidence=self.tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def find_hands(self, image, draw=True):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def find_position(self, image, draw=False):
        self.landmarks_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[0]  # Assuming only one hand is detected
            for id, landmark in enumerate(my_hand.landmark):
                height, width, _ = image.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                self.landmarks_list.append([id, cx, cy])
        return self.landmarks_list

    def fingersUp(self):
        fingers = []

        if len(self.landmarks_list) != 0:
            # Check if thumb is up
            if self.landmarks_list[self.tipIds[0]][2] > self.landmarks_list[self.tipIds[0] - 1][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Check if index, middle, ring, pinky fingers are up
            for id in range(1, 5):
                if self.landmarks_list[self.tipIds[id]][2] < self.landmarks_list[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        return fingers




def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    while True:
        ret, frame = cap.read()
        frame = tracker.find_hands(frame)
        landmarks_list = tracker.find_position(frame)
        if len(landmarks_list) != 0:
            print(landmarks_list)

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
