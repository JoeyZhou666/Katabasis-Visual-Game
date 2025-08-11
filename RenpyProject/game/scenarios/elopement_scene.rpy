# *********************************************************************
# Elopement Scenario
# 
# This scene focuses on the consequences of skipping class (elopement),
# helping students with emotional and behavioral disorders understand
# the importance of attending class and proper communication when feeling overwhelmed.
# *********************************************************************

# Variables for tracking player choices in elopement_scene
default visited_library = False          # Whether player has visited the library
default visited_school_grounds = False   # Whether player has visited the school grounds
default helped_mousy = False             # Whether player helped Mousy in the restroom
default memory_game_completed = False    # Whether player completed the memory card game
default racing_game_completed = False    # Whether player completed the racing game
default reaction_game_completed = False  # Whether player completed the reaction time game

label elopement_scene:
    # Start in the hallway
    scene hallway3
    
    play music "audio/music/hsdream.wav" loop fadein 1 fadeout 1 volume 0.2

    # Player's inner thoughts
    n "I walk past the classroom I'm supposed to be in. Ms. Johnson's voice fades as I continue down the hallway."
    
    n "I've been feeling so overwhelmed lately. Maybe I just need some time to myself."
    
    n "As I reach the end of the hallway, I pause. Should I really be doing this? Maybe I should go back to class..."
    
    # Player's choice to continue skipping or return to class
    menu:
        "Return to class":
            n "I take a deep breath and turn around. As much as I want to skip, I know it'll only cause more problems."
            
            n "I head back to the classroom, hoping Ms. Johnson won't be too upset about my brief absence."
            
            # Randomly select between disruptive_scene and emotional_outburst_scene
            $ random_scenario = renpy.random.choice(["disruptive", "emotional"])
            
            if random_scenario == "disruptive":
                jump disruptive_scene
            else:
                jump emotional_outburst_scene
                
        "Continue skipping class":
            n "I've already come this far. Might as well see it through."
            
            n "I continue down the hallway, my heart racing a little. I've never skipped class before."
            
            n "I should probably stop by the restroom first. It's usually empty during class time."
            
            jump elopement_restroom

# *********************************************************************
# Restroom Scene
# *********************************************************************
label elopement_restroom:
    # Set the bathroom scene
    scene image "images/bathroom.png"
    
    n "I push open the door to the restroom, expecting it to be empty."
    
    n "But as I step inside, I hear voices. Someone's arguing."
    
    # Show Mousy and Crusher
    show msad at left
    show d at right
    
    n "I freeze. It's Mousy and Crusher. I duck behind the door, peering through the crack."
    
    d "You think you're so smart, don't you? Always answering questions in class."
    
    e "P-please leave me alone, Crusher. I don't want any trouble."
    
    d "Too bad. You've been trouble since you got here with your stupid squeaky voice and perfect grades."
    
    n "I watch as Crusher towers over Mousy, who's backed against the wall, looking terrified."
    
    d "I bet you're the one who told Ms. Johnson I was cheating on that test!"
    
    e "I-I didn't! I swear!"
    
    # Crusher hits Mousy
    play sound "audio/music/punch.mp3" volume 0.2
    hide d
    show ds at right
    
    e "Ow!" with hpunch
    
    n "Crusher shoves Mousy hard against the wall. Mousy looks like they might cry."
    
    # Player's choice on how to respond
    menu:
        "Tell the administrator about the fight":
            $ helped_mousy = True
            
            n "I can't just stand by and watch this. I need to get help."
            
            n "I quietly back away from the door and hurry down the hallway to find the administrator."
            
            scene image "images/hallwayintermission.png"
            
            n "I spot the administrator, Donkey, at the end of the hallway."
            
            show ac
            
            n "Excuse me! There's a fight in the bathroom. Crusher is bullying Mousy!"
            
            hide ac
            show ashock
            
            a "What? Show me immediately!"
            
            n "I lead the administrator back to the bathroom."
            
            scene image "images/bathroom.png"
            show msad at left
            show ds at right
            show ashock at center
            
            a "What is going on in here?"
            
            n "Crusher immediately steps away from Mousy, looking caught."
            
            a "Both of you, come with me right now."
            
            hide msad
            hide ds
            
            n "The administrator leads Mousy and Crusher away. Before leaving, he turns to me."
            
            a "Thank you for alerting me. But shouldn't you be in class right now?"
            
            n "I... um... was just using the restroom."
            
            a "Make sure you get back to class promptly."
            
            n "I nod, feeling a mix of relief for helping Mousy and anxiety about almost getting caught skipping."
            
            hide ashock
            
            n "Once the administrator is gone, I slip out of the bathroom and continue with my plan."
            
        "Walk away":
            n "This isn't my fight. If I get involved, I might get caught skipping class."
            
            n "I quietly back away from the door and continue down the hallway, Mousy's frightened face still in my mind."
            
            n "I feel guilty for not helping, but what could I really do against Crusher?"
    
    # Player chooses where to go next
    n "I need to find somewhere to hang out until the next period. Where should I go?"
    
    menu:
        "Go to the library":
            jump elopement_library
        "Go to the school grounds":
            jump elopement_school_grounds

