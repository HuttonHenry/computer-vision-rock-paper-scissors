import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

computer_wins = 0
user_wins = 0

def get_prediction():
    while True: 
        if computer_wins == 3 or user_wins == 3:
            break
        start = time.time()
        while time.time() < start + 5:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            if prediction[0] > 0.5:
                computer_wins += 1
                print("Computer wins this round!")
            else:
                user_wins += 1
                print("User wins this round!")
    print("Game over! Computer wins: ", computer_wins, " User wins: ", user_wins)

def main():
     get_prediction()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

