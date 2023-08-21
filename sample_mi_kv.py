#Note: The openai-python library support for Azure OpenAI is in preview.
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
import os
import openai

openai.api_type = "azure"
openai.api_base = "<URL of Azure OpenAI instance>"
openai.api_version = "<API version for Azure Open AI>"

mi_id=os.environ.get("DEFAULT_IDENTITY_CLIENT_ID")

default_credential = ManagedIdentityCredential(client_id=mi_id)

# KeyVault Part to retrieve secret
KVUri = "<KeyVault URL>"

# Set the client with the KV and the mi credential class
client = SecretClient(vault_url=KVUri, credential=default_credential)

print("Retrieving your secret oai-key")

# Retrieved secret
retrieved_secret = client.get_secret("<Secret name in KeyVault for azure open ai key>")

# Set the keyvault secret as api token for aoai
openai.api_key = retrieved_secret.value

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
