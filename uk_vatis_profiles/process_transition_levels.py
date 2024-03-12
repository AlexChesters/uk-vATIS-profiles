def process_transition_levels(transition_levels):
    result = []

    for entry in transition_levels:
        result.append({
            "Low": entry["low"],
            "High": entry["high"],
            "Altitude": entry["altitude"]
        })

    return result
