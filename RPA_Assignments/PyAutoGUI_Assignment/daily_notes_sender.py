import pyautogui
import pyperclip
import time
import webbrowser


with open("notes.txt", "r", encoding="utf-8") as file:
    notes = file.read()

# Copy notes to clipboard
pyperclip.copy(notes)

webbrowser.open("https://web.whatsapp.com")

print("Opening WhatsApp Web...")
time.sleep(10)   # Time to load WhatsApp

pyautogui.moveTo(375, 208, duration=2)
pyautogui.click()

# SEARCH CONTACT NAME
contact_name = "Mrs.Abimanyu"

pyautogui.write(contact_name, interval=0.1)

time.sleep(2)

pyautogui.moveTo(298, 441, duration=2)
pyautogui.click()

time.sleep(1)

pyautogui.moveTo(888, 1030, duration=2)
pyautogui.click()

# PASTE NOTES
pyautogui.hotkey("ctrl", "v")

time.sleep(1)

pyautogui.moveTo(1864, 1026, duration=2)
pyautogui.click()

print("Notes sent successfully!")

pyautogui.moveTo(1900, 20, duration=2)
pyautogui.click()