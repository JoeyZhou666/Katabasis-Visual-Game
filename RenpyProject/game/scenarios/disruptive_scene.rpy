# *********************************************************************
# Disruptive Behavior Scenario
# 
# This scene focuses on classroom disruption and decision-making,
# helping students with emotional and behavioral disorders understand
# the consequences of their choices and develop better decision intelligence.
# ********************************************************************* 
label disruptive_scene:
    play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2

    scene hallway3
    
    voice "audio/disruptive_scene_n_01.mp3"
    n "As I walk through the empty hallway, the sound of my footsteps echoes against the lockers. The conversation with Mousy still lingers in my mind."
    
    voice "audio/disruptive_scene_n_02.mp3"
    n "I can't help but wonder what today's class will bring. Hopefully I don't have a test soon like Mousy did."
        
    voice "audio/disruptive_scene_n_03.mp3"
    n "After a short walk I found my way to the classroom and with a deep breath, I push open the classroom door, ready to face whatever comes next."
    
    # Set the classroom scene
    scene bg classroom

    show t

    voice "audio/disruptive_scene_t_01.mp3"
    t "Welcome everyone, please pay attention. This material will definitely be on Friday's test."
    
    # Inner thoughts based on mood
    if mood == "Angry":
        n "*You tap your pencil impatiently as Ms. Johnson goes on about ecosystems.*"
    elif mood == "Nervous":
        n "*Your stomach feels tight as you think about the upcoming test.*"
    elif mood == "Excited!":
        n "*You're ready to learn, but keeping still is challenging today.*"
    else:
        n "*You struggle to keep your eyes open as Ms. Johnson talks about ecosystems.*"
    
    # Effects based on sleep
    if sleep == "Less than 6 hours":
        n "*The words on the board seem to blur together.*"
    
    # Hide teacher temporarily to show Bandit
    hide t
    show f 
    play sound "audio/music/punch.mp3" volume 0.2
    stop music
    # Bandit leans over and hits the player
    voice "audio/disruptive_scene_f_01.mp3"
    f "Hey [povname]..." with hpunch
    play music "audio/music/mischiefmusic.wav" loop volume 0.2
    
    voice "audio/disruptive_scene_n_04.mp3"
    n "Bandit punches your arm playfully but a bit too hard."
    
    voice "audio/disruptive_scene_f_02.mp3"
    f "Did you watch that hilarious cat video I sent you yesterday?"
    
    voice "audio/disruptive_scene_n_05.mp3"
    n "Bandit's eyes light up with excitement as they lean closer to your desk, rubbing the spot where they just hit you."
    
    # Player's choice on how to respond to Bandit
    menu:
        "Ignore Bandit":
            hide f
            jump ignore
        "Quickly whisper \"Yeah\" and turn back":
            hide f
            jump brief_response
        "Start talking about the video":
            hide f
            jump chatty_response

