import random
from lib import collision_avoidance, visual_signals, communications, aerodromes


def practice_exam():

    # number of questions on the exam
    num_questions = 50

    # count total number of questions available per category
    collision_questions = collision_avoidance.collision_avoidance()
    collision_num_questions = len(collision_questions)

    visual_questions = visual_signals.visual_signals()
    visual_num_questions = len(visual_questions)

    comm_questions = communications.communications()
    comm_num_questions = len(comm_questions)

    aerodromes_questions = aerodromes.aerodromes()
    aerodromes_num_questions = len(aerodromes_questions)

    equipment_num_questions = 11
    pilotresp_num_questions = 23
    turbulence_num_questions = 15
    aeromedical_num_questions = 13
    flightplan_num_questions = 11
    clearance_num_questions = 6
    aircraft_ops_num_questions = 17
    general_num_questions = 21
    controlled_num_questions = 12
    occurences_num_questions = 5

    # total exam questions
    total_questions = (
        collision_num_questions
        + visual_num_questions
        + comm_num_questions
        + aerodromes_num_questions
        + equipment_num_questions
        + pilotresp_num_questions
        + turbulence_num_questions
        + aeromedical_num_questions
        + flightplan_num_questions
        + clearance_num_questions
        + aircraft_ops_num_questions
        + general_num_questions
        + controlled_num_questions
        + occurences_num_questions
    )

    # determine number of exam questions per category
    collision_perc_questions = collision_num_questions / total_questions
    collision_exam_num_questions = collision_perc_questions * num_questions
    collision_exam_num_questions = round(collision_exam_num_questions)

    visual_perc_questions = visual_num_questions / total_questions
    visual_exam_num_questions = visual_perc_questions * num_questions
    visual_exam_num_questions = round(visual_exam_num_questions)

    comm_perc_questions = comm_num_questions / total_questions
    comm_exam_num_questions = comm_perc_questions * num_questions
    comm_exam_num_questions = round(comm_exam_num_questions)

    aerodromes_perc_questions = aerodromes_num_questions / total_questions
    aerodromes_exam_num_questions = aerodromes_perc_questions * num_questions
    aerodromes_exam_num_questions = round(aerodromes_exam_num_questions)

    equipment_perc_questions = equipment_num_questions / total_questions
    equipment_exam_num_questions = equipment_perc_questions * num_questions
    equipment_exam_num_questions = round(equipment_exam_num_questions)

    pilotresp_perc_questions = pilotresp_num_questions / total_questions
    pilotresp_exam_num_questions = pilotresp_perc_questions * num_questions
    pilotresp_exam_num_questions = round(pilotresp_exam_num_questions)

    turbulence_perc_questions = turbulence_num_questions / total_questions
    turbulence_exam_num_questions = turbulence_perc_questions * num_questions
    turbulence_exam_num_questions = round(turbulence_exam_num_questions)

    aeromedical_perc_questions = aeromedical_num_questions / total_questions
    aeromedical_exam_num_questions = aeromedical_perc_questions * num_questions
    aeromedical_exam_num_questions = round(aeromedical_exam_num_questions)

    flightplan_perc_questions = flightplan_num_questions / total_questions
    flightplan_exam_num_questions = flightplan_perc_questions * num_questions
    flightplan_exam_num_questions = round(flightplan_exam_num_questions)

    clearance_perc_questions = clearance_num_questions / total_questions
    clearance_exam_num_questions = clearance_perc_questions * num_questions
    clearance_exam_num_questions = round(clearance_exam_num_questions)

    aircraft_ops_perc_questions = aircraft_ops_num_questions / total_questions
    aircraft_ops_exam_num_questions = aircraft_ops_perc_questions * num_questions
    aircraft_ops_exam_num_questions = round(aircraft_ops_exam_num_questions)

    general_perc_questions = general_num_questions / total_questions
    general_exam_num_questions = general_perc_questions * num_questions
    general_exam_num_questions = round(general_exam_num_questions)

    controlled_perc_questions = controlled_num_questions / total_questions
    controlled_exam_num_questions = controlled_perc_questions * num_questions
    controlled_exam_num_questions = round(controlled_exam_num_questions)

    occurences_perc_questions = occurences_num_questions / total_questions
    occurences_exam_num_questions = occurences_perc_questions * num_questions
    occurences_exam_num_questions = round(occurences_exam_num_questions)

    # used to verify total exam questions
    total_exam_questions = (
        visual_exam_num_questions
        + comm_exam_num_questions
        + collision_exam_num_questions
        + aerodromes_exam_num_questions
        + equipment_exam_num_questions
        + pilotresp_exam_num_questions
        + turbulence_exam_num_questions
        + aeromedical_exam_num_questions
        + flightplan_exam_num_questions
        + clearance_exam_num_questions
        + aircraft_ops_exam_num_questions
        + general_exam_num_questions
        + controlled_exam_num_questions
        + occurences_exam_num_questions
    )

    # verify total exam questions
    if total_exam_questions == num_questions:
        pass
    else:
        print(
            f"{num_questions} expectations have not been met; total is {total_exam_questions}."
        )
        exit()

    # generate random 1exam questions
    questions: dict[str, list[str]] = {}
    exam_question_list = []

    collision_questions_list = [
        random.choice(list(collision_questions))
        for i in range(collision_exam_num_questions)
    ]
    for key in collision_questions_list:
        questions.update({key: collision_questions[key]})

    visual_questions_list = [
        random.choice(list(visual_questions)) for i in range(visual_exam_num_questions)
    ]
    for key in visual_questions_list:
        questions.update({key: visual_questions[key]})

    comm_questions_list = [
        random.choice(list(comm_questions)) for i in range(comm_exam_num_questions)
    ]
    for key in comm_questions_list:
        questions.update({key: comm_questions[key]})

    aerodromes_questions_list = [
        random.choice(list(aerodromes_questions))
        for i in range(aerodromes_exam_num_questions)
    ]
    for key in aerodromes_questions_list:
        questions.update({key: aerodromes_questions[key]})

    return questions


"""
# questions need to be added
    equipment_questions_list = [random.choice(list(equipment_questions)) for i in range(equipment_exam_num_questions)]
    pilotresp_questions_list = [random.choice(list(pilotresp_questions)) for i in range(pilotresp_exam_num_questions)]
    turbulence_questions_list = [random.choice(list(turbulence_questions)) for i in range(turbulence_exam_num_questions)]
    aeromedical_questions_list = [random.choice(list(aeromedical_questions)) for i in range(aeromedical_exam_num_questions)]
    flightplan_questions_list = [random.choice(list(flightplan_questions)) for i in range(flightplan_exam_num_questions)]
    clearance_questions_list = [random.choice(list(clearance_questions)) for i in range(clearance_exam_num_questions)]
    aircraft_ops_questions_list = [random.choice(list(aircraft_ops_questions)) for i in range(aircraft_ops_exam_num_questions)]
    general_questions_list = [random.choice(list(general_questions)) for i in range(general_exam_num_questions)]
    controlled_questions_list = [random.choice(list(controlled_questions)) for i in range(controlled_exam_num_questions)]
    occurences_questions_list = [random.choice(list(occurences_questions)) for i in range(occurences_exam_num_questions)]
"""
