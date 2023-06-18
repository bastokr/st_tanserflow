from flask import Flask, jsonify, request
from flask_cors import CORS
import keras
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)

# MNIST 학습 모델 https://www.tensorflow.org/tutorials/quickstart/beginner?hl=ko

def ajaxImage(imageSize):
    #content = request.values['image'].split(';')[1]
    print(request)
    #image_encoded = content.split(',')[1]
    #body = base64.decodebytes(image_encoded.encode('utf-8'))
    #img = np.array(Image.open(BytesIO(body)).convert("L"))
    #image = cv2.resize(img, imageSize)/255.0
    #image = np.reshape(image, (1, imageSize[0], imageSize[1]))
    return {'a':1}

@app.route('/predict', methods=['GET'])
def ajax():
    image = ajaxImage((28,28))
    ### code 작성 ###
    
@app.route('/test', methods=['POST'])
def test_get():
    data = request.json
    #print(data['image'])
    content = data['image'].split(';')[1]
    #print(request)
    image_encoded = content.split(',')[1]
    body = base64.decodebytes(image_encoded.encode('utf-8'))
    fh = open("imageToSave.png", "wb")
    fh.write(body)
    fh.close()

    img = np.array(Image.open(BytesIO(body)).convert("L"))
    image = cv2.resize(img, (28,28))/255.0
    image = np.reshape(image, (1, (28,28)[0], (28,28)[1]))
   
    new_model = keras.models.load_model('./tf-model.h5')
    predictions=new_model.predict(image)
    print(np.argmax(predictions[0]))
    print(np.argmax(predictions[:10],axis=1))
    print(predictions[0])
    
    
    return jsonify(data) #JSON 형태로 응답을 리턴

if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=False)