import random
import ollama
import string

# All the fancy addons go in this file. the bot will referance this for specific functions

def equationSolver(equation: str) -> float:
    # This function will solve the equation given to it.
    # It will return the answer
    pass

def createProgram(description: str) -> str:
    # This function will create a program with the given description and code
    # It will return the file path of the program
    pass

def createScript(description: str, filepath: str)-> str:
    #Appends code to an existing file
    """with open(filepath, "r") as f:
        fileData = f.read()
        f.close()"""
    convo = [{'role': 'system', 'content': f"Here is a description for a script to be created: {description} Only respond with the code."}]
    response = ollama.chat(model='llama3', messages=convo)['message']['content']
    if "`" in response:
        response = response.split("```")[1]
    if "python" in response:
        response = response.split("python")[1]
    #print(response)
    with open(f"programs/{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}.py", "w") as f:
        f.write(response)
        f.close()
    return response


def createModel(description: str) -> str:
    #Using openscad, it will create a model with the given description and dimensions
    #Returns the file path
    insert = "The following is a description for a part to be made in OpenScad. Model it as best as possible. \n" + description
    convo = []
    convo.append({
        'role': 'user',
        'content': insert,
    })
    response = ollama.chat(model='llama3', messages=convo)
    with open(f"models/{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}.txt", "w") as f:
        f.write(response ['message']['content'])
        f.close()
    return response ['message']['content']