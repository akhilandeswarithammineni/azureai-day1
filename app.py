!pip install openai
! pip install azure-ai-ml
!python -m pip install azure-identity
from openai import AzureOpenAI
endpoint = "https://25695a3201-2301-resource.services.ai.azure.com/api/projects/25695a3201-2301"
api_key = "C46Hj82fsbco8MyWQvIBjr4jWRGiRONzslwAjNpUCfYcz0UimZ8nJQQJ99CKACE1PydXJ3w3AAAAACOGw0Bl"
deployment_name = "gpt-5-mini"
from openai import OpenAI
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://25695a3201-2301-resource.services.ai.azure.com/",
    api_key=api_key,
    api_version="2024-10-21",
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "india prime minister"}
    ],
)

print(response.choices[0].message.content)