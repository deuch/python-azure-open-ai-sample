# Azure ML Python sample with Azure Open AI

This repository provides very simple sample to use a notebook with Azure ML to connect and use Azure Open AI.

**sample_mi.py** uses a managed identity to authenticate to Open AI directly.

**sample_mi_kv.py** uses a managed identity to connect to a KeyVault to retrieve a secret.  
This secret stores the api token of your Azure Open AI resource. This api key is used to connect to Azure OpenAI

## Getting Started

### 1. Azure deployment

- Create an Azure ML Workspace and the compute
- Choose Python 3.8 Azure ML as kernel
- Assign an identity to the compute (system or managed)
- Add the Role Assignement to the Azure Open AI and/or KeyVault targeted resources
    - For Azure Open AI, use "Cognitive Service User" as Role
    - For KeyVault "Keyvault Secrets User" as Role
    - With System Assigned Identity, you need to use the principal named **\<azure_ml_workspace_name\>/compute/\<vm_name\>** for the role assignment

### 2. Python dependencies

Install dependencies in the notebook :

* !pip install openai
* !pip install azure-identity
* !pip install azure-keyvault-secrets

### 3. Set up the variables

In the notebook, please provide those informations :
* openai.api_base = "**\<URL of Azure OpenAI instance\>**"
* openai.api_version = "**\<API version for Azure Open AI\>**"
* engine = "**\<Name of your model deployment\>**"
* KVUri = "**\<KeyVault URL\>**"
* retrieved_secret = client.get_secret("**\<Secret name in KeyVault for azure open ai key\>**")



