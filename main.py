import ollama

convo = {}

def ask(sentence: str) -> str:
    global convo
    response = ollama.chat(model='llama2', messages=[
        {
            'role': 'user',
            'content': convo,
        },
    ])
    return response['message']['content']
