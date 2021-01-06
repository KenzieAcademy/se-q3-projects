#!/usr/bin/env python
__author__ = "Daniel Lomelino, Nico Alfonso, Yaseen Al-salamy, Martina Taylor"

import os
import signal
from tkinter import Tk, Button, Entry, Frame, Label, StringVar, END

WIN_WIDTH = 380
WIN_HEIGHT = 425
BG_COLOR = "white"
sigtable = {s.name[3:]: s.value for s in signal.Signals}
btns = []


def main():
    root = Tk()
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
    root.title("Signal Box!")
    root["background"] = BG_COLOR
    mainframe = Frame(root, width=WIN_WIDTH, height=WIN_HEIGHT)
    mainframe["background"] = BG_COLOR
    mainframe.grid(row=0, column=0, padx=20, pady=20)
    mystring = StringVar(mainframe)

    topframe = Frame(mainframe, width=100, height=30)
    topframe["background"] = BG_COLOR
    topframe.grid(row=0, column=0)
    l_pid = Label(topframe, text="PID", background=BG_COLOR)
    l_pid.grid(row=0, column=0)
    t = Entry(topframe, textvariable=mystring, width=10)
    t.grid(row=1, column=0, sticky="nsew")
    b = Button(
        topframe,
        text="Clear",
        command=lambda t=t: clear_pid(t))
    b.grid(row=1, column=1, sticky="nsew")

    frame = Frame(mainframe, width=WIN_WIDTH, height=WIN_HEIGHT)
    frame["background"] = BG_COLOR
    frame["highlightthickness"] = 2
    frame.config(highlightbackground="lightblue")
    frame.grid(row=2, column=0, padx=20, pady=20)

    # dynamically create buttons for each available signal
    for i, pieces in enumerate(sigtable.items()):
        row = i % 8
        col = i // 8
        label, signum = pieces
        b = Button(
            frame,
            text=label,
            command=lambda i=i, s=mystring: send_sig(i, s.get())
        )
        b.grid(column=col, row=row, padx=2, pady=3)
        btns.append(b)

    root.mainloop()


def send_sig(btn_index, pid):
    """Send a signal to a process id."""
    label = btns[btn_index].cget("text")
    signum = sigtable[label]
    if pid:
        print(f"Sending SIG{label} ({signum}) to {pid}")
        os.kill(int(pid), signum)


def clear_pid(t):
    """Clear the PID text input."""
    t.delete(0, END)
    t.insert(0, "")


if __name__ == '__main__':
    main()
