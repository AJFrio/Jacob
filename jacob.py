# This fiule will have a class that will hold all the LLMs

import ollama
from openai import OpenAI

class Jacob:
    def __init__(self, elevenKey: str, openaiKey: str):
        self.elevenKey = elevenKey
        self.openaiKey = openaiKey
        self.openaiClient = OpenAI(api_key = openaiKey)
        

    def chat(self, sentence: str, prime: list, model = 'llama3') -> str:
        if model == 'llama3':
            return self.useOllama(sentence, prime, model)
        elif model == 'llama2':
            return self.useOllama(sentence, prime, model)
        elif model == 'openai':
            return self.useOpenAI(sentence, prime)

    def useOllama(self, sentence: str, prime: list, modelName: str) -> str:
        return ollama.chat(model=modelName, messages=[{'role': 'user', 'content': sentence}])['message']['content']
    
    def useOpenAI(self, sentence: str, prime: str) -> str:
        builtMessages = []
        builtMessages.append({'role': 'system', 'content': prime})
        

        completion = self.openaiClient.chat.completions.create(
        model="gpt-4o",
        messages=[
                {"role": "system", "content": "You are an assistant to help with coding projects. When given a description for a project, create it. if no language is specified, use Python. If no description is given, ask for one."},
                {"role": "user", "content": "Create a program that finds the bollinger bands of a stock."}
            ]
        )
        print(completion.choices[0].message)

elevenKey = "615130847087d080f81d744df4515671"
openaiKey = "sk-proj-ZinofvFZMLSPSwWq5RY4T3BlbkFJjlFdVV6ezkDzW3S9TPEL"

jacob = Jacob(elevenKey=elevenKey, openaiKey=openaiKey)

jacob.chat("hello", [{'role': 'system', 'content': "hello"}], model='openai')