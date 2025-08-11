# *********************************************************************
# Emotional Outburst Scenario
# 
# This scene focuses on emotional regulation and decision-making in a classroom setting,
# helping students with emotional and behavioral disorders understand
# how to manage their emotions and the consequences of emotional outbursts.
# *********************************************************************

# Variables for tracking player choices in emotional_outburst_scene
default focus_choice = ""                  # How player handles difficulty focusing
default math_answer = ""                   # Player's answer to math problem
default fidget_response = ""               # How player responds when fidgeting
default help_response = ""                 # How player responds when asking for help
default group_approach = ""                # How player approaches group work
default third_problem = ""                 # How player handles the third math problem
default response_to_insult = ""            # How player responds to Crusher's insult
default final_response = ""                # Player's final response in confrontation
default crusher_friendship = 0             # Tracks positive interactions with Crusher

label emotional_outburst_scene:
    # Set the classroom scene
    scene bg classroom5
    
    play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2

    # Set the scene
    pov "After the incident at the lockers, I make my way to Ms. Johnson's math class."
    
    pov "My mind is still racing from finding the note in Mousy's locker. It's hard to shake off the feeling of being targeted."
    
    pov "As I enter the classroom, the familiar scent of chalk dust fills my nostrils. Students are settling into their seats, the soft murmur of conversation filling the air."
    
    # Show teacher at the front of the class
    show t
    
    t "Good morning, everyone. Please take your seats. We have a lot to cover today."
    
    n "Ms. Johnson's voice cuts through the chatter, and students begin to quiet down. Everyone gets into their desk, pulling out their notebooks and pencils."
    
    t "Today we'll be reviewing math concepts and then working on some group activities to practice what we've learned."
    
    # Inner thoughts based on mood from previous scenes
    if mood == "Angry":
        n "Great. Math. Just what I need when I'm already irritated. The numbers on the board seem to blur together as my frustration from earlier continues to simmer."
    elif mood == "Nervous":
        n "My stomach tightens at the mention of group work. After what happened at my locker, the last thing I want is to interact with more people."
    elif mood == "Excited!":
        n "Despite what happened earlier, I try to focus on the positive. Math isn't my favorite, but at least it's predictable. Unlike people."
    else:
        n "I stare blankly at the board, my mind still stuck on the note from my locker. The equations Ms. Johnson writes might as well be in another language."
    
    # Effects based on sleep from intro scene
    if sleep == "Less than 6 hours":
        n "My lack of sleep isn't helping either. The fluorescent lights seem too bright, and Ms. Johnson's voice fades in and out as I struggle to stay alert."
    
    # Ms. Johnson begins the lesson
    t "Let's start by reviewing what we learned yesterday about math arithmetics."
    
    n "Ms. Johnson turns to write on the board, the chalk making a soft scratching sound as she writes out several problems."
    
    n "I try to focus, but my mind keeps wandering. The classroom feels too loud, too bright, too... everything."
    
    # Player's first choice on how to handle their difficulty focusing
    menu:
        "Put my head down to block out the noise":
            $ focus_choice = "head_down"
            jump head_down
        "Fidget with my pencil":
            $ focus_choice = "fidget"
            jump fidget_pencil
        "Ask Ms. Johnson for help focusing":
            $ focus_choice = "ask_help"
            jump ask_for_help

# *********************************************************************
# Head Down Path
# *********************************************************************
label head_down:
    pov "It's all too much. I slowly lower my head onto my folded arms, hoping to block out some of the sensory overload."
    
    pov "The sounds of the classroom become muffled, and the harsh lights no longer burn my eyes. I take a deep breath, trying to recenter myself."
    
    pov "For a moment, it works. The chaos in my mind begins to quiet down."
    
    stop music fadeout 5
    # Teacher notices
    "... ... ..."
    "... ... ..."
    "... ... ..."
    
    play music "audio/music/hsdream.wav" loop fadein 5 volume 0.2
    t "[povname]?"
    
    n "Ms. Johnson's voice cuts through my moment of rest, and I can feel the eyes of my classmates turning toward me."
    
    t "Since you seem so comfortable, perhaps you'd like to come to the board and solve this problem for us?"
    
    n "I slowly lift my head to see Ms. Johnson pointing to an equation on the board: Square root of 144."
    
    n "My cheeks burn with embarrassment as I realize I may have been caught not paying attention."
    
    # Player's choice on how to respond
    menu:
        "12":
            $ math_answer = "correct"
            hide t
            show ts
            pov "It's 12."

            hide ts
            show t           
            t "That's correct. But I'd still appreciate it if you'd stay engaged with the class, [povname]."
            
            n "There are a few snickers from around the room, but at least I got the answer right."
            
            # Introduce Crusher character
            n "From the back of the room, I hear a voice."
            
            # Show Dog character (Crusher)
            hide t
            show d
            stop music
            play music "audio/music/mischiefmusic.wav" fadein 1 volume 0.2
            d "Teacher's pet still knows the answers even when they're sleeping. How cute."
            
            n "I recognize that voice. It belongs to Crusher, the class bully. He's been making my life difficult since the beginning of the year."
            
            # Player's stress increases
            $ stress = "medium"
            
        "14":
            $ math_answer = "incorrect"
            pov "Um... 14?"
            
            n "I know it's wrong as soon as the words leave my mouth. Math has never been my strong suit, especially when put on the spot."
            
            # Teacher's disappointed response
            t "No, [povname], the square root of 144 is 12. Perhaps if you were paying attention instead of sleeping, you would know that."
            
            n "The class erupts in laughter, and my face burns hotter."
            
            # Introduce Crusher character
            hide t
            show d
            stop music
            play music "audio/music/mischiefmusic.wav" loop fadein 1 volume 0.2
            d "Wow, can't even answer a simple problem. Maybe you should go back to elementary school!"
            
            n "That's Crusher, the class bully. Of course he'd take this opportunity to make me feel worse."
            
            # Player's stress increases significantly
            $ stress = "high"
            
        "Admit I don't know":
            $ math_answer = "honest"
            pov "I'm sorry, Ms. Johnson. I don't know the answer right now. I'm having trouble focusing."
            
            t "I appreciate your honesty, [povname]. The answer is 12. Please try to stay with us, this material will be on a test."
            
            n "Ms. Johnson's tone is firm but not unkind. Still, I can feel the judgment from my classmates."
            
            # Crusher still makes a comment
            hide t
            show d
            stop music
            play music "audio/music/mischiefmusic.wav" fadein 1 volume 0.2
            d "Aww, poor baby can't focus. Maybe you need a nap time."
            
            n "I clench my fists under my desk. Crusher always knows exactly how to get under my skin."
            
            # Player's stress is moderate
            $ stress = "medium"
    
    # Return to the main flow
    stop music fadeout 1
    hide d
    jump group_work_intro

