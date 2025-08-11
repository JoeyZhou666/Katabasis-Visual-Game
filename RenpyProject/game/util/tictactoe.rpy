# *********************************************************************
# Tic-Tac-Toe Minigame Implementation
# *********************************************************************

# Initialize game variables
init python:
    # Board state: 0 = empty, 1 = player (X), 2 = CPU (O)
    ttt_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ttt_game_over = False
    ttt_winner = 0  # 0 = no winner yet, 1 = player, 2 = CPU, 3 = tie
    
    def reset_ttt_game():
        """Reset the tic-tac-toe game state."""
        global ttt_board, ttt_game_over, ttt_winner
        ttt_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ttt_game_over = False
        ttt_winner = 0
    
    def check_ttt_winner():
        """Check if there's a winner or a tie."""
        global ttt_board, ttt_game_over, ttt_winner
        
        # Check rows
        for i in range(0, 9, 3):
            if ttt_board[i] != 0 and ttt_board[i] == ttt_board[i+1] == ttt_board[i+2]:
                ttt_game_over = True
                ttt_winner = ttt_board[i]
                return
        
        # Check columns
        for i in range(3):
            if ttt_board[i] != 0 and ttt_board[i] == ttt_board[i+3] == ttt_board[i+6]:
                ttt_game_over = True
                ttt_winner = ttt_board[i]
                return
        
        # Check diagonals
        if ttt_board[0] != 0 and ttt_board[0] == ttt_board[4] == ttt_board[8]:
            ttt_game_over = True
            ttt_winner = ttt_board[0]
            return
        
        if ttt_board[2] != 0 and ttt_board[2] == ttt_board[4] == ttt_board[6]:
            ttt_game_over = True
            ttt_winner = ttt_board[2]
            return
        
        # Check for tie
        if 0 not in ttt_board:
            ttt_game_over = True
            ttt_winner = 3
            return
    
    def cpu_move():
        """Make a move for the CPU (very simple AI with randomness to make it easier)."""
        global ttt_board, ttt_game_over, ttt_winner
        import random
        
        # Make CPU easier by adding randomness - only make smart moves 20% of the time
        # This means the CPU will win approximately 1/5 of the time
        if random.random() < 0.2:  # 20% chance to make optimal moves
            # First, check if CPU can win in the next move
            for i in range(9):
                if ttt_board[i] == 0:
                    ttt_board[i] = 2
                    check_ttt_winner()
                    if ttt_game_over and ttt_winner == 2:
                        return
                    # Reset if no win
                    ttt_board[i] = 0
                    ttt_game_over = False
                    ttt_winner = 0
            
            # Second, block player from winning
            for i in range(9):
                if ttt_board[i] == 0:
                    ttt_board[i] = 1
                    check_ttt_winner()
                    if ttt_game_over and ttt_winner == 1:
                        ttt_board[i] = 2
                        ttt_game_over = False
                        ttt_winner = 0
                        check_ttt_winner()
                        return
                    # Reset if no block needed
                    ttt_board[i] = 0
                    ttt_game_over = False
                    ttt_winner = 0
            
            # Take center if available
            if ttt_board[4] == 0:
                ttt_board[4] = 2
                check_ttt_winner()
                return
        
        # Most of the time (80%), just make a random move
        available_spots = [i for i, val in enumerate(ttt_board) if val == 0]
        if available_spots:
            spot = random.choice(available_spots)
            ttt_board[spot] = 2
            check_ttt_winner()
            return

# Define the tic-tac-toe screen
screen tictactoe_game():
    modal True
    
    # Paper background using the new tictactoe_paper image - moved to the right side
    frame:
        xalign 0.75  # Positioned on the right half of the screen
        yalign 0.5
        xsize 300
        ysize 450
        background "images/tictactoe_paper.png"
        
        # Title - styled to look handwritten
        text "Tic-Tac-Toe" xalign 0.5 ypos 20 color "#000000" font "fonts/ArchitectsDaughter.ttf" size 30 outlines [(1, "#ffffff", 0, 0)]
        
        # Add grid lines for the tic-tac-toe board - centered on the paper
        # Horizontal lines
        add Solid("#000000", xpos=45, ypos=150, xsize=200, ysize=2)  # Top horizontal line
        add Solid("#000000", xpos=45, ypos=225, xsize=200, ysize=2)  # Bottom horizontal line
        
        # Vertical lines
        add Solid("#000000", xpos=110, ypos=85, xsize=2, ysize=200)  # Left vertical line
        add Solid("#000000", xpos=180, ypos=85, xsize=2, ysize=200)  # Right vertical line
        
        # Game grid - centered on the paper
        grid 3 3:
            xalign 0.5
            yalign 0.13
            yoffset 50  # Centered vertically on the paper
            spacing 5   # Reduced spacing between cells
            
            for i in range(9):
                button:
                    xsize 70    # Cell size to fit the paper
                    ysize 70
                    background None  # Transparent background to show the paper
                    hover_background "#e0e0e080"  # Semi-transparent hover effect
                    
                    if ttt_board[i] == 1:  # Player's X - styled to look handwritten and larger
                        text "X" xalign 0.5 yalign 0.5 size 60 color "#0000ff" font "fonts/ArchitectsDaughter.ttf"
                    elif ttt_board[i] == 2:  # CPU's O - styled to look handwritten and larger
                        text "O" xalign 0.5 yalign 0.5 size 60 color "#ff0000" font "fonts/ArchitectsDaughter.ttf"
                    else:
                        text "" xalign 0.5 yalign 0.5
                    
                    # Only allow clicking on empty cells and when game is not over
                    sensitive ttt_board[i] == 0 and not ttt_game_over
                    
                    action [SetDict(ttt_board, i, 1), Function(check_ttt_winner), If(not ttt_game_over, Function(cpu_move))]
        
        # Game status - styled to look handwritten and positioned below the grid
        if ttt_game_over:
            if ttt_winner == 1:
                text "You won!" xalign 0.5 ypos 290 color "#0000ff" font "fonts/ArchitectsDaughter.ttf" size 28 outlines [(1, "#ffffff", 0, 0)]
            elif ttt_winner == 2:
                text "Bandit won!" xalign 0.5 ypos 290 color "#ff0000" font "fonts/ArchitectsDaughter.ttf" size 28 outlines [(1, "#ffffff", 0, 0)]
            else:
                text "It's a tie!" xalign 0.5 ypos 290 color "#000000" font "fonts/ArchitectsDaughter.ttf" size 28 outlines [(1, "#ffffff", 0, 0)]
        
        # Close button - styled to look handwritten and positioned at the bottom
        textbutton "Done" xalign 0.5 ypos 390 text_font "fonts/ArchitectsDaughter.ttf" text_size 24 text_color "#000000" text_hover_color "#0000ff" text_outlines [(1, "#ffffff", 0, 0)] action Return()

# Label to call the tic-tac-toe game
label play_tictactoe:
    $ reset_ttt_game()
    call screen tictactoe_game
    return
