# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("Game") # narrator character
$playerNName= "" #PLAYER PREFERED NAME

image bg: 
    "images/background_lns.png"
    zoom 1.7
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
    y "I can't fall asleep."
    b "Maybe because you had coffee this morning?"
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

    # This ends the game.
    return
