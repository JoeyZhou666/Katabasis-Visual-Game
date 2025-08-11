########################################################################
# 2) Main script, including the classroom conflict scene
########################################################################

# Emotion indicators
image anger_indicator = "images/anger.png"
image happy_indicator = "images/happy.png"
image calm_indicator = "images/calm.png"

# Example images (you can replace these with your actual images)
image books = "images/books.png"
image scattered_books = "images/Scattered_books.png"

# Simple transforms (flip, smaller, etc.)
transform smaller:
    zoom 0.8

transform flipped:
    xzoom -1.0

transform smaller_flipped:
    zoom 0.8
    xzoom -1.0

# Variables
default anger_level = 0
default chosen_response = ""
default body_language = ""
default conflict_outcome = ""

# Persistent variable to track if the conflict was mastered
default persistent.conflict_mastery = False

# Optional screen to display emotion state
screen emotion_indicator():
    if anger_level < 3:
        add "happy_indicator"
    elif anger_level < 7:
        add "calm_indicator"
    elif anger_level < 8:
        add "anger_indicator"
    else:
        add "anger_indicator"
        add Solid("#ff000033")  # Red overlay for high anger

label classroom_conflict:
    # Reset conflict-related variables
    $ breathing_success = False
    $ chosen_response = ""
    $ body_language = ""
    $ conflict_outcome = ""

    scene bg classroom
    show screen emotion_indicator
    show books:
        xalign 0.4
        yalign 0.55
        zoom 0.8

    n "You sit quietly in the classroom, focusing on your textbook and notes."
    n "Today's math assignment is more difficult than expected, but you're working hard to solve the problems."

    # Crusher enters from the left
    show d at smaller_flipped:
        xalign -1.0
        yalign 1.0
    show d at smaller_flipped:
        ease 1.5 xalign 0.35

    $ renpy.pause(0.2)

    show d at smaller_flipped:
        ease 0.3 xalign 0.15
    with hpunch

    hide books

    $ anger_level = 7

    show scattered_books:
        xalign 0.65
        yalign 0.7
        zoom 0.7

    n "Suddenly, someone bumps into your desk, causing your books and notes to scatter on the floor."
    d "Watch it, dummy. Can't you place your desk properly?"

    menu body_reaction:
        "What's your first reaction?"

        "Clench your fists":
            $ body_language = "aggressive"
            $ anger_level = 8
            n "You feel blood boiling in your veins, unconsciously clenching your fists."
            d "Oh, you want to fight? Come on!"

        "Take a deep breath":
            $ body_language = "calm"
            
            n "You try to stay calm and take a deep breath."

            # Call the enhanced breathing minigame
            call do_breathing_minigame

            $ anger_level = 4

        "Step back":
            $ body_language = "defensive"
            n "You step back to give yourself some space."
            $ anger_level = 4

    # Inner thoughts
    menu inner_thoughts:
        "What are you thinking inside?"

        "I'll make him pay!":
            $ anger_level = 8
            n "A strong desire for revenge rises within you."
            with Dissolve(0.3)
            scene bg classroom with ImageDissolve("images/anger.png", 1.0, ramplen=8)

        "Stay calm, don't take the bait...":
            $ anger_level = 4
            n "You tell yourself not to get provoked, it might just be an accident."

        "This is so unfair!":
            $ anger_level = 7
            n "You feel a sense of grievance and injustice."

    # Pause and think
    menu pause_and_think:
        "Pause and think:"

        "Analyze the situation":
            scene bg classroom with dissolve
            n "You try to rationally analyze the current situation."
            n "Crusher bumped into your desk, but maybe it was just an accident? Though his attitude is indeed poor."
            n "Starting a conflict in the classroom could lead to serious consequences."
            $ anger_level = 4

        "Consider the consequences":
            scene bg classroom with dissolve
            n "You think about the possible consequences of different reactions."
            n "If you fight, you risk escalating the situation. You could be punished."
            n "If you stay calm, you might avoid major trouble."
            $ anger_level = 4

        "React immediately":
            $ anger_level = 7
            n "You decide to react immediately without further thought."

    hide d

    # Show correct sprite based on anger level
    if anger_level > 7:
        show d at right, flipped
    else:
        show ds at right, flipped

    # Final response menu
    menu final_response:
        "How do you respond to Crusher?"

        "Stand up and push back" if anger_level > 6:
            $ chosen_response = "aggressive"
            n "You abruptly stand up and push Crusher."
            d "Hey! You dare push me?"
            show t at left with dissolve
            t "What's going on here? [povname] and Crusher, both of you come to my office right now!"
            scene bg office with fade
            show t at center
            n "Your impulsive reaction got you sent to the office..."
            t "This is unacceptable. You will both receive a week of detention."
            $ conflict_outcome = "negative"

        "Calmly express your displeasure":
            $ chosen_response = "assertive"
            pov "Crusher, you bumped into my desk and knocked my books off. I think you should apologize."

            if body_language == "calm" or anger_level < 5:
                show ds at right, flipped
                d "Uh... I guess I was a bit reckless. Sorry."
                n "Crusher helps you pick up some of your books."
                n "The conflict is peacefully resolved."
                $ conflict_outcome = "positive"
            else:
                d "Whatever, you're too sensitive."
                n "Crusher walks away. It's not fully resolved, but at least it didn't escalate."
                $ conflict_outcome = "neutral"

        "Seek help" if body_language != "aggressive":
            $ chosen_response = "help"
            n "You look around for help."

            menu seek_help:
                "Who do you ask for help?"

                "Ms. Johnson":
                    show t at left with dissolve
                    pov "Ms. Johnson, could you help me? Crusher knocked my books off."
                    t "What happened, [povname]?"
                    pov "Crusher bumped my desk, but he won't apologize."
                    t "Crusher, is this correct?"
                    show ds at right, flipped
                    d "I... I didn't mean to."
                    t "Then please apologize."
                    d "I'm sorry, I shouldn't have been so rude."
                    n "With Ms. Johnson mediating, the conflict is resolved."
                    $ conflict_outcome = "positive"

                "Bandit":
                    show f at left with dissolve
                    pov "Hey Bandit, can you help me?"
                    f "What's going on?"
                    pov "Crusher bumped my desk and was quite rude."
                    f "Crusher, be nicer. Help pick up the books."
                    n "Surprisingly, Crusher listens to Bandit."
                    show ds at right
                    d "Fine, here."
                    n "Crusher helps pick up your books, though he looks a bit unwilling."
                    $ conflict_outcome = "neutral"

        "Stay silent and clean up yourself":
            $ chosen_response = "passive"
            n "You decide not to respond and quietly pick up your books."

            if anger_level > 7:
                n "You're calm on the outside, but anger still burns inside. This might not be a healthy solution."
                n "Crusher grows bored and leaves, unresolved."
                $ conflict_outcome = "neutral"
            else:
                n "You keep cool and don't let emotions overwhelm you."
                d "..."
                n "Seeing no reaction, Crusher awkwardly leaves."
                n "You didn't get an apology, but at least it didn't escalate."
                $ conflict_outcome = "neutral"

    scene bg classroom with fade

    # Summarize outcome
    if conflict_outcome == "positive":
        n "【Learning Feedback】You managed to resolve the conflict effectively without losing your cool."
        n "Positive communication like this helps build healthier relationships."
        nvl clear
        nvl_narrator "When facing conflicts, express your feelings without attacking others."
        nvl_narrator "Stay aware of your emotions, remain calm, and use 'I' statements instead of accusing with 'you'."
        nvl_narrator "Rational communication often brings better results than impulsive outbursts."
        nvl clear

    elif conflict_outcome == "neutral":
        n "【Learning Feedback】You avoided escalation, but the conflict may not be fully resolved."
        n "Sometimes it's important to express your feelings appropriately."
        nvl clear
        nvl_narrator "Avoiding conflict can be wise, but total avoidance can let problems fester."
        nvl_narrator "Balance expressing yourself and your boundaries without attacking or suppressing."
        nvl_narrator "Seeking help from trusted people is also a practical way to handle difficult situations."
        nvl clear

    else:
        n "【Learning Feedback】Impulsive reactions often lead to bigger issues. Next time, try to calm down before acting."
        nvl clear
        nvl_narrator "Strong emotions can cloud judgment. Recognizing physical anger signals (heart rate, tension) is the first step in controlling impulses."
        nvl_narrator "Before responding, consider taking deep breaths or counting to 10 to give yourself space to think."
        nvl_narrator "Remember: You cannot control others’ actions, but you can control your response."
        nvl clear

    hide screen emotion_indicator

    # Offer the player a chance to retry
    menu try_again:
        "Do you want to try this scene again?"

        "Yes, I want to try a different approach":
            jump classroom_conflict

        "No, continue the game":
            n "You take these lessons forward as you continue your school life..."
            if conflict_outcome == "positive":
                $ persistent.conflict_mastery = True
            return