# *********************************************************************
# Fidget Pencil Path
# *********************************************************************
label fidget_pencil:
    n "I pick up my pencil and begin tapping it against my notebook, trying to channel my restless energy into something physical."
    
    n "The rhythmic tapping helps me focus on Ms. Johnson's words, giving my hands something to do while my brain processes the math concepts."
    
    # Other students notice
    n "After a minute or two, I notice a few students glancing in my direction. The tapping must be louder than I realized."
    
    # Introduce Crusher character
    hide t
    show d
    
    stop music
    play music "audio/music/mischiefmusic.wav" loop fadein 1 fadeout 1 volume 0.2
    d "Can you stop that? Some of us are trying to learn here."
    
    n "The comment comes from Crusher, as everyone calls him, he's the class bully. He's sitting a few desks away, glaring at me with obvious annoyance."
    
    # Teacher notices the disruption
    hide d
    show t
    
    t "Is there a problem back there?"
    
    # Player's choice on how to respond
    menu:
        "Apologize and stop tapping":
            $ fidget_response = "apologize"

            stop music fadeout 1
            play music "audio/music/hsdream.wav" loop fadein 1 volume 0.2
            pov "Sorry, Ms. Johnson. I'll stop."
            
            n "I set my pencil down, feeling a bit embarrassed but also frustrated since the tapping was helping me focus."
            
            t "Thank you. Now, as I was saying..."
            
            n "Ms. Johnson returns to the lesson, but now I'm back to square one with my concentration."
            
            # Stress level is moderate
            $ stress = "medium"
            
        "Explain that it helps me focus":
            $ fidget_response = "explain"
            pov "The tapping helps me focus, Ms. Johnson. I can try to do it more quietly."
            
            # Teacher's understanding response
            t "I understand, [povname], but it's distracting to others. Perhaps you could try doodling instead? It's quieter but still gives your hands something to do."
            
            n "I nod, appreciating her suggestion. At least she didn't just shut me down."
            
            # Crusher still makes a comment
            hide t
            show d
            
            d "Special treatment as usual. If I did that, I'd get detention."
            
            n "I ignore Crusher's comment, focusing instead on Ms. Johnson's suggestion. I begin to doodle random patterns in the corners of my notebook."
            
            stop music fadeout 1
            # Stress level is lower
            $ stress = "low"
            
        "Glare at Crusher":
            $ fidget_response = "confront"
            
            pov "I stop tapping but look over at Crusher. He is the one who made an unnecessary comment!"
            
            hide t
            show d
            
            d "What? Got something to say?"
            
            pov "Crusher's challenging tone makes my blood boil. He's always looking for ways to provoke me."
            
            # Teacher intervenes
            hide d
            show t
            
            t "That's enough, both of you. [povname], please stop the tapping. And Crusher, focus on your own work."
            
            pov "I reluctantly comply, but the tension between Crusher and me lingers in the air like an electrical charge."
            
            stop music fadeout 1
            # Stress level is high
            $ stress = "high"
    
    # Return to the main flow
    hide d
    hide t
    hide ts
    jump group_work_intro

