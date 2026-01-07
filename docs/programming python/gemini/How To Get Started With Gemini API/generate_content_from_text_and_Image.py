# Code based on the example from https://ai.google.dev/gemini-api/docs/text-generation?_gl=1*1jqyj3n*_up*MQ..*_ga*MTEyNDQyODE5MC4xNzMzMzYwMjE5*_ga_P1DBVKWT6V*MTczMzM2MDIxOC4xLjAuMTczMzM2MDIxOC4wLjAuNzQ1MzcyMTU5&lang=python#generate-text-from-text-and-image

# pip install -q -U google-generativeai
import google.generativeai as genai

import PIL.Image
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    genai.configure(api_key=os.getenv("GEMINI_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    car = PIL.Image.open(r"IMG-20231024-WA0026.jpg")
    response = model.generate_content(["Tell me about this car", car])
    print(response.text)