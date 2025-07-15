import xml.etree.ElementTree as ET
import json

def parse_flightplan_to_json(xml_path, json_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    general = root.find("general")
    aircraft = general.find("aircraft").text if general.find("aircraft") is not None else "Unknown"
    dep_icao = root.find("origin").find("icao_code").text if root.find("origin") is not None else "Unknown"
    arr_icao = root.find("destination").find("icao_code").text if root.find("destination") is not None else "Unknown"
    flight_time = general.find("times").find("est_time_enroute").text if general.find("times") is not None else "Unknown"
    cruise_level = general.find("initial_altitude").text if general.find("initial_altitude") is not None else "Unknown"

    data = {
        "aircraft": aircraft,
        "departure": dep_icao,
        "arrival": arr_icao,
        "estimated_time_enroute": flight_time,
        "cruise_level": cruise_level
    }

    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Flightplan data saved to {json_path}")

if __name__ == "__main__":
    parse_flightplan_to_json("/home/patrick/copilot/ofp.xml", "/home/patrick/copilot/flightplan.json")