# *********************************************************************
# Ask for Help Path
# *********************************************************************
label ask_for_help:
    # Player raises hand to ask for help
    n "I take a deep breath and raise my hand, deciding to be honest about my struggle."
    
    # Teacher acknowledges
    show t
    
    t "Yes, [povname]?"
    
    # Player explains
    pov "Ms. Johnson, I'm having trouble focusing today. Is there something I can do that might help?"
    
    n "The words come out quieter than I intended, but Ms. Johnson hears me. A few students turn to look, curiosity on their faces."
    
    # Teacher's response
    t "Thank you for letting me know. Would it help if you moved to the front row? Or perhaps you could try taking notes in a different format—some students find that drawing concept maps helps them engage with the material."
    
    n "Ms. Johnson's understanding response makes me feel a bit better. At least she's not dismissing my struggle."
    
    # Crusher mocks the player
    hide t
    show d
    
    stop music
    play music "audio/music/mischiefmusic.wav" loop fadein 1 fadeout 1 volume 0.2
    d "Aww, does the baby need special attention? Maybe we should all stop learning so [povname] can catch up."
    
    n "Crusher's mocking voice carries across the classroom, followed by a few snickers from his friends."
    
    # Player's choice on how to respond to Crusher
    menu:
        "Ignore him and thank Ms. Johnson":
            $ help_response = "ignore"
            
            hide d
            show t
            
            pov "Thanks, Ms. Johnson. I'll try the concept mapping."
            
            t "Good. And Crusher, that comment was unnecessary and unkind. See me after class."
            
            n "I feel a small surge of satisfaction as Ms. Johnson calls Crusher out. Maybe there is some justice in the world."
            
            # Stress level is low
            $ stress = "low"
            
        "Call Crusher a name back":
            $ help_response = "retaliate"
            
            hide d
            show ds

            pov "At least I'm trying to learn, unlike some people who just waste everyone's time with stupid comments."
            
            n "The words fly out of my mouth before I can stop them. The classroom goes silent as everyone waits for what will happen next."
            
            # Crusher's response
            d "What did you just say to me?"
            
            # Teacher intervenes
            hide d
            show ts
            
            t "That's enough! Both of you, this is a classroom, not a playground. One more outburst from either of you, and you'll be spending time in the principal's office."
            
            hide ts
            show t
            
            n "Ms. Johnson's stern voice cuts through the tension, but I can feel Crusher's eyes boring into the back of my head. This isn't over."
            
            # Stress level is high
            $ stress = "high"
            
        "Try a calming technique":
            $ help_response = "calm"
            
            n "I close my eyes and take a deep breath, counting to five in my head before exhaling slowly. The counselor taught me this technique for moments exactly like this."
            
            hide d
            show t
            
            pov "I'll try the concept mapping, Ms. Johnson. Thank you."
            
            t "Good choice. And Crusher, that comment was inappropriate. Please see me after class."
            
            n "I focus on my breathing, letting Crusher's words roll off me like water. It's not easy, but it's better than letting him see how much he affects me."
            
            # Stress level is medium
            $ stress = "medium"
    
    # Return to the main flow
    hide d
    hide t
    hide ts
    jump group_work_intro