# *********************************************************************
# Ignore Path
# *********************************************************************
label ignore:
    # Player ignores Bandit
    voice "audio/disruptive_scene_n_06.mp3"
    n "You ignore Bandit and keep your eyes on Ms. Johnson's notes on the board."
    
    # Show Bandit trying again and hitting the player harder
    show f

    play sound "audio/vibration.mp3" 
    
    voice "audio/disruptive_scene_f_03.mp3"
    f "Hey, [povname]," with hpunch
    
    voice "audio/disruptive_scene_n_07.mp3"
    n "Bandit punches your arm again, harder this time."
    
    voice "audio/disruptive_scene_f_04.mp3"
    f "Did you see the part with the cat? It was hilarious!"
    
    # Player continues to ignore
    voice "audio/disruptive_scene_n_08.mp3"
    n "You rub your arm and continue to ignore them, but Bandit is persistent."
    
    # Bandit tries a different approach
    voice "audio/disruptive_scene_f_05.mp3"
    f "Come on, I know you're listening. Look what I drew."
    
    voice "audio/disruptive_scene_n_09.mp3"
    n "Bandit slides a piece of paper onto your desk. It's a tic-tac-toe grid."
    
    menu:
        "Keep ignoring and push the paper away":
            voice "audio/disruptive_scene_n_10.mp3"
            n "You gently push the paper back without looking at Bandit."
            
            voice "audio/disruptive_scene_f_06.mp3"
            f "Fine, be that way."
            
            voice "audio/disruptive_scene_n_11.mp3"
            n "Bandit finally gives up with a frustrated sigh and turns away."
            
            hide f
            
            # Show teacher noticing the player's focus
            show t
            
            voice "audio/disruptive_scene_n_12.mp3"
            n "Ms. Johnson continues writing on the board, occasionally glancing back at the class."
            
            voice "audio/disruptive_scene_t_02.mp3"
            t "Now, the food chain is a crucial part of any ecosystem. Energy flows from producers to consumers..."
            
            # Teacher gives an approving nod
            voice "audio/disruptive_scene_n_13.mp3"
            n "Ms. Johnson notices your focus and gives you an approving nod."
            
            voice "audio/disruptive_scene_t_03.mp3"
            t "I'm glad to see some students are taking their education seriously."
            
            # Player's thoughts
            $ thoughts = renpy.input("How do you feel about ignoring your friend?")
            
            voice "audio/disruptive_scene_n_14.mp3"
            n "You feel a mix of pride for focusing on your work and a twinge of guilt for ignoring Bandit."
            
            # Continue focusing on the lesson
            jump focus_on_lesson
            
            voice "audio/disruptive_scene_n_15.mp3"
        "Play one quick game of tic-tac-toe":

            voice "audio/disruptive_scene_n_16.mp3"
            n "You decide one quick game won't hurt."
            
            # Call the tic-tac-toe minigame
            call play_tictactoe
            
            hide f
            show fs

            # Game outcome affects the story
            if ttt_winner == 1:
                # Player won
                voice "audio/disruptive_scene_f_07.mp3"
                f "No way! How did you beat me?"
                
                voice "audio/disruptive_scene_n_17.mp3"
                n "Bandit looks impressed but wants a rematch."
                
                voice "audio/disruptive_scene_f_08.mp3"
                f "One more game? I bet I can beat you this time."
                
            elif ttt_winner == 2:
                # CPU (Bandit) won
                voice "audio/disruptive_scene_f_09.mp3"
                f "Ha! I win! Better luck next time."
                
                voice "audio/disruptive_scene_n_18.mp3"
                n "Bandit does a little victory dance in their seat."
                
                voice "audio/disruptive_scene_f_10.mp3"
                f "Want to try again? I'll go easy on you this time."
                
            else:
                # Tie game
                voice "audio/disruptive_scene_f_11.mp3"
                f "A tie? Come on, let's play again to break the tie."
            
            # Teacher catches you
            hide fs
            show t
            
            n "*Ms. Johnson stops mid-sentence and walks toward your desk.*"
            
            voice "audio/disruptive_scene_t_04.mp3"
            t "[povname], what's that you're working on?"
            
            n "*She picks up the tic-tac-toe paper.*"

            hide t
            show ts
            
            voice "audio/disruptive_scene_t_05.mp3"
            t "This doesn't look like ecosystem notes to me."

            hide ts
            show t
            
            menu:
                "Apologize immediately":
                    pov "Sorry, Ms. Johnson. It won't happen again."
                    
                    voice "audio/disruptive_scene_t_06.mp3"
                    t "I should hope not. This material will be on your test."
                    
                    n "*She returns to the front of the class, keeping the tic-tac-toe paper.*"
                    
                    hide t
                    show f
                    
                    n "*Bandit gives you an apologetic look.*"
                    
                    voice "audio/disruptive_scene_f_12.mp3"
                    f "Sorry about that. I didn't mean to get you in trouble."
                    
                    hide f
                    show t
                    
                    jump teacher_warning
                    
                "Make an excuse":
                    pov "We were just... illustrating the food chain connections."
                    
                    n "*Ms. Johnson raises an eyebrow, clearly not convinced.*"
                    
                    voice "audio/disruptive_scene_t_07.mp3"
                    t "Really? And how exactly does tic-tac-toe relate to ecosystems?"
                    
                    n "*The class snickers quietly.*"
                    
                    voice "audio/disruptive_scene_t_08.mp3"
                    t "This is your warning. Pay attention or you'll need to move seats."
                    
                    jump teacher_warning

