#Using trasnformers and functions call  to return the message or call the function

#Trelis/Mixtral-8x7B-Instruct-v0.1-function-calling-v3

from transformers import pipeline

generator = pipeline("text-generation")

def generate_text(text):
    output = generator(text, max_length=100, temperature=0.9)
    return output[0]["generated_text"]


