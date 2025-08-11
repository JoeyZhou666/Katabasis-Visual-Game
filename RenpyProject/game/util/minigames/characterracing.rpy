# Character Racing Game for Elopement Scenario
# Assets adapted from https://www.youtube.com/@essRenPyTutorials 

init python:
    def reset_racing_game():
        """Function to reset variables for the mini-game so it can start over."""
        global race_selected_character, race_character_positions, player_wins
        global race_complete, race_countdown_timer, race_started
        global left_key_pressed, right_key_pressed, player_start_move
        
        # Reset all game variables
        race_countdown_timer = 3
        player_wins = False
        race_complete = False
        race_started = False
        race_selected_character = None
        left_key_pressed = False
        right_key_pressed = False
        player_start_move = False
        
        # Reset character positions
        character_1.x = character_start_xpos
        character_2.x = character_start_xpos
        character_3.x = character_start_xpos
        
        # Reset player position tracking
        race_character_positions = [0, 0]
        
        # Hide game over screen and show the menu again
        renpy.hide_screen("racing_game_over")
        renpy.hide_screen("racing_mini_game")
        renpy.show_screen("racing_game_menu")

    def npc_movement(st):
        """Update function for the SpriteManager to move NPC characters automatically."""
        global race_complete, player_wins
        
        # Only update if race has started and not completed
        if not race_complete and race_countdown_timer == 0:
            # Move NPCs based on which character the player selected
            if race_selected_character == "character_1":
                # Player is character 1, so move characters 2 and 3
                npc_move(character_2)
                npc_move(character_3)
            elif race_selected_character == "character_2":
                # Player is character 2, so move characters 1 and 3
                npc_move(character_1)
                npc_move(character_3)
            elif race_selected_character == "character_3":
                # Player is character 3, so move characters 1 and 2
                npc_move(character_1)
                npc_move(character_2)
            
            return 0  # Continue updating
        elif race_countdown_timer != 0:
            return 0  # Still counting down, continue updating
        else:
            return None  # Stop updating

    def npc_move(character):
        """Move an NPC character according to its speed."""
        global race_complete, race_winner
        
        # Move the character forward if it hasn't reached the goal
        if character.x < goal_xpos:
            character.x += character.speed
        else:
            # Character reached the goal
            race_complete = True
            race_winner = character
            renpy.show_screen("racing_game_over")
            renpy.restart_interaction()

    def character_move(character):
        """Move the player character according to its speed."""
        global race_complete, race_winner, race_character_positions
        
        # Move the character forward if it hasn't reached the goal
        if character.x < goal_xpos:
            character.x += player_char_speed
            race_character_positions = [character.x, character.y]
            renpy.restart_interaction()
        else:
            # Character reached the goal
            race_complete = True
            race_winner = character
            player_wins = True
            renpy.show_screen("racing_game_over")
            renpy.restart_interaction()

    def character_events(event, x, y, st):
        """Event handler for the SpriteManager - handles key presses."""
        global left_key_pressed, right_key_pressed, player_start_move
        
        # Only process events if the countdown is finished
        if event.type == renpy.pygame_sdl2.KEYDOWN and race_countdown_timer == 0:
            # Get the current state of all keys
            keys_pressed = renpy.pygame_sdl2.key.get_pressed()
            
            # Check for left and right arrow keys
            if keys_pressed[renpy.pygame_sdl2.K_LEFT]:
                # Left key pressed
                player_start_move = True
                left_key_pressed = True
            elif keys_pressed[renpy.pygame_sdl2.K_RIGHT]:
                # Right key pressed
                player_start_move = True
                right_key_pressed = True
            
            # If both keys have been pressed (alternating), move the player character
            if left_key_pressed and right_key_pressed:
                # Reset for next sequence
                left_key_pressed = False
                right_key_pressed = False
                
                # Move the selected character
                if race_selected_character == "character_1":
                    character_move(character_1)
                elif race_selected_character == "character_2":
                    character_move(character_2)
                elif race_selected_character == "character_3":
                    character_move(character_3)
        
        return None  # Continue handling events

    def setup_racing_game():
        """Initialize the race with character positions."""
        global race_character_positions
        
        # Set initial character positions
        character_1.x = character_start_xpos
        character_1.y = 500
        character_1.speed = 0.1  # Speed for NPC
        
        character_2.x = character_start_xpos
        character_2.y = 620
        character_2.speed = 0.4  # Speed for NPC
        
        character_3.x = character_start_xpos
        character_3.y = 730
        character_3.speed = 0.3  # Speed for NPC
        
        # Set player character position for indicator
        if race_selected_character == "character_1":
            race_character_positions = [character_1.x, character_1.y]
        elif race_selected_character == "character_2":
            race_character_positions = [character_2.x, character_2.y]
        elif race_selected_character == "character_3":
            race_character_positions = [character_3.x, character_3.y]
        
        # Hide menu and show race
        renpy.hide_screen("racing_game_menu")
        renpy.show_screen("racing_mini_game")

