def get_branch(decision_tree):
    branches = decision_tree["branches"]
    try:
        print()
        answer = int(
            input(
                decision_tree["question"] + f"\nPlease input a number between 1 and {len(branches)} corresponding to the path you wish to take: "
            )
        )
    except ValueError:
        print("\nInvalid response. Please try agian")
        return get_branch(decision_tree)

    try:
        return decision_tree["branches"][answer - 1]
    except IndexError:
        print("\nInvalid response. Please try again")
        return get_branch(decision_tree)


decision_tree = {
    "question": "You wake up in the middle of the night in a cold sweat. "
                "A storm is raging outside your window. All of a sudden, "
                "you realize you forgot you have a coding assignment due "
                "tomorrow. Do you (1) jump out of bed and try to finish "
                "it as quickly as possible, or (2) go back to bed and "
                "worry about it later?",
    "branches": [
        {
            "question": "You rush to your desk and spend the rest of the night "
                        "coding. For loops and if statements are all you can "
                        "think about as the sun comes up. When you finally finish, "
                        "do you (1) test your code, or (2) submit it as is?\n"
                        "(Grave consequences will result from your choice)",
            "branches": [
                {
                    "outcome": "You spend your entire morning testing and refining "
                               "your sleeplessly written code. By the time you're done, "
                               "you are so tired that you fall asleep on your keyboard. "
                               "When you wake up, it is evening, and you missed class. "
                               "You are about to despair, but then your notice that you "
                               "pressed the delete key during your slumber and deleted "
                               "not only your assignment, but your entire file system. "
                               "Luckily, you made backups, but you sleep-deleted those "
                               "as well. You sit in shock and stare vacantly at your "
                               "blank screen, knowing that you are a failure. Because "
                               "of your missing assingment, you fail to get into college "
                               "and get a job, so you spend the rest of your life in your "
                               "parent's basement, wondering why you just had to test your "
                               "code."
                },
                {
                    "outcome": "Your day progresses as normal, and during class your "
                               "teacher says nothing about the assignment. However, "
                               "that night, you notice flashing lights outside your house "
                               "and hear crashes as FBI agents break into your room and "
                               "tackle you. You are arrested and taken to an interrogation "
                               "room. You are questioned about a cyber attack that took out "
                               "the US government's entire infrastructure. The attack was "
                               "traced back to your house. Apparently, the code you wrote "
                               "sleeplessly last night was so bad it was mistaken for malware. "
                               "You try to explain this to the investigators, but they won't hear "
                               "you. You are tried, convicted, and sentenced to life in prison. "
                               "As the days pass behind bars, you wonder why you couldn't've just "
                               "written tests."
                }
            ]
        },
        {
            "question": "You wake up in the morning and go to school. The only thing "
                        "you can think about is your missing coding assignment. You "
                        "walk into class and prepare to tell your teacher that you "
                        "forgot the assignment when you notice that one of your "
                        "classmates has left their computer unlocked. Do you (1) "
                        "steal their assignment and pass it off as your own, or (2) "
                        "take the high road an come clean to your teacher?"
                        "(Your entire future rests on this moment)",
            "branches": [
                {
                    "question": ""
                }
            ]
        }
    ]
}

print("Welcome to the life decision simulator! Choose wisely!\n")

while decision_tree.get("question"):
    decision_tree = get_branch(decision_tree)

print()
print(decision_tree.get("outcome", "The end"))
print("Thanks for playing the life decision simulator!")
