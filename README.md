# 🎙️ Jarvis - Python Voice Assistant

Jarvis is a Python-based voice assistant that uses speech recognition and text-to-speech capabilities to perform a variety of actions, such as opening websites, playing music, and reading news headlines aloud.

## 🧠 Features

* 🔊 Voice activation using the keyword **"Jarvis"**
* 🌐 Opens popular websites like Google, YouTube, Facebook, and Stake
* 🎵 Plays songs from a pre-defined music library
* 📰 Fetches and reads the latest news headlines (India) using the NewsAPI
* 🎤 Uses `speech_recognition` for voice input
* 💬 Uses `pyttsx3` for speech output

## 🚀 Getting Started

### ✅ Prerequisites

Make sure Python is installed on your system, and install the following required libraries:

```bash
pip install SpeechRecognition pyttsx3 requests
```

You also need:

* **Microphone access** for voice recognition
* A valid **[NewsAPI](https://newsapi.org/)** key

### 📁 Project Structure

```
mega_project.py       # Main script for the Jarvis assistant
musiclibrary.py       # (Expected) Contains dictionary of song names and URLs
```

### 🧩 Example musiclibrary.py

Ensure you have a `musiclibrary.py` file in the same directory with content like:

```python
music = {
    "song1": "https://example.com/song1",
    "song2": "https://example.com/song2"
}
```

## 🛠️ Usage

Run the assistant using:

```bash
python mega_project.py
```

Once it starts, say **"Jarvis"** followed by a command:

Examples:

* `Jarvis open Google`
* `Jarvis play song1`
* `Jarvis news`

## 🔐 API Key

Replace the placeholder API key in `mega_project.py`:

```python
newsapi = "YOUR_NEWS_API_KEY"
```

> **Note**: Do not expose your API keys in public repositories.

## 🧩 Known Issues

* Short phrase listening time; some commands may not register clearly
* Speech recognition may vary based on background noise

## 📜 License

This project is open source and free to use for educational purposes.

---

Let me know if you want this as a downloadable `.md` file or if you'd like to enhance this assistant with more features!