# *********************************************************************
# Library Scene
# *********************************************************************
label elopement_library:
    # Set the library scene
    scene image "images/library.png"
    
    $ visited_library = True
    
    n "I slip into the library, relieved to find it mostly empty. The librarian is busy at her desk, and a few students with free periods are scattered around."
    
    n "I've never been much of a reader. Why did I even come here?"
    
    n "I wander between the shelves, pretending to browse. Most of the books are academic and boring."
    
    n "Just as I'm about to leave, I spot a row of computers in the corner."
    
    n "Perfect! I can kill some time online."
    
    n "I sit down at one of the computers and check to make sure no one's watching me."
    
    n "The computer is unlocked and ready to use. I wonder if I can find any games to play..."
    
    n "After a quick search, I find a memory card matching game. That should help pass the time."
    
    # Memory card game
    n "The game loads up, showing a grid of cards. They're face down, but when I flip them, I see they have pictures of people from school!"
    
    # Call the memory card game
    $ memory_game_completed = True
    $ mousy_card_seen = False  # Reset the flag for Mousy card
    call start_memory_game
    
    n "I finish the matching game with ease. It was actually pretty fun seeing the familiar faces on the cards."
    
    n "When I flipped over a card with Mousy's face, I couldn't help but think about what I saw in the bathroom."
    
    n "I should probably get moving before someone asks why I'm not in class."
    
    # Check if player has visited both locations
    if visited_school_grounds:
        n "I've explored both the library and the school grounds now. Where should I go next?"
        
        menu:
            "Go to the auditorium":
                jump elopement_auditorium
            "Go to the computer lab":
                jump elopement_computer_lab
    else:
        # Player hasn't visited school grounds yet, so they encounter the administrator
        jump elopement_intermission