# *********************************************************************
# Group Work Introduction
# *********************************************************************
label group_work_intro:
    # Teacher introduces group work
    play music "audio/music/hsdream.wav" loop fadein 1 volume 0.2
    show t
    
    t "Alright, class. Now that we've reviewed the concepts, it's time to put them into practice. I'm going to divide you into groups of three for a collaborative problem-solving activity."
    
    n "A collective groan ripples through the classroom. Group work is rarely anyone's favorite, but for me, it's particularly challenging, especially after what just happened."
    
    t "I've already assigned the groups. When I call your name, please move to sit with your team members."
    
    n "Ms. Johnson begins reading names from her list. I silently pray to be grouped with anyone but Crusher."
    
    t "[povname], you'll be working with Bandit and{cps=4}... {/cps}{cps=10}Crusher.{/cps}"
    
    n "My heart sinks. Of all the students in class, I get paired with Crusher? At least Bandit is in our group too, he's always been friendly to me."
    
    hide t
    show f
    
    f "Hey, [povname]! Looks like we're a team. This should be interesting, huh?"
    
    n "Bandit's cheerful greeting lifts my spirits slightly. He's always had a knack for lightening tense situations."
    
    # Show Crusher joining the group
    hide f
    show ds
    
    d "Great. Stuck with the space cadet and the class clown. This should be a disaster."
    
    n "Crusher drops his books on the desk with a loud thud, making it clear he's not happy with the arrangement either."
    
    # Show both Bandit and Crusher (need to create this image or use positioning)
    hide ds
    show f at left
    show d at right
    
    f "Come on, Crusher, it won't be that bad. Let's just get through these problems and be done with it."
    
    n "Bandit tries to mediate, but there is still tension between Crusher and I. I take a deep breath, reminding myself that I just need to get through this class."
    
    # Teacher hands out worksheets
    hide f
    hide d
    show t
    
    t "Each group will receive a worksheet with three problems. Work together to solve them, and make sure everyone in the group understands the solutions. You have 20 minutes."
    
    n "Ms. Johnson hands out the worksheets. I glance at the problems: 10 + 35, 57 + 28, and a third one that seems blurry—the numbers are hard to make out."
    
    n "Simple addition problems. Under normal circumstances, these would be easy, but with Crusher in my group and my emotions already running high, nothing feels simple today."
    
    # Return to group work
    hide t
    show f at left
    show d at right
    
    pov "Okay, let's tackle these one by one. The first one is 10 + 35. That's 45, right?"
    
    play music "audio/music/mischiefmusic.wav" loop fadein 1 fadeout 1 volume 0.2
    d "Wow, you can add. Want a gold star?"
    
    n "Crusher's sarcasm is already grating on my nerves, and we've barely started."
    
    # Player's choice on how to handle the first problem
    menu:
        "Try to keep things civil":
            $ group_approach = "civil"
            $ crusher_friendship += 1  # Friendship point for staying civil
            
            pov "Yes, it's 45. Let's move on to the next one: 57 + 28."
            
            n "I decide to focus on the task at hand rather than engaging with Crusher's attitude."
            
            f "Let's see... 7 + 8 is 15, so that's 5 with 1 carried over. And 5 + 2 + 1 is 8. So the answer is 85."
            
            d "At least one of you knows basic math."
            
            # Stress increases slightly
            if stress == "low":
                $ stress = "medium"
            
        "Call out Crusher's attitude":
            $ group_approach = "confront"
            
            pov "Do you have to be such a jerk about everything? We're just trying to get this done."
            
            n "I can't hold back my frustration any longer. Crusher's constant negativity is pushing me to my limit."
            
            d "Oh, did I hurt your feelings? Maybe if you paid attention in class instead of daydreaming, you wouldn't need my help."
            
            f "Guys, come on. We need to finish this worksheet. The second problem is 57 + 28, which is 85."
            
            # Stress increases significantly
            if stress == "low":
                $ stress = "medium"
            elif stress == "medium":
                $ stress = "high"
            
        "Let Bandit handle it":
            $ group_approach = "passive"
            
            n "I decide to let Bandit take the lead, hoping to minimize my interaction with Crusher."
            
            f "Ignore him, [povname]. Let's focus on the problems. The second one is 57 + 28, which gives us 85."
            
            d "Yeah, hide behind your friend. Typical."
            
            # Stress remains the same
    
    # Move to the third problem
    n "We move on to the third problem, but the numbers are strangely blurry. I squint, trying to make them out."
    
    f "What's the third problem? I can't quite read it."
    
    d "It's 63 + 29. Even I can see that."
    
    n "I'm not sure if Crusher is right, but I don't want to admit I can't see it clearly, Crusher would surely use this against me."
    
    # Player's choice on the third problem
    menu:
        "Trust Crusher's reading":
            $ third_problem = "trust"
            $ crusher_friendship += 1  # Friendship point for having faith in Crusher 
            
            pov "Okay, so 63 + 29... that's 92."
            
            f "Are you sure? Let me see..."
            
            n "Bandit leans over to look at the problem more closely."
            
            f "Actually, I think it's 68 + 24, which would be 92 anyway. So same answer, different problem."
            
            d "What? Let me see that."
            
            n "Crusher grabs the paper, frowning as he looks at the problem."
            
            play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2
            d "Huh, you're right. I misread it."
            
            n "For a moment, Crusher seems almost human. The admission that he made a mistake catches me off guard."
            
        "Admit you can't see it clearly":
            $ third_problem = "admit"
            $ crusher_friendship += 1  # Friendship point for honesty
            
            pov "I can't really make out the numbers. They look blurry to me."
            
            f "Let me take a look. It's 68 + 24."
            
            d "What? No, it's 63 + 29."
            
            f "Look closer, Crusher. It's definitely 68 + 24."
            
            n "Crusher leans in, squinting at the paper."
            
            play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2
            d "Huh. You're right. I guess I need glasses or something."
            
            n "There's a hint of vulnerability in Crusher's voice that I've never heard before."
            
            # If player chose to be honest about their own difficulty seeing, Crusher is slightly more open
            if crusher_friendship >= 2:
                d "I... uh... sometimes have trouble with small print too. It's annoying."
                
                n "It's a small admission, but coming from Crusher, it feels significant."
            
        "Guess an answer":
            $ third_problem = "guess"
            
            pov "It looks like... maybe 68 + 24? So that's 92."
            
            d "Wrong. It's 63 + 29, which is 92. At least you got the answer right by accident."
            
            f "Actually, Crusher, [povname] is right. It is 68 + 24. Look closer."
            
            n "Crusher scowls but leans in to check the problem again."
            
            d "Whatever. The answer's still 92."
            
            n "He's clearly annoyed at being wrong, but at least he's not taking it out on me directly."
    
    stop music
    play music "audio/music/mischiefmusic.wav" loop fadein 1 fadeout 1 volume 0.2
    # Transition to confrontation
    n "We've finished all three problems, but I still sense some tension in the air. Crusher occasionally glancing at me with barely concealed hostility."
    
    f "Well, that wasn't so bad. We got all the answers right."
    
    d "Yeah, no thanks to [povname]."
    
    n "The comment stings, especially since I did contribute to solving the problems."
    
    # Player's choice on how to respond to Crusher's comment
    menu:
        "Ignore the comment":
            $ response_to_insult = "ignore"
            
            n "I take a deep breath and decide not to engage. It's not worth it."
            
            f "Come on, Crusher. We all worked on this together."
            
            d "Whatever. Just make sure Ms. Johnson knows I did most of the work."
            
            # Stress level remains the same
            
        "Defend yourself calmly":
            $ response_to_insult = "defend"
            $ crusher_friendship += 1  # Friendship point for calm defense
            
            pov "I helped solve these problems too, Crusher. We all contributed."
            
            n "I keep my voice steady, trying not to let him see how much his comment bothered me."
            
            # If friendship is building, Crusher's response is less harsh
            if crusher_friendship >= 2:
                d "Fine, whatever. You did get that one answer right, I guess."
                
                n "It's not exactly high praise, but coming from Crusher, it's practically a compliment."
            else:
                d "Oh please. You were barely paying attention. If it weren't for me and Bandit, you'd still be staring at the first problem."
            
            f "Hey, that's not fair. [povname] did help."
            
            # Stress increases slightly
            if stress == "low":
                $ stress = "medium"
            
        "Snap back at Crusher":
            $ response_to_insult = "snap"
            
            pov "What is your problem? I've been trying to work with you this whole time, and you just keep being a jerk!"
            
            n "My voice comes out louder than I intended, and a few students from nearby groups turn to look."
            
            d "My problem? You're the one who can't even focus for five minutes without spacing out or complaining."
            
            # Stress increases significantly
            if stress == "low":
                $ stress = "medium"
            elif stress == "medium":
                $ stress = "high"
    
    # Crusher escalates the situation
    d "You know what? I'm sick of having to carry people like you. Some of us actually care about our grades."
    
    n "Crusher's voice gets louder, and I can feel the eyes of more classmates turning toward our group."
    
    d "First you can't focus in class, then you need special help, and now you can't even read a simple math problem. What's next? Are you going to ask Ms. Johnson to do your homework for you too?"
    
    # Bandit tries to intervene
    f "Crusher, that's enough. We're supposed to be working together."
    
    d "Stay out of this, Bandit. You're always defending [povname], but you know I'm right."
    
    # Critical decision point based on stress level
    if stress == "high":
        # High stress path - emotional outburst is more likely
        jump outburst_choice
    else:
        # Lower stress path - controlled response is more likely
        stop music
        jump controlled_choice

