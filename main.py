from gemini_client import get_gemini_response
import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """
    Speaks the given text, ensuring the engine is stopped for reliability.
    This function BLOCKS until the speech is complete.
    """
    try:
        # 1. Stop any currently running speech for a clean start
        engine.stop()

        # 2. Queue the new text
        engine.say(text)

        # 3. BLOCKS the program until the speech is done.
        engine.runAndWait()

    except Exception as e:
        print(f"Error in speak: {e}")


def listen(r, source):
    """Listens to the microphone and returns the recognized text."""
    print("Listening...")
    try:
        # Increased limit slightly
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
        print("Recognizing...")
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
    """Processes the recognized command."""

    # --- Web Browser Commands ---
    if "open google" in command:
        speak("Opening Google")
        # webbrowser.open() runs immediately after speak() blocks and finishes
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    # --- General Gemini Query ---
    else:
        # Send general queries to Gemini
        query = command.replace("lyra", "").strip()
        print(f"Sending to Gemini: {query}")

        # 1. Speak the pre-response (BLOCKS the program until done)
        speak("Let me ask Gemini.")

        # 2. Make the blocking API call (runs immediately after speech finishes)
        response = get_gemini_response(query)
        print(f"Gemini response: {response}")

        # 3. Speak the final response (BLOCKS the program until done)
        if response:
            speak(response)
        else:
            speak("I couldn't get a response.")


if __name__ == "__main__":
    r = sr.Recognizer()

    # Setup microphone once
    mic = sr.Microphone(device_index=0)

    with mic as source:
        print("Adjusting for ambient noise... Please wait.")
        # Increased duration slightly
        r.adjust_for_ambient_noise(source, duration=1.5)
        r.energy_threshold = 300
        r.pause_threshold = 0.8

        speak("Lyra is ready")
        print("Lyra is ready.")

        while True:
            command = listen(r, source)

            if command:
                if "stop" in command or "exit" in command:
                    speak("Goodbye!")
                    break

                if "lyra" in command:
                    processCommand(command)
                else:
                    pass
