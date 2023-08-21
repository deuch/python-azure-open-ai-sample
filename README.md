# Azure ML Python sample with Azure Open AI

This repository provides very simple sample to use a notebook with Azure ML to connect and use Azure Open AI.

## Getting Started

- Create an Azure ML Workspace and the compute
- Assign an identity to the compute (system or managed)
- Add the Role Assignement to the Azure Open AI and/or KeyVault targeted resources
    - For Azure Open AI, use "Cognitive Service User" as Role
    - For KeyVault "Keyvault Secrets User" as Role

In the notebook, please provide those informations :
* openai.api_base = "**\<URL of Azure OpenAI instance\>**"
* openai.api_version = "**\<API version for Azure Open AI\>**"
* engine = "**\<Name of your model deployment\>**"
* KVUri = "**\<KeyVault URL\>**"
* retrieved_secret = client.get_secret("**\<Secret name in KeyVault for azure open ai key\>**")