# *********************************************************************
# Outburst Choice Path
# *********************************************************************
label outburst_choice:
    n "My heart pounds like a drum. Heat rushes to my face as frustration bubbles inside me, ready to explode."
    
    n "Crusher's words echo in my head, mixing with all the other frustrations of the day—the note in my locker, the difficulty focusing, the embarrassment in class."
    
    n "Something inside me is about to snap."
    
    # Player's choice on how to handle the intense emotions
    menu:
        "Try a last-minute calming technique":
            $ final_response = "calm"
            
            stop music fadeout 2
            n "I close my eyes and take several deep breaths, trying to remember the techniques the counselor taught me."
            
            n "In for four counts, hold for seven, out for eight. I focus on the sensation of air filling and leaving my lungs."
            
            n "It's hard, but I manage to pull myself back from the edge."
            
            pov "I'm not going to let you get to me, Crusher. We finished the assignment. That's what matters."
            
            d "Whatever. Just stay out of my way next time."
            
            n "Crusher seems almost disappointed that I didn't take the bait. He turns away, muttering something under his breath."
            
            f "Good job keeping your cool, [povname]. He was really trying to get to you."
            
            # Jump to resolution
            jump controlled_resolution
            
        "Verbally lash out at Crusher":
            $ final_response = "verbal_outburst"
            
            pov "You know what, Crusher? I'm sick of you! You think you're so much better than everyone else, but you're just a bully who makes everyone miserable!"
            
            n "The words pour out of me in a torrent. My voice is shaking with anger, and I can feel tears threatening to form in my eyes."
            
            pov "You've been making fun of me all year, and I'm done with it! You're not smarter than me—you're just meaner!"
            
            n "The classroom has gone completely silent. Everyone is staring at our group now."
            
            d "Wow, looks like someone can't handle a little criticism. Maybe if you—"
            
            # Teacher intervenes
            hide f
            hide d
            show ts
            
            t "[povname]! Crusher! That's enough!"

            hide ts
            show t
            
            n "Ms. Johnson's sharp voice cuts through the tension. She's standing by our group now, her expression a mix of concern and disappointment."
            
            # Jump to teacher intervention
            jump teacher_intervention
            
        "Physically lash out (push or hit Crusher)":
            $ final_response = "physical_outburst"
            
            n "Something inside me snaps. Before I can think, I'm on my feet, my chair scraping loudly against the floor."
            
            n "I lunge forward and shove Crusher hard, sending him stumbling backward." 
            
            hide d
            show ds at right

            play sound "audio/music/punch.mp3" volume 0.2
            stop music
            d "What the—!" with hpunch
            
            n "Crusher regains his balance and steps toward me, his face contorted with anger."
            
            f "[povname], stop!"
            
            # Teacher intervenes immediately
            hide f
            hide ds
            show ts
            
            t "STOP THIS IMMEDIATELY!"
            
            n "Ms. Johnson's voice thunders through the classroom. She rushes over, positioning herself between Crusher and I."
            
            t "Both of you, to the principal's office. NOW."
            
            # Jump to serious consequences
            jump serious_consequences

# *********************************************************************
# Controlled Choice Path
# *********************************************************************
label controlled_choice:
    play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2
    n "I can feel my emotions rising, but I'm still in control. Crusher's words sting, but I have options for how to respond."
    
    # Player's choice on how to handle the situation
    menu:
        "Take a deep breath and stay calm":
            $ final_response = "deep_breath"
            $ crusher_friendship += 2  # Extra friendship points for emotional control
            
            n "I take a deep breath, counting to five in my head before responding."
            
            pov "Look, Crusher, I'm just trying to get through this assignment like everyone else. Can we please just finish without arguing?"
            
            n "My calm response seems to take some of the wind out of Crusher's sails."
            
            # If friendship is building, Crusher's response is noticeably different
            if crusher_friendship >= 3:
                d "Yeah... okay. Sorry, I guess I'm just stressed about the test on Friday."
                
                n "Did Crusher just... apologize? I'm so surprised I almost don't know how to respond."
                
                f "We're all a bit on edge. Let's just finish this up."
            else:
                d "Fine. Whatever. Let's just get this over with."
                
                f "Great idea. We're almost done anyway."
            
            # Jump to positive resolution
            jump controlled_resolution
            
        "Ask Bandit for help":
            $ final_response = "seek_help"
            
            n "I turn to Bandit, hoping he can help defuse the situation."
            
            pov "Bandit, can you help us finish up? I think we're all getting a bit frustrated."
            
            f "Sure thing. Let's just focus on getting these answers written up neatly so we can turn them in."
            
            n "Bandit takes the lead, organizing our answers on the worksheet. Crusher seems reluctant but follows along."
            
            d "Fine. But make sure you write down that I solved the third problem."
            
            f "We'll note that we all contributed, Crusher."
            
            # Jump to positive resolution
            jump controlled_resolution
            
        "Quietly alert Ms. Johnson":
            $ final_response = "get_teacher"
            
            n "I raise my hand, hoping to get Ms. Johnson's attention without making a scene."
            
            # Teacher approaches
            hide f
            hide d
            show t
            
            t "Yes, [povname]? Do you have a question about the assignment?"
            
            pov "Ms. Johnson, we're having some trouble working together in our group."
            
            t "I see. Let me check in with your group."
            
            # Teacher addresses the group
            hide t
            show t at center
            show f at left
            show d at right
            
            t "How is everyone doing over here? Are you making progress on the problems?"
            
            f "We've solved all three problems, Ms. Johnson. We just need to write up our answers."
            
            t "Excellent. And is everyone contributing to the group effort?"
            
            n "Ms. Johnson's pointed question hangs in the air. Crusher shifts uncomfortably in his seat."
            
            d "Yes, Ms. Johnson. We're all working together."
            
            t "Good. I'll be checking in again shortly. Remember, collaboration is part of your grade for this assignment."
            
            # Teacher leaves
            hide t
            
            play music "audio/music/mischief.wav" loop fadein 1 fadeout 1 volume 0.2
            n "As Ms. Johnson walks away, Crusher gives me a look that could curdle milk."
            
            d "Teacher's pet."
            
            n "He mutters the insult, but doesn't say anything else for the rest of the activity."
            
            stop music
            play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2
            # Jump to teacher-assisted resolution
            jump teacher_resolution