# *********************************************************************
# School Grounds Scene
# *********************************************************************
label elopement_school_grounds:
    # Set the school grounds scene
    scene image "images/schoolgrounds.png"
    
    $ visited_school_grounds = True
    
    n "I push open the side door and step outside onto the school grounds. The fresh air feels good after being cooped up inside."
    
    n "There's a gym class happening on the track and field. Students are playing basketball, soccer, and some are even racing."
    
    # Change background to track and field
    scene image "images/trackandfield.png"
    
    n "I walk around the track, trying to look like I belong here. Maybe if anyone asks, I can say I'm running an errand for a teacher."
    
    n "Suddenly, two kids appear in front of me, blocking my path."
    
    "Kid 1" "Hey, you! Want to race with us? We need one more person!"
    
    "Kid 2" "Yeah, come on! It'll be fun!"
    
    n "I hesitate. I don't want to draw attention to myself, but they seem really eager."
    
    "Kid 1" "Please? We've been practicing all week and need someone new to race against."
    
    n "They're not giving me much choice. And I guess it could be fun..."
    
    menu:
        "Agree to the race":
            n "Alright, I'll race with you guys."
            
            "Kid 1" "Awesome! How good are you at running? We can take it easy on you if you want."
            
            # Player chooses difficulty
            menu:
                "I'm not very fast (Easy)":
                    $ race_difficulty = "easy"
                    "Kid 2" "No problem! We'll keep it casual."
                    
                "I'm pretty average (Medium)":
                    $ race_difficulty = "medium"
                    "Kid 2" "Cool, we'll give you a fair challenge!"
                    
                "I'm really fast (Hard)":
                    $ race_difficulty = "hard"
                    "Kid 1" "Oh yeah? We'll see about that! Get ready for a real race!"
            
            n "We line up at the starting line. The kids explain that we need to alternate pressing the left and right arrow keys to run."
            
            n "I take a deep breath. Ready, set..."
            
            # Hide window before calling the racing game
            window hide
            
            # Call the character racing game
            $ racing_game_completed = True
            call start_racing_game
            
            # Restore the scene to trackandfield
            scene image "images/trackandfield.png"
            
            # Ensure window is properly shown before continuing with dialogue
            $ renpy.game.interface.suppress_dialogue = False
            $ renpy.game.interface.force_noninteractive = False
            $ _window_auto = True
            window auto
            
            n "After the race, I'm breathing hard but feeling good. That was actually pretty fun."
            
            "Kid 1" "That was awesome! Thanks for racing with us!"
            
            "Kid 2" "Yeah, we should do this again sometime!"
            
            n "I smile and nod, but I know I should get moving. I've been outside too long."
            
            n "All that running has made me tired. I should head back inside and find somewhere to rest."
    
    # Check if player has visited both locations
    if visited_library:
        n "I've explored both the library and the school grounds now. Where should I go next?"
        
        menu:
            "Go to the auditorium":
                jump elopement_auditorium
            "Go to the computer lab":
                jump elopement_computer_lab
    else:
        # Player hasn't visited library yet, so they encounter the administrator
        jump elopement_intermission

# *********************************************************************
# Intermission Scene
# *********************************************************************
label elopement_intermission:
    # Set the hallway intermission scene
    scene image "images/hallwayintermission.png"
    
    n "I walk through the hallway, trying to decide where to go next."
    
    n "Suddenly, I hear the sound of keys jingling. Clink, clink, clink."
    
    n "Someone's coming!"
    
    # Show administrator
    show ac
    
    n "It's the administrator, Donkey. He hasn't seen me yet."
    
    n "I freeze, hoping he'll pass by without noticing me."
    
    # Administrator notices player
    hide ac
    show ashock
    
    play sound "audio/vibration.mp3"
    
    a "Hey! Stop there!" with hpunch
    
    a "Aren't you supposed to be in class?"
    
    n "My heart races. I've been caught!"
    
    n "Without thinking, I turn and run in the opposite direction."
    
    hide ashock
    
    n "I can hear the administrator calling after me, but I don't stop."
    
    n "I need to find somewhere to hide, and fast!"
    
    # Player runs to the location they haven't visited yet
    if visited_library:
        n "I dash toward the school grounds. Maybe I can lose him outside."
        
        $ visited_school_grounds = True
        jump elopement_school_grounds
    else:
        n "I dash toward the library. Maybe I can hide among the bookshelves."
        
        $ visited_library = True
        jump elopement_library

