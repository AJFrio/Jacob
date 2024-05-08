from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs

key = "615130847087d080f81d744df4515671"



with open("prime.txt", "r") as f:
    prime = f.read().replace("\n", " ")
    f.close()

print(prime)