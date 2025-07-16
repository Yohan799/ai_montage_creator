# 🎬 AI Montage Creator

An AI-powered web application that takes a collection of images and a descriptive text prompt, then automatically:
- Ranks the best-fitting images
- Generates AI captions for each image
- Selects mood-matching music
- Creates a cinematic video montage with transitions and audio

Built with **Flask**, **HTML/CSS/JS**, **CLIP**, **BLIP**, **MoviePy**, and **FFmpeg**.

---

## 🚀 Features
- 🖼️ Upload multiple images
- 🧠 Enter a prompt like: "sunset on the beach with friends, nostalgic and peaceful"
- 🏆 AI ranks images that best match your prompt
- 💬 Generates AI captions per image
- 🎵 Adds mood-based royalty-free music
- 🎥 Outputs a downloadable video montage (MP4)

---

## 🗂️ Project Structure
```
ai_montage_creator/
├── app.py
├── requirements.txt
├── static/
│   ├── music/               # Pre-downloaded mood-based mp3s
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── utils/
│   ├── image_ranker.py      # Uses CLIP
│   ├── caption_generator.py # Uses BLIP
│   ├── music_selector.py    # Matches music to mood
│   └── video_creator.py     # Uses MoviePy + FFmpeg
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repo & Navigate
```bash
git clone https://github.com/your-username/ai-montage-creator.git
cd ai_montage_creator
```

### 2. (Optional) Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install transformers timm
```

### 4. Install FFmpeg (Required for video output)
- Windows: https://www.gyan.dev/ffmpeg/builds/
- macOS: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

### 5. Run the App
```bash
python app.py
```

Open in browser: `http://127.0.0.1:5000`

---

## 🧪 How to Use
1. Upload 3–5 images (JPG/PNG)
2. Enter a natural language prompt (e.g. "romantic dinner by candlelight, peaceful and intimate")
3. Click **Generate Montage**
4. Wait ~15 seconds
5. Preview and download your MP4 video

---

## 🎵 Music Licensing
All background music is sourced from **Pixabay Music** (royalty-free, no attribution needed).

Place MP3 files in:
```
static/music/
```
And name them:
- `relaxed1.mp3`, `happy1.mp3`, `nostalgic1.mp3`, etc.

---

## 🛠️ Built With
- Flask
- HuggingFace Transformers (CLIP, BLIP)
- MoviePy
- FFmpeg
- HTML/CSS/JS

---

## 📦 Future Features
- Voice narration of captions
- Drag & drop interface
- Reordering image sequence
- User music preview and selection
- Deployment to Render/Streamlit Cloud

---

## 👨‍💻 Author
[Yohan G.](https://github.com/your-profile)

---

## 📄 License
MIT License. Free to use, modify, and distribute.

