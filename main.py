import random


# List of colors.

colortypes = ['Bright', 'Light', 'Medium', 'Dark']
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Pink']

# List of classes and aspects.

classes = ['Heir', 'Witch', 'Page', 'Knight', 'Maid', 'Sylph', 'Seer', 'Mage', 'Bard', 'Prince', 'Rogue', 'Thief']
mclasses = ['Lord', 'Muse']
cclasses = ['Host', 'Guide', 'Judge', 'Scribe', 'Saint', 'Soul', 'Hound', 'Will', 'Smith', 'Fae', 'Bane', 'Scourge',
            'Queen', 'King', 'Knave', 'Rook']
aspects = ['Time', 'Space', 'Light', 'Void', 'Life', 'Doom', 'Breath', 'Blood', 'Heart', 'Mind', 'Hope', 'Rage']


def options():
    mastertoggle = str(input("Include masterclasses? Y or N. "))
    if mastertoggle.lower() == 'y':
        classes.extend(mclasses)

    customtoggle = str(input("Include custom classes? Y or N. "))
    if customtoggle.lower() == 'y':
        classes.extend(cclasses)

    characters = input(
        "How many characters to generate? A number, recommended below 12 unless including custom terms. ")
    generatechars(characters)


# Actual character generator.
def generatechars(characters):
    for num in range(0, int(characters)):
        print(random.choice(colortypes) + " " + random.choice(colors) + "-eyed " + random.choice(
            classes) + " of " + random.choice(aspects))
    repeat_prompt()


def repeat_prompt():
    repeat = str(input("Would you like to reroll? "))
    print(repeat)
    if repeat.lower() == 'y':
        ans = int(input("How many? "))
        generatechars(ans)

    exit()


# This is where the program starts
options()
