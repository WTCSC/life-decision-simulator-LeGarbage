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
                    "question": "You rush to the unlocked computer and frantically search "
                                "for your classmate's code. After digging through their "
                                "files, you finally find it. Quickly, you copy the code "
                                "and head back to your computer. After a minute of changing "
                                "their code so it doesn't look exactly the same, you submit it "
                                "and breathe a sigh of relief. Suddenly, a shadow looms over you "
                                "and you turn around to see your teacher standing with his arms "
                                "crossed and a dissapointed look on his face. Do you (1) confess, "
                                "or (2) double down?",
                    "branches": [
                        {
                            "outcome": "You break down and confess everything to your teacher. "
                                       "To your surprise, he sighs and says, \"Finally, some honesty.\" "
                                       "He explains that the assignment was actually a trap to test "
                                       "your integrity, and you failed. You are immediately expelled. "
                                       "Years later, you find yourself working as a cashier at a gas "
                                       "station, bitterly reminding customers to have a nice day while "
                                       "wondering what might have been if you hadn’t stolen that code."
                        },
                        {
                            "outcome": "You look your teacher dead in the eye and declare that the "
                                       "work is yours. The classroom falls silent. Your teacher smirks, "
                                       "then calls your classmate to the front. They reveal their code "
                                       "is written in Python, while your submission was in Java. You "
                                       "panic. Your teacher announces to the class that you attempted "
                                       "the most pathetic plagiarism in academic history. Your classmates "
                                       "stare at you in shoked silence, wondering how you could even mess "
                                       "that up, and to be honest, you can't believe it either. Your "
                                       "teacher doesn't even have to tell you to leave as you slowly "
                                       "walk out of the classroom, never to be seen agian."
                        }
                    ]
                },
                {
                    "outcome": "You straighten your back, take a deep breath, and admit to your "
                               "teacher that you forgot to do the assignment. He stares at you for "
                               "a while with a quizzical look on his face. Finally, he speaks: "
                               "\"Assignment? What assignment?\" You show him, and a look of "
                               "realization crosses his face. \"Oh, that? That's just a typo.\" The entire class "
                               "bursts out in laughter. You sit back in your chair, cheeks burning, and realize "
                               "you ruined your entire week over nothing. You spend the rest of your life "
                               "double and triple checking any document that you read, forever haunted "
                               "by made-up deadlines."
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
