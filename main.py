import tkinter as tk
import keyboard
from tkinter import ttk
import time
import threading


afk = False
simulation_thread = None

def toggle_afk():
    global afk, simulation_thread
    if afk:
        afk = False
        if simulation_thread:
            simulation_thread.stop()
        update_ui()
    else:
        afk = True
        simulation_thread = SimulationThread()
        simulation_thread.start()
        update_ui()

class SimulationThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            hold_and_release_key('w', 0.1)
            time.sleep(1)
            hold_and_release_key('a', 0.1)
            time.sleep(1)
            hold_and_release_key('s', 0.1)
            time.sleep(1)
            hold_and_release_key('d', 0.1)
            time.sleep(1)

    def stop(self):
        self._stop_event.set()

def hold_and_release_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def update_ui():
    if afk:
        status_var.set("You are AFK now.")
        button.config(text="I'm back", command=toggle_afk)
    else:
        status_var.set("Press the button to go AFK or press F6")
        button.config(text="Go AFK", command=toggle_afk)

def toggle_afk_with_f6(event):
    toggle_afk()

root = tk.Tk()
root.title("Anti AFK")
root.geometry("400x200+100+100")
root.resizable(False, False)
root.attributes("-topmost", True)

# Create a StringVar to hold the status text
status_var = tk.StringVar()
status_var.set("Press the button to go AFK or press F6")

# Create and style the label using the StringVar
label = tk.Label(root, textvariable=status_var, font=("Helvetica", 14), bg="lightgray")
label.pack(pady=20)

# Create and style the button
button = ttk.Button(root, text="Go AFK", command=toggle_afk, style="TButton")
button.pack()

# Register the F6 key press event
keyboard.on_press_key("F6", toggle_afk_with_f6)

root.mainloop()
