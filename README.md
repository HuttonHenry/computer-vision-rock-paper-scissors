# Computer Vision Rock / Paper / Scissors

This is a new project from AiCore which starts the journey into ML.

## The Teachable Machine.

The "teachable machine" is a web-based application created by Google that allows users to train a machine learning model using their own data. The model can be trained to recognize images, sounds, or poses using a webcam or microphone. The user can upload their own data, train the model using that data, and then test the model's performance by providing new examples. The goal of this application is to make machine learning more accessible and understandable to non-experts.

### Eye Opening.

Really impresssed by this task already.

### The Python environment I've used for this is called RPSML

(Rock Paper Scissors ML)

I have specified Python 3.8 for this virtual environemnt.

TensorFlow wouldn't install, so I found this on StackOverFlow:

pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl


This is what the script does:

This script imports the OpenCV library, the Keras deep learning library, and the NumPy library. It loads a pre-trained Keras model called 'keras_model.h5' and captures video from the default camera (indicated by the parameter '0' in cv2.VideoCapture(0)). It then continuously captures frames from the video, resizes them to (224, 224), normalizes the pixel values, and uses the loaded model to make predictions on the image data. The script also displays each frame of the video and continuously prints out the model's predictions. The script can be closed by pressing the 'q' key.





