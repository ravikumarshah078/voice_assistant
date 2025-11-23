import speech_recognition as sr


def test_microphones():
    r = sr.Recognizer()
    mics = sr.Microphone.list_microphone_names()

    print(f"Found {len(mics)} microphones. Testing each for 3 seconds...")

    for index, name in enumerate(mics):
        print(f"\n--- Testing Mic {index}: {name} ---")
        try:
            with sr.Microphone(device_index=index) as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Speak now!")
                try:
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    print("Audio captured! Attempting recognition...")
                    try:
                        text = r.recognize_google(audio)
                        print(f"SUCCESS! Heard: '{text}'")
                        print(f"*** USE DEVICE INDEX {index} ***")
                        return  # Found a working one
                    except sr.UnknownValueError:
                        print(
                            "Audio captured but speech not recognized (Mic might be working but unclear)")
                    except sr.RequestError:
                        print("Connection error")
                except sr.WaitTimeoutError:
                    print("Timeout - No audio detected.")
        except Exception as e:
            print(f"Error accessing mic: {e}")


if __name__ == "__main__":
    test_microphones()
