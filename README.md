AI Copilot for Flight Simulation
This project delivers an innovative conversational AI interface for flight information, specifically designed for flight simulation enthusiasts. It seamlessly integrates SimBrief flight plans, allowing you to verbally ask questions about your flight and receive spoken answers from a natural-sounding voice.

Core Features
Flight Plan Parsing: Efficiently converts SimBrief XML flight plans into a structured JSON format.

Interactive Q&A: An intuitive Command-Line Interface (CLI) lets you directly query details about your flight plan.

Modular Design: The project is built with separate, easy-to-maintain scripts for parsing, conversion, and interaction.

Speech Recognition & Synthesis (Planned): Full integration with Whisper ASR (Automatic Speech Recognition) for voice input and Piper TTS (Text-to-Speech) for spoken responses is planned for hands-free operation.

Installation Guide
Follow these steps to install the AI Copilot on your Ubuntu system.

1. Clone Project & Navigate
Open your terminal and execute the following commands:

Bash

git clone https://github.com/NemesisNL/ai-copilot-flightsim.git
cd ai-copilot-flightsim
2. Install Essential Software
Ensure your system is up-to-date and install the necessary Python components:

Bash

sudo apt update
sudo apt install python3 python3-pip
3. Install Piper (Text-to-Speech)
Piper converts text into natural-sounding speech.

Clone and Compile Piper Repository:

Bash

git clone https://github.com/rhasspy/piper.git
cd piper
mkdir build && cd build
cmake ..
make -j$(nproc)
Download Piper Voice Model:
(Example: English UK Alan Medium. Create the directories within your ai-copilot-flightsim directory for better organization).

Bash

mkdir -p ~/ai-copilot-flightsim/piper/models
cd ~/ai-copilot-flightsim/piper/models
wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/alan/medium/en_GB-alan-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/alan/medium/en_GB-alan-medium.onnx.json
4. Install Whisper.cpp (Speech Recognition)
Whisper converts spoken audio into written text.

Clone and Compile Whisper.cpp Repository:

Bash

git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
cmake -B build
cmake --build build --config Release
Download Whisper Language Model:
(Example: base English model. Create the directories within your ai-copilot-flightsim directory for better organization).

Bash

mkdir -p ~/ai-copilot-flightsim/whisper.cpp/models
cd ~/ai-copilot-flightsim/whisper.cpp/models
wget https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin
5. Place Your SimBrief Flight Plan
Place your downloaded SimBrief flight plan (typically ofp.xml) into the main project directory:

Bash

mv /path/to/your/ofp.xml ~/ai-copilot-flightsim/ofp.xml
Usage Instructions
Viewing Flight Plan Data (Text Mode)
Convert your XML flight plan to JSON:

Bash

python3 flightplan_to_json.py
Start the Q&A interface:

Bash

python3 flightplan_qa.py
Ask your questions!

You can now type questions such as:

"What is my destination?"

"What is the estimated time enroute?"

"What is my cruise level?"

"What is my departure airport?"

"What is the DA(H) for runway 24 at Schiphol?"

Type exit to quit the program.

Notes & Future Developments
Current DA(H) (Decision Altitude/Height) information is limited by the data available in the SimBrief XML format.

The biggest planned future expansion is the integration of speech input and output using Whisper and Piper, enabling a fully hands-free experience. This also includes hotword detection ("Hey Copilot!").

Further plans include integration with flight simulators like Microsoft Flight Simulator (via API or local file system) and automatic updates of SimBrief/Navigraph data.

Author
Proudly made by Patrick (NemesisNL)
