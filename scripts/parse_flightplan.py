import xml.etree.ElementTree as ET

def parse_flightplan(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Vind de tags die we nodig hebben
    general = root.find("general")
    aircraft = root.find("aircraft")
    origin = root.find("origin")
    destination = root.find("destination")
    times = root.find("times")

    # Haal tekst uit elementen, met fallback als ze niet bestaan
    aircraft_name = aircraft.find("name").text if aircraft is not None else "Unknown"
    dep_icao = origin.find("icao_code").text if origin is not None else "Unknown"
    arr_icao = destination.find("icao_code").text if destination is not None else "Unknown"
    flight_time = times.find("est_time_enroute").text if times is not None else "Unknown"
    cruise_level = general.find("initial_altitude").text if general is not None else "Unknown"

    print("✈️  Aircraft:", aircraft_name)
    print("🛫 Departure:", dep_icao)
    print("🛬 Arrival:", arr_icao)
    print("⏱ Estimated Time Enroute:", flight_time)
    print("☀️ Cruise Level:", cruise_level)

if __name__ == "__main__":
    parse_flightplan("/home/patrick/copilot/ofp.xml")