# *********************************************************************
# Brief Response Path
# *********************************************************************
label brief_response:
    # Player gives a brief response
    pov "Yeah, it was cool."
    
    voice "audio/disruptive_scene_n_19.mp3"
    n "You whisper quickly, then turn back to your notes, trying to stay focused on the lesson."
    
    # Bandit continues trying to engage
    show f
    
    voice "audio/disruptive_scene_n_20.mp3"
    n "Bandit isn't satisfied with your brief answer and leans closer."
    
    hide f 
    show fs

    voice "audio/disruptive_scene_f_13.mp3"
    f "Did you see the part where they fell into the pool? I couldn't stop laughing."
    
    voice "audio/disruptive_scene_n_21.mp3"
    n "Bandit mimics someone falling and makes a quiet splashing sound."
    
    voice "audio/disruptive_scene_n_22.mp3"
    n "You can feel Ms. Johnson glancing in your direction occasionally."
    
    # Player's choice on how to proceed
    menu:
        "Keep focusing on the lesson":
            hide fs
            show f
            n "*You give Bandit a quick smile but point to your notes, indicating you need to focus.*"
            
            n "*Bandit looks disappointed but understands.*"
            
            voice "audio/disruptive_scene_f_14.mp3"
            f "Fine, we'll talk after class."
            
            n "*Bandit turns back to their own notes with a small sigh.*"
            
            hide f
            jump focus_on_lesson
            
        "Give in and continue chatting":
            pov "That part was hilarious! And when they tried to act all cool afterward..."
            
            n "*You and Bandit both start giggling quietly.*"
            
            voice "audio/disruptive_scene_f_15.mp3"
            f "I know, right? I almost died laughing!"
            
            n "*Your conversation is getting louder without you realizing it.*"
            
            hide fs
            jump teacher_warning

# *********************************************************************
# Chatty Response Path
# *********************************************************************
label chatty_response:
    show f

    # Player engages enthusiastically
    pov "Oh my gosh, yes!"
    
    voice "audio/disruptive_scene_n_23.mp3"
    n "You whisper back enthusiastically, momentarily forgetting you're in class."
    
    pov "That part with the dog was so funny! I couldn't believe when it started dancing!"
    
    # Bandit gets more excited by your response
    hide f
    show fs
    
    voice "audio/disruptive_scene_n_24.mp3"
    n "Bandit's eyes light up, thrilled that you're engaging with them."
    
    voice "audio/disruptive_scene_f_16.mp3"
    f "Right?! And when they tried to climb the fence but their pants got caught!"
    
    # Bandit laughs too loudly
    voice "audio/disruptive_scene_n_25.mp3"
    n "Bandit laughs a little too loudly, unable to contain their excitement."
    
    voice "audio/disruptive_scene_n_26.mp3"
    n "Several students turn to look at you both. Some seem amused, others annoyed at the disruption."
    
    # Teacher notices the disruption
    hide fs
    show t
    
    voice "audio/disruptive_scene_n_27.mp3"
    n "Ms. Johnson stops writing on the board and turns around slowly."
    
    voice "audio/disruptive_scene_n_28.mp3"
    n "The chalk makes a slight squeaking sound as she sets it down, and the room falls silent."
    
    voice "audio/disruptive_scene_t_09.mp3"
    t "Is there something interesting happening back there that you'd like to share with the whole class?"
    
    voice "audio/disruptive_scene_n_29.mp3"
    n "Her tone is calm but firm, and her gaze is fixed directly on you and Bandit."
    
    # Player's choice on how to respond to the teacher
    menu:
        "Quickly apologize":
            jump quick_apology
        "Make an excuse: \"Just asking about the lesson\"":
            jump make_excuse
        "Say \"It's nothing\" with attitude":
            jump attitude_response

# *********************************************************************
# Focus on Lesson Path
# *********************************************************************
label focus_on_lesson:
    play music "audio/music/hsdream.wav" loop volume 0.2
    # Show teacher continuing the lesson
    show t
    
    n "*You focus on the lesson about ecosystems. Ms. Johnson explains how different organisms depend on each other and how energy flows through the food chain.*"
    
    voice "audio/disruptive_scene_t_10.mp3"
    t "Remember that producers like plants convert sunlight into energy through photosynthesis. Then primary consumers eat the plants, and secondary consumers eat the primary consumers."
    
    n "*You take good notes that will help you study for Friday's test.*"
    
    voice "audio/disruptive_scene_t_11.mp3"
    t "This will definitely be on the test, so make sure you understand the relationship between producers and consumers in an ecosystem."
    
    n "*When class ends, you feel good about what you've learned.*"
    
    # Proceed to reflection
    jump reflection

