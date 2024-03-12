from uk_vatis_profiles.processing.process_presets import process_presets
from uk_vatis_profiles.processing.process_transition_levels import process_transition_levels

position_map = {
    "GMC": "GROUND"
}

def process_profile(profile):
    airfield_name = profile["name"]

    return {
        "Name": airfield_name,
        "Identifier": profile["code"],
        "Contractions": [
            {
            "String": "HPA",
            "Spoken": "HECTO-PASKALS"
            },
            {
            "String": "RNAV",
            "Spoken": "ARE-NAV"
            },
            {
            "String": "CAVOK",
            "Spoken": "CAV-OH-KAY"
            },
            {
            "String": "RNP",
            "Spoken": "ARE-ENN-PEE"
            },
            {
            "String": "WIP",
            "Spoken": "WORK-IN-PROGRESS"
            },
            {
            "String": "ILS",
            "Spoken": "EYE-ELL-ESS"
            },
            {
            "String": "ATC",
            "Spoken": "AY-TEE-SEE"
            },
            {
            "String": "DATALINK",
            "Spoken": "DATA-LINK"
            }
        ],
        "AtisFrequency": profile["atis_frequency"],
        "ObservationTime": {
            "Enabled": False,
            "Time": 0
        },
        "MagneticVariation": {
            "Enabled": False,
            "MagneticDegrees": 0
        },
        "AtisVoice": {
            "UseTextToSpeech": True,
            "Voice": "UK Female"
        },
        "IDSEndpoint": None,
        "Presets": process_presets(profile["presets"]),
        "AirportConditionDefinitions": [],
        "NotamDefinitions": [
            {
                "Ordinal": 1,
                "Text": "ATC LOW VISIBILITY PROCEDURES IN FORCE.",
                "Enabled": False
            },
            {
                "Ordinal": 2,
                "Text": "DATALINK CLEARANCES ARE AVAILABLE",
                "Enabled": False
            }
        ],
        "TransitionLevels": process_transition_levels(profile["transition_levels"]),
        "atisFormat": {
            "altimeter": {
                "pronounceDecimal": False,
                "template": {
                    "text": "QNH {altimeter} ({altimeter|text})",
                    "voice": "QNH {altimeter}"
                }
            },
            "closingStatement": {
                "autoIncludeClosingStatement": True,
                "template": {
                    "text": profile["closing_statement"],
                    "voice": profile["closing_statement"]
                }
            }
        }
    }
