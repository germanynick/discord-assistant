#Using trasnformers and functions call  to return the message or call the function

#Trelis/Mixtral-8x7B-Instruct-v0.1-function-calling-v3

from transformers import pipeline, AutoTokenizer

generator = pipeline("text-generation")

#TODO: using function calling model
# tokenizer = AutoTokenizer.from_pretrained('Trelis/Llama-2-7b-chat-hf-function-calling-v3', trust_remote_code=True)



def generate_text(text):
    output = generator(text, max_length=100, temperature=0.9)
    return output[0]["generated_text"]