# *********************************************************************
# Auditorium Scene
# *********************************************************************
label elopement_auditorium:
    # Set the auditorium scene
    scene image "images/auditorium.png"
    
    n "I slip into the auditorium, closing the door quietly behind me."
    
    n "Whoa... I've never been in here before. It's huge!"
    
    n "The stage stretches out before me, and I can imagine what it must be like when it's filled with people during assemblies and performances."
    
    n "I walk down the center aisle, my footsteps echoing in the empty space."
    
    n "As I approach the front, I can't help but stare at the stage. It's so tempting..."
    
    # Player's choice to get on stage
    menu:
        "Get on the stage":
            n "I can't resist. I climb the steps at the side of the stage and walk out to the center."
            
            n "Standing here feels different. I can see the entire auditorium from this perspective."
            
            n "There's a microphone stand in the center of the stage. I approach it cautiously."
            
            n "I've always wondered what it would be like to perform on a stage like this."
            
            # Player's choice to sing
            menu:
                "Sing into the microphone":
                    # Player taps the mic
                    play sound "audio/mictest.mp3"
                    
                    n "I tap the microphone gently, and a loud thump echoes through the auditorium."
                    
                    n "Taking a deep breath, I lean in and let out my best singing voice."
                    
                    pov "AaaaaaaaaaAAAAAAHHHHH!"
                    
                    n "My voice echoes dramatically through the empty auditorium. For a moment, I feel like a real performer."
                    
                    # Administrator bursts in
                    a "THERE YOU ARE!"
                    
                    n "My heart drops. The administrator has found me!"
                    
                    n "I look around frantically for an escape route."
                    
                    n "There! Behind the stage curtains, I can see a door marked 'EXIT'."
                    
                    n "I dash behind the curtain, through the backstage area, and push through the exit door."
                        
                    # Player escapes outside
                    scene image "images/outsideschool.png"
                    
                    n "I find myself outside, at the side of the school building."
                    
                    n "Breathing hard, I jog around to the front of the school and spot a bench."
                    
                    n "I sit down, trying to catch my breath. That was close!"
                    
                    n "Maybe I'm finally safe..."
                    
                    # Administrator catches up
                    a "Did you really think you could outrun me?"
                    
                    n "I look up to see the administrator standing in front of me, not even out of breath."
                    
                    a "I know this school better than anyone. Including all the shortcuts."
                    
                    n "My shoulders slump. There's no escape now."
                    
                    a "Skipping class, disrupting school property, running from staff... You've had quite the day, haven't you?"
                    
                    # Transition to reflection
                    jump elopement_auditorium_reflection
        
        "Resist the urge":
            n "I should probably not draw attention to myself by getting on stage."
            
            n "But the stage looks so cool... Maybe just for a minute?"
            
            # Loop back to the same choice
            menu:
                "Get on the stage":
                    n "I can't resist. I climb the steps at the side of the stage and walk out to the center."
                    
                    n "Standing here feels different. I can see the entire auditorium from this perspective."
                    
                    n "There's a microphone stand in the center of the stage. I approach it cautiously."
                    
                    n "I've always wondered what it would be like to perform on a stage like this."
                    
                    # Player's choice to sing
                    menu:
                        "Sing into the microphone":
                            # Player taps the mic
                            play sound "audio/mictest.mp3"
                            
                            n "I tap the microphone gently, and a loud thump echoes through the auditorium."
                            
                            n "Taking a deep breath, I lean in and let out my best singing voice."
                            
                            pov "AaaaaaaaaaAAAAAAHHHHH!"
                            
                            n "My voice echoes dramatically through the empty auditorium. For a moment, I feel like a real performer."
                            
                            # Administrator bursts in
                            a "THERE YOU ARE!"
                            
                            n "My heart drops. The administrator has found me!"
                            
                            n "I look around frantically for an escape route."
                            
                            n "There! Behind the stage curtains, I can see a door marked 'EXIT'."
                            
                            n "I dash behind the curtain, through the backstage area, and push through the exit door."
                            
                            # Player escapes outside
                            scene image "images/outsideschool.png"
                            
                            n "I find myself outside, at the side of the school building."
                            
                            n "Breathing hard, I jog around to the front of the school and spot a bench."
                            
                            n "I sit down, trying to catch my breath. That was close!"
                            
                            n "Maybe I'm finally safe..."
                            
                            # Administrator catches up
                            a "Did you really think you could outrun me?"
                            
                            n "I look up to see the administrator standing in front of me, not even out of breath."
                            
                            a "I know this school better than anyone. Including all the shortcuts."
                            
                            n "My shoulders slump. There's no escape now."
                            
                            a "Skipping class, disrupting school property, running from staff... You've had quite the day, haven't you?"
                            
                            # Transition to reflection
                            jump elopement_auditorium_reflection
                
                "Resist the urge":
                    n "I really shouldn't... but the stage is calling to me!"
                    
                    n "It looks so cool up there. Maybe just for a quick moment?"
                    
                    # Third time's the charm - force the player to get on stage
                    menu:
                        "Get on the stage":
                            n "I can't resist any longer. I climb the steps at the side of the stage and walk out to the center."
                            
                            n "Standing here feels different. I can see the entire auditorium from this perspective."
                            
                            n "There's a microphone stand in the center of the stage. I approach it cautiously."
                            
                            n "I've always wondered what it would be like to perform on a stage like this."
                            
                            # Player's choice to sing
                            menu:
                                "Sing into the microphone":
                                    # Player taps the mic
                                    play sound "audio/mictest.mp3"
                                    
                                    n "I tap the microphone gently, and a loud thump echoes through the auditorium."
                                    
                                    n "Taking a deep breath, I lean in and let out my best singing voice."
                                    
                                    pov "AaaaaaaaaaAAAAAAHHHHH!"
                                    
                                    n "My voice echoes dramatically through the empty auditorium. For a moment, I feel like a real performer."
                                    
                                    # Administrator bursts in
                                    a "THERE YOU ARE!"
                                    
                                    n "My heart drops. The administrator has found me!"
                                    
                                    n "I look around frantically for an escape route."
                                    
                                    n "There! Behind the stage curtains, I can see a door marked 'EXIT'."
                                    
                                    n "I dash behind the curtain, through the backstage area, and push through the exit door."
                                    
                                    # Player escapes outside
                                    scene image "images/outsideschool.png"
                                    
                                    n "I find myself outside, at the side of the school building."
                                    
                                    n "Breathing hard, I jog around to the front of the school and spot a bench."
                                    
                                    n "I sit down, trying to catch my breath. That was close!"
                                    
                                    n "Maybe I'm finally safe..."
                                    
                                    # Administrator catches up
                                    a "Did you really think you could outrun me?"
                                    
                                    n "I look up to see the administrator standing in front of me, not even out of breath."
                                    
                                    a "I know this school better than anyone. Including all the shortcuts."
                                    
                                    n "My shoulders slump. There's no escape now."
                                    
                                    a "Skipping class, disrupting school property, running from staff... You've had quite the day, haven't you?"
                                    
                                    # Transition to reflection
                                    jump elopement_auditorium_reflection

