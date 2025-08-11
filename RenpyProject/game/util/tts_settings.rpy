# Voice and Sound Effects Settings Screen
# This file contains the screen and variables for voice and sound effects settings

# Define a default variable to track if voice acting is enabled
default persistent.tts_enabled = True

# define a default variable to track if dialogue sound effects are enabled
# default, dialogue sound effects are enabled if voice acting is disabled
default persistent.dialogue_sfx_enabled = not persistent.tts_enabled

# screen that appears at the beginning of the game to configure voice settings
screen tts_settings():
    modal True
    
    frame:
        style_prefix "tts_settings"
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 300
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            label _("Audio Settings"):
                xalign 0.5
                text_size 40
            
            null height 20
            
            vbox:
                xalign 0.5
                spacing 15
                
                label _("Enable Text-to-Speech?"):
                    xalign 0.5
                
                hbox:
                    xalign 0.5
                    spacing 30
                    
                    textbutton _("Yes"):
                        action [SetVariable("persistent.tts_enabled", True), SetVariable("persistent.dialogue_sfx_enabled", False)]
                        selected persistent.tts_enabled
                    
                    textbutton _("No"):
                        action [SetVariable("persistent.tts_enabled", False), SetVariable("persistent.dialogue_sfx_enabled", True)]
                        selected not persistent.tts_enabled
            
            null height 40
            
            textbutton _("Continue"):
                xalign 0.5
                action Return()

# Style definitions for the TTS settings screen
style tts_settings_frame is gui_frame
style tts_settings_label is gui_label
style tts_settings_label_text is gui_label_text
style tts_settings_button is gui_button
style tts_settings_button_text is gui_button_text

style tts_settings_frame:
    padding (40, 40)
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style tts_settings_label_text:
    size 28
    color "#fff"
    outlines [(2, "#000", 0, 0)]

style tts_settings_button:
    properties gui.button_properties("tts_settings_button")
    padding (20, 10)

style tts_settings_button_text:
    properties gui.button_properties("tts_settings_button_text")
    size 24
    idle_color "#fff"
    hover_color "#ffcc00"
    selected_color "#00ff00"
    outlines [(2, "#000", 0, 0)]
