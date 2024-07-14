import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)