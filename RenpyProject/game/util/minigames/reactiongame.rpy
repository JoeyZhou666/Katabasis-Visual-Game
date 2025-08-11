# **** SCRIPT INFO ****
# This script was made for a free online video tutorial on Youtube for teaching purposes by creator "__ess__ Ren'Py Tutorials".
#
# This finished script is only available to download and use in projects by being a Patreon in the tier "Supporter" or higher on the Patreon page as linked to below.
#
# URL to video tutorial: https://www.youtube.com/watch?v=JwkR_IBcDlA
#
# The script comes with no warranty that it will work as the Ren'Py engine updates/changes.
#
# If you don't understand how something is working in this script, it's recommended you have a look at the tutorial video for more information.
#
# Please, do not redistribute this script for download anywhere. If you wish to share it with others, please link to the Patreon page as specified below.
#
# You may use and adapt this script for your game for personal or commercial purposes.
#
# Patreon page where this script is available: https://www.patreon.com/ess_renpy_tutorials
#
# Images available for this tutorial can be used in your finished commercial or personal projects if you wish.
#
# Update 1.0.2: Updated the screen to change the "image" displayable for the more appropriate "add" statement, as "image" is deprecated but still works. 

init python:
    import random # Importing python random module so we can make a unique random list of numbers.

    def light_button():
        # Function that lights a button up.
        global random_button_indexes
        global current_button_index

        # We want to pick the next value in the "random_button_indexes" list every time this function runs.
        # To do that, we add 1 to the "current_button_index" variable that we then use to pick a value from the list with.
        if current_button_index < buttons - 1:
            # Add 1 to the variable as long as it's value isn't larger than the list size.
            current_button_index += 1
        else:
            # The variable has a value that is the same size as the list, so now we reset it back to 0 and generate a new random button index list.
            current_button_index = 0
            random_button_indexes = random.sample(range(6), k = 6)
        # Set the randomly picked button state in the states list to have the value "lit" instead of "idle".
        random_button_index = random_button_indexes[current_button_index]
        button_states[random_button_index] = "lit"

    def reflex_game_bpress(btn):
        # Function that runs when the player clicks on a button.
        global score

        if button_states[btn] == "lit":
            # If the user clicked on a button that was lit, we add 1 to their score.
            score += 1
            # We then reset the button back to idle.
            button_states[btn] = "idle"

    def setup_reflex_game():
        # Function to setup the mini-game before it starts.
        global random_button_indexes

        for i in range(buttons):
            # Fill the "button_states" list with "idle" values according to how many buttons there should be in the game.
            # Each "idle" value therefore represents a button.
            button_states.append("idle")
        # Re-generate a list of random button indexes.
        random_button_indexes = random.sample(range(buttons), k = buttons)

    def reset_reflex_game():
        # Reset the mini-game so it can be played again.
        global play_time
        global score
        global initial_countdown

        initial_countdown = 3.0
        play_time = 10.0
        score = 0
        for i in range(buttons):
            button_states[i] = "idle"

        renpy.show_screen("countdown_timer") # Re-show the countdown timer.

screen reflex_minigame_over:
    modal True
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            background "util/minigames/images/game-over-bg.png"
            xysize(1072, 698)
            align(0.5, 0.5)
            text "Your score: [score]" size 50 text_align 0.5 align(0.5, 0.4)
            imagebutton idle "util/minigames/images/quit-button.png" align(0.5, 0.8) action Jump("reaction_game_end") # Continue button to return to the story

screen countdown_timer:
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "[initial_countdown]" size 120 text_align 0.5 align(0.5, 0.5) color "#FFFFFF"

    # Timer runs every second to subtract 1.0 from the "initial_countdown" variable. Once the variable is equal to 1.0, we stop the timer and hide this screen.
    timer 1.0 action If(initial_countdown > 1, SetVariable("initial_countdown", initial_countdown - 1), Hide("countdown_timer")) repeat If(initial_countdown > 1, True, False)

screen reflex_minigame:
    on "show" action Show("countdown_timer")
    add "util/minigames/images/reactionbackground.png"

    grid int(buttons/2) 2:
        xspacing 100
        yspacing 20
        align (0.5, 0.85)
        for i in range(buttons):
            imagebutton idle "util/minigames/images/button-%s.png" % button_states[i] focus_mask True action Function(reflex_game_bpress, btn = i)

    # Score display - match the style of the time display
    text "[score]" size 78 color "#FFFFFF" align (0.79, 0.1) text_align 0.5
    
    # Timer display
    text "[play_time]" size 78 color "#FFFFFF" align (0.79, 0.355) text_align 0.5

    if renpy.get_screen("countdown_timer") == None:
        if "lit" not in button_states:
            timer 0.1 action Function(light_button) repeat False
        timer 1.0 action If(play_time > 1, SetVariable("play_time", play_time - 1), Show("reflex_minigame_over")) repeat If(play_time > 1, True, False)

default button_states = [] # Will contain the different states of the buttons ("idle" or "lit").
default buttons = 6 # How many buttons will be on the screen.
default random_button_indexes = [] # Will contain randomly generated numbers (indexes) corresponding to the amount of buttons available (0-5). This will be used to pick random buttons to light up.
default current_button_index = 0 # Keeps track of the currently picked button index.
default score = 0 # Keeps track of the player's score.
default final_reaction_score = 0 # Stores the final score for use in the story
default play_time = 20 # Keeps track of the time left.
default initial_countdown = 3 # How many seconds the countdown timer will count down for before the game begins.

# This label is used for testing the game directly
label reaction_game_test:
    $setup_reflex_game() # Setup the mini-game
    call screen reflex_minigame
    return

# This label is called from the elopement scene
label start_reaction_game:
    # Clear button states to ensure a fresh start
    $ button_states = []
    $ score = 0
    $ play_time = 20
    $ initial_countdown = 3
    
    # Hide window and disable dialogue advancement
    $ renpy.game.interface.suppress_dialogue = True
    $ renpy.game.interface.force_noninteractive = True
    $ _window_auto = False
    window hide
    
    # Setup and start the game
    $ setup_reflex_game()
    call screen reflex_minigame
    
    # This should never be reached directly as the game ends with a jump to reaction_game_end
    return

# This label is called when the game ends
label reaction_game_end:
    # Hide all reaction game screens
    $ renpy.hide_screen("reflex_minigame")
    $ renpy.hide_screen("reflex_minigame_over")
    $ renpy.hide_screen("countdown_timer")
    
    # Save final score before clearing game state
    $ final_reaction_score = score
    
    # Clear game state
    $ button_states = []
    $ score = 0
    
    # Restore normal dialogue behavior
    $ renpy.game.interface.suppress_dialogue = False
    $ renpy.game.interface.force_noninteractive = False
    $ _window_auto = True
    window auto
    
    # Return to the elopement scene
    jump elopement_reaction_game_complete
