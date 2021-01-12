#!/usr/bin/env python
__author__ = "Daniel Lomelino, Nico Alfonso, Yaseen Al-salamy, Martina Taylor"

import os
import re
import signal
import subprocess
from tkinter import Tk, Button, Canvas, Entry, Frame, Label, Listbox, Scrollbar, StringVar, END

WIN_WIDTH = 720
WIN_HEIGHT = 445
BG_COLOR = "white"
sigtable = {s.name[3:]: s.value for s in signal.Signals}
btns = []
root = Tk()
processes = []
processesvar = StringVar(value=processes)
search_value = StringVar(root)
lb = None
entry_pid = None


def main():
    get_processes()

    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
    # root.resizable(False, False)
    root.title("Signal Box!")
    root["background"] = BG_COLOR
    mainframe = Frame(root, width=WIN_WIDTH, height=WIN_HEIGHT)
    mainframe["background"] = BG_COLOR
    mainframe.grid(row=0, column=0, padx=20, pady=20)
    btn_label = StringVar(mainframe)

    topframe = Frame(mainframe, width=100, height=30)
    topframe["background"] = BG_COLOR
    topframe.grid(row=0, column=0)
    l_pid = Label(topframe, text="PID", background=BG_COLOR)
    l_pid.grid(row=0, column=0)

    global entry_pid
    entry_pid = Entry(topframe, textvariable=btn_label, width=10)
    entry_pid.grid(row=1, column=0, sticky="nsew")
    b = Button(
        topframe,
        text="Clear",
        command=clear_pid)
    b.grid(row=1, column=1, sticky="nsew")

    frame = Frame(mainframe, width=WIN_WIDTH, height=WIN_HEIGHT)
    frame["background"] = BG_COLOR
    frame["highlightthickness"] = 2
    frame.config(highlightbackground="lightblue")
    frame.grid(row=2, column=0, padx=20, pady=20)

    topframe2 = Frame(mainframe, width=100, height=30)
    topframe2["background"] = BG_COLOR
    topframe2.grid(row=0, column=1)
    l_search = Label(topframe2, text="Search", background=BG_COLOR)
    l_search.grid(row=1, column=1, padx=5)
    search = Entry(topframe2, textvariable=search_value, width=20)
    search.grid(row=1, column=2)
    search_value.trace_add("write", search_updated)

    pframe = Frame(mainframe, width=300, height=300)
    pframe["background"] = BG_COLOR
    pframe["highlightthickness"] = 2
    pframe.config(highlightbackground="lightblue")
    pframe.grid(row=2, column=1, padx=20, sticky="w")

    global lb
    lb = Listbox(pframe, listvariable=processesvar, width=40, height=16)
    lb.grid(row=2, column=1)
    lb.bind('<<ListboxSelect>>', fill_pid)
    # sb = Scrollbar(pframe)
    # sb.grid(sticky="e")
    # sb.config(command=lb.yview)

    # dynamically create buttons for each available signal
    for i, pieces in enumerate(sigtable.items()):
        row = i % 8
        col = i // 8
        label, signum = pieces
        b = Button(
            frame,
            text=label,
            command=lambda i=i, s=btn_label: send_sig(i, s.get())
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
        get_processes(search_value.get())
        clear_pid()


def clear_pid():
    """Clear the PID text input."""
    entry_pid.delete(0, END)
    entry_pid.insert(0, "")


def fill_pid(event):
    cur = lb.curselection()
    process = processes[cur[0]]
    pid = process.split()[1]
    entry_pid.delete(0, END)
    entry_pid.insert(0, pid)


def search_updated(var, indx, mode):
    val = search_value.get()
    get_processes(filter_str=val)


def get_processes(filter_str=None):
    print("Getting processes", filter_str)
    cmd = ['ps', 'aux']
    output, err = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                  ).communicate()
    process_list = list(filter(None, output.split("\n")))[1:]
    if filter_str:
        print(f"Filtering by {filter_str}")
        process_list = list(filter(lambda p: p.find(filter_str) != -1, process_list))
    global processes
    processes.clear()
    for process in process_list:
        pdata = re.sub(r"\s+", " ", process).split()
        user, pid, _, _, _, _, _, _, _, _, *cmd = pdata
        cmd = " ".join(cmd)
        processes.append(f"{user}   {pid}     {cmd}")
    print(processes)
    processesvar.set(processes)


if __name__ == '__main__':
    main()
    processes = get_processes()
    print(processes)
