import ollama
from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs

elevenKey = "615130847087d080f81d744df4515671"

convo = []

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


def respond(response: str):
    print(response)
    speak(response)
    
def ask(sentence: str  = "hello") -> str:
    global convo
    convo.append({
        'role': 'user',
        'content': sentence,
    })
    response = ollama.chat(model='llama3', messages=convo)
    convo.append(response ['message'])
    return response ['message']['content']

while True:
    q = input(">>>")
    respond(ask(q))