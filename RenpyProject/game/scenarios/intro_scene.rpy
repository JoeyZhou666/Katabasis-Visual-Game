# *********************************************************************
# Locker and Sticky Note Scene
# *********************************************************************

label intro_scene:
    # Initialize scenario tracking variables
    $ scenario_disruptive = 0     # Scenario for disruptive behavior
    $ scenario_disrespectful = 0  # Scenario for disrespectful language
    $ scenario_emotional = 0      # Scenario for emotional outburst
    $ scenario_refusal = 0        # Scenario for work refusal
    $ scenario_conflict = 0       # Scenario for peer conflict

    # Start by showing a blurred lockers background with an entrance transition effect
    play sound "audio/schoolbell.mp3"
    show bg lockersblurred with in_eye
    hide bg lockers with out_eye

    # Mousy greets the player in a sleepy tone

    voice "audio/intro_scene_e_01.mp3"
    e "Oh my, are you falling asleep?!"

    voice "audio/intro_scene_e_02.mp3"
    e "Wake up! The day just started!"

    play music "audio/music/afternoontea.wav" loop volume 0.2
    # Transition to a clear lockers background and display Mousy smiling
    show bg lockers with in_eye    
    show ms

    voice "audio/intro_scene_e_03.mp3"
    e "Hiya, it's me Mousy. Do you remember me, sleepy head?"

    # *****************************************************************
    # PLAYER CHOICE: Do you remember Mousy?
    # *****************************************************************
    menu:
        "Yes, of course":
            $ remembersMousy = "Yes"   # Player remembers Mousy
            hide ms
            show mh                 # Change expression to happy
        "Not really":
            $ remembersMousy = "No"   # Player does not remember Mousy

    # Branch dialogue based on the player's response
    if remembersMousy == "Yes":

        voice "audio/intro_scene_e_04.mp3"
        e "Of course, how could you ever forget me! Let's hope you didn't forget your own name."
        hide mh
        show ms                 # Revert to smiling expression
    else:

        # TODO change this: voice "audio/intro_scene_e_05.mp3"
        e "Oh, really?! Hmm, maybe you're still waking up. I'm Mousy! We sit next to eachother in health class."
        e "(A little quieter, and almost to themself) Oh gosh, you know what? My memory's a little fuzzy this morning too..." 
        e "What was your name again?"

    # *****************************************************************
    # PLAYER INPUT: Get the protagonist's name
    # *****************************************************************

    voice "audio/intro_scene_e_06.mp3"
    $ povname = renpy.input("What is your name?: ", length=32)
    $ povname = povname.strip() or "El"  # Default name is "El" if no input provided
    pov "My name is [povname]."

    # Change expression to happy for continued dialogue
    hide ms
    show mh

    voice "audio/intro_scene_e_07.mp3"
    e "It is nice to have you back, [povname]!"

    voice "audio/intro_scene_e_08.mp3"
    e "Did you get enough sleep? I almost lost you there!"

    # *****************************************************************
    # PLAYER CHOICE: How much sleep did you get?
    # *****************************************************************
    menu:
        "Less than 6 hours":
            $ sleep = "Less than 6 hours"
            hide mh 
            show msad         # Mousy looks sad when the player slept little
            $ scenario_emotional += 2      # Lack of sleep increases emotional
            $ scenario_disruptive += 1     # May be more disruptive when tired
            $ scenario_refusal += 1        # May refuse work when tired
        "About 6-8 hours":
            $ sleep = "6-8 hours"
            show mh           # Mousy remains happy
        "More than 8 hours":
            $ sleep = "More than 8 hours"
            show mh           # Mousy remains happy
            $ scenario_emotional -= 1      # Good sleep decreases emotional issues
            $ scenario_disruptive -= 1     # Less likely to be disruptive when rested
            $ scenario_refusal -= 1        # More likely to engage in work

    # Branch dialogue based on sleep duration
    if sleep == "Less than 6 hours":

        voice "audio/intro_scene_e_09.mp3"
        e "No wonder you're so sleepy! Make sure you get some rest next time!"
    elif sleep == "6-8 hours":

        voice "audio/intro_scene_e_10.mp3"
        e "Hmm, you slept a good amount! Don't worry, I also get tired in the mornings."
    elif sleep == "More than 8 hours":

        voice "audio/intro_scene_e_11.mp3"
        e "You really are a sleepy head, hehe."

    # Reset expressions to smiling for the next dialogue
    hide msad
    hide mh
    show ms

    voice "audio/intro_scene_e_12.mp3"
    e "Besides sleep, how are you feeling?"
    
    # *****************************************************************
    # PLAYER CHOICE: How are you feeling?
    # *****************************************************************
    menu:
        "Excited!":
            $ mood = "Excited!"    # Player is excited
            hide ms
            show mh             # Mousy looks happy
            $ scenario_emotional -= 2      # Positive emotions reduce emotional issues
            $ scenario_disruptive -= 1     # Less likely to be disruptive when happy
            $ scenario_disrespectful -= 1  # Less likely to be disrespectful when happy
            $ scenario_refusal -= 1        # Less likely to refuse work when positive
            $ scenario_conflict -= 1       # Less likely to engage in conflict when happy
        "It's whatever":
            $ mood = "Neutral"     # Player feels neutral
            hide ms
            show msad           # Mousy looks sad
            $ scenario_emotional += 0      # Neutral emotional state
            $ scenario_disruptive += 0     # Neutral for disruptive
            $ scenario_disrespectful += 1  # Slightly disrespectful tone
            $ scenario_refusal += 1        # Slight increase in work refusal possibility
            $ scenario_conflict += 0       # Neutral for conflict
        "I'm already so over it":
            $ mood = "Angry"       # Player is angry
            hide ms
            show msad           # Mousy looks sad
            $ scenario_emotional += 3      # Strong indicator for emotional issues
            $ scenario_disruptive += 2     # Anger can lead to disruption
            $ scenario_disrespectful += 2  # Anger can lead to disrespect
            $ scenario_refusal += 1        # May refuse work when upset
            $ scenario_conflict += 2       # Anger can lead to conflict
        "I'd rather be anywhere else":
            $ mood = "Nervous"     # Player is nervous
            hide ms
            show msad           # Mousy looks sad
            $ scenario_emotional += 2      # Anxiety is an emotional issue
            $ scenario_disruptive += 1     # May be disruptive due to anxiety
            $ scenario_disrespectful += 0  # Neutral for disrespectful
            $ scenario_refusal += 2        # Strong indicator for work refusal
            $ scenario_conflict += 1       # May engage in conflict due to anxiety

    # Reset expression before continuing
    hide mh
    hide msad
    show ms

    # Dialogue based on the player's mood
    if mood == "Excited!":
        voice "audio/intro_scene_e_13.mp3"
        e "Awesome! It's great to hear you're off to a good start today."
    else:
        voice "audio/intro_scene_e_14.mp3"
        e "Aww, I'm sure it'll get better as the day progresses."

    voice "audio/intro_scene_e_15.mp3"
    e "Are you excited for classes today?"

    # *****************************************************************
    # PLAYER CHOICE: Class excitement level
    # Note: This menu reuses the 'mood' variable to capture the player's
    # attitude toward class. It will overwrite the previous mood value.
    # *****************************************************************
    menu:
        "Yeah! All of them!":
            $ mood = "Excited!"    # Player is excited about classes
            hide ms
            show mh             # Mousy looks happy
            $ scenario_emotional -= 1      # Positive attitude decreases emotional issues
            $ scenario_disruptive -= 2     # Less likely to be disruptive when engaged
            $ scenario_disrespectful -= 1  # Less likely to be disrespectful when interested
            $ scenario_refusal -= 2        # Much less likely to refuse work when interested
            $ scenario_conflict -= 1       # Less likely to engage in conflict when positive
        "None really, just trying to get through it":
            $ mood = "Neutral"     # Player is neutral about classes
            hide ms
            show msad           # Mousy looks sad
            $ scenario_emotional += 1      # Slight increase in emotional indicators
            $ scenario_disruptive += 1     # Slight increase in disruptive potential
            $ scenario_disrespectful += 1  # Slight increase in disrespectful potential
            $ scenario_refusal += 2        # Higher chance of work refusal
            $ scenario_conflict += 0       # Neutral for conflict
        "Class is so boring! I always get called on for no reason!":
            $ mood = "Angry"       # Player is angry about class
            hide ms
            show msad           # Mousy looks sad
            $ scenario_emotional += 2      # Frustration is an emotional issue
            $ scenario_disruptive += 3     # Strong indicator for disruptive behavior
            $ scenario_disrespectful += 2  # Likely to be disrespectful if frustrated
            $ scenario_refusal += 2        # Likely to refuse work if finds class boring
            $ scenario_conflict += 1       # May engage in conflict due to frustration
        "I'm thinking of just not going":
            $ mood = "Nervous"     # Player is nervous about attending class
            hide ms
            show msad           # Mousy looks sad
            $ scenario_emotional += 1      # Avoidance indicates emotional issues
            $ scenario_disruptive += 1     # May be disruptive to avoid class
            $ scenario_disrespectful += 1  # May be disrespectful to get sent out
            $ scenario_refusal += 3        # Very strong indicator for work refusal
            $ scenario_conflict += 1       # May engage in conflict to avoid class

    # Branch dialogue based on class excitement
    if mood == "Excited!":
        voice "audio/intro_scene_e_16.mp3"
        e "Awesome! I wish I had some of your excitement. I'm a bit scared for my exam!"
    elif mood == "Neutral":
        voice "audio/intro_scene_e_17.mp3"
        e "Yeah, I feel the same way right now, considering I have an exam. I'm sure it'll be better for the both of us soon enough!"
    else:
        voice "audio/intro_scene_e_18.mp3"
        e "I'm sorry you feel that way. Hopefully, everything works out!"

    # Hide all expressions before ending the introduction
    hide msad
    hide mh
    show ms

    call locker_scene

    # not sure if this is correct place for this, but here we are
    
    # # Determine which scenario has the highest score
    # python:
    #     scenario_scores = {
    #         "disruptive": scenario_disruptive,
    #         "disrespectful": scenario_disrespectful,
    #         "emotional": scenario_emotional,
    #         "refusal": scenario_refusal,
    #         "conflict": scenario_conflict
    #     }
        
    #     # Find the scenario with the highest score
    #     highest_scenario = max(scenario_scores, key=scenario_scores.get)
    #     highest_value = scenario_scores[highest_scenario]
        
    #     # In case of a tie, prioritize in this order
    #     priority_order = ["disrespectful", "emotional", "disruptive", "refusal", "conflict"]
        
    #     # Check for ties and resolve based on priority
    #     ties = [s for s in scenario_scores if scenario_scores[s] == highest_value]
    #     if len(ties) > 1:
    #         # Find the highest priority scenario among ties
    #         for scenario in priority_order:
    #             if scenario in ties:
    #                 highest_scenario = scenario
    #                 break

    # e "Well, it's almost time for class. Let's get going!"

    # # Jump to the appropriate scenario
    # if highest_scenario == "disruptive":
    #     jump disruptive_scenario
    # elif highest_scenario == "disrespectful":
    #     jump disrespectful_scenario
    # elif highest_scenario == "emotional":
    #     jump emotional_scenario
    # elif highest_scenario == "refusal":
    #     jump refusal_scenario
    # elif highest_scenario == "conflict":
    #     jump conflict_scenario
    # else:
    #     # Default scenario if something goes wrong
    #     jump disrespectful_scenario
    
    return