# *********************************************************************
# Computer Lab Scene
# *********************************************************************
label elopement_computer_lab:
    # Set the computer lab scene
    scene image "images/computerlab.png"
    
    n "I slip into the computer lab, relieved to find it mostly empty during class time."
    
    n "The room is filled with rows of computers. My eyes light up at the possibilities of games I could play."
    
    n "As I look around for a place to sit, I notice a familiar face in the corner."
    
    # Show Bandit
    show f
    
    n "It's Bandit! What's he doing here?"
    
    f "Hey, [povname]! What brings you to the computer lab?"
    
    n "Bandit seems excited to see me, not questioning why I'm not in class."
    
    pov "Just... taking a break. What about you?"
    
    f "I'm supposed to be studying for an exam, but I found this awesome game online!"
    
    hide f
    show fs
    
    f "It's a reaction game where you have to click buttons as fast as you can when they light up. My high score is 10!"
    
    f "Want to try it? I bet you can't beat my score!"
    
    pov "What's your high score again?"
    
    f "10! I've been trying to get to 11 all morning."
    
    # Player's choice to play the game
    menu:
        "Play the reaction game":
            n "I sit down at the computer next to Bandit. The game looks simple enough."
            
            f "Just click the buttons as fast as you can when they light up. The more you click, the higher your score!"
            
            n "I crack my knuckles dramatically, making Bandit laugh."
            
            pov "Let me show you how it's done."
            
            # Hide window before calling the reaction game
            window hide
            
            # Call the reaction game
            $ reaction_game_completed = True
            call start_reaction_game
            
            # The game will return to elopement_reaction_game_complete after completion

