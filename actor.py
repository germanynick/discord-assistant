
import tensorflow as tf
import numpy as np
import pandas as pd

print(tf.__version__)
model = tf.keras.models.load_model("models/actor/model.h5")
mapping = pd.read_csv("models/actor/index_to_label_map.csv")

def predict(image):
    image = tf.image.resize(image, (180, 180))
    inputs = np.expand_dims(image, axis=0)
    outputs = model.predict(inputs)
    index = np.argmax(outputs[0])
    return mapping.iloc[index].loc['Label']
    


