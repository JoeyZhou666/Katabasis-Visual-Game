import re

with open("../scenarios/locker_scene.rpy", "r", encoding="utf-8") as file:
    lines = file.readlines()

audio_counter = 1

with open("locker_scene_with_audio.rpy", "w", encoding="utf-8") as file:
    for line in lines:
        match = re.match(r'^\s*e\s+"([^"]+)"', line)
        if match:
            file.write(f'    voice "audio/locker_scene_e_{audio_counter:02d}.mp3"\n')
            audio_counter += 1
        file.write(line)

print("Voice statements added successfully!")