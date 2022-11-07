def collision_avoidance():

    # the correct answer is the first dictionary value
    questions: dict[str, list[str]] = {
        "Which statement is true with regard to aircraft converging at approximately the same altitude?": [
            "An aircraft towing objects has the right of way over all power-driven heaver-than-air-aircraft.",
            "A jetliner has the right of way over all aircraft.",
            "An aeroplane has the right of way over all other airacraft which are converging from the left.",
            "Aeroplanes towing gliders must give way to helicopters.",
        ],
        "When two aircraft are converging at approximately the same altitude": [
            "the aircraft that has the other on its right shall give way.",
            "both aircraft shall alter heading to the left.",
            "the aircraft on the right shall avoid the other by descending.",
            "the aircraft that has the other on its left shall give way.",
        ],
        "When two aircraft are converging at approximately the same altitude, which statement applies?": [
            "Power-driven heavier-than-air aircraft shall give way to gliders.",
            "Gliders shall give way to helicopters.",
            "Aeroplanes shall give way to power-driven heavier-than-air aircraft",
            "Gliders shall give way to aeroplanes.",
        ],
        # since the following two questions are the same, end spaces are required to create a unique key
        "When two aircraft are converging at approximately the same altitude, which statement applies? ": [
            "Helicopters shall give way to gliders.",
            "Gliders shall give way to helicopters.",
            "Aeroplanes shall give way to helicopters.",
            "Helicopters shall give way to aeroplanes.",
        ],
        "When two aircraft are converging at approximately the same altitude, which statement applies?  ": [
            "Gliders shall give way to balloons.",
            "Gliders shall give way to helicopters.",
            "Aeroplanes shall give way to helicopters.",
            "Helicopters shall give way to aeroplanes.",
        ],
        "When converging at approximately the same altitude": [
            "aeroplanes towing gliders shall give way to balloons.",
            "balloons shall give way to hang gliders.",
            "balloons shall give way to gliders.",
            "balloons shall give way to airships.",
        ],
        "When two power-driven heavier-than-air aircraft are converging at approximately the same altitude": [
            "the one on the right has the right of way.",
            "the one on the left has the right of way.",
            "both shall alter their heading to the left.",
            "the one on the right shall give way by descending.",
        ],
        "When two aircraft are approaching head-on or approximately so and there is danger of collision, each pilot shall": [
            "alter heading to the right.",
            "decrease airspeed",
            "increase airspeed",
            "alter heading to the left",
        ],
        "When overtaking an aircraft at your 12 o'clock position, at your altitude, you should": [
            "alter heading to your right.",
            "alter heading to your left.",
            "climb",
            "descend",
        ],
        "Two aircraft are on approach to land, the aircraft at the higher altitude shall": [
            "give way.",
            "have the right of way.",
            "overtake the lower aircraft on the left.",
            "complete a 360° turn to the right.",
        ],
    }

    return questions
