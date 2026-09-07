# Developer: Dessaure, Terrance
# Project: Angentic_API 


# test_key.py

from dotenv import load_dotenv
import os
import httpx2 as httpx
from anthropic import Anthropic

# This looks for a .env file in the current working directory
# and loads its contents into the environment
load_dotenv()
client = Anthropic()

custom_http_client = httpx.Client(
    headers={"Accept-Encoding": "gzip, deflate"}
)

client = Anthropic(http_client=custom_http_client)

# The actual function - pure Python does the real work
def get_weather(city: str) -> str:
    return f'It is sunny in {city}'

# Piece 2: the schema — a plain dictionary describing that function to the LLM
weather_tool = {
    "name": "get_weather",
    "description": "Use this when someone wants to know current weather condition for a city. ",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "The name of the city to check  the weather for, e.g. 'Charlestion' or 'New York'"}
        },
        "required": ["city"]
    }
}

def summarize_text(text: str) -> str:
    return text.split(".")[0]

summarize_tool= {
    "name": "summarize_text",
    "description": "Use if the user give you a block of text and wants a shorter version of it",
    "input_schema": {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "Return the summary of the block of text that is sent by the user."}
            },
        "required": ["text"]
    }
}

# Bundle them into a list — this is what we'll hand to Claude
tools = [weather_tool, summarize_tool]

tool_map = {
    "get_weather": get_weather,
    "summarize_text" : summarize_text,   
    }

while True:
    user_input = input("You: ")
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        tools=tools,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print(response.content)

    for block in response.content:
        
        if block.type == 'tool_use':
            func = tool_map[block.name]
            result = func(**block.input)
            print(result)
            
        elif block.type == 'text':
            print(block.text)
        