# *********************************************************************
# Resolution Paths
# *********************************************************************
label controlled_resolution:
    play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2
    # Positive outcome from controlled emotions
    n "We manage to finish the assignment without further incident. It's not exactly friendly, but at least we're not at each other's throats."
    
    n "As we're wrapping up, Bandit leans over to me."
    
    f "Hey, good job keeping your cool. Crusher can be a lot to handle."
    
    n "I nod, feeling a small sense of accomplishment. It wasn't easy, but I managed to get through the situation without losing control."
    
    # Teacher collects the worksheets
    hide f
    hide d
    show t
    
    t "Time's up! Please pass your worksheets forward."
    
    n "As we hand in our work, Ms. Johnson gives our group an approving nod."
    
    t "I'm glad to see you all working together effectively."
    
    # Class ends
    n "The bell rings, signaling the end of class. As I gather my things, I feel a sense of relief that the group work is over."
    
    hide t

    n "I managed to keep my emotions in check, even when Crusher was trying his best to provoke me. That's a small victory."
    
    show f
    # Bandit offers encouragement
    f "Hey, want to grab lunch together? I think you deserve a break after dealing with Crusher."
    
    hide f
    show fs

    n "I smile, grateful for Bandit's friendship. Sometimes having just one ally can make all the difference."
    
    # Reflection on the experience
    scene bg cafeteria
    
    "*Looking back on what happened in class today:*"
    
    # Player reflects on their actions
    $ action_reflection = renpy.input("What actions did you take that affected how things turned out?")
    
    # Player reflects on the results
    $ result_reflection = renpy.input("What happened as a result of your choices?")
    
    # Player reflects on their feelings
    $ feeling_reflection = renpy.input("How do you feel about the outcome?")
    
    # Player reflects on external factors
    $ external_reflection = renpy.input("What factors outside your control influenced the situation?")
    
    # Bandit provides feedback
    show f
    
    f "You handled that really well, [povname]. Crusher can be difficult to work with, but you didn't let him get to you."
    
    n "Bandit's words make you feel proud of how you managed the situation."
    
    f "It's not easy to stay calm when someone's pushing your buttons like that. I think you showed a lot of maturity."
    
    n "As you reflect on the experience, you realize that controlling your emotions doesn't mean ignoring them—it means acknowledging them and choosing how to respond."
    
    # Check if the player has built enough friendship with Crusher
    if crusher_friendship >= 4:
        stop music
        jump unexpected_encounter
    else:
        stop music
        jump disruptive_scene

# *********************************************************************
# Unexpected Encounter - Secret Crusher Friendship Path
# *********************************************************************
label unexpected_encounter:
    scene cafe
    
    n "A few days after the incident in Ms. Johnson's class, you're sitting alone in the school cafeteria, picking at your lunch."
    
    n "The events from the past week have left you feeling drained. Between the note in your locker and the tension with Crusher, school has been more stressful than usual."
    
    play music "audio/music/mischiefmusic.wav" loop fadein 1 fadeout 1 volume 0.2
    n "You're lost in thought when a shadow falls across your table."
    
    show d
    
    n "You look up to find Crusher standing there, lunch tray in hand, looking uncharacteristically uncertain."
    
    d "Hey... mind if I sit here? Everywhere else is full."
    
    n "You glance around the cafeteria. There are definitely other seats available, which makes his request all the more puzzling."
    
    # Player choice to accept or reject
    menu:
        "Sure, go ahead":
            jump crusher_conversation
        "I'd rather eat alone":
            jump crusher_rejected

