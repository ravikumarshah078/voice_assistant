# Lyra - Voice Assistant

A simple voice assistant project built with Python. This project is a practice exercise to understand how voice assistants work, utilizing text-to-speech and speech recognition libraries.

## Project Goal
To create a basic voice assistant that can perform simple tasks and interact with the user via voice commands.

## Features
- **Text-to-Speech**: Converts text into spoken words using `pyttsx3`.
- **Speech Recognition**: (Planned) Will listen to user commands.

## Prerequisites
- Python 3.x installed
- Virtual environment set up

## Setup & Installation

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Activate the virtual environment**:
    ```powershell
    .\.venv\Scripts\activate
    ```

3.  **Install dependencies**:
    If you have a `requirements.txt` file:
    ```powershell
    pip install -r requirements.txt
    ```
    
    Otherwise, install the necessary packages manually:
    ```powershell
    pip install pyttsx3 pypiwin32 comtypes
    ```

## Usage

1.  Ensure your virtual environment is active.
2.  Run the main script:
    ```powershell
    python main.py
    ```

## Future Improvements
- Add speech recognition (using `speech_recognition` library).
- Implement command processing (e.g., "What is the time?", "Open Google").
- Improve voice configuration (rate, volume, voice type).