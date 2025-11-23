import speech_recognition as sr


def list_microphones():
    print("Available Microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(
            f"Microphone with name \"{name}\" found for `Microphone(device_index={index})`")


if __name__ == "__main__":
    list_microphones()
