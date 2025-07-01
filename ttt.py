import pyautogui
import time
import random

# --- Configuration ---
IDLE_THRESHOLD_SECONDS = 5
MOVE_OFFSET_PIXELS_MAX = 10
MOVE_DURATION_SECONDS = 0.1
KEY_PRESS_INTERVAL_SECONDS = 30 # Press a key every 30 seconds of jiggling
LAST_KEY_PRESS_TIME = time.time()

# Non-character keys that are generally safe to press
# 'scrolllock', 'numlock', 'capslock' can be disruptive.
# 'shift', 'ctrl', 'alt' are generally safe.
SAFE_KEYS = ['shift', 'ctrl', 'alt', 'cmd'] # 'cmd' for mac, 'win' for windows

def jiggle_mouse(current_x, current_y):
    global LAST_KEY_PRESS_TIME # Declare global to modify it
    # (Mouse jiggling code from your previous script...)
    offset_x = random.randint(-MOVE_OFFSET_PIXELS_MAX, MOVE_OFFSET_PIXELS_MAX)
    offset_y = random.randint(-MOVE_OFFSET_PIXELS_MAX, MOVE_OFFSET_PIXELS_MAX)
    if offset_x == 0 and offset_y == 0:
        if random.choice([True, False]):
            offset_x = random.choice([-1, 1]) * random.randint(1, MOVE_OFFSET_PIXELS_MAX)
        else:
            offset_y = random.choice([-1, 1]) * random.randint(1, MOVE_OFFSET_PIXELS_MAX)
    new_x = current_x + offset_x
    new_y = current_y + offset_y
    screen_width, screen_height = pyautogui.size()
    new_x = max(0, min(new_x, screen_width - 1))
    new_y = max(0, min(new_y, screen_height - 1))
    print(f"    Jiggling mouse to: ({new_x}, {new_y})")
    pyautogui.moveTo(new_x, new_y, duration=MOVE_DURATION_SECONDS)

    # --- Add sporadic key press ---
    if time.time() - LAST_KEY_PRESS_TIME > KEY_PRESS_INTERVAL_SECONDS:
        key_to_press = random.choice(SAFE_KEYS)
        print(f"    Pressing '{key_to_press}' key.")
        pyautogui.press(key_to_press)
        LAST_KEY_PRESS_TIME = time.time()


def main():
    # (Main function code from your previous script, ensure LAST_KEY_PRESS_TIME is initialized if needed outside jiggle_mouse)
    print(f"Mouse Jiggler started. Press Ctrl+C to stop.")
    print(f"Checking for idle every {IDLE_THRESHOLD_SECONDS} seconds.")
    print(f"Moving mouse by up to {MOVE_OFFSET_PIXELS_MAX} pixels if idle.")
    print(f"Pressing a harmless key every {KEY_PRESS_INTERVAL_SECONDS} seconds of jiggling.\n")

    last_pos = pyautogui.position()
    global LAST_KEY_PRESS_TIME # Initialize it before the loop if used in main logic
    LAST_KEY_PRESS_TIME = time.time()


    try:
        while True:
            time.sleep(IDLE_THRESHOLD_SECONDS)
            current_pos = pyautogui.position()
            if current_pos == last_pos:
                print(f"Mouse has been idle for {IDLE_THRESHOLD_SECONDS} seconds at {current_pos}.")
                jiggle_mouse(current_pos.x, current_pos.y)
                last_pos = pyautogui.position()
            else:
                print(f"Mouse moved by user to {current_pos}. Resetting idle timer.")
                last_pos = current_pos

    except KeyboardInterrupt:
        print("\nMouse Jiggler stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("Starting in 3 seconds...")
    time.sleep(3)
    main()