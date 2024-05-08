
import ollama

# All the fancy addons go in this file. the bot will referance this for specific functions

def equation_solver(equation: str) -> float:
    # This function will solve the equation given to it.
    # It will return the answer
    pass

def createProgram(description: str) -> str:
    # This function will create a program with the given description and code
    # It will return the file path of the program
    pass

def createScript(description: str, filepath: str)-> str:
    #Appends code to an existing file
    pass

def createModel(description: str) -> str:
    #Using openscad, it will create a model with the given description and dimensions
    #Returns the file path
    insert = "The following is a description for a part to be made in OpenScad. Model it as best as possible. Only respond with code for the model, Nothing else. \n" + description
    convo = []
    convo.append({
        'role': 'user',
        'content': insert,
    })
    response = ollama.chat(model='llama3', messages=convo)
    convo.append(response ['message'])
    return response ['message']['content']