# *********************************************************************
# Quick Apology Path
# *********************************************************************
label quick_apology:
    # Player apologizes quickly
    pov "Sorry, Ms. Johnson."
    
    n "*You sit up straighter in your chair.*"
    
    play music "audio/music/hsdream.wav" loop volume 0.2
    # Teacher acknowledges the apology
    voice "audio/disruptive_scene_t_12.mp3"
    t "Please pay attention. This will be on the test."
    
    # Player focuses on the lesson
    hide t
    jump focus_on_lesson

# *********************************************************************
# Make Excuse Path
# *********************************************************************
label make_excuse:
    # Player makes an excuse
    pov "I was just asking about the ecosystems."
    
    n "*You try to sound convincing, but your voice wavers slightly.*"
    
    n "*You can feel Bandit trying not to laugh behind you.*"
    
    # Teacher is not convinced
    voice "audio/disruptive_scene_t_13.mp3"
    t "If you have questions about the material, you should raise your hand and ask me, not disrupt your neighbor."
    
    n "*Ms. Johnson raises an eyebrow, clearly not convinced. Her eyes move from you to Bandit and back again.*"
    
    n "*A few students are watching the interaction with interest, and you feel your face getting warm.*"
    
    # Player's choice on how to proceed
    menu:
        "Nod and focus on the lesson":
            n "*You nod quickly and look down at your notebook, pretending to write something important.*"
            
            n "*Ms. Johnson watches you for a moment longer before returning to the front of the class.*"
            
            voice "audio/disruptive_scene_t_14.mp3"
            t "As I was saying before the interruption..."
            
            hide t
            jump teacher_warning

# *********************************************************************
# Attitude Response Path
# *********************************************************************
label attitude_response:
    # Player responds with attitude
    pov "It's nothing."
    
    n "*You say with a slight eye roll, not quite meeting Ms. Johnson's gaze.*"
    
    n "*The classroom goes quiet. You can feel everyone watching the interaction.*"
    
    # Teacher becomes stern
    voice "audio/disruptive_scene_t_15.mp3"
    t "That attitude won't help you pass Friday's test."
    
    n "*Ms. Johnson's expression hardens, and her voice takes on an edge that wasn't there before.*"
    
    n "*You feel a mix of embarrassment and defiance as the tension in the room builds.*"
    
    # Player's choice on how to proceed
    menu:
        "Look down and focus on the lesson":
            n "*You realize you've pushed too far and lower your gaze to your notebook.*"
            
            n "*Your cheeks burn with embarrassment as you feel the weight of Ms. Johnson's disapproval.*"
            
            n "*After what feels like an eternity, she returns to the front of the class.*"
            
            hide t
            jump teacher_warning

# *********************************************************************
# Teacher Warning Path
# *********************************************************************
label teacher_warning:
    # Teacher gives a direct warning
    show t
    
    voice "audio/disruptive_scene_t_16.mp3"
    t "This is a warning. I need you to pay attention and stop distracting others."
    
    n "*Several students are looking at you now, and you feel your face getting warm.*"
    
    # Player's choice on how to proceed
    menu:
        "Comply and focus":
            hide t
            jump focus_on_lesson
        "Keep talking to Bandit when she turns around":
            hide t
            jump second_warning

