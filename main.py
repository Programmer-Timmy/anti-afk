import tkinter as tk
import keyboard
import time

afk = False
key_simulation_enabled = False

def toggle_afk():
    global afk, key_simulation_enabled
    if afk:
        afk = False
        key_simulation_enabled = False  # Disable key simulation
    else:
        afk = True
        key_simulation_enabled = True  # Enable key simulation
    update_ui()

def hold_and_release_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def simulate_keypress():
    if afk and key_simulation_enabled:
        hold_and_release_key('w', 0.1)
        time.sleep(1)
        hold_and_release_key('a', 0.1)
        time.sleep(1)
        hold_and_release_key('s', 0.1)
        time.sleep(1)
        hold_and_release_key('d', 0.1)
        time.sleep(1)
        if key_simulation_enabled:  # Check if key simulation should continue
            label.after(100, simulate_keypress)

def update_ui():
    if afk:
        label.config(text="You are AFK now.")
        button.config(text="I'm back")
        simulate_keypress()
    else:
        label.config(text="Press the button to go AFK. Or press F6")
        button.config(text="Go AFK")
def toggle_afk_with_f6(event):
    toggle_afk()

root = tk.Tk()
root.title("Anti AFK")
root.geometry("400x200+100+100")
root.resizable(False, False)
root.attributes("-topmost", True)

label = tk.Label(root, text="Press the button to go AFK")
label.pack()

button = tk.Button(root, text="Go AFK", command=toggle_afk)
button.pack()

keyboard.on_press_key("F6", toggle_afk_with_f6)

root.mainloop()