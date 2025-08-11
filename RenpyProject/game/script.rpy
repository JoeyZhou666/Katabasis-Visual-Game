# *********************************************************************
# Interactive Story Game: Overview & Developer Notes
#
# Overview:
# This Ren'Py script presents an interactive narrative where the player,
# identified as [povname], navigates the complexities of school life.
# Throughout the story, you'll encounter various scenarios involving
# peer interactions, teacher confrontations, and bullying situations.
# Each decision you make influences the storyline and shapes your character's
# emotional journey, encouraging reflection and self-awareness.
#
# Developer Notes:
# - The script is organized into labeled sections such as "start", "near_friends",
#   "isolated", "assigned", and various reaction and reflection labels.
# - Comments have been added throughout the code to describe each section's purpose.
# - This structure is designed for easy maintenance and future expansion.
#
# *********************************************************************

# Define characters with their respective display names
define e = Character("Mousy", callback=name_callback, cb_name="mousy")               # Main character: Mousy
define pov = Character("[povname]", callback=name_callback, cb_name=None)          # Protagonist; name provided by the player
define f = Character("Bandit", callback=name_callback, cb_name="bandit")               # Friend character (Bandit)
define t = Character("Ms. Johnson", callback=name_callback, cb_name="teacher")          # Teacher character
define n = Character("Narratage", callback=name_callback, cb_name=None)          # Narratage character (setting cb_name to None makes all sprites unfocused)
define d = Character("Crusher", callback=name_callback, cb_name="crusher")                    # Dog character (bully)
define a = Character("Administrator", callback=name_callback, cb_name="administrator")  # Administrator character (Donkey)

# Set default game variables for weather and background color
default bg_weather = "Sunny"                 # Default weather is sunny
default bg_color = "Green"                   # Default background color is green
define previous_day = ""

# Define images used in the game
image classroom = "images/classroom.png"             # Classroom image
image bg classroom5 = "images/classroom5.png"
image hallway3 = "images/hallway3.png"                 # Hallway3 image
image bg hallway9 = "images/bg hallway9.png"
image bg office = "images/bg office.png"
image bg cafeteria = "images/cafe.png"
image bg classroom = "images/bg classroom.png"         # Alternate classroom background image
image bg lockers = "images/lockers.png"                # Lockers background image
image note = "images/sticky_note.png"  
image bg lockers = "images/lockers.png"                # Lockers background image
image bg lockersblurred = "images/lockersblurred.png"    # Blurred lockers background image
image trash_bin = "images/trash_bin.png"  

# Define transition effects for scene changes
define in_eye = ImageDissolve("images/eye.png", 3.0)         # Transition when entering a scene
define out_eye = ImageDissolve("images/eye.png", 3.0, reverse=True)  # Transition when exiting a scene

# Define character expression images for Mousy, teacher, friend, and others
image ms = At("images/mousy smile.png", sprite_highlight("mousy"))         # Mousy smiling expression
image mh = At("images/mousy happy.png", sprite_highlight("mousy"))          # Mousy happy expression
image msad = At("images/mousy sad.png", sprite_highlight("mousy"))          # Mousy sad expression

image t = At("images/teacher.png", sprite_highlight("teacher"))               # Teacher image
image ts = At("images/teacher_surprised.png", sprite_highlight("teacher"))    # Teacher surprised expression

image f = At("images/raccoon.png", sprite_highlight("bandit"))               # Friend (Raccoon) image
image fs = At("images/raccoon_surprised.png", sprite_highlight("bandit"))    # Friend surprised expression

image d = At("images/dog_mocks.png", sprite_highlight("crusher"))             # Dog mocking expression
image ds = At("images/dog_serious.png", sprite_highlight("crusher"))          # Dog serious expression

image ac = At("images/donkey_chill.png", sprite_highlight("administrator"), Transform(zoom=0.5))  # Administrator calm expression
image ashock = At("images/donkey_shock.png", sprite_highlight("administrator"), Transform(zoom=0.5))  # Administrator shocked expression

# *********************************************************************
# GAME START: INTRODUCTION & CHARACTER INTERACTION
# *********************************************************************
label start:
    # Show the text-to-speech settings screen before starting the game
    call screen tts_settings
    
call intro_scene

# *********************************************************************
# Classroom conflict Scene
# *********************************************************************

call classroom_conflict

# *********************************************************************
# Elopement Scene
# *********************************************************************

call elopement_scene

# *********************************************************************
# Emotional Outburst Scene
# *********************************************************************

call emotional_outburst_scene

# *********************************************************************
# Disruptive scene
# *********************************************************************

call disruptive_scene


# *********************************************************************
# Game end: Call cdd tool
# *********************************************************************
call cdd_tool_scene