# Crusher conversation path
label crusher_conversation:
    pov "Yeah, sure."
    
    n "Crusher sets his tray down and sits across from you. For a moment, neither of you speaks. The silence is awkward but not entirely hostile."
    
    d "So... that math test is coming up tomorrow."
    
    pov "Yeah, I've been studying for it."
    
    d "Ms. Johnson's tests are always hard."
    
    n "Another silence falls. Crusher seems to be struggling with something."
    
    d "Look, about what happened in class the other day..."
    
    n "He pauses, pushing his food around with his fork."
    
    play music "audio/music/afternoontea.wav" loop fadein 1 fadeout 1 volume 0.2
    d "I was being a jerk. I get like that sometimes when... when I'm stressed about stuff."
    
    n "You're so surprised by this admission that you're not sure how to respond."
    
    d "My dad's always on my case about grades. Says if I don't get straight As, I can forget about basketball."
    
    pov "That sounds like a lot of pressure."
    
    d "Yeah, well... whatever. It's not an excuse."
    
    n "Crusher looks up from his tray, meeting your eyes directly for perhaps the first time."
    
    d "Anyway, I just wanted to say... you know... sorry or whatever."
    
    # Player response to Crusher's apology
    menu:
        "I appreciate that, Crusher":
            pov "I appreciate that, Crusher. It takes guts to apologize."
            
            n "A hint of a smile crosses his face."
            
            d "Yeah, well, don't go telling everyone. I've got a reputation to maintain."
            
            n "There's no real heat behind his words though."
            
            d "You're actually pretty cool when you're not being all... you know."
            
            pov "When I'm not being all what?"
            
            d "I don't know. Just... whatever."
            
            n "You both laugh, the tension between you dissolving."
            
            d "Hey, you want to study for that math test together? I could use some help with those equation things."
            
            pov "Sure, why not?"
            
            n "As you begin to discuss the upcoming test, you realize that beneath Crusher's tough exterior is just another kid trying to figure things out, just like you."
            
            n "Sometimes people surprise you. And sometimes, the most unexpected friendships can form when you're willing to look past first impressions."
            
        "Why are you really here, Crusher?":
            pov "Why are you really here, Crusher? You've never wanted to talk to me before."
            
            n "Crusher shifts uncomfortably in his seat."
            
            d "I told you. I just wanted to say sorry."
            
            n "He hesitates, then continues."
            
            d "And maybe... I don't know. You handled that whole thing pretty well. Most people either freak out at me or just take it."
            
            d "You stood your ground but didn't lose it. That was... different."
            
            pov "I'm trying to work on controlling my reactions."
            
            d "Yeah, well, it's a good skill to have. I should probably work on that too."
            
            n "There's a moment of understanding between you."
            
            d "Anyway, I should probably go. But... maybe see you around?"
            
            pov "Yeah, see you around, Crusher."
            
            n "As he walks away, you realize that people are more complex than they first appear. Even someone like Crusher has depths you hadn't seen before."
            
            n "It's a small moment, but somehow it feels significant—like the beginning of something new."
    
    # End of unexpected encounter
    scene bg classroom
    
    show ms
    
    e "Sometimes the most meaningful connections come from the most unexpected places."
    
    e "By showing emotional control and empathy, you were able to see a different side of Crusher—and perhaps help him see a different side of himself."
    
    hide ms
    
    stop music
    jump disruptive_scene

# Crusher rejected path
label crusher_rejected:
    pov "I'd rather eat alone today, if you don't mind."
    
    n "Crusher's expression hardens slightly, but he nods."
    
    d "Yeah, whatever. No big deal."
    
    n "He turns to leave, then pauses."
    
    d "For what it's worth... you handled yourself pretty well in Johnson's class. Not many people stand up to me like that."
    
    n "Before you can respond, he's walking away, disappearing into the crowd of students."
    
    n "You're left wondering what might have happened if you'd made a different choice."
    
    # End of unexpected encounter rejection
    scene bg classroom
    
    show ms
    
    e "Sometimes opportunities for connection come in unexpected ways. Not every choice leads to the same outcome."
    
    hide ms
    
    stop music
    jump disruptive_scene

# *********************************************************************
# Teacher Resolution Path
# *********************************************************************
label teacher_resolution:
    # Teacher-assisted resolution
    n "With Ms. Johnson's intervention, the rest of the group work goes smoothly. Crusher keeps his comments to himself, though I can feel his resentment."
    
    n "Bandit takes the lead in organizing our answers, and I contribute where I can. Even Crusher reluctantly participates."
    
    # Teacher returns to check on the group
    show t
    
    t "How are things going over here?"
    
    f "We're just finishing up, Ms. Johnson. We've got all the answers worked out."
    
    t "Excellent. I'm glad to see you working together."
    
    # Class ends
    n "The bell rings, signaling the end of class. As we pack up our things, Ms. Johnson calls Crusher over to her desk."
    
    hide t
    hide d
    hide f
    show f
    
    n "I catch Bandit's eye, and he gives me an encouraging smile."
    
    f "Hey, don't let Crusher get to you. He's like that with everyone."
    
    n "I nod, grateful for Bandit's support. As I leave the classroom, I feel a mix of emotions—frustration at Crusher's behavior, but also pride that I didn't let him push me over the edge."
    
    n "Sometimes, asking for help is the strongest thing you can do."
    
    # Reflection on the experience
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
    
    # Teacher provides feedback
    show t
    
    t "I noticed how you handled that difficult situation with Crusher today. Asking for help was a mature decision."
    
    n "Ms. Johnson's words make you feel validated in your choice to seek assistance rather than trying to handle everything alone."
    
    t "Learning to recognize when you need support is an important skill. It shows self-awareness and good judgment."
    
    n "As you reflect on the experience, you realize that there's strength in knowing when to reach out to others, especially authority figures who can help mediate difficult situations."
    
    # Check if the player has built enough friendship with Crusher
    if crusher_friendship >= 4:
        jump unexpected_encounter
    else:
        stop music
        jump disruptive_scene

