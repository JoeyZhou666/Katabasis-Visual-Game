# Import necessary modules
init python:
    import time
    
    # Define a custom character for breathing instructions
    # This will show text but not wait for input
    b = Character("", what_style="breathing_text", window_style="breathing_window")

# Define custom styles
style breathing_text:
    color "#ffffff"
    size 24
    text_align 0.5 
    xalign 0.5
    
style breathing_window:
    background None  # Transparent window

# Images for the breathing minigame
image breathing_circle = "images/breathing_circle.png"

# Progress bar overlay image - create this as a separate overlay
image breathing_progress_empty = Solid("#fdfcfc")
image breathing_progress_fill = Solid("#64f360")

# Transforms for breathing animation
transform breathing_expand:
    zoom 0.4
    ease 4.0 zoom 0.7

transform breathing_contract:
    zoom 0.7
    ease 4.0 zoom 0.4

# Overlay screen for progress bar that appears above everything
screen breathing_progress_overlay(progress):
    layer "overlay"  # Force to overlay layer
    
    # Progress bar container
    frame:
        xalign 0.5
        yalign 0.9  # Near bottom of screen
        xsize 550
        ysize 35
        background "#a7a1a1f6"  # Semi-transparent black
        
        # Background bar
        bar:
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 30
            value StaticValue(100, 100)  # Always full width
            left_bar "breathing_progress_empty"
            right_bar "breathing_progress_empty"
        
        # Foreground fill bar
        bar:
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 30
            value progress
            range 100
            left_bar "breathing_progress_fill"
            right_bar "breathing_progress_empty"
        
        text "Breathing Progress: [progress]%" xalign 0.5 yalign 0.5 size 20 color "#070606"

# Improved breathing minigame that keeps dialogue visible
label do_breathing_minigame:
    # Hide all character sprites
    hide d
    hide ds
    hide t
    hide f
    hide scattered_books
    
    # Introduction
    n "Let's try to calm down with some deep breathing."
    
    # Center the breathing circle
    show breathing_circle:
        xalign 0.5
        yalign 0.5
        zoom 0.4
    
    n "Follow the circle - breathe in as it expands and out as it contracts."
    
    # Initialize progress
    $ breathing_progress = 0
    
    # Show progress overlay (on top layer)
    show screen breathing_progress_overlay(breathing_progress)
    
    # Inhale phase - show in dialogue
    n "Breathe in..."
    
    # Inhale phase (expand) - 0% to 50%
    show breathing_circle at breathing_expand
    $ target_progress = 50
    $ start_time = time.time()
    $ duration = 4.0
    
    while breathing_progress < target_progress:
        $ elapsed = time.time() - start_time
        $ breathing_progress = int(min(elapsed / duration * target_progress, target_progress))
        $ renpy.pause(0.1, hard=False)
        show screen breathing_progress_overlay(breathing_progress)
    
    # Hold phase dialog
    n "Hold..."
    
    # Brief hold - 50% to 60%
    $ target_progress = 60
    $ start_time = time.time()
    $ duration = 1.0
    
    while breathing_progress < target_progress:
        $ elapsed = time.time() - start_time
        $ breathing_progress = 50 + int(min(elapsed / duration * 10, 10))
        $ renpy.pause(0.1, hard=False)
        show screen breathing_progress_overlay(breathing_progress)
    
    # Exhale phase dialog
    n "Breathe out..."
    
    # Exhale phase (contract) - 60% to 100%
    show breathing_circle at breathing_contract
    $ target_progress = 100
    $ start_time = time.time()
    $ duration = 4.0
    
    while breathing_progress < target_progress:
        $ elapsed = time.time() - start_time
        $ breathing_progress = 60 + int(min(elapsed / duration * 40, 40))
        $ renpy.pause(0.1, hard=False)
        show screen breathing_progress_overlay(breathing_progress)
    
    # Show completion message
    hide screen breathing_progress_overlay
    hide breathing_circle
    
    n "Breathing exercise complete!"
    
    n "You feel your heart rate slowing down and your muscles relaxing."
    
    # Show characters again based on where we were in the script
    show scattered_books:
        xalign 0.65
        yalign 0.7
        zoom 0.7
    
    show d at right, flipped
    
    # Return to main script
    return