# *********************************************************************
# Second Warning Path
# *********************************************************************
label second_warning:
    # Player waits for teacher to turn around
    n "*You wait until Ms. Johnson turns to write on the board, her chalk scratching against the green surface.*"
    
    # Show Bandit
    show f
    
    # Player whispers to Bandit
    pov "She's always so strict."
    
    n "*Bandit nods in agreement, leaning closer to whisper back.*"
    
    voice "audio/disruptive_scene_f_17.mp3"
    f "I know, right? Last week she—"
    
    # Teacher catches the player
    hide f
    show t
    
    n "*Ms. Johnson turns around immediately, as if she has eyes in the back of her head. The chalk makes a sharp sound as she sets it down.*"
    
    n "*She walks directly to your desk, her footsteps echoing in the suddenly silent classroom.*"
    
    voice "audio/disruptive_scene_t_17.mp3"
    t "This is the second time I've had to stop teaching. One more disruption and you'll need to move seats."
    
    n "*Her voice is calm but firm, leaving no room for argument.*"
    
    n "*The whole class is watching now. Some students look down at their desks, avoiding eye contact, while others stare openly at the confrontation.*"
    
    # Player's choice on how to proceed
    menu:
        "Finally stop talking":
            n "*You nod silently, feeling a mix of embarrassment and frustration.*"
            
            n "*Ms. Johnson holds your gaze for a moment longer before returning to the board.*"
            
            hide t
            jump focus_on_lesson
            
        "Say \"That's not fair!\"":
            hide t
            show ts

            n "*The words escape your mouth before you can stop them.*"
            
            n "*A few students gasp quietly, and you immediately regret speaking up.*"
            
            hide ts
            jump final_escalation
            
        "Roll your eyes at the teacher":
            hide t
            show ts
            n "*You roll your eyes, not quite able to hide your frustration.*"
            
            hide ts
            show t
            n "*Ms. Johnson's expression shifts from stern to genuinely disappointed.*"
            
            hide t
            jump final_escalation

# *********************************************************************
# Final Escalation Path
# *********************************************************************
label final_escalation:
    # Teacher's patience runs out
    show t
    
    n "*Ms. Johnson takes a deep breath, clearly trying to maintain her composure.*"
    
    voice "audio/disruptive_scene_t_18.mp3"
    t "[povname], this is unacceptable. Move to the front seat now."
    
    n "*Her voice is quiet but intense, and her expression has hardened into something that leaves no room for argument.*"
    
    n "*The classroom is completely silent. You can hear the clock ticking on the wall and someone's pencil rolling off their desk.*"
    
    n "*Everyone is staring at you. Some look uncomfortable, others seem almost eager to see what happens next.*"
    
    n "*You feel a knot forming in your stomach as the tension builds.*"
    
    # Player's choice on how to proceed
    menu:
        "Reluctantly move":
            n "*You feel a mix of anger and embarrassment, but something tells you this isn't a battle worth fighting.*"
            
            n "*With a heavy sigh, you begin gathering your things.*"
            
            hide t
            jump continue_lesson
            
        "Refuse to move":
            n "*A surge of defiance rises in you. You've been pushed too far, and something inside snaps.*"
            
            n "*You cross your arms and plant yourself firmly in your seat.*"
            
            hide t
            jump sent_to_office

# *********************************************************************
# Continue Lesson Path
# *********************************************************************
label continue_lesson:
    # Player moves to the front seat
    n "*With a heavy sigh, you gather your things - your notebook, pencil case, and textbook - and slowly make your way to the front seat.*"
    
    n "*The sound of your chair scraping against the floor seems impossibly loud in the silent classroom.*"
    
    n "*Your face burns with embarrassment as you feel everyone watching you. You avoid making eye contact with anyone, especially Bandit.*"
    
    n "*As you settle into your new seat, you notice a few sympathetic glances from other students, but most quickly look away when you notice them.*"
    
    # Show teacher continuing the lesson
    show t
    
    n "*Ms. Johnson nods once, satisfied with your compliance, and returns to the board.*"
    
    voice "audio/disruptive_scene_t_19.mp3"
    t "Now, as I was saying before the interruption, the energy transfer between trophic levels is inefficient, with only about 10% of energy moving from one level to the next..."
    
    n "*It's harder to concentrate now. Your embarrassment has turned to a dull anger that makes it difficult to focus on ecosystems and food chains.*"
    
    n "*Still, you try to take notes for the test, knowing that missing this information will only make things worse.*"
    
    n "*The minutes drag by slowly, but eventually the bell rings.*"
    
    n "*When class finally ends, you quickly pack up your things, eager to escape the room before anyone can talk to you about what happened.*"
    
    # Proceed to reflection
    hide t
    jump reflection