# This label is called when the reaction game ends
label elopement_reaction_game_complete:
            # Restore the scene to computer lab
            scene image "images/computerlab.png"
            show fs
            
            # Ensure window is properly shown before continuing with dialogue
            $ renpy.game.interface.suppress_dialogue = False
            $ renpy.game.interface.force_noninteractive = False
            $ _window_auto = True
            window auto
            
            n "I focus intently on the game, clicking as fast as I can whenever a button lights up."
            
            n "My reflexes are put to the test as the buttons light up faster and faster."
            
            # Different responses based on final_reaction_score
            if final_reaction_score <= 8:
                n "When the time runs out, my final score is [final_reaction_score]."
                
                pov "Not bad, but I didn't beat your score this time."
                
                f "Hey, that's still pretty good for your first try! It took me weeks to get to 10."
                
                n "Bandit seems genuinely impressed despite my lower score."
                
                f "You should definitely try again sometime. I bet you could beat my score with a little practice!"
                
            elif final_reaction_score <= 10:
                n "When the time runs out, my final score is [final_reaction_score]."
                
                if final_reaction_score == 10:
                    pov "Yes! I tied your high score, Bandit!"
                else:
                    pov "So close! Just missed your high score by a little bit."
                
                f "Wow! That's really impressive for your first try!"
                
                n "Bandit looks genuinely surprised and pleased."
                
                f "You've got some quick reflexes! We should definitely have a rematch sometime."
                
            else:
                n "When the time runs out, my final score is [final_reaction_score]!"
                
                pov "Yes! I beat your high score, Bandit!"
                
                f "No way! Let me see!"
                
                n "Bandit leans over, looking impressed and a little shocked."
                
                f "Wow, you're really good at this! I've been trying to break 10 all week!"
                
                pov "I guess I just have quick reflexes."
                
                f "You definitely do! That was amazing!"
            
            jump elopement_computer_lab_continue

# Continue with the computer lab scene
label elopement_computer_lab_continue:
            
            # Ms. Johnson enters with her class
            play sound "audio/opendoor.mp3"
            
            n "Suddenly, the door bursts open. Ms. Johnson walks in, leading a group of students."
            
            hide fs
            show t
            
            t "Alright class, we're here to complete an in-class assignment. No playing games until your work is done."
            
            n "Ms. Johnson scans the room and freezes when she sees me."
            
            hide t
            show ts
            
            t "[povname]! What are you doing here? You're supposed to be in my class right now!"
            
            n "My heart sinks. I've been caught."
            
            hide ts
            show t
            
            t "And Bandit, I didn't expect to see you here either."
            
            hide t
            show f
            
            f "Hi Ms. Johnson! Nice to see you!"
            
            hide f
            show t
            
            t "Hello Bandit. At least you have a free period."
            
            n "Ms. Johnson turns back to me, her expression stern."
            
            t "Come with me, [povname]. We need to have a talk."
            
            # Transition to hallway
            scene image "images/hallwayoffice.png"
            show t
            
            t "I'm very disappointed, [povname]. Skipping class is a serious offense."
            
            t "We're going to see the administrator about this."
            
            # Transition to office
            scene image "images/bg office.png"
            show t at left
            show ac at right
            
            t "Administrator Donkey, I found [povname] in the computer lab during my class period."
            
            a "I see. Thank you, Ms. Johnson. I'll handle this from here."
            
            hide t
            
            a "Have a seat, [povname]. We need to talk about the choices you've made today."
            
            # Transition to reflection
            jump elopement_computer_lab_reflection

# *********************************************************************
# Auditorium Ending Reflection
# *********************************************************************
label elopement_auditorium_reflection:
    # Set the outside school scene for reflection
    scene image "images/outsideschool.png"
    show ac
    
    a "Let's sit down and talk about what happened today."
    
    n "The administrator sits next to me on the bench. His expression is stern but not unkind."
    
    a "As you sit here with me, I want you to think about your actions today."
    
    # Player reflects on their actions
    "*Looking back on your decision to skip class today:*"
    
    # Player reflects on their actions
    $ action_reflection = renpy.input("What actions did you take that affected how things turned out?")
    
    # Player reflects on the results
    $ result_reflection = renpy.input("What happened as a result of your choices?")
    
    # Player reflects on their feelings
    $ feeling_reflection = renpy.input("How do you feel about the outcome?")
    
    # Player reflects on external factors
    $ external_reflection = renpy.input("What factors outside your control influenced the situation?")
    
    # Additional reflection specific to elopement
    $ elopement_reflection = renpy.input("What could you have done differently?")
    
    # Administrator provides feedback
    a "Thank you for your honesty, [povname]."
    
    # Feedback varies slightly based on whether player helped Mousy
    if helped_mousy:
        a "I noticed that you did the right thing by reporting the bullying situation with Mousy and Crusher. That shows good character."
        
        a "But skipping class is still a serious issue. When you're not where you're supposed to be, you miss important learning opportunities."
    else:
        a "Skipping class might seem harmless, but it has real consequences. You miss important learning, and it shows a lack of respect for your teachers and the school rules."
    
    a "Running away from me only made the situation worse. It's always better to face problems directly rather than trying to escape them."
    
    a "I understand that sometimes school can feel overwhelming. But there are better ways to handle those feelings than skipping class."
    
    a "If you're feeling stressed or overwhelmed, talk to a teacher, counselor, or even me. We're here to help you succeed."
    
    n "I nod, feeling a mix of embarrassment and relief that the administrator is being understanding despite my actions."
    
    a "Now, let's head back inside. We'll need to discuss appropriate consequences for your actions today."
    
    n "As we walk back toward the school, I realize that running away from my problems only led to bigger ones. Maybe next time I'll make better choices."
    
    # End of auditorium ending
    hide ac
    jump elopement_end

# *********************************************************************
# Computer Lab Ending Reflection
# *********************************************************************
label elopement_computer_lab_reflection:
    # Set the office scene for reflection
    scene image "images/bg office.png"
    show ac
    
    a "I want you to think about the choices you made today, [povname]."
    
    n "The administrator's expression is serious as he sits across from me at his desk."
    
    a "Thinking about the choices you made today:"
    
    # Player reflects on their actions
    $ action_reflection = renpy.input("What actions did you take that affected how things turned out?")
    
    # Player reflects on the results
    $ result_reflection = renpy.input("What happened as a result of your choices?")
    
    # Player reflects on their feelings
    $ feeling_reflection = renpy.input("How do you feel about the outcome?")
    
    # Player reflects on external factors
    $ external_reflection = renpy.input("What factors outside your control influenced the situation?")
    
    # Additional reflection specific to this ending
    $ impact_reflection = renpy.input("How might your actions have affected others?")
    
    # Administrator provides feedback
    a "Thank you for reflecting on your actions, [povname]."
    
    # Feedback varies slightly based on whether player helped Mousy
    if helped_mousy:
        a "I appreciate that you showed concern for Mousy by reporting the bullying. That was the right thing to do."
        
        a "However, that doesn't excuse skipping class. Your teachers worry when students don't show up where they're supposed to be."
    else:
        a "When you skip class, it doesn't just affect you. Your teachers worry, and you miss important learning opportunities."
    
    a "Ms. Johnson had planned an important lesson today, and your absence disrupted her class when she had to take time to deal with this situation."
    
    a "I understand that school can be challenging sometimes. But avoiding your responsibilities only creates more problems in the long run."
    
    a "If you're feeling overwhelmed or need a break, there are appropriate ways to address that. You can speak with a counselor or talk to your teachers about what you're experiencing."
    
    n "I nod, taking in the administrator's words. He's right, even if it's hard to admit."
    
    a "We'll need to discuss appropriate consequences for your actions today. But I also want to make sure you have the support you need to make better choices in the future."
    
    n "As the administrator continues talking, I realize that skipping class didn't solve any of my problems. It just created new ones."
    
    # End of computer lab ending
    hide ac
    jump elopement_end

# *********************************************************************
# End of Elopement Scenario
# *********************************************************************
label elopement_end:
    # Show Mousy for the conclusion
    scene bg classroom
    show ms
    
    # Mousy thanks the player
    e "Thank you for experiencing this scenario, [povname]!"
    
    e "Skipping class might seem like an easy solution when you're feeling overwhelmed, but as you've seen, it often leads to bigger problems."
    
    # Different feedback based on player's choices
    if helped_mousy:
        e "You showed compassion by helping me when you saw me being bullied. That was a good choice!"
        
        e "Even when we make mistakes, like skipping class, we can still make positive choices that help others."
    else:
        e "When you saw me being bullied, you chose to walk away. Sometimes it's scary to get involved, but speaking up can make a big difference."
        
        e "Remember that there are adults at school who can help in difficult situations."
    
    e "The next time you feel like skipping class, try talking to a teacher or counselor about what you're feeling instead."
    
    e "They can help you find better ways to handle stress and overwhelming feelings."
    
    # Final message
    e "Remember, running away from problems usually just makes them bigger. Facing them directly, with help when needed, is almost always the better choice."
    
    # Return to the main script
    return
