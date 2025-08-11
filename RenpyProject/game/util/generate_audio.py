import os
import re
from elevenlabs.client import ElevenLabs
from elevenlabs import save

# Set the ElevenLabs API key
api_key = "sk_db3c899d4c903d74f283631bbfb0622f7cf07e584ccc04c4"  # ElevenLabs API 
client = ElevenLabs(api_key=api_key)

# Read the intro_scene.rpy file
with open("../scenarios/locker_scene.rpy", "r", encoding="utf-8") as file:
    script_content = file.read()

# The regular expression matches the dialogue
dialogue_pattern = re.compile(r'^\s*e\s+"([^"]+)"', re.MULTILINE)
dialogues = dialogue_pattern.findall(script_content)

# Generate audio files
for i, dialogue in enumerate(dialogues, start=1):
    # Generate the audio file name
    audio_filename = f"audio/locker_scene_e_{i:02d}.mp3"

    # Use ElevenLabs to generate female voices
    audio = client.generate(
        text=dialogue,
        voice="Jessica",  
        model="eleven_monolingual_v1" 
    )

    # Save the audio file
    save(audio, audio_filename)
    print(f"Generated: {audio_filename}")

print("All audio files generated successfully!")