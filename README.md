# 🎸 StrumSense

> ### Because Great Guitar Playing Isn't Just Heard — It's Seen.

🏆 **Build with Bharat 2.0 | National Hackathon Submission | NIT Delhi**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Google-orange?style=for-the-badge)
![Librosa](https://img.shields.io/badge/Librosa-Audio%20DSP-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)

---

# 📖 Overview

StrumSense is an AI-powered hybrid audio-visual guitar learning assistant that helps beginners improve their strumming technique by combining Computer Vision and Audio Signal Processing.

Unlike traditional guitar learning applications that only analyze audio, StrumSense simultaneously understands:

- 🎵 Which chord is being played
- 👋 How the chord is being strummed

By combining both inputs in real time, StrumSense provides intelligent feedback on rhythm and strumming accuracy.

---

# 🚨 Problem Statement

Millions of self-taught guitarists learn through YouTube videos and online tutorials without receiving real-time feedback.

Most existing applications focus only on detecting notes or chords from audio.

They fail to understand the player's right-hand movement, making it impossible to identify incorrect upstrokes, downstrokes, or rhythm mistakes.

As a result, beginners often develop poor strumming habits that become difficult to correct later.

---

# 💡 Our Solution

StrumSense introduces a Hybrid AI Pipeline that combines:

- Computer Vision
- Audio Signal Processing

to analyze both the guitar sound and the player's strumming motion simultaneously.

The system detects:

- Chord being played
- Upstroke / Downstroke
- Timing alignment
- Real-time feedback

Instead of only listening to the guitar,

**StrumSense can both hear and see the performance.**

---

# ⭐ Key Features

- 🎵 Real-time chord detection
- 👋 Upstroke & Downstroke recognition
- 🎥 MediaPipe Pose wrist tracking
- 🎧 Chroma-CQT based audio analysis
- 🔄 Audio-Video timestamp synchronization
- 📊 Live feedback dashboard
- ⚡ Low-latency processing
- 🎸 Beginner-friendly interface

---

# 🏗 System Architecture

```
Camera
   │
   ▼
MediaPipe Pose
   │
Right Wrist Tracking
   │
Strum Detection
   │
──────────────┐
              │
              ▼
      Fusion Engine
              ▲
──────────────┘
   │
Microphone
   │
Librosa Chroma
   │
Chord Detection
   │
   ▼

Real-Time Feedback Dashboard
```

---

# ⚙️ Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Live Streaming | streamlit-webrtc |
| Computer Vision | OpenCV |
| Pose Estimation | MediaPipe Pose |
| Audio Processing | Librosa |
| Numerical Computing | NumPy |
| Audio Capture | SoundDevice |
| Language | Python |

---

# 📂 Project Structure

```text
StrumSense/

├── app.py
├── requirements.txt
├── README.md

├── audio/
├── vision/
├── fusion/
├── frontend/
├── utils/
├── config/
├── docs/
├── tests/
├── models/
└── assets/
```

---

# 🚀 MVP Scope

The first prototype will support:

✅ Live Camera

✅ Live Microphone

✅ Open Chord Detection

- C
- G
- D
- Em

✅ Strumming Direction

- Upstroke
- Downstroke

✅ Live Dashboard

---

# 🔮 Future Scope

- Full chord vocabulary
- Finger placement analysis
- Rhythm scoring
- Tempo analysis
- AI Practice Coach
- Session Recording
- Performance Analytics
- Mobile Application

---

# 📌 Current Status

| Module | Status |
|---------|--------|
| Documentation | ✅ Completed |
| Repository Setup | ✅ Completed |
| Project Structure | ✅ Completed |
| Vision Module | 🚧 In Progress |
| Audio Module | 🚧 In Progress |
| Fusion Engine | 🚧 In Progress |
| Dashboard | 🚧 In Progress |

---

# 🛠 Installation

```bash
git clone https://github.com/amansinghrajput-asr/StrumSense.git

cd StrumSense

pip install -r requirements.txt

streamlit run app.py
```

---

# 📜 License

This project is licensed under the MIT License.

---

> **Existing apps hear your guitar. StrumSense hears and sees it.**