# Character sprites
default character_sprites = SpriteManager(update=npc_movement, event=character_events)
default character_1 = character_sprites.create("util/minigames/images/character_1.png")
default character_2 = character_sprites.create("util/minigames/images/character_2.png")
default character_3 = character_sprites.create("util/minigames/images/character_3.png")

# Character variables
default character_start_xpos = 100  # Starting X position
default goal_xpos = 1500  # Finish line position
default player_char_speed = 20  # Speed of player character

# Game state variables
default race_selected_character = None  # Selected character
default race_character_positions = [0, 0]  # Current position of player character
default race_winner = None  # Character that won the race
default race_complete = False  # Whether the race is complete
default race_countdown_timer = 3  # Countdown timer
default player_wins = False  # Whether the player won
default race_started = False  # Whether the race has started

# Key press variables
default left_key_pressed = False  # Whether left key has been pressed
default right_key_pressed = False  # Whether right key has been pressed
default player_start_move = False  # Whether player has started moving

# Screens
screen racing_game_menu:
    modal True
    
    # Block all keys from advancing dialogue
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()
    key "mouseup_1" action NullAction()
    
    # Background
    add "util/minigames/images/background.png"
    add Solid("#00000080")  # Semi-transparent overlay
    
    # Title
    text "Select your character" size 50 align(0.5, 0.1) color "#FFFFFF"
    
    # Character selection
    hbox:
        align(0.5, 0.4)
        spacing 10
        
        # Character 1
        imagebutton:
            idle "util/minigames/images/Menu/character_1_idle.png"
            hover "util/minigames/images/Menu/character_1_hover.png"
            selected_idle "util/minigames/images/Menu/character_1_selected_idle.png"
            selected_hover "util/minigames/images/Menu/character_1_selected_hover.png"
            selected race_selected_character == "character_1"
            action SetVariable("race_selected_character", "character_1")
        
        # Character 2
        imagebutton:
            idle "util/minigames/images/Menu/character_2_idle.png"
            hover "util/minigames/images/Menu/character_2_hover.png"
            selected_idle "util/minigames/images/Menu/character_2_selected_idle.png"
            selected_hover "util/minigames/images/Menu/character_2_selected_hover.png"
            selected race_selected_character == "character_2"
            action SetVariable("race_selected_character", "character_2")
        
        # Character 3
        imagebutton:
            idle "util/minigames/images/Menu/character_3_idle.png"
            hover "util/minigames/images/Menu/character_3_hover.png"
            selected_idle "util/minigames/images/Menu/character_3_selected_idle.png"
            selected_hover "util/minigames/images/Menu/character_3_selected_hover.png"
            selected race_selected_character == "character_3"
            action SetVariable("race_selected_character", "character_3")
    
    # Start button
    imagebutton:
        idle "util/minigames/images/Menu/play_button_idle.png"
        align(0.5, 0.8)
        sensitive race_selected_character is not None
        action Function(setup_racing_game)

screen racing_countdown_timer:
    # Block all keys from advancing dialogue
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()
    key "mouseup_1" action NullAction()
    
    # Countdown overlay
    frame:
        background "#00000080"
        align(0.5, 0.5)
        xysize(400, 250)
        vbox:
            align(0.5, 0.5)
            text "Get Ready!" size 40 xalign 0.5 color "#FFFFFF"
            text "[race_countdown_timer]" size 40 xalign 0.5 color "#FFFFFF"
    
    # Timer to count down
    timer 1.0:
        if race_countdown_timer > 1:
            action SetVariable("race_countdown_timer", race_countdown_timer - 1)
            repeat True
        else:
            action [
                SetVariable("race_countdown_timer", 0),
                SetVariable("race_started", True),
                Hide("racing_countdown_timer")
            ]
            repeat False

