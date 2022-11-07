def visual_signals():

    # the correct answer is the first dictionary value
    questions: dict[str, list[str]] = {
        "A series of green flashes directed at an aircraft means respectively in flight/on the ground": [
            "return for landing; cleared to taxi.",
            "cleared to land; cleared to taxi.",
            "return for landing: cleared for take-off.",
            "cleared to land",
            "cleared for take-off.",
        ],
        "A steady red light direct at an aircraft means in flight/on the ground.": [
            "give way to other aircraft and continue circling; stop.",
            "give way to other aircraft and continue circling; taxi clear of landing area in use.",
            "airport unsafe do not land; taxi clear of landing area in use.",
            "airport unsafe do not land; stop.",
        ],
        "A series of red flashes direct at an aircraft means respectively in flight/on the ground": [
            "airport unsafe, do not land; taxi clear on landing area in use.",
            "give way to other aircraft and continue circling; stop.",
            "do not land for time being; return to starting point on airport.",
            "you are in prohibited area, alter course; stop.",
        ],
        "A steady green light directed at an aircraft means respectively in flight/on ground": [
            "cleared to land; cleared for take-off.",
            "cleared to land; cleared to taxi.",
            "return for landing; cleared for take-off.",
            "return for landing; cleared to taxi.",
        ],
        "A flashing white lite directed at an aircraft on the manoeuvering area of an airport means": [
            "return to starting point on the airport.",
            "stop.",
            "cleared to taxi.",
            "taxi clear of landing area in use.",
        ],
        "Blinking runway lights advises vehicles and pedestrians to": [
            "vacate the runways immediately.",
            "return to the apron.",
            "be aware that an emergency is in progress; continue with caution.",
            "be aware that an emergency in in progress; hold your position.",
        ],
        "Chrome yellow and black strips painted on pylons or on the roof of a building identifies": [
            "a fur farm.",
            "an area where explosives are in use.",
            "an artillery range.",
            "an open pit mine.",
        ],
        "Pilots should not overfly reindeer or caribou at an altitude of less than": [
            "2,000 feet AGL.",
            "2,500 feet AGL.",
            "1,500 feet AGL.",
            "1,000 feet AGL.",
        ],
    }

    return questions
