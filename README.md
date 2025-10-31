# 🖌️ AirCanvas – Draw in the Air using Hand Gestures

<p align="center">
  <img src="Header/1.jpg" alt="AirCanvas Preview" width="600">
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white"></a>
  <a href="https://opencv.org/"><img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white"></a>
  <a href="https://developers.google.com/mediapipe"><img src="https://img.shields.io/badge/MediaPipe-Live%20Tracking-orange?logo=google&logoColor=white"></a>
  <a href="https://github.com/SubhashreeProjects/AirCanvas/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow"></a>
  <a href="https://github.com/SubhashreeProjects/AirCanvas/stargazers"><img src="https://img.shields.io/github/stars/SubhashreeProjects/AirCanvas?style=social"></a>
</p>

---

### 🪄 Overview

**AirCanvas** is a fun and interactive project that lets you **draw, erase, and switch colors using hand gestures** — all through your **webcam**.  
No stylus or touchscreen needed — just your hand and some creativity! ✋🎨

---

## 🚀 Features

- 🧠 **Real-Time Hand Tracking** using MediaPipe  
- 🎨 **Virtual Drawing Canvas** controlled by finger movements  
- 🧽 **Eraser Mode** to clean up your drawing  
- 🌈 **Color Palette Selection** through gestures  
- ⚙️ **Adjustable Brush Thickness** using keyboard shortcuts  
- 🖥️ **Seamless Integration** with OpenCV video feed  

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| 🐍 **Python** | Core programming language |
| 🎥 **OpenCV** | Video capture, drawing, and processing |
| ✋ **MediaPipe** | Hand tracking framework |
| 🔢 **NumPy** | Image array manipulation |

---

## 🖼️ Demo

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/14d08ecb-a54e-4d23-a07a-4ee8d9ca8e35" />
<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/4f76c1ac-ea72-4db2-ac3e-5cf64b9a23ea" />


---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/SubhashreeProjects/AirCanvas.git
cd AirCanvas
2️⃣ Install required dependencies
bash
Copy code
pip install opencv-python mediapipe numpy
3️⃣ Run the application
bash
Copy code
python main.py
🎮 Controls
Action	Description
✋ Index + Middle Finger Up	Selection Mode (choose color or eraser)
☝️ Only Index Finger Up	Drawing Mode
🎨 Top Color Boxes	Change drawing color
⬛ Black Box	Eraser mode
🔼 Press i	Increase brush thickness
🔽 Press d	Decrease brush thickness
❌ Press q	Quit application

📁 Folder Structure
bash
Copy code
AirCanvas/
│
├── Header/                # Toolbar Images
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   └── 4.jpg
│
├── HandTrackingModule.py  # Custom module for hand tracking
├── main.py                # Main application logic
└── README.md              # Documentation
🧑‍💻 Author
👩‍💻 Subhashree Projects
📍 Developed as a Computer Vision learning project.
📧 [your-email@example.com]
🌐 GitHub Profile

💡 Future Enhancements
💾 Save your drawings as images

🎨 Add multi-color palette

🤲 Support for both hands

🔁 Gesture-based undo/redo feature

⭐ Contribute
Contributions are always welcome!

Fork this repository

Create your feature branch

Commit your changes

Push to your branch and open a Pull Request

🖤 Support
If you liked this project, please give it a ⭐ on GitHub —
it helps others find this repo and motivates me to build more creative projects!