screen racing_mini_game:
    modal True
    
    # Show countdown when screen is first shown
    on "show" action Show("racing_countdown_timer")
    
    # Block all keys from advancing dialogue
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()
    key "mouseup_1" action NullAction()
    
    # Background
    add "util/minigames/images/background.png"
    
    # Character sprites
    add character_sprites
    
    # Show player how to play the game
    if not player_start_move and race_countdown_timer == 0:
        frame:
            align(0.5, 0.3)
            xysize(600, 250)
            background "#00000080"
            vbox:
                spacing 20
                align(0.5, 0.5)
                text "Alternate arrow keys to move" xalign 0.5 color "#FFFFFF"
                add "racing_arrow_keys" xalign 0.5
    
    # Player's character indicator
    if race_character_positions[0] > 0:  # Only show if position is set
        add "util/minigames/images/player_indicator.png" pos (race_character_positions[0] + 50, race_character_positions[1] - 50)

screen racing_game_over:
    modal True
    
    # Block all keys from advancing dialogue
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()
    key "mouseup_1" action NullAction()
    
    # Background with semi-transparent overlay
    add "util/minigames/images/background.png"
    add Solid("#00000080")
    
    # Result frame
    frame:
        align(0.5, 0.5)
        xysize(500, 350)
        background Solid("#00000080")
        
        # Title
        text "Race Complete!" size 50 align(0.5, 0.2) color "#FFFFFF"
        
        # Result message
        if race_winner == character_1:
            if race_selected_character == "character_1":
                text "You won!" size 40 align(0.5, 0.4) color "#FFFFFF"
            else:
                text "Character 1 won!" size 40 align(0.5, 0.4) color "#FFFFFF"
        elif race_winner == character_2:
            if race_selected_character == "character_2":
                text "You won!" size 40 align(0.5, 0.4) color "#FFFFFF"
            else:
                text "Character 2 won!" size 40 align(0.5, 0.4) color "#FFFFFF"
        elif race_winner == character_3:
            if race_selected_character == "character_3":
                text "You won!" size 40 align(0.5, 0.4) color "#FFFFFF"
            else:
                text "Character 3 won!" size 40 align(0.5, 0.4) color "#FFFFFF"
        
        # Continue button
        textbutton "Continue" xalign 0.5 yalign 0.8 xsize 250 ysize 60 text_size 30 text_color "#000000" background "#FFFFFF" action Return()

# Animated arrow keys image
image racing_arrow_keys:
    zoom 0.5
    "util/minigames/images/arrow_keys_1.png"
    pause 0.5
    "util/minigames/images/arrow_keys_2.png"
    pause 0.5
    repeat

# Main label for the racing game
label start_racing_game:
    # Explicitly hide the dialogue window
    window hide
    
    # Disable dialogue advancement
    $ renpy.game.preferences.afm_enable = False
    $ config.skipping = None
    $ config.allow_skipping = False
    $ config.keymap['dismiss'] = []
    
    # Reset game variables
    $ race_countdown_timer = 3
    $ race_complete = False
    $ race_started = False
    $ player_wins = False
    $ left_key_pressed = False
    $ right_key_pressed = False
    $ player_start_move = False
    $ race_selected_character = None
    $ race_character_positions = [0, 0]
    
    # Show the character selection menu
    call screen racing_game_menu
    
    # Ensure all racing game screens are hidden
    $ renpy.hide_screen("racing_game_menu")
    $ renpy.hide_screen("racing_mini_game")
    $ renpy.hide_screen("racing_game_over")
    $ renpy.hide_screen("racing_countdown_timer")
    
    # Clear all displayables to remove any racing game assets
    $ renpy.scene()
    
    # Restore dialogue settings
    $ renpy.game.preferences.afm_enable = True
    $ config.allow_skipping = True
    $ config.keymap['dismiss'] = ['dismiss', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'mouseup_1']
    
    # Return to the main game
    window auto
    return
