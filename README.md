# Azure ML Python sample with Azure Open AI

This repository provides very simple sample to use a notebook with Azure ML to connect and use Azure Open AI.

## Getting Started

Create an Azure ML Workspace.  
Assign an identity to the compute (system or managed). Do not forget to add a Role Assignement to the Azure Open AI and/or KeyVault targeted resources.

For Azure Open AI, use "Cognitive Service User", and for KeyVault "Keyvault Secrets User"

In the notebook, please provide those informations :
* openai.api_base = <URL of Azure OpenAI instance>
* openai.api_version = <API version for Azure Open AI>
* engine = <Name of your model deployment>
* KVUri = <KeyVault URL>
* retrieved_secret = client.get_secret(<Secret name in KeyVault for azure open ai key>)



