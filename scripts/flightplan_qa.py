import json

def load_flightplan(json_path):
    with open(json_path) as f:
        return json.load(f)

def answer_question(flightplan, question):
    question = question.lower()
    if "destination" in question or "arrival" in question:
        return f"The destination airport is {flightplan['arrival']}."
    elif "departure" in question:
        return f"The departure airport is {flightplan['departure']}."
    elif "aircraft" in question:
        return f"The aircraft type is {flightplan['aircraft']}."
    elif "cruise level" in question or "altitude" in question:
        return f"The cruise altitude is {flightplan['cruise_level']} feet."
    elif "estimated time" in question or "enroute" in question:
        return f"The estimated time enroute is {flightplan['estimated_time_enroute']} seconds."
    elif "da(h)" in question and "runway" in question:
        return "DA(H) info is not yet available."
    else:
        return "Sorry, I don't have an answer for that question yet."

if __name__ == "__main__":
    flightplan = load_flightplan("/home/patrick/copilot/flightplan.json")
    while True:
        q = input("Ask me about your flight plan (or type 'exit'): ")
        if q.lower() == "exit":
            break
        print(answer_question(flightplan, q))
