
from langchain_openai import ChatOpenAI,AzureChatOpenAI
from openai import OpenAI
from pydantic import SecretStr
from app.config.settings import Settings

class ModelService:
    def __init__(self, settings: Settings):
        self.settings = settings

    def invoke(self):
        # llm = ChatOpenAI(
        #     model=self.model_name,
        #     temperature=self.temperature,
        #     streaming=True
        if self.settings.azure_openai_key is None:
            raise ValueError("azure_openai_key must be set in the config before invoking the model")
        llm = AzureChatOpenAI(
            azure_deployment=self.settings.azure_openai_deployment,
            azure_endpoint=self.settings.azure_openai_endpoint,
            api_key=SecretStr(self.settings.azure_openai_key),             
            temperature=1.0,
            api_version="2024-12-01-preview",            
            streaming=True
        )
       
        return llm
    

 