
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image

print(tf.__version__)
model = tf.keras.models.load_model("models/actor/model_v5.h5")
mapping = pd.read_csv("models/actor/index_to_label_map.csv")

def predict(image):
    image = tf.image.resize(image, (180, 180))
    inputs = np.expand_dims(image, axis=0)
    outputs = model.predict(inputs)
    index = np.argmax(outputs[0])

    #EX: Ascetic_Monk/icon_101014_cb1e8dde41.jpg
    label = mapping.iloc[index].loc['Label']

    #Load full image
    full_image = Image.open("images/" + label)
    full_image = full_image.resize((180, 180))

    name = label.split("/")[0].replace("_", " ")
    return name, full_image
    


