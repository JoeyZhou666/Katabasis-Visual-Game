# *********************************************************************
# GAME START: INTRODUCTION & CHARACTER INTERACTION
# *********************************************************************

# Define the screen for sticky note interaction
screen sticky_note_interaction():
    modal True  # Makes the screen modal, blocking other interactions
    
    # Add the sticky note image
    add "images/sticky_note.png":
        xpos 400
        ypos 300
    
    # Add the trash bin image
    add "images/trash_bin.png":
        xpos 800  # Adjust to match the position of the trash bin
        ypos 500
    
    # Create a menu for user interaction
    vbox:
        xpos 400
        ypos 500
        spacing 10
        
        # Option to ignore the note
        textbutton "Ignore":
            action Return("ignore")
        
        # Option to throw the note into the trash bin
        textbutton "Throw":
            action Return("throw")

# Define the animation for the note flying into the trash bin
transform rotate_and_fly(start_x, start_y):
    # Initial position
    xpos start_x
    ypos start_y
    rotate 0
    alpha 1.0
    zoom 1.0  # Start at normal size

    # Rotate 360 degrees while shrinking to 50% size
    linear 1.0 rotate 360 zoom 0.5  # Rotate and shrink

    # Fly to the trash bin position (xpos 800, ypos 600) while rotating
    linear 1.5 xpos 800 ypos 600 rotate 720  # Fly to the trash bin while spinning

    # Step 3: Fade out after reaching the trash bin
    linear 0.5 alpha 0.0  # Fade out after reaching the trash bin

label locker_scene:

    n "*clink!*"

    # The character reacts to their locker being opened
    
    voice "audio/locker_scene_e_01.mp3"
    e "Oop! Looks like I just got my locker opened, time to get my stuff!"

    voice "audio/locker_scene_e_02.mp3"
    e "..."

    show note:
            xpos 400
            ypos 300

    voice "audio/locker_scene_e_03.mp3"
    e "Hmm... what's this?"

    # Change the character's expression to sad and display the sticky note
    hide ms
    show msad
    voice "audio/locker_scene_e_04.mp3"
    e "On a sticky note coming from the inside of my locker that reads, 'you smell like a dog!'"

    voice "audio/locker_scene_e_05.mp3"
    e "Ugh! Some people don't know how to leave someone alone!"
        
    hide msad
    hide note
    
    # Show the sticky note interaction screen
    call screen sticky_note_interaction
    
    # Handle the user's choice
    $ choice = _return
    
    if choice == "ignore":
        voice "audio/locker_scene_e_06.mp3"
        e "You decided to ignore the sticky note."
    elif choice == "throw":
        # Animate the note flying into the trash bin
        show trash_bin:
            xpos 800  # X position of the trash bin
            ypos 500  # Y position of the trash bin
        show note at rotate_and_fly(400, 300)
        pause 2.5  # Wait for the animation to complete
        hide note
        hide trash_bin
        voice "audio/locker_scene_e_07.mp3"
        e "You threw the sticky note."

    show mh

    voice "audio/locker_scene_e_08.mp3"
    e "Well, I won't let that bother me. Time to focus on the day ahead!"
    
# *********************************************************************
# Scene
# *********************************************************************
# *********************************************************************
# Curiosity Menu: Who or Why?
# *********************************************************************
menu:
    "Who did that?":
        $ curious = "who"
    "Why would someone do that?":
        $ curious = "why"

# Branch based on player's curiosity choice
if curious == "who":
    voice "audio/locker_scene_e_09.mp3"
    e "It's just some peers who don't like me for some reason."

    voice "audio/locker_scene_e_10.mp3"
    e "They've been picking on me, and I'm not quite sure how to handle them..."
elif curious == "why":
    voice "audio/locker_scene_e_11.mp3"
    e "I don't know! :( Some peers just think I'm not worth any respect!"

# *********************************************************************
# Decision on Reporting the Incident
# *********************************************************************

    voice "audio/locker_scene_e_12.mp3"
e "Should I tell someone about this?"
menu:
    "You have to! Tell the teacher, that is not okay.":
        $ tell = "yes"
    "Maybe if it gets worse, but right now, maybe just ignore them":
        $ tell = "later"
    "No way! That'll make it worse, better to handle it yourself":
        $ tell = "no"

# Branch based on the decision to report
if tell == "yes":
 
    voice "audio/locker_scene_e_13.mp3"
    e "Hmm, I wonder if that's the right thing to do. Sometimes I feel like the teachers don't help me."
elif tell == "later":

    voice "audio/locker_scene_e_14.mp3"
    e "I'll try to, hopefully that was the last of them."
elif tell == "no":

    voice "audio/locker_scene_e_15.mp3"
    e "Sometimes I feel that telling the teacher won't make much of a difference anyways."

# *********************************************************************
# Expressing Frustration & Asking for Advice
# *********************************************************************
voice "audio/locker_scene_e_16.mp3"
e "Ugh! I wish there was a way to just make it all go away!"
voice "audio/locker_scene_e_17.mp3"
e "I don't know what to do! What would you do if some peers like them wouldn't stop making fun of you?"
menu:
    "I think I would just deal with it":
        $ action = "deal"
    "Depends on my mood":
        $ action = "mood"
    "I wouldn't let it go! I'd have to say something back!":
        $ action = "conflictprone"
    "I'd try to avoid them entirely":
        $ action = "elope"

# Change the character's expression back to normal
hide mh
show ms

# Branch based on the player's chosen action for handling the situation
if action == "deal":
    voice "audio/locker_scene_e_18.mp3"
    e "I wish I was as strong as you are!"
elif action == "mood":
    voice "audio/locker_scene_e_19.mp3"
    e "They better hope they don't mess with you!"
elif action == "conflictprone":
    voice "audio/locker_scene_e_20.mp3"
    e "Hehe, you may need to be my bodyguard. I wish I was as strong as you are!"
elif action == "elope":
    voice "audio/locker_scene_e_21.mp3"
    e "I suppose that's a good way of dealing with it!"

# We're still at the lockers from the previous scene
scene bg lockers
    
# Bell rings to signal the start of class
n "ding ding ding"
hide ms
show mh    
voice "audio/locker_scene_e_22.mp3"
e "Looks like that's the bell, it was great talking to you!"
voice "audio/locker_scene_e_23.mp3"
e "Anyways, we should be getting to class, wouldn't want to be late, right?"

menu:
    "Yeah, see you later!":
        $ goClass = "yes"
    "Eh, I guess...":
        $ goClass = "moody"
    "I'm gonna take my time!":
        $ goClass = "defiance"
    "I might just skip this one":
        $ goClass = "elope"

# Branch based on the player's attitude toward going to class
if goClass == "yes":
    voice "audio/locker_scene_e_24.mp3"
    e "Awesome! See you later, [povname]!"
elif goClass == "moody":
    voice "audio/locker_scene_e_25.mp3"
    e "It'll get better soon enough. See you later, [povname]!"
else:
    voice "audio/locker_scene_e_26.mp3"
    e "Hehe, okay good luck you troublemaker! Bye, [povname]!"
    
    return
