import os
import random

from lib import (
    aerodromes,
    aeromedical,
    aircraft_operations,
    aviation_occurences,
    clearance_instructions,
    collision_avoidance,
    communications,
    controlled_airspace,
    equipment,
    flight_plans,
    general_airspace,
    pilot_responsibilities,
    practice_exam,
    visual_signals,
    wake_turbulence,
)


def categories():

    topic_list = [
        "1. Collision Avoidance",
        "2. Visual Signals",
        "3. Communications",
        "4. Aerodromes",
        "5. Equipment",
        "6. Pilot Responsibilities",
        "7. Wake Turbulence",
        "8. Aeromedical",
        "9. Flight Plans",
        "10. Clearances and Instructions",
        "11. Aircraft Operations",
        "12. General Airspace",
        "13. Controlled Airspace",
        "14. Aviation Occurences",
        "15. Practice Exam",
    ]
    num_columns = 2

    while True:
        os.system("clear")
        print("Choose a category:")
        for item in topic_list:
            print((item).expandtabs(10))

        answer = input("> ")
        print(answer)

        match answer:
            case "1":
                return (
                    collision_avoidance.collision_avoidance(),
                    "Collision Avoidance",
                )
            case "2":
                return (
                    visual_signals.visual_signals(),
                    "Visual Signals",
                )
            case "3":
                return (
                    communications.communications(),
                    "Communications",
                )
            case "4":
                return (
                    aerodromes.aerodromes(),
                    "Aerodromes",
                )
            case "5":
                return (
                    equipment.equipment(),
                    "Equipment",
                )
            case "6":
                return (
                    pilot_responsibilities.pilot_responsibilities(),
                    "Pilot Responsibilities",
                )
            case "7":
                return (
                    wake_turbulence.wake_turbulence(),
                    "Wake Turbulence",
                )
            case "8":
                return (
                    aeromedical.aeromedical(),
                    "Aeromedical",
                )
            case "9":
                return (
                    flight_plans.flight_plans(),
                    "Flight Plans",
                )
            case "10":
                return (
                    clearance_instructions.clearance_instructions(),
                    "Clearance and Instructions",
                )
            case "11":
                return (
                    aircraft_operations.aircraft_operations(),
                    "Aircraft Operations",
                )
            case "12":
                return (
                    general_airspace.general_airspace(),
                    "General Airspace",
                )
            case "13":
                return (
                    controlled_airspace.controlled_airspace(),
                    "Controlled Airspace",
                )
            case "14":
                return (
                    aviation_occurences.aviation_occurences(),
                    "Aviation Occurences",
                )
            case "15":
                return (practice_exam.practice_exam(), "Practice Exam")
            case _:
                print(f"Invalid option; {answer}")
                input("Press Enter to continue...")


def generator(categories):

    questions_correct: int = 0
    review_questions: list[str] = []

    questions = categories[0]
    num_questions = len(questions)
    topic = categories[1]

    index = 0
    while index < len(questions):
        random_question = key, val = random.choice(list(questions.items()))
        random_answer: str = random_question[1][0]

        choice: list[str] = ["a", "b", "c", "d"]
        choices: list[str] = [
            random_question[1][0],
            random_question[1][1],
            random_question[1][2],
            random_question[1][3],
        ]

        correct_statement: str = random_question[1][0]

        random.shuffle(choices)

        question = list(random_question)

        os.system("clear")
        print(f"{topic}\n")
        print(f"{question[0]}")

        correct_answer: str = ""

        for val, val_choice in zip(choice, choices):
            print(f" {val}.) {val_choice}")
            if val_choice == correct_statement:
                correct_answer = val

        answer = input("> ")

        if answer == correct_answer:
            questions_correct = questions_correct + 1
        else:
            review_questions.append(question)

        questions.pop(question[0])

    print(f"You have answered {questions_correct} out of {num_questions} correctly.")
    print(f"Review the following questions:\n{review_questions[0:]}")


generator(categories())
