# Imports the Computer Vision libary, started by Intel in 1999. 
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
import cv2

# Kera is a deep learning module for python it appears to be built on top of TensorFlow.
# https://keras.io/

from keras.models import load_model

# The fundamental package for scientific computing with Python
import numpy as np

# Load the model into Keras object
model = load_model('keras_model.h5')
# Place video into CV2 object
cap = cv2.VideoCapture(0)

# Place data into numy object
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
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
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()