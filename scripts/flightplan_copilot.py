import xml.etree.ElementTree as ET
import json
import os

def parse_flightplan(xml_path):
    """Parse het SimBrief XML vluchtplan en haalt relevante data eruit."""
    if not os.path.isfile(xml_path):
        raise FileNotFoundError(f"XML-bestand niet gevonden: {xml_path}")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    general = root.find("general")
    aircraft = root.find("aircraft")
    origin = root.find("origin")
    destination = root.find("destination")
    times = general.find("times") if general is not None else None

    # Haal data op met fallback naar 'Unknown'
    aircraft_name = aircraft.find("name").text if aircraft is not None and aircraft.find("name") is not None else "Unknown"
    dep_icao = origin.find("icao_code").text if origin is not None and origin.find("icao_code") is not None else "Unknown"
    arr_icao = destination.find("icao_code").text if destination is not None and destination.find("icao_code") is not None else "Unknown"
    flight_time = times.find("est_time_enroute").text if times is not None and times.find("est_time_enroute") is not None else "Unknown"
    cruise_level = general.find("initial_altitude").text if general is not None and general.find("initial_altitude") is not None else "Unknown"

    # DA(H) zoeken in text sectie (simpele scan)
    dah = "Unknown"
    text_section = root.find("text")
    if text_section is not None:
        for elem in text_section.iter():
            if elem.text and "DA(H)" in elem.text:
                dah = elem.text.strip()
                break

    data = {
        "aircraft": aircraft_name,
        "departure": dep_icao,
        "arrival": arr_icao,
        "estimated_time_enroute": flight_time,
        "cruise_level": cruise_level,
        "decision_altitude_height": dah
    }

    return data

def save_to_json(data, json_path):
    """Sla parsed vluchtplan data op als JSON."""
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Flightplan data saved to {json_path}")

def answer_question(data, question):
    """Beantwoord vluchtplan gerelateerde vragen."""
    question = question.lower()
    if "destination" in question or "arrival" in question:
        return f"The destination airport is {data.get('arrival', 'Unknown')}."
    elif "departure" in question or "origin" in question:
        return f"The departure airport is {data.get('departure', 'Unknown')}."
    elif "aircraft" in question:
        return f"The aircraft type is {data.get('aircraft', 'Unknown')}."
    elif "cruise level" in question or "altitude" in question:
        return f"The cruise level is {data.get('cruise_level', 'Unknown')} feet."
    elif "estimated time" in question or "eta" in question or "enroute" in question:
        eta = data.get('estimated_time_enroute', 'Unknown')
        if eta != "Unknown":
            return f"The estimated time enroute is {eta} seconds."
        else:
            return "The estimated time enroute is unknown."
    elif "da(h)" in question or "decision altitude" in question:
        dah = data.get("decision_altitude_height", "Unknown")
        if dah == "Unknown":
            return "Decision altitude (DA(H)) info is not available in the flight plan."
        else:
            return f"Decision Altitude/Height info: {dah}"
    else:
        return "Sorry, I don't have an answer for that. Try asking about destination, departure, ETA, aircraft, cruise level, or DA(H)."

def interactive_loop(data):
    """Start een interactieve Q&A sessie voor vluchtplan vragen."""
    print("Ask me about your flight plan (or type 'exit' to quit):")
    while True:
        question = input("> ").strip()
        if question.lower() in ("exit", "quit", "stop"):
            print("Goodbye!")
            break
        answer = answer_question(data, question)
        print(answer)

if __name__ == "__main__":
    XML_PATH = "/home/patrick/copilot/ofp.xml"  # Pas aan naar jouw XML-bestand
    JSON_PATH = "/home/patrick/copilot/ofp.json"  # Optioneel, als je JSON wilt opslaan

    try:
        flightplan_data = parse_flightplan(XML_PATH)
        save_to_json(flightplan_data, JSON_PATH)  # Opslaan als JSON, kan je weghalen als je dat niet wil
        interactive_loop(flightplan_data)
    except Exception as e:
        print(f"Fout bij verwerken vluchtplan: {e}")
