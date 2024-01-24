from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
# import openai
import SpryngtimeOpenAI as openai
# from openai import OpenAI




# client = OpenAI()
openai.api_key = str(os.getenv("AZURE_OPENAI_KEY"))
print(os.getenv("AZURE_OPENAI_KEY"))
openai.api_base = str(os.getenv("AZURE_OPENAI_ENDPOINT")) # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this might change in the future

deployment_name='gpt-35-turbo' #This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
print('Sending a test completion job')
response = openai.ChatCompletion.create(
    engine="gpt-35-turbo", # engine = "deployment_name".
    messages=[
        {"role": "user", "content": "What is 5*2"},
    ],
max_tokens=20,
    # custom_properties={"test": "test"}
)
text = response['choices'][0]['message']['content']
print(text)
print(response)


embed = openai.Embedding.create(input=["Testing"],
            engine="text-embedding-ada-002")
print(embed)