import keyboard
import speech_recognition as sr
import tkinter as tk

# initialize speech recognition engine
r = sr.Recognizer()

# define the default keyboard keys to press for each command
key_commands = {
    "flight ready": "r",
    "engage hyperdrive": "h",
    "fire missiles": "m"
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
        text = r.recognize_google_cloud(audio) # replace with your Speech-to-Text API of choice
        print(f"You said: {text}")
        if text.lower() in key_commands:
            execute_key_press(key_commands[text.lower()])
    except sr.UnknownValueError:
        print("Sorry, I did not understand what you said.")
    except sr.RequestError as e:
        print(f"Speech-to-Text API error: {e}")

# define the function to update the key_commands dictionary when the user presses the "Save" button
def update_key_commands():
    for i in range(len(command_entries)):
        command = command_entries[i].get().lower()
        key = key_entries[i].get().lower()
        if command != "" and key != "":
            key_commands[command] = key

# create the GUI
root = tk.Tk()
root.title("Voice Recognition Program")

# create labels and entries for each command-key pair
command_entries = []
key_entries = []
for i, command in enumerate(key_commands.keys()):
    command_label = tk.Label(root, text=f"{i+1}. {command}")
    command_label.grid(row=i, column=0, padx=5, pady=5)

    command_entry = tk.Entry(root)
    command_entry.insert(0, command)
    command_entry.grid(row=i, column=1, padx=5, pady=5)
    command_entries.append(command_entry)

    key_entry = tk.Entry(root)
    key_entry.insert(0, key_commands[command])
    key_entry.grid(row=i, column=2, padx=5, pady=5)
    key_entries.append(key_entry)

# create the "Save" button to update the key_commands dictionary
save_button = tk.Button(root, text="Save", command=update_key_commands)
save_button.grid(row=len(key_commands), column=1, pady=10)

# create the "Start" button to begin voice recognition
start_button = tk.Button(root, text="Start", command=process_voice_input)
start_button.grid(row=len(key_commands), column=2, pady=10)

# start the GUI event loop
root.mainloop()
