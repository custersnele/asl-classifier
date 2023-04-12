from flask import Flask, request, make_response, render_template
import numpy as np
from keras.utils import load_img, img_to_array
import os
import PIL
from PIL import Image
from keras.models import load_model

app = Flask(__name__)

# set paths to upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['IMAGE_UPLOADS'] = os.path.join(APP_ROOT, 'static')


@app.route("/image-classifier", methods=["POST"])
def classify_image():
    print("in post")
    # read and upload resized files to folder
    print(request.files)
    image = request.files['file']
    filename = image.filename
    file_path = os.path.join('/uploads/', filename)
    image_pil = Image.open(image)
    image_pil.thumbnail((600, 300), Image.ANTIALIAS)
    image_pil.save(file_path)

    # classify image
    image = load_img('/uploads/' + filename, target_size=(64, 64))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction = asl_model.predict(image)
    prediction = label_map[np.argmax(prediction)]

    # display prediction and image
    return prediction


if __name__ == '__main__':
    asl_model = load_model('resources/asl_cnn_model_v1.h5')
    class_indices = np.load('resources/asl_labels.npy', allow_pickle=True).item()
    label_map = dict((v, k) for k, v in class_indices.items())
    app.run(host='0.0.0.0', debug=False, threaded=False, port=8000)