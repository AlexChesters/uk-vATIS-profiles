def process_presets(presets):
    result = []

    for preset in presets:
        runway_identifier = preset["runway_identifier"]

        result.append({
            "Name": preset["name"],
            "AirportConditions": preset.get("conditions"),
            "Notams": None,
            "ArbitraryText": None,
            "Template": f"THIS IS [FACILITY] INFORMATION [ATIS_CODE] AT TIME [OBS_TIME]. RUNWAY IN USE {runway_identifier}. [TL]. [WIND]. [VIS]. [RVR]. [PRESENT_WX]. [CLOUDS]. [TEMP]. [DEW]. [PRESSURE]. [ARPT_COND]. [NOTAMS]. ACKNOWLEDGE RECEIPT OF INFORMATION [ATIS_CODE]."
        })

    return result
