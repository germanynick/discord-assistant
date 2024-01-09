
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import os

print(tf.__version__)
model = tf.keras.models.load_model("models/actor/model_v5.h5")
names_mapping = pd.read_csv("models/actor/mapping.csv",)


def predict_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        image = Image.open(os.path.join(directory, filename)).convert('RGB').resize((180, 180))
        images.append(np.array(image, dtype=np.uint8))
    
    inputs = np.array(images, dtype=np.uint8)
    outputs = model.predict(inputs)

    indices = np.argmax(outputs, axis=1)

    names = names_mapping.iloc[indices]
    names['Role'] = pd.Categorical(names['Role'], ["Tank", "Dame", "Support"])

    names = names.sort_values("Role")
    names = names["Name"].values.tolist()

    message = ", ".join(names)
    
    return message