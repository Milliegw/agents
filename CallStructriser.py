# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 09:33:54 2025

@author: crjones
"""
import os
import subprocess
from langchain.prompts import PromptTemplate
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from langchain_core.messages import HumanMessage, SystemMessage



def run_structurizr(action="inspect", dslFile="test.dsl"):
    cmd = [  
        "docker", "run",  
        "--rm",  
        # Remove -it flags to avoid TTY errors when capturing output  
        "-v", f"{os.getcwd()}:/usr/local/structurizr",  
        "structurizr/cli",  
        action,  
        "-w", dslFile  
    ]  
    
    result = subprocess.run(cmd, capture_output=True, text=True)  
    if result.returncode == 0:  
        # If there's an error, you might want to raise an exception  
        # or return stderr instead. Adjust as needed.  
        return 200
    
    return result.stdout  
 
run_structurizr(action="validate")
run_structurizr(action="inspect")


model = AzureAIChatCompletionsModel(
    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
    model_name="gpt-4o"
)





messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)


