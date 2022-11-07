def communications():

    # the correct answer is the first dictionary value
    questions: dict[str, list[str]] = {
        "When making initial contact with a Canadian ATC unit, the pilot of aircraft C-GFLU should transmit the registration as": [
            "Golf - Foxtrot - Lima - Uniform over.",
            "Lima - Uniform over.",
            "Foxtrot - Lima - Uniform over.",
            "Charlie - Golf - Foxtrot - Lima - Uniform over.",
        ],
        "When making initial contact with a Canadian ATC unit, the pilot of aircraft C-FBSQ should transmit the registration as": [
            "Foxtrot, Bravo, Sierra, Quebec.",
            "Fox, Baker, Sugar, Queen.",
            "FBSQ.",
            "Bravo, Sierra, Quebec.",
        ],
        "After a Canadian privately registered aircraft has made initial contact with an ATS unit, which items may be omitted from subsequent transmissions? The aircraft type and": [
            "the first two letter of the registration, if initiated by ATS.",
            "any registration letters omitted by ATS in the last communication.",
            "the first three letters of the registration.",
            "the phonetic equivalents.",
        ],
        "On initial radio contact with an ATS unit the pilot shall transmit the": [
            "type of aircraft and last four letters of the registration in phonetics.",
            "last three letters of the registration in phonetics.",
            "whole registration in phonetics.",
            "type of aircraft and the last three letters of the registration in phonetics.",
        ],
        "ATIS is normally provided": [
            "to relieve frequency congestion.",
            "to replace the FSS.",
            "for the rapid updating of weather forecasts.",
            "only when VFR conditions exist at airports.",
        ],
        "Where ATIS is available the information which should be included on first contact with ATC is the": [
            "ATIS phonetic identifier.",
            "phrase 'with the numbers'.",
            "phrase 'with ATIS received'.",
            "phrase 'with the information'.",
        ],
        "Wherever practicable, pilots operating VFR en route in uncontrolled airspace should continuously monitor": [
            "126.7 MHz.",
            "122.2 MHz.",
            "123.2 MHz.",
            "122.8 MHz.",
        ],
        "En route aircraft should, whenever possible, maintain a listening watch for aircraft in distress on": [
            "121.5 on the aircraft receiver.",
            "121.5 during the first 5 minutes of each hour.",
            "the receiver mode of the ELT.",
            "the voice frequency of the navigation aid in use.",
        ],
        "The specific frequency, distance and altitude within which MF procedures are to be followed are given in the": [
            "CFS.",
            "Designated Airspace Handbook.",
            "TC AIM.",
            "Flight Training Manual",
        ],
        "Pilots broadcasting on a MF where no ground station is in operation should direct their transmission to the": [
            "aerodrome traffic.",
            "first aircraft heard on the frequency.",
            "aerodrome UNICOM.",
            "closest ATC unit.",
        ],
        "Pilots operating in VMC and intending to land at aerodromes where no UNICOM exists, should broadcast their intentions on the ATF of": [
            "123.2 MHz.",
            "121.5 MHz.",
            "122.2 MHz.",
            "126.7 MHz.",
        ],
        "If a MF is in use, pilots departing VFR shall monitor that frequency until": [
            "beyond the specified distance or altitude.",
            "established en route.",
            "established at cruise altitude.",
            "clear of the aerodrome circuit pattern.",
        ],
        "A pilot is cleared to taxi to the runway in use without a hold short clearance. To get there, the aircraft must cross two taxiways and one runway. This authorizes the pilot to": [
            "the runway in use, but further clearance is required to cross the other runway.",
            "the runway in use, but further clearance is required to cross each taxiway and runway en route.",
            "position on the runway without further clearance.",
            "the runway in use, but must hold short.",
        ],
        "Ground control authorizes 'GOLF ALPHA BRAVO CHARLIE TAXI RUNWAY 29 HOLD SHORT OF RUNWAY 04'. The pilot should acknowledge this by replying 'GOLF ALPHA BRAVO CHARLIE TO": [
            "HOLD SHORT OF 04'.",
            "RUNWAY 04'.",
            "RUNWAY 29'.",
            "HOLD SHORT OF 29'.",
        ],
        "When a clearance for an 'immediate take-off' is accepted, the pilot shall": [
            "taxi onto the runway and take off in one continuous movement.",
            "back-track on the runway to use the maximum available length for take-off.",
            "complete the pre-take-off check before taxiing onto the runway and taking off.",
            "taxi to a full stop in position on the runway and take off without a further clearance.",
        ],
        "A pilot flying a heading of 270° , receives the following message from ATV, 'Traffic 2 o'clock, 5 miles, eastbound'. This information indicates the traffic is ": [
            "60° to the right, altitude unknown.",
            "90° to the right, at the same altitude.",
            "90° to the left, at the same altitude.",
            "60° to the left, altitude unknown",
        ],
        "A pilot receives the following ATC clearance 'CLEARED TO LAND, TURN RIGHT AT THE FIRST INTERSECTION'. The pilot should": [
            "land and turn off at the nearest intersection possible commensurate with safety.",
            "land and attempt to turn off even though the speed is considered too high to safely accomplish the turn.",
            "complete a touch-and-go if it is not possible to safely accomplish the turn.",
            "land and do a 180° turn and taxi back to clear the runway at the required intersection.",
        ],
        "The radiotelephone distress signal to indicate grave and/or imminent danger requiring immediate assistance is": [
            "MAYDAY, MAYDAY, MAYDAY.",
            "SECURITY, SECURITY, SECURITY.",
            "EMERGENCY, EMERGENCY, EMERGENCY.",
            "PAN PAN, PAN PAN, PAN PAN.",
        ],
        "The radiotelephone urgency signal to indicate a condition concerning the safety of an aircraft, vehicle or of some person on board which does not require immediate assistance is": [
            "PAN PAN, PAN PAN, PAN PAN.",
            "URGENCY, URGENCY, URGENCY.",
            "MAYDAY, MAYDAY, MAYDAY",
            "EMERGENCY, EMERGENCY, EMERGENCY",
        ],
        "What should be included along with the call sign of the aircraft and time to indicate the cancellation of a distress message": [
            "MAYDAY, ALL STATIONS, ALL STATIONS, ALL STATIONS, SILENCE FINISHED, OUT.",
            "MAYDAY, MAYDAY, MAYDAY, ALL STATIONS, DISTRESS TRAFFIC ENDED, OUT.",
            "MAYDAY CANCELLED, MAYDAY CANCELLED, MAYDAY CANCELLED.",
            "ALL STATIONS, ALL STATIONS, ALL STATIONS, EMERGENCY OVER.",
        ],
        "A departing flight will normally remain on tower frequency until": [
            "clear of the control zone.",
            "the flight is 2,000 feet AGL.",
            "25 NM from the airport.",
            "15 NM from the Control Zone.",
        ],
        "You advise the ATC that you are on the downwind leg. If there is other traffic in the circuit, ATC will then": [
            "inform you of your number in the approach sequence or other appropriate instructions.",
            "inform you of the runway in use, wind and altimeter.",
            "advise you of all the other circuit traffic.",
            "clear you to land.",
        ],
        "A radio equipped aircraft has been cleared to land at a controlled airport. The pilot should acknowledge the clearance by": [
            "transmitting the aircraft call signs.",
            "clicking the microphone button.",
            "replying 'Roger'.",
            "replying 'Wilco'.",
        ],
        "An initial call to Timmins FSS should be 'Timmins": [
            "radio...'",
            "Flight Service Station...'",
            "UNICOM...'",
            "this is...'",
        ],
        "A responsibility of a flight service specialist is to provide": [
            "flight planning service.",
            "terminal radar service.",
            "air traffic service in uncontrolled airspace only.",
            "all traffic control.",
        ],
        "NOTAMS are": [
            "available at all FIC.",
            "valid for 24 hours.",
            "issued for airport facility closures only.",
            "mailed to all pilots.",
        ],
        "A new or replacing NOTAM without the term 'APRX' is valid": [
            "until the time quoted in the NOTAM.",
            "for the day it was issued.",
            "for 48 hours only.",
            "until a cancelling NOTAM is issued.",
        ],
        "The term 'APRX' when contained in a new or replacing NOTAM means the NOTAM is valid": [
            "until a cancelling or replacing NOTAM is issues.",
            "for approximately 24 hours.",
            "for approximately 48 hours.",
            "until the time quoted in the NOTAM.",
        ],
        "Your radio transmissions are reported READABILITY THREE. This means that your transmissions are": [
            "readable with difficulty.",
            "readable now and then.",
            "readable.",
            "perfectly readable.",
        ],
    }

    return questions