# *********************************************************************
# Teacher Intervention Path
# *********************************************************************
label teacher_intervention:
    # Teacher intervenes after verbal outburst
    n "Ms. Johnson's stern voice silences the entire classroom. I'm still shaking with anger, but her presence brings me back to reality."
    
    t "I want both of you to take a moment to calm down. This kind of behavior is unacceptable in my classroom."
    
    show t at left
    show ds at right

    # Crusher tries to defend himself
    d "But Ms. Johnson, [povname] started it by—"
    
    t "I'm not interested in who started it, Crusher. I'm interested in ending it. Now."
    
    # Teacher addresses the class
    n "Ms. Johnson turns to address the whole class, who have all stopped working to watch the drama unfold."
    
    t "Everyone, please continue with your assignments. You have ten more minutes."
    
    # Teacher turns back to player and Crusher
    t "As for you two, I'd like to speak with both of you after class."
    
    # Crusher's reaction
    d "But I have basketball practice—"
    
    t "This won't take long, but it is necessary."
    
    hide t
    show f at left
    # Class continues
    n "Ms. Johnson returns to her desk, and slowly the classroom returns to its normal buzz of activity. Crusher glares at me but says nothing more."
    
    # Bandit tries to help
    f "Let's just finish the worksheet, okay? We're almost done."
    
    n "I nod, still feeling the aftereffects of my emotional outburst. My heart is racing, and my face feels hot."
    
    # Class ends
    n "The rest of the class passes in tense silence between Crusher and me. When the bell rings, the other students file out while we remain seated."
    
    # Teacher's discussion
    hide f
    hide d
    show t at left
    
    t "I want to talk to both of you about what happened today. This kind of confrontation isn't productive for anyone."
    
    # Teacher addresses player
    t "[povname], I understand that Crusher's comments were out of pocket, but responding with an outburst only escalates the situation."
    
    # Teacher addresses Crusher
    t "And Crusher, your behavior toward [povname] has been consistently disrespectful. That needs to stop."
    
    # Teacher's suggestion
    t "I'm going to ask both of you to attend a conflict resolution session with the school counselor. This isn't a punishment—it's an opportunity to learn how to communicate more effectively."
    
    # Player's reflection
    n "I feel a mix of emotions—embarrassment at losing my cool, but also a sense of validation that Ms. Johnson recognized Crusher's behavior as part of the problem."
    
    scene bg hallway9

    # End of scene
    n "As I leave the classroom, I realize quicker than ever that I didn't handle the situation perfectly. But at least I'd be able to explain my side of the story."

    scene bg office
    with fade

    "*Okay both of you, lets go over what happened in class today:*"
    
    # Player reflects on their actions
    $ action_reflection = renpy.input("What actions did you take that affected how things turned out?")
    
    # Player reflects on the results
    $ result_reflection = renpy.input("What happened as a result of your choices?")
    
    # Player reflects on their feelings
    $ feeling_reflection = renpy.input("How do you feel about the outcome?")
    
    # Player reflects on external factors
    $ external_reflection = renpy.input("What factors outside your control influenced the situation?")
    
    # Counselor provides feedback
    "Counselor" "Thank you both for your honesty. It's important to recognize how our actions affect others and to find better ways to communicate."
    
    # Crusher's response
    d "I still think [povname] overreacted. I was just trying to get the work done."
    
    "Counselor" "Crusher, remember that your words have impact too. What might seem like a joke to you can feel like an attack to someone else."
    
    # Counselor addresses both students
    "Counselor" "Both of you need to work on communicating more respectfully. [povname], I'd like you to practice those calming techniques we've discussed when you feel overwhelmed. And Crusher, I'd like you to think about how your comments might be received before you speak."
    
    n "As you leave the counselor's office, you realize that managing your emotions is a skill that takes practice. Today was difficult, but it was also a learning opportunity."
    
    stop music
    jump disruptive_scene

# *********************************************************************
# Serious Consequences Path
# *********************************************************************
label serious_consequences:
    # Aftermath of physical confrontation
    n "The classroom is completely silent. I can feel everyone's eyes on me, and the reality of what I just did hits me like a bucket of cold water."
    
    hide ts
    show t

    # Teacher's immediate response
    t "Everyone else, continue with your work. Crusher and [povname], come with me right now."
    
    scene bg hallway9
    show t at left
    show ds at right

    # Walking to the principal's office
    n "Ms. Johnson leads us out of the classroom and down the hallway toward the principal's office. No one speaks. My heart is pounding, and my hands are shaking."
    
    n "I've never been sent to the principal before. What was I thinking? I wasn't thinking—that's the problem."

    # Crusher breaks the silence
    d "This is ridiculous. [povname] attacked me! I didn't even do anything."
    
    t "We'll discuss exactly what happened when we get to the Principals office, Crusher."
    
    # Arriving at the principal's office
    scene bg office
    with fade
    
    play music "audio/music/afternoontea.wav" loop fadein 1 fadeout 1 volume 0.2
    n "The next thirty minutes are a blur of explanations, accusations, and stern lectures about appropriate behavior and the school's zero-tolerance policy for physical aggression."
    
    # Show Crusher and the principal for the reflection
    show d at right
    
    "*Okay both of you, lets go over what happened in class today:*"
    
    # Player reflects on their actions
    $ action_reflection = renpy.input("What actions did you take that affected how things turned out?")
    
    # Player reflects on the results
    $ result_reflection = renpy.input("What happened as a result of your choices?")
    
    # Player reflects on their feelings
    $ feeling_reflection = renpy.input("How do you feel about the outcome?")
    
    # Player reflects on external factors
    $ external_reflection = renpy.input("What factors outside your control influenced the situation?")
    
    # Principal addresses both students
    "Principal" "I hope both of you understand the seriousness of physical confrontation in our school. This kind of behavior affects not just you, but disrupts the learning environment for everyone."
    
    # Crusher's response
    d "It wasn't my fault! [povname] attacked me first!"
    
    "Principal" "Crusher, we've discussed your role in provoking this situation. Both of you need to find better ways to resolve conflicts."
    
    # End of scene with reflection on consequences
    "Principal" "Actions have consequences. [povname], you'll be serving a suspension. Crusher, you'll have detention for your role in this incident."
    
    n "As you leave the principal's office, you realize how quickly things escalated from a simple classroom interaction to serious school discipline."
    
    stop music
    jump disruptive_scene
