import mido
import time
import random
import keyboard

inputPort = mido.open_input("Digital Keyboard-1 0")
outputPort = mido.open_output("Microsoft GS Wavetable Synth 0")


def is_in_list(start_num, target):
    num_list = []
    for i in range(6):
        num_list.append(start_num + (12 * i))
    return target in num_list


def is_note(note_number, start_target):
    current = 0
    while current <= 6:
        if is_in_list(start_target, note_number + (12 * current)):
            return True
        current += 1
    return False


def get_white_key(note_number):
    if is_note(note_number, 36):
        return "C"
    if is_note(note_number, 38):
        return "D"
    if is_note(note_number, 40):
        return "E"
    if is_note(note_number, 41):
        return "F"
    if is_note(note_number, 43):
        return "G"
    if is_note(note_number, 45):
        return "A"
    if is_note(note_number, 47):
        return "B"


START_TIME = time.time()


NOTES = ["A", "B", "C", "D", "E", "F", "G"]

target_note = None


def set_random_note():
    global target_note
    target_note = random.choice(NOTES)
    print(target_note)


def get_random_note():
    return target_note


set_random_note()

running = True

while running:
    for msg in inputPort.iter_pending():
        if hasattr(msg, "note") and hasattr(msg, "velocity"):
            if msg.velocity != 0:
                outputPort.send(msg)
                if get_random_note() == get_white_key(msg.note):
                    print("Correct! :)")
                    set_random_note()
    if keyboard.is_pressed("q"):
        print("Quit")
        running = False
