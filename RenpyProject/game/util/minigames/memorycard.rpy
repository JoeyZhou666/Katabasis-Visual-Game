# Memory Card Game for Elopement Scenario
# A simple memory matching game with 8 pairs of cards (16 total)
# Assets adapted from https://www.youtube.com/@essRenPyTutorials 

# Variable to track if Mousy card has been seen
default mousy_card_seen = False

# Card class to store card information
init python:
    class Card:
        def __init__(self, id, image_name):
            self.id = id          # Unique identifier for the card
            self.image_name = image_name  # Image file name (e.g., "card-1")
            self.flipped = False  # Whether the card is face up
            self.matched = False  # Whether the card has been matched
    
    def create_cards():
        """Create a shuffled deck of 16 cards (8 pairs)"""
        cards = []
        # Create 8 pairs of cards
        for i in range(1, 9):
            # Create two cards with the same image
            cards.append(Card(len(cards), "card-{}".format(i)))
            cards.append(Card(len(cards), "card-{}".format(i)))
        
        # Shuffle the cards
        renpy.random.shuffle(cards)
        return cards
    
    def flip_card(card_index):
        """Handle card flipping logic"""
        global memory_cards, first_card, second_card, can_flip, matches_found, check_match
        
        # If we can't flip cards right now, do nothing
        if not can_flip:
            return
        
        # Get the card at the specified index
        card = memory_cards[card_index]
        
        # If the card is already flipped or matched, do nothing
        if card.flipped or card.matched:
            return
        
        # Flip the card
        card.flipped = True
        
        # If this is the first card flipped
        if first_card is None:
            first_card = card
        # If this is the second card flipped
        elif second_card is None:
            second_card = card
            can_flip = False  # Prevent further flips until these are processed
            check_match = True  # Set flag to check for match

# Game state variables
default memory_cards = []      # List of Card objects
default first_card = None      # First card selected in a pair
default second_card = None     # Second card selected in a pair
default can_flip = True        # Whether player can flip cards
default matches_found = 0      # Number of matches found
default check_match = False    # Flag to check for matches

# Card display transform
transform card_transform:
    size (161, 225)  # 15% larger than previous size

# Function to process card matches
init python:
    def process_match():
        global first_card, second_card, can_flip, matches_found, check_match
        
        # If we need to check for a match
        if check_match and first_card is not None and second_card is not None:
            # Check if the cards match
            if first_card.image_name == second_card.image_name:
                # Cards match!
                first_card.matched = True
                second_card.matched = True
                matches_found += 1
            else:
                # Cards don't match, flip them back
                first_card.flipped = False
                second_card.flipped = False
            
            # Reset for next pair
            first_card = None
            second_card = None
            can_flip = True
            check_match = False
            
            # Force screen update
            renpy.restart_interaction()

# Screen for the memory card game
screen memory_mini_game():
    # Background
    add "util/minigames/images/backgroundCARD.png"
    
    # Game title
    text "Memory Card Game" size 40 color "#FFFFFF" outlines [(absolute(2), "#000000", 0, 0)] align (0.5, 0.05)
    
    # Timer to check for matches
    if check_match:
        timer 1.0 action Function(process_match) repeat False
    
    # Card grid - 4x4 grid for 16 cards
    # To move cards down: adjust the second value in align (0.5, 0.6) 
    # Higher values move cards down, e.g., 0.5 is center, 0.6 is lower, 0.7 is even lower
    frame:
        background None
        align (0.5, 0.8)
        
        grid 4 4:
            spacing 10
            align (0.5, 0.5)
            
            # Loop through all 16 cards
            for i, card in enumerate(memory_cards):
                frame:
                    background None
                    xysize (161, 225)
                    
                    if card.matched:
                        # Card is matched - keep showing the card image
                        add "util/minigames/images/{}.png".format(card.image_name) at card_transform
                    elif card.flipped:
                        # Card is face up - show the image
                        add "util/minigames/images/{}.png".format(card.image_name) at card_transform
                        
                        # Show special dialogue for Mousy cards
                        if (card.image_name == "card-1" or card.image_name == "card-2") and not mousy_card_seen:
                            $ mousy_card_seen = True
                            text "Omg Mousy is in this game!" size 20 color "#FFFFFF" outlines [(absolute(2), "#000000", 0, 0)] align (0.5, 0.2)
                    else:
                        # Card is face down - show the back
                        imagebutton:
                            idle "util/minigames/images/card-back.png"
                            action Function(flip_card, i)
                            at card_transform
    
    # Continue button (only shown when all matches are found)
    if matches_found == 8:
        frame:
            background "#00000080"
            padding (20, 10)
            align (0.5, 0.9)
            
            textbutton "Continue":
                text_size 30
                action Return()

# Label to start the memory card game
label start_memory_game:
    # Initialize game state
    $ memory_cards = create_cards()
    $ first_card = None
    $ second_card = None
    $ can_flip = True
    $ matches_found = 0
    $ check_match = False
    $ mousy_card_seen = False
    
    # Show the game screen
    call screen memory_mini_game
    
    # Return to the main game
    return
