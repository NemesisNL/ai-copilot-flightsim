# 🧠 AI Copilot for Flight Simulation

**AI Copilot for Flight Sim** is a local voice-enabled assistant built for Microsoft Flight Simulator enthusiasts.  
It integrates SimBrief flight plans and allows you to interactively ask questions about your flight — via keyboard or voice — and get natural speech responses using [Whisper](https://github.com/ggerganov/whisper.cpp) and [Piper](https://github.com/rhasspy/piper).

---

## ✨ Features

- 🛫 **SimBrief Flight Plan Parsing**  
  Reads and converts your SimBrief OFP (XML) into structured JSON format.

- 💬 **Command-Line Flight Plan Q&A**  
  Ask questions like “What is my cruise level?” or “What’s the destination?” — and get instant answers.

- 🗣️ **(Planned) Full Voice Interface**  
  Whisper for automatic speech recognition (ASR) + Piper for text-to-speech replies in natural voices.

- 🧩 **Modular Python Scripts**  
  Clean and separate modules: flightplan parsing, Q&A, conversion and voice interaction (soon).

---

## 🧰 Installation Guide

Tested on **Ubuntu 22.04+**  
Make sure you have Python 3 and build tools installed.

### 1. Clone This Repository

```bash
git clone https://github.com/NemesisNL/ai-copilot-flightsim.git
cd ai-copilot-flightsim
```

### 2. Install Required Software

```bash
sudo apt update
sudo apt install python3 python3-pip git cmake build-essential
```

### 3. Install and Compile [Piper (TTS)](https://github.com/rhasspy/piper)

```bash
git clone https://github.com/rhasspy/piper.git
cd piper
mkdir build && cd build
cmake ..
make -j$(nproc)
cd ../..
```

> 📁 Place your downloaded Piper voice model in `piper/models/`  
> For example: `en_GB-alan-medium.onnx`

---

## 🚀 Usage

### Step 1: Convert SimBrief XML to JSON

Place your `ofp.xml` (SimBrief) in the root of the project.  
Then run:

```bash
python3 scripts/flightplan_copilot.py
```

It will generate `ofp.json` and allow you to ask questions interactively.

Example questions:

- What is my destination?
- What is my estimated time enroute?
- What aircraft am I flying?
- What is the DA(H)?

### Step 2 (Coming Soon): Full Voice Interaction 🎙️

A separate script will handle:

- Wake word detection (e.g. “Copilot”)
- Automatic speech recognition with Whisper
- Natural spoken response using Piper

---

## 📁 Folder Structure

```bash
.
├── scripts/
│   ├── flightplan_copilot.py        # Full parser + Q&A CLI
│   ├── flightplan_to_json.py        # SimBrief OFP XML to JSON converter
│   ├── flightplan_qa.py             # CLI Q&A based on parsed JSON
│   ├── parse_flightplan.py          # Simple print-only test parser
├── piper/                           # Piper cloned repo
│   └── models/                      # Place your voice .onnx file here
├── ofp.xml                          # Your latest SimBrief flight plan
├── ofp.json                         # Auto-generated JSON version
└── README.md
```

---

## 🤖 Tech Stack

- 🐍 Python 3
- 📄 XML / JSON
- 🗣️ Whisper (voice input, CLI only for now)
- 🔊 Piper (offline speech synthesis)

---

## 📌 TODO

- [ ] Add hotword detection (e.g. with `Porcupine` or `openWakeWord`)
- [ ] Add Whisper speech input integration
- [ ] Connect Whisper + Piper + JSON in one `copilot.py`
- [ ] GUI version (Kivy or Electron later?)

---

## 🙌 Credits

- SimBrief: [https://www.simbrief.com](https://www.simbrief.com)  
- Whisper ASR: [ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp)  
- Piper TTS: [rhasspy/piper](https://github.com/rhasspy/piper)

---

## 📜 License

This project is open-source under the **MIT License**.  
Use it, modify it, and fly safe! ✈️

---

> Built by [NemesisNL](https://github.com/NemesisNL) to enhance the immersion of virtual flying.  
> Contributions and feedback are welcome!
>>>>>>> 896b140 (Update README with full project description)
