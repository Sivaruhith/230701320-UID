import speech_recognition as sr
import os

def rename_file_from_voice_command(command):
    try:
        words = command.lower().split(" ")
        if "rename" in words and "to" in words:
            rename_index = words.index("rename")
            to_index = words.index("to")

            # Extract old and new filenames
            old_name = words[rename_index + 1]
            new_name = words[to_index + 1]

            # Check if file exists
            if not os.path.exists(old_name):
                print(f"Error: File '{old_name}' not found.")
                return

            # Rename file
            os.rename(old_name, new_name)
            print(f"✅ File renamed from '{old_name}' to '{new_name}'")

        else:
            print("Invalid command format. Say: 'Rename oldfile.txt to newfile.txt'")

    except Exception as e:
        print(f"Error: {e}")

def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Listening for command to rename a file...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🎙 Command received: {command}")
        rename_file_from_voice_command(command)
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand the command.")
    except sr.RequestError as e:
        print(f"⚠ Could not request results from Google Speech Recognition service; {e}")

if _name_ == "_main_":
    listen_for_command()
