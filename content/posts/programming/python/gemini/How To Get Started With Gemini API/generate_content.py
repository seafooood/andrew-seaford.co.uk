# Code is based on the example from https://ai.google.dev/gemini-api/docs/quickstart?lang=python

import google.generativeai as genai
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    genai.configure(api_key=os.getenv("GEMINI_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    print(response.text)