import json
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
 
    
@app.route('/predict', methods=['POST'])
def test_get():
    data = request.json
    #print(data['image'])
    content = data['image'].split(';')[1]
    #print(request)
    image_encoded = content.split(',')[1]
    body = base64.decodebytes(image_encoded.encode('utf-8'))
    fh = open("imageToSave.png", "wb") #이미지 파일로 떨거봄 /*서비스 할때 삭제*/
    fh.write(body)
    fh.close()
    # 들어온이미지를 28 28 정사각형 사이즈로  변화
    img = np.array(Image.open(BytesIO(body)).convert("L"))
    image = cv2.resize(img, (28,28))/255.0
    image = np.reshape(image, (1, (28,28)[0], (28,28)[1]))
    # 이미 만들어지 모델을 가져옴 (한습한 데이터)
    new_model = keras.models.load_model('./tf-model.h5')
    predictions=new_model.predict(image)
    print("1",np.argmax(predictions[0])) #가장 근사한 값을 나열한것중 첫벗째 
    print("2",np.argmax(predictions[:10],axis=1))
    print("3",predictions[0])  
    result =int(np.argmax(predictions[0]))
      #return rDate
    return jsonify({
        "greeting": ["hello", "world"],
        "result": result
    })
if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=False)