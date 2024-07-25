import math
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycles = 0
pomodoros_done = ""
timer = ""


def reset_timer():
    """Reset the app for its initial status"""

    global pomodoros_done, cycles, timer

    # enable back the start button
    btn_start.config(state=NORMAL)

    # cancel the timer (window.after)
    if timer:
        window.after_cancel(timer)

    # reset counters
    pomodoros_done = ""
    cycles = 0

    # reset labels
    lbl_pomodoros_done.config(text="Done: ")
    lbl_title.config(text="Start", fg=GREEN)

    canvas.itemconfig(timer_text, text=return_str_min_sec(0))


def start_timer():
    """Start the timer for Work, Break or Long Break"""

    # disable button start to avoid clicking and triggering the timer again
    btn_start.config(state=DISABLED)

    global cycles
    cycles += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # cycle 1: work
    # cycle 2: short break
    # cycle 3: work
    # cycle 4: short break
    # cycle 5: work
    # cycle 6: short break
    # cycle 7: work
    # cycle 8: long break
    if cycles % 8 == 0:  # every 8th it's a long break
        lbl_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif cycles % 2 == 0:  # every pair it's a short break
        lbl_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:  # every odd it's work
        lbl_title.config(text="Work", fg=GREEN)
        count_down(work_sec)


def return_str_min_sec(total_seconds):
    """Return the total of seconds formatted MM:SS"""

    # get minutes and seconds from the total of seconds
    minutes = math.floor(total_seconds / 60)
    seconds = total_seconds % 60

    # 2 digit formatting
    str_minutes = f"{minutes:02}"
    str_seconds = f"{seconds:02}"

    return f"{str_minutes}:{str_seconds}"


def bring_to_front():
    """Restore the window if it's minimized and bring it on top of the others"""

    window.deiconify()  # Restore the window if it's minimized
    window.lift()  # Bring the window to the top
    window.attributes('-topmost', True)  # Make the window topmost
    window.attributes('-topmost', False)  # Reset the topmost attribute
    window.focus_force()  # Focus the window


def count_down(count):
    """Count down the seconds"""

    global pomodoros_done, cycles, timer

    # update the text of the canvas text
    canvas.itemconfig(timer_text, text=return_str_min_sec(count))

    if count > 0:
        # wait 1000 ms and call count_down again, passing the counter - 1
        # storing the window.after to a global variable, so we can cancel it on reset
        timer = window.after(1000, count_down, count - 1)
    else:
        # when timer reaches 0

        # bring the window to the front
        bring_to_front()

        # sound a bell
        window.bell()

        # if cycle is odd (work) increments pomodoros done
        if cycles % 2 != 0:
            pomodoros_done += "🍅"
            lbl_pomodoros_done.config(text=f"Done: {pomodoros_done}")

        # if auto start, starts the next cycle automatically
        if auto_start.get():
            start_timer()
        else:
            # enables start button so the user can start the timer again
            btn_start.config(state=NORMAL)


# GUI Setup
window = Tk()
window.title("🍅 Pomodoro 🍅")
window.config(bg=YELLOW, padx=50, pady=50)

lbl_title = Label(text="Start", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))

# canvas with the size of the bg image
canvas = Canvas(width=400, height=300, bg=YELLOW)
# removes the canvas border
canvas.config(highlightthickness=0)
# gets the PhotoImage object from the image file
pomodoro_img = PhotoImage(file="pomodoro.png")
# create the image positioned at half of the image size
canvas.create_image(200, 150, image=pomodoro_img)
# create a variable for the canvas timer text, so we can use to change the timer
timer_text = canvas.create_text(200, 150, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))

# buttons
btn_start = Button(text="Start", padx=10, pady=10, command=start_timer)
btn_reset = Button(text="Reset", padx=10, pady=10, command=reset_timer)

# auto start
auto_start = IntVar()
check_auto_start = Checkbutton(text="Auto start", variable=auto_start)

lbl_pomodoros_done = Label(text="Done: ", font=(FONT_NAME, 20), bg=YELLOW)

# grid layout
lbl_title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
btn_start.grid(row=2, column=0)
check_auto_start.grid(row=2, column=1)
btn_reset.grid(row=2, column=2)
lbl_pomodoros_done.grid(row=3, column=1)

window.mainloop()
