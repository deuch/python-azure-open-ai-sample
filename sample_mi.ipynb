#Note: The openai-python library support for Azure OpenAI is in preview.
from azure.identity import ManagedIdentityCredential
import os
import openai
openai.api_type = "azure_ad"
openai.api_base = "<URL of Azure OpenAI instance>"
openai.api_version = "<API version for Azure Open AI>"

mi_id=os.environ.get("DEFAULT_IDENTITY_CLIENT_ID")

default_credential = ManagedIdentityCredential(client_id=mi_id)

token = default_credential.get_token("https://cognitiveservices.azure.com")
openai.api_key = token.token

response = openai.ChatCompletion.create(
  engine="<Name of your model deployment>",
  messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},         {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},{"role": "user", "content": "Do other Azure AI services support this too?"}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response)
print(response['choices'][0]['message']['content'])
