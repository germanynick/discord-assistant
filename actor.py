
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import os

print(tf.__version__)
model = tf.keras.models.load_model("models/actor/model_v5.h5")
mapping = pd.read_csv("models/actor/index_to_label_map.csv")


def predict_from_directory(directory):

    images = []
    for filename in os.listdir(directory):
        image = Image.open(os.path.join(directory, filename))
        image = image.convert('RGB')
        image = image.resize((180, 180))
        images.append(np.array(image, dtype=np.uint8))
    
    inputs = np.array(images, dtype=np.uint8)
    outputs = model.predict(inputs)

    indices= np.argmax(outputs, axis=1)    

    labels = [mapping.iloc[index].loc['Label'] for index in indices]


    names = [label.split("/")[0].replace("_", " ") for label in labels]
    
    names = list(set(names))
    names = ", ".join(names)
    
    return names, 
