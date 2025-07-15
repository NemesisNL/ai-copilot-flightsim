# ai-copilot-flightsim
Local AI Copilot for flight simulator using Whisper and Piper

# ai-copilot-flightsim

**Local AI Copilot for flight simulator using Whisper and Piper**

---

## What is this?

This project is a local AI copilot designed for flight simulators. It uses speech recognition with Whisper, parses flight plans from SimBrief XML files, and provides spoken answers via the Piper text-to-speech engine.

You can ask questions about your flight plan, such as "What is my destination?" and the system will respond via speech (future versions will be fully voice-controlled).

---

## Features

- Parsing SimBrief flight plan XML files
- Converting flight plan data into JSON for quick access
- Command-line interactive Q&A about flight data
- Basic integration with Piper text-to-speech (speech output)
- Preparation for a voice-controlled copilot workflow with Whisper and Piper

---

## Installation

### Requirements

- Linux system (Ubuntu/Debian recommended)
- Python 3.12 or higher
- Pip3
- Espeak-ng and associated development libraries
- Compiled Whisper (whisper.cpp) and Piper binaries ready

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/NemesisNL/ai-copilot-flightsim.git
   cd ai-copilot-flightsim
Install required packages:

bash
Copy
sudo apt update
sudo apt install python3 python3-pip espeak-ng libespeak-ng-dev
Download and install Whisper and Piper:

Follow instructions in the /scripts directory or documentation

Make sure to download the Whisper and Piper models and place them in the correct folders

Place your SimBrief XML flight plan in the /flightplans directory (or another folder you prefer)

Parse the flight plan to JSON:

bash
Copy
python3 scripts/parse_flightplan.py
Start the Q&A session:

bash
Copy
python3 scripts/flightplan_qa.py
Usage
Keep your SimBrief flight plan XML file updated.

Run the parser script to generate JSON data.

Launch the interactive Q&A script to ask questions about your flight such as departure, destination, estimated time enroute, cruise level, and DA(H).

Future versions will enable fully voice-controlled interaction using your microphone and Piper for spoken answers.

Example Questions
What is my destination?

What is my departure airport?

How long is my flight?

What is my cruise level?

What is the DA(H) for runway 24?

Future Enhancements
Full integration of speech recognition (Whisper) and speech output (Piper)

Integration with Microsoft Flight Simulator for live flight data

Improved natural language processing and context-aware answers

Adding METAR/TAF and weather information retrieval

Automatic flight plan updates through API

Repository Structure
graphql
Copy
ai-copilot-flightsim/
│
├── scripts/
│   ├── parse_flightplan.py          # Parser for SimBrief XML to JSON and console output
│   ├── flightplan_qa.py             # Q&A script for flight plan data
│   ├── additional scripts for speech integration (work in progress)
│
├── README.md                       # This file
├── .gitignore                     # Git ignore list
├── models/                        # Place Whisper and Piper models here
├── flightplans/                   # Place your SimBrief XML files here
Contact & Contributions
Contributions, bug reports, and feature requests are welcome via GitHub issues or pull requests.

Happy flying & coding! ✈️🤖
