Contact Me at talhahussain1100@gmail.com 
# workfolio-hack
Workfolio Hack is a Python script that automates the setup and activation of your online portfolio. It simplifies portfolio management, allowing you to integrate, update, and customize your Workfolio with ease. Perfect for users looking to streamline their portfolio workflow with minimal effort.

How to Run Your Python Script as a Standalone Application
If you want to run your Python program as a standalone script without needing to open PyCharm every time, follow these steps. This guide outlines the process of running Python scripts directly on your system.

1. Save Your Code
Ensure your Python code is saved in a .py file (e.g., mouse_jiggler.py). You can use any text editor (Notepad, VS Code, Sublime Text, or PyCharm) to save the code.

Here's an example code that uses Python libraries like pyautogui to simulate mouse movements and key presses:

python
Copy
Edit
import pyautogui
import time
import random

# --- Configuration ---
IDLE_THRESHOLD_SECONDS = 5  # Check for idle every 5 seconds
MOVE_OFFSET_PIXELS_MAX = 10 # How many pixels to move at most
MOVE_DURATION_SECONDS = 0.1 # How long the mouse move should take
KEY_PRESS_INTERVAL_SECONDS = 30 # Press a key every 30 seconds of jiggling
LAST_KEY_PRESS_TIME = time.time()

# Non-character keys that are generally safe to press
SAFE_KEYS = ['shift', 'ctrl', 'alt'] # 'win' might open start, 'cmd' for mac
# Avoid 'scrolllock', 'numlock', 'capslock' as they can be disruptive.

def jiggle_mouse_and_keys(current_x, current_y):
    """Moves the mouse slightly and occasionally presses a key."""
    global LAST_KEY_PRESS_TIME

    # --- Mouse Jiggle ---
    offset_x = random.randint(-MOVE_OFFSET_PIXELS_MAX, MOVE_OFFSET_PIXELS_MAX)
    offset_y = random.randint(-MOVE_OFFSET_PIXELS_MAX, MOVE_OFFSET_PIXELS_MAX)

    if offset_x == 0 and offset_y == 0: # Ensure some movement
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

    # --- Sporadic Key Press ---
    if time.time() - LAST_KEY_PRESS_TIME > KEY_PRESS_INTERVAL_SECONDS:
        try:
            key_to_press = random.choice(SAFE_KEYS)
            print(f"    Pressing '{key_to_press}' key.")
            pyautogui.press(key_to_press)
            LAST_KEY_PRESS_TIME = time.time()
        except Exception as e:
            print(f"    Could not press key '{key_to_press}': {e}")
            LAST_KEY_PRESS_TIME = time.time() # Still update time to avoid rapid retries

def main():
    print(f"Mouse Jiggler started. Press Ctrl+C in the console to stop.")
    print(f"Checking for idle every {IDLE_THRESHOLD_SECONDS} seconds.")
    print(f"Moving mouse by up to {MOVE_OFFSET_PIXELS_MAX} pixels if idle.")
    print(f"Pressing a harmless key approx. every {KEY_PRESS_INTERVAL_SECONDS} seconds of jiggling.\n")

    last_pos = pyautogui.position()
    global LAST_KEY_PRESS_TIME
    LAST_KEY_PRESS_TIME = time.time() # Initialize

    try:
        while True:
            time.sleep(IDLE_THRESHOLD_SECONDS)
            current_pos = pyautogui.position()

            if current_pos == last_pos:
                print(f"Mouse has been idle for {IDLE_THRESHOLD_SECONDS} seconds at {current_pos}.")
                jiggle_mouse_and_keys(current_pos.x, current_pos.y)
                last_pos = pyautogui.position() # Update last_pos to the jiggled position
            else:
                print(f"Mouse moved by user to {current_pos}. Resetting idle timer.")
                last_pos = current_pos

    except KeyboardInterrupt:
        print("\nMouse Jiggler stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("Starting in 3 seconds... (switch to target window if needed)")
    time.sleep(3)
    main()
2. Ensure Python is Installed and in PATH
Make sure Python is installed and accessible on your Windows 11 machine. To check:

Open Command Prompt (cmd).

Type the following command:

bash
Copy
Edit
python --version
If you see a version (e.g., Python 3.9.7), you're good to go. Otherwise, you need to install Python from python.org, ensuring that you check the box "Add Python to PATH" during installation.

3. Install Required Libraries
Your script uses the pyautogui library. If you only installed it in PyCharm’s virtual environment, make sure it's installed globally or in the active environment.

To install pyautogui, open Command Prompt (or PowerShell) and run:

bash
Copy
Edit
pip install pyautogui
The time and random libraries are built-in, so no installation is required.

4. Run the Script from Command Prompt/PowerShell
To run your script, follow these steps:

Open Command Prompt (or PowerShell).

Navigate to the directory where your .py file is saved. For example:

bash
Copy
Edit
cd C:\Users\YourUserName\Desktop\MyScripts
Run the script using:

bash
Copy
Edit
python mouse_jiggler_enhanced.py
Your script will run in the Command Prompt window, and you'll see its output there. To stop it, click into the Command Prompt window and press Ctrl+C.

5. (Optional) Run Without a Visible Console Window
If you want the script to run in the background without showing a console window, use pythonw.exe:

Open Command Prompt or PowerShell.

Navigate to your script's directory.

Run it with pythonw.exe:

bash
Copy
Edit
pythonw.exe mouse_jiggler_enhanced.py
Note: If you use pythonw.exe, you won’t see any print output. To stop the script, you’ll need to open Task Manager, locate pythonw.exe, and end the task.

6. Running as Administrator (If Needed)
If your script needs to interact with applications running with administrator privileges (like Task Manager or Workfolio), run the script as administrator:

Search for "Command Prompt" or "PowerShell" in the Start Menu.

Right-click it and select Run as administrator.

In the administrator console, navigate to your script's directory and run:

bash
Copy
Edit
python your_script_name.py
By following these steps, you can run your Python script as a standalone application without needing to open PyCharm each time.
