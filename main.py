import ollama
from elevenlabs import Voice, VoiceSettings, play, stream
from elevenlabs.client import ElevenLabs
import functions as fn
import jacob

elevenKey = "615130847087d080f81d744df4515671"
openaiKey = "sk-proj-ZinofvFZMLSPSwWq5RY4T3BlbkFJjlFdVV6ezkDzW3S9TPEL"

jacob = jacob.Jacob(elevenKey=elevenKey, openaiKey=openaiKey)

with open("catPrime.txt", "r") as f:
    catPrime = f.read().replace("\n", " ")
    f.close()

with open("convoPrime.txt", "r") as f:
    convoPrime = f.read().replace("\n", " ")
    f.close()

cat = [{'role': 'system', 'content': catPrime}]
convo = [{'role': 'system', 'content': convoPrime}]

client = ElevenLabs(
  api_key=elevenKey, # Defaults to ELEVEN_API_KEY
)

def speak(text: str):
    audio = client.generate(
        text=text,
        voice=Voice(
            voice_id='EXAVITQu4vr4xnSDxMaL',
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        )
    )
    play(audio)
"""
def speak(text: str):
    audio_stream = client.generate(
    text=text,
    stream=True
    )
    stream(audio_stream)
"""


def respond(response: str):
    print(response)
    #speak(response)

def categorize(sentence: str) -> str:
    category = ollama.chat(model='openai', messages=[{'role': 'user', 'content': catPrime + sentence}])
    return category['message']['content']

def ask(sentence: str  = "hello") -> str:
    global convo
    convo.append({
        'role': 'user',
        'content': sentence,
    })
    response = jacob.chat(sentence, convo, model='llama3')
    convo.append({'role': 'assistant', 'content': response})
    return response

while True:
    q = input(">>>")
    checker = categorize(q)
    print(checker)
    if checker == "[]":
        respond(ask(q))
    elif checker.split('"')[1] == "equationSolver":
        respond(fn.equationSolver(checker.split('"')[5]))
    elif checker.split('"')[1] == "createModel":
        respond(fn.createModel(checker.split('"')[5]))
    elif checker.split('"')[1] == "createProgram":
        respond(fn.createProgram(checker.split('"')[5]))
    elif checker.split('"')[1] == "createScript":
        respond(fn.createScript(checker.split('"')[5], checker.split('"')[9]))
    print(convo)



