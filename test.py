from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs

key = "615130847087d080f81d744df4515671"



client = ElevenLabs(
  api_key=key, # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
    text="Hello! My name is Bella.",
    voice=Voice(
        voice_id='EXAVITQu4vr4xnSDxMaL',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio)