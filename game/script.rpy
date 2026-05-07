# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("Game") # narrator character
$playerNName= "" #PLAYER PREFERED NAME

init python:
    upleft = Position(xpos=0.88, ypos=0.4)

image bg: 
    "images/background_lns.png"
    zoom 1.7
# Food images:
image pchips:
    "images/pchip_lns.png"
image coke:
    "images/coke_lns.png"
image monster:
    "images/monster_lns.png"
image lpop:
    "images/lpop_lns.png"

#Emotion images:
image angry: 
    "images/angry_lns.png"
    zoom 0.7
image sad:
    "images/sad_lns.png"
    zoom 0.7
image shock:
    "images/shock_lns.png"
    zoom 0.7
image happy:
    "images/happy_lns.png"
    zoom 0.7
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    $playerNName = renpy.input(default= '', prompt="What do you like to be called?")
    define y = Character("[playerNName]")

    b "You want to be called [playerNName]."
    b "It's night time,"
    b "Almost 12 A.M."
    show sad at upleft 
    y "I can't fall asleep."
    b "Maybe because you had coffee this morning?"
    hide sad
    y "That's not gonna help me."
    b "Well am I wrong?"
    menu:
        "Shut up.":
            jump coffee
        "Not really...":
            jump coffee
label coffee: 
    b "Hahahaha, too bad"
    y "Well what do you suggest I do???"
    b "I don't know, why are you asking me?"
    show angry at upleft
    y "BECAUSE YOU'RE THE ONE LAUGHING AT ME!!!"
    y "WHO EVEN ARE YOU?! WHAT ARE YOU DOING IN MY ROOM?!"
    b "Woah woah woah chill,"
    hide angry
    b "I'm just the game talking to you"
    b "You can't possibly get rid of me while playing."
    y "I wish I could"
    show shock at upleft
    b "Hey that's not nice!"
    
    menu:
        "Haha":
            jump second
        "Sorry":
            jump second
label second:
    hide shock
    b "Anyways..."
    b "Now that you can't sleep, what are your plans?"
    y "Well go on my phone I guess..."
    b "HELL NAH!!!"
    show shock at upleft
    y "Are you crazy???"
    b "Hehehehe"
    hide shock
    b "But if you go on your phone I'll be bored :("
    y "And...?"
    b "Come on now"
    menu:
        "Fine":
            jump third
        "No":
            jump loop1
label loop1:
    b "Please?"
    b "I'll be sooooo bored"
    menu:
        "Fine":
            jump third
        "No":
            jump loop1
label third:
    b "Yayyyyy!!!"
    y "Well what do you suggest I do?"
    b "Eat some snacks and talk to me!"
    show angry at upleft
    y "ME??? STUCK WITH YOU???"
    b "I mean you're in this game, so you're stuck with me! :>"
    hide angry
    y "Do you know how annoying you are?"
    b "That's the goal, to be annoying. It's fun!"
    show angry at upleft
    y "IT'S NOT FUN"
    b "Okay calm down it's not that deep"
    hide angry
    y "Whatever..."
    y "I'm kinda hungry anyway,"
    y "What snacks do we have?"
    show pchips:
        pos (0.7, 0.25)
    show coke:
        pos (0.49, 0.25)
    show monster:
        pos (0.27, 0.25)
    show lpop:
        pos (0.05, 0.25)
    b "We have potato chips, a can of coke, a monster energy dring, and a lolipop!"
    b "But you can only choose one!"
    show shock at upleft
    y "Why not more?"
    b "Because I say so!"
    hide shock
    y "That sucks, but okay."
    b "Well which one do you choose?"
    menu:
        "Potato chips":
            jump potatoc
        "Can of Coke":
            jump coka
        "Monster energy drink":
            jump monsdrink
        "Lolipop":
            jump lolipop
label potatoc:
    hide coke
    hide monster
    hide lpop
    hide pchips
    show pchips:
        pos (0.4, 0.25)
    b "Okay that's a pretty solid choice!"
    y "I mean who doesn't like potato chips?"
    b "I love potato chips!!!"
    show sad at upleft
    y "I didn't mean you are included..."
    b "Awhhh"
    hide sad
    b "But I like to be included!"
    y "You annoyed me way too much."
    b "Fine I'm sorry!"
    show angry at upleft
    y "Wow now you say sorry?"
    hide angry
    show shock at upleft
    b "Hey you're in MY game!"
    b "You CAN'T talk like that to me!!!"
    hide shock
    show happy at upleft
    y "Hahahaha now look who's annoyed!"
    b "You're being annoying."
    hide happy
    y "Anyways, I like these chips"
    y "They taste pretty good."
    b "Can I have some?"
    hide pchips
    y "I already ate all of it..."
    b "HOW FAT DO YOU HAVE TO BE TO EAT ALL THAT???"
    y "Hahaha"
    b "This is NOT funny"
    y "Then why am I laughing?"
    b "GET OUT OF MY GAME ALREADY I'M SICK OF YOU YOU CAN'T EVEN GIVE ME SOME CHIPS"
    y "Hehehehe"
    y "I'm gonna sleep now be quiet."
    b "YES JUST SLEEP I DON'T WANNA TALK TO YOU ANYMORE!!!"
    return
label coka:
    hide pchips
    hide monster
    hide lpop
    hide coke
    show coke:
        pos (0.4, 0.25)
    b "The coke?"
    b "Good choice I like that too"
    b "It's so yummy"
    y "We finally agree on something"
    b "See I'm not THAT annoying"
    y "You kinda are though"
    b "That's NOT nice"
    y "Hehehe I successfully annoyed you"
    b "No it doesn't count"
    y "Anyways let me drink some"
    y "Yummy"
    y "It's so good I'm about to cry"
    b "Damn that's actually crazy"
    b "How good is it?"
    y "It tastes like it came from heaven"
    y "Yum yum yum yum yum"
    b "Can I have some?"
    y "NO!!!"
    b "BUT YOU STILL HAVE SOME LEFT!"
    hide coke
    y "Too bad I drank it all..."
    b "WHA-"
    b "HOW DID YOU DRINK ALL THAT???"
    y "I'm just cool like that!"
    return
label monsdrink:
    b "Test"
    return
label lolipop:
    b "Test"
    return
    


    # This ends the game.
    return
