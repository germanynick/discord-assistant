
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import os

print(tf.__version__)
model = tf.keras.models.load_model("models/actor/model_v7.h5")
names_mapping = pd.read_csv("models/actor/mapping.csv")
names_mapping['Role'] = pd.Categorical(names_mapping['Role'], ["Tank", "Dame", "Support"])


def predict_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image = Image.open(os.path.join(directory, filename)).convert('RGBA')
            
            image_with_white_bg = Image.new("RGBA", image.size, (255, 255, 255))
            x, y = image.size
            image_with_white_bg.paste(image, (0, 0, x, y), image)

            image = image_with_white_bg.convert('RGB')
            
            image = image.resize((180, 180))
            images.append(np.array(image, dtype=np.uint8))

    inputs = np.array(images, dtype=np.uint8)
    outputs = model.predict(inputs)

    indices = np.argmax(outputs, axis=1)

    names = names_mapping.iloc[indices]
    
    # print(names)

    names = names.sort_values("Role")
    names = list(set(names["Name"].values))

    message = ", ".join(names)
    
    return message
