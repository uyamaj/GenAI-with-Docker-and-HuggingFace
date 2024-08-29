from fastapi import FastAPI
from transformers import pipeline

#create a new fastAPI app instance
app=FastAPI()

#initiate the text generation pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return{"message":"Hello World"}

#Define a function to handle the GET request as '/generate'

@app.get("/generate")
def generate(text:str):
    ##use the pipleline to generate text from input text
    output =pipe(text)

    ##return the generated text in json response
    return {"output":output[0]['generated_text']}




