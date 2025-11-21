import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Speaks the given text."""
    engine.say(text)
    engine.runAndWait()


def listen(r, source):
    """Listens to the microphone and returns the recognized text."""
    print("Listening...")
    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        print("Recognizing...")
        # Using Google Speech Recognition (requires internet)
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return None
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("I'm having trouble connecting to the internet.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def processCommand(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    else:
        # Only speak if we are sure it was a command meant for Lyra but not understood
        # For now, we can just ignore unknown commands to avoid spamming
        pass


if __name__ == "__main__":
    r = sr.Recognizer()

    # Setup microphone once
    # Using device_index=0 as confirmed by user
    mic = sr.Microphone(device_index=0)

    with mic as source:
        # Adjust for ambient noise ONLY ONCE at startup
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 300
        r.pause_threshold = 0.8

        speak("Lyra is ready")
        print("Lyra is ready.")

        while True:
            # Pass the already open source and recognizer
            command = listen(r, source)

            if command:
                if "stop" in command or "exit" in command:
                    speak("Goodbye!")
                    break

                # Check for wake word "Lyra"
                if "lyra" in command:
                    processCommand(command)
                else:
                    # Optional: Echo back only if not a command
                    # speak(f"You said: {command}")
                    pass
