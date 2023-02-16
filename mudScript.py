import pyautogui
from pynput.keyboard import *

running = True
paused = True
toggle = 'x'
delay = 0.5


def setup() -> bool:
    global toggle, delay
    userinput = pyautogui.confirm("Welcome to mudScript!\n"
                                  "Default Delay: " + str(delay) + " seconds\n"
                                  "Default Key to toggle the script: " + toggle + "\n"
                                  "Key to stop the script: esc\n"
                                  "Would you like to customize the settings?",
                                  title="mudScript", buttons=['Yes', 'No', 'Exit'])
    if userinput == 'Yes':
        return True
    elif userinput == 'No':
        return False
    else:
        exit()


def setdelay():
    # Sets the delay between left & right click
    global delay
    userDelay = pyautogui.prompt("Please enter your custom delay between left & right click in seconds (e.g. 0.8)\n"
                                 "The default value is " + str(delay) + " seconds!", title="mudScript")

    # Check if the userDelay is valid
    if userDelay is None:
        exit()
    elif userDelay == '':
        delay = 0.5
    elif userDelay.isnumeric():
        delay = userDelay
    else:
        try:
            delay = float(userDelay)
        except ValueError:
            pyautogui.alert("Invalid input!", title="mudScript")
            exit()


def setkey():
    # Set the key to toggle the script
    global toggle
    userKey = pyautogui.prompt("Please enter your custom key to toggle the script. \n"
                               "The default key is " + toggle + ".\n"
                               "Custom keys have to follow the pynput specification.",
                               title="mudScript")
    # Check if the userKey is valid
    if userKey is None:
        exit()
    elif userKey == '':
        toggle = 'x'
    else:
        toggle = userKey


def on_press(key):
    global toggle, paused, running
    print(key)

    # Checks for toggling & exiting the script
    if type(key) == Key:
        if key == Key.esc:
            running = False
    elif key.char == toggle:
        paused = not paused
        if paused:
            pyautogui.alert("mudScript paused!", title="mudScript")
        else:
            pyautogui.alert("mudScript resumed!", title="mudScript")


def main():
    if setup():
        setdelay()
        pyautogui.alert("The delay has been set to " + str(delay) + " seconds!", title="mudScript")
        setkey()
        pyautogui.alert("The toggle has been set to " + toggle + "!", title="mudScript")
    else:
        pyautogui.alert("Default config loaded", title="mudScript")

    listener = Listener(on_press=on_press)
    listener.start()
    while running:
        while not paused:
            pyautogui.leftClick()
            pyautogui.rightClick()
            pyautogui.PAUSE = delay
    listener.stop()
    pyautogui.alert("Script has been stopped!", title="mudScript")


if __name__ == "__main__":
    main()
