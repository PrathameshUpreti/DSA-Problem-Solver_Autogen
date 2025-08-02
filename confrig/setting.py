import os
from dotenv import load_dotenv
from confrig.storedvar import Model

load_dotenv()

from autogen_ext.models.openai import OpenAIChatCompletionClient

api_key=os.getenv("OPENAI_API_KEY")

def get_model():
    model_client=OpenAIChatCompletionClient(api_key=api_key,model=Model)
    return model_client

