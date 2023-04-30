import keyboard
import speech_recognition as sr

# initialize speech recognition engine
r = sr.Recognizer()

# define the keyboard keys to press for each voice command
keys_to_press = {
    "flight ready": "r",
    "launch": "l",
    "boost": "b"
}

# define the function to execute the key press
def execute_key_press(key):
    keyboard.press(key)
    keyboard.release(key)

# define the function to capture and process voice input
def process_voice_input():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_sphinx(audio) # replace with your Speech-to-Text API of choice
        print(f"You said: {text}")
        for voice_command, key_to_press in keys_to_press.items():
            if text.lower() == voice_command:
                execute_key_press(key_to_press)
    except sr.UnknownValueError:
        print("Sorry, I did not understand what you said.")
    except sr.RequestError as e:
        print(f"Speech-to-Text API error: {e}")

# run the program indefinitely to capture and process voice input
while True:
    process_voice_input()