# *********************************************************************
# Sent to Office Path
# *********************************************************************
label sent_to_office:
    show ts

    # Player refuses to move
    pov "I'm not moving. This is so unfair!"
    
    n "*The words come out louder than you intended, echoing in the silent classroom.*"
    
    n "*A few students gasp. Someone whispers, \"Oh no...\" from somewhere behind you.*"
    
    hide ts
    show t

    stop music fadeout 2
    n "*Ms. Johnson's expression shifts from shocked to resigned. She doesn't argue or raise her voice.*"
    
    n "*Instead, she walks calmly to her desk and picks up the phone, speaking quietly into it.*"
    
    n "*The tension in the room is unbearable as everyone waits. You can feel your heart pounding in your chest.*"
    
    n "*A few minutes later, the assistant principal arrives at the classroom door. He's a tall man with a serious expression.*"
    
    # Assistant principal takes the player to the office
    "Assistant Principal" "Let's go have a conversation in my office, [povname]."
    
    n "*His tone is neutral, neither angry nor sympathetic.*"
    
    n "*As you gather your things and walk toward the door, you notice the range of expressions on your classmates' faces.*"
    
    n "*Some look uncomfortable or even worried for you. Others seem entertained by the drama, hiding smirks behind their hands.*"
    
    n "*Bandit won't meet your eyes as you pass by.*"
    
    n "*In the hallway, the assistant principal walks silently beside you. The click of his dress shoes against the floor tiles seems to emphasize how much trouble you're in.*"
    
    "*You miss the rest of the lesson about ecosystems that will be on Friday's test, and you wonder how this will affect your grade... and what your parents will say when they find out.*"
    
    # Proceed to reflection
    hide t
    jump reflection

# *********************************************************************
# Reflection Path
# *********************************************************************
label reflection:
    # Set a neutral background for reflection
    play music "audio/music/afternoontea.wav" loop volume 0.2
    scene bg classroom
    
    "*Looking back on what happened in class today:*"
    
    # Player reflects on their actions
    $ action_reflection = renpy.input("What actions did you take that affected how things turned out?")
    
    # Player reflects on the results
    $ result_reflection = renpy.input("What happened as a result of your choices?")
    
    # Player reflects on their feelings
    $ feeling_reflection = renpy.input("How do you feel about the outcome?")
    
    # Player reflects on external factors
    $ external_reflection = renpy.input("What factors outside your control influenced the situation?")
    
    # Show Mousy for the conclusion
    show ms
    
    # Mousy thanks the player
    voice "audio/disruptive_scene_e_01.mp3"
    e "[povname], thank you for experiencing this scenario!"
    
    # Create a variable to track the player's path
    $ path_taken = ""
    
    if "ignore" in action_reflection.lower() or "focus" in action_reflection.lower():
        $ path_taken = "focused"
        voice "audio/disruptive_scene_e_02.mp3"
        e "You made some good choices to stay focused despite distractions. That's a skill that will help you succeed in school!"
    elif "move" in action_reflection.lower() or "front" in action_reflection.lower():
        $ path_taken = "moved"
        voice "audio/disruptive_scene_e_03.mp3"
        e "You had some challenges with distractions, but in the end, you made the right choice to follow the teacher's instructions."
    elif "refuse" in action_reflection.lower() or "office" in action_reflection.lower():
        $ path_taken = "office"
        voice "audio/disruptive_scene_e_04.mp3"
        e "It can be hard to control our reactions sometimes, but remember that refusing to follow instructions can lead to bigger problems."
    else:
        voice "audio/disruptive_scene_e_05.mp3"
        e "Every choice we make has consequences. Thinking about how our actions affect others is an important skill."
    
    # End the scene
    voice "audio/disruptive_scene_e_06.mp3"
    e "Remember, the choices you make in class affect not just your learning, but everyone around you too."
    
    # Return to the main script
    jump final

# *********************************************************************
# Final Label
# *********************************************************************
label final:
    voice "audio/disruptive_scene_e_07.mp3"
    e "[povname], thank you for experiencing this demo so far!"
    voice "audio/disruptive_scene_e_08.mp3"
    e "Demo ends here."
    "More content To Be Continued..."
    "Access the CDD like this..."
    # End the game.
    return
