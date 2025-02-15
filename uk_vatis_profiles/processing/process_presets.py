def process_presets(presets):
    result = []

    for preset in presets:
        single_runway_identifier = preset.get("runway_identifier")

        departure_runway_identifier = preset.get("departure_runway_identifier")
        arrival_runway_identifier = preset.get("arrival_runway_identifier")

        template = None

        single_runway_template = f"THIS IS [FACILITY] INFORMATION [ATIS_CODE] AT TIME [OBS_TIME]. RUNWAY IN USE ^{single_runway_identifier}. [TL]. [WIND]. [VIS]. [RVR]. [PRESENT_WX]. [CLOUDS]. [TEMP]. [DEW]. [PRESSURE]. [ARPT_COND]. [NOTAMS]. ACKNOWLEDGE RECEIPT OF INFORMATION [ATIS_CODE]."
        dual_runway_template = f"THIS IS [FACILITY] INFORMATION [ATIS_CODE] AT TIME [OBS_TIME]. DEPARTING RUNWAY ^{departure_runway_identifier}. ARRIVING RUNWAY ^{arrival_runway_identifier}. [TL]. [WIND]. [VIS]. [RVR]. [PRESENT_WX]. [CLOUDS]. [TEMP]. [DEW]. [PRESSURE]. [ARPT_COND]. [NOTAMS]. ACKNOWLEDGE RECEIPT OF INFORMATION [ATIS_CODE]."

        if single_runway_identifier:
            template = single_runway_template
        elif departure_runway_identifier and arrival_runway_identifier:
            template = dual_runway_template
        else:
            raise ValueError("preset is missing either runway_identifier or both departure_runway_identifier and arrival_runway_identifier")

        result.append({
            "Name": preset["name"],
            "AirportConditions": preset.get("conditions"),
            "Notams": None,
            "ArbitraryText": None,
            "Template": template
        })

    return result
