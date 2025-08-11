# Dialogue Sound Effects System
# file contains functions for playing dialogue sound effects and managing voice acting

# Register the dialogue sound effects channel during initialization
init:
    # Register a channel for dialogue sound effects
    $ renpy.audio.audio.register_channel("dialogue_sfx", mixer="sfx", loop=True)

init python:
    # Import necessary modules
    import random
    
    # Variables to track dialogue sound effects
    dialogue_sound_playing = False
    
    # Function to start playing dialogue sound effects
    def play_dialogue_sound():
        global dialogue_sound_playing
        
        # Only play if dialogue sound effects are enabled
        if persistent.dialogue_sfx_enabled:
            # Choose a random pen sound
            sound_file = random.choice(["audio/dialogue/Pen_v4_wav.wav", "audio/dialogue/Pen_v5_wav.wav"])
            
            # Play the sound on the dialogue sound channel
            renpy.sound.play(sound_file, channel="dialogue_sfx", loop=True)
            dialogue_sound_playing = True
    
    # Function to stop playing dialogue sound effects
    def stop_dialogue_sound():
        global dialogue_sound_playing
        
        # Stop the sound if it's playing
        if dialogue_sound_playing:
            renpy.sound.stop(channel="dialogue_sfx")
            dialogue_sound_playing = False
    
    # Function to update voice channel based on text-to-speech setting
    def update_voice_channel():
        # If text-to-speech is disabled, mute the voice channel
        if not persistent.tts_enabled:
            renpy.music.set_volume(0, channel="voice")
        else:
            # If text-to-speech is enabled, unmute the voice channel
            renpy.music.set_volume(1, channel="voice")
    
    # Callback function for dialogue events
    def dialogue_callback(event, interact=True, **kwargs):
        if interact:
            if event == "begin":
                # Update voice channel based on text-to-speech setting
                update_voice_channel()
                
                # Start playing dialogue sound effects when text starts displaying
                if persistent.dialogue_sfx_enabled:
                    play_dialogue_sound()
            
            elif event == "end" or event == "slow_done":
                # Stop playing dialogue sound effects when text is done displaying
                # or when the text is fully displayed (slow_done)
                if dialogue_sound_playing:
                    stop_dialogue_sound()
    
    # Add the dialogue_callback function to the character callbacks
    config.all_character_callbacks.append(dialogue_callback)
    
    # Initialize voice channel based on initial text-to-speech setting
    def initialize_voice_channel():
        update_voice_channel()
    
    # Call initialize_voice_channel when the game starts
    config.start_callbacks.append(initialize_voice_channel)
