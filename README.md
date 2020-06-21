# CNN_AR-Sandbox

### Table of contents
1. [Software requirements](#software-requirements)
2. [Source files description](#source-files-description)

### Software requirements
- Python 2.7
- [Keras 2.4.2](https://pypi.org/project/Keras/): Deep learning API for Python
- [Pyttsx 1.1](https://pypi.org/project/pyttsx/): Text-to-speech engine for Python
- [wxPython](https://pypi.org/project/wxPython/): GUI toolkit for Python
- [imutils](https://pypi.org/project/imutils/): Image processing library for Python
- [Opencv for python 4.2.0.34](https://pypi.org/project/opencv-python/)
- [Numpy](https://pypi.org/project/numpy/)

### Source files description

| File name  | Description |
| :---: | :---: |
| core_Entrenador.py  | Link Datos and Modelo files to train the model |
| Datos.py  | Upload test and training data (images) to the CNN |
| Modelo.py  | Convolutional Neural Network model definition |

| File name  | Description |
| :---: | :---: |
| core_prediction.py  | Load trained model and use color_space.py for input image |
| color_space.py  | Color Space segmentation method execution |
