from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import messagebox
import numpy as np
import serial
import time
import serial.tools.list_ports
from threading import Thread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path
from os import path
import sys
import os
from datetime import datetime
import time

class OnMyWatch:
    # Set the directory on watch
    #watchDirectory = path = sys.argv[1] if len(sys.argv) > 1 else '.'
    try:
        watchDirectory = path = "C:/Users/" + os.getenv('username') + "/AppData/Roaming/GRETECH/GOMPlayer/Log"

    except:

        print("Install GOM Player.")
        sys.exit()

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        global turn_off

        try:
            while True:
                if turn_off:
                    self.observer.stop()
                    sys.exit()
                else:
                    time.sleep(5)

        except:
            self.observer.stop()
            if 's' in globals():
                s.close()

            sys.exit()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        global state
        global ind_time_txt
        global cond
        global signal
        global ax
        global lines
        global signal
        global data
        global turn_off
        global signal_ID
        global s

        if event.is_directory:
            return None

        #elif event.event_type == 'created':
            # Event is created, you can process it now
         #   print("Watchdog received created event - % s." % event.src_path)



        elif event.event_type == 'modified': #and 'ser' in globals():
            # Event is modified, you can process it now
            #print("Watchdog received modified event - % s." % event.src_path)
            #temp = state
            # state = not(state)
            if(cond):
                ax.cla()
                data = np.array([])
                lines = ax.plot([], [])[0]

            else:

                now = datetime.now()
                current_time = now.strftime("%d-%m-%Y_%H;%M;%S")
                signal_ID = current_time + '.txt'
            cond = not(cond)
            ax.set_title('Arduino data')
            ax.set_xlabel('Samples')
            ax.set_ylabel('Voltage(V)')
            ax.set_xlim(0, 100)
            ax.set_ylim(-0.5, 6)


            if turn_off:
                sys.exit()



       # elif event.event_type == 'deleted':
            # Event is modified, you can process it now
        #    print("Watchdog received deleted event - % s." % event.src_path)
def fun1():
    if __name__ == '__main__':
        watch = OnMyWatch()
        watch.run()

global start_plot
global turn_off
turn_off = False
start_plot = False




def fun2():
    #global variables
    global cond, data
    data = np.array([])
    cond = False
    global signal
    global ax
    global lines
    global signal
    global label
    global baud_info
    global baud_rate
    global s
    global baud_entry
    global start_plot
    global root

    #plot data

    def plot_data():
        global cond, data
        global signal
        global signal_ID
        global root
        global arduino_info
        global turn_off
        global start_plot
        global lines
        global time_elapsed
        global s

        if cond and 's' in globals()and 'signal_ID' in globals():
            s.flush()
            s.flushInput()
            s.flushOutput()
            try:
                a = s.readline()
            except:
                print('Arduino error')
                arduino_info = tk.Label(root, text='Arduino error!')
                arduino_info.place(x=5, y=100)
                turn_off = True
                s.close()
                time.sleep(5)
                sys.exit()

            f = a.decode()
            signal = open(signal_ID, 'a')
            if(len(data)<100):
                try:
                    data = np.append(data, float(a[0:4]))

                except:
                    arduino_info = tk.Label(root, text='Arduino error!')
                    arduino_info.place(x=5, y=100)
                    s.close()
                    turn_off = True
                    sys.exit()
            else:
                try:
                    data[0:99] = data[1:100]
                    data[99] = float(a[0:4])

                except:
                    data[0:99] = data[1:100]
                    data[99] = data[98]

            lines.set_xdata(np.arange(0,len(data)))

            lines.set_ydata(data)

            signal.write(f)
            canvas.draw()

        root.after(1, plot_data)

    #functions
    def plot_start():
        global cond
        global signal_ID
        global s
        cond = True
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y_%H;%M;%S")
        signal_ID = current_time+'.txt'

        ax.set_title('Arduino data')
        ax.set_xlabel('Samples')
        ax.set_ylabel('Voltage(V)')
        ax.set_xlim(0, 100)
        ax.set_ylim(-0.5, 6)

    def plot_stop():
        global lines
        global cond
        global data
        global ax
        global s

        ax.cla()
        cond = False
        data = np.array([])
        lines = ax.plot([],[])[0]

    def set_baud_rate():
        global baud_rate
        global baud_info
        global baud_entry
        global s
        global start_plot
        global signal
        global turn_off

        baud_rate = baud_entry.get()

        baud_info = tk.Label(root, text='Baud rate is set.')
        baud_info.place(x=5, y=75)



        try:
            ports = list(serial.tools.list_ports.comports())
            str = ''
            str = str.join(ports[0])
            com_port = str[0:4]
            s = serial.Serial(com_port, baud_rate)
        except:
            turn_off = True
            if 's' in globals():
                s.close()
            if 'signal' in globals():
                signal.close()
            sys.exit()
        start_plot = True

    def turn_off_fcn():
        global signal, s
        global turn_off
        global root
        turn_off = True
        if 'signal' in globals():
            signal.close()
        if 's' in globals():
            s.close()

        sys.exit()


    def on_closing():
        global turn_off
        turn_off = True
        if messagebox.askokcancel("Quit", "Do you want to quit?"):

            sys.exit()
            root.destroy()

    #Main GUI code

    root = tk.Tk()
    root.title('Acquisition detector')
    root.geometry("700x500")#window size
    root.configure(background = 'white')



    #Create plot
    global lines
    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title('Arduino data')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Voltage(V)')
    ax.set_xlim(0,100)
    ax.set_ylim(-0.5,6)

    lines = ax.plot([],[])[0]

    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.get_tk_widget().place(x = 95, y = 60, width = 600, height = 400)
    canvas.draw()

    #Create buttons

    root.update()

    label = tk.Label(root, text = 'Click start button or play video to start acquisition', font = (14))
    label.place(x = 235, y = 2)


    start = tk.Button(root, text = 'Start', font = ('calibri',12), command = lambda :plot_start())
    start.place(x = 265, y = 30)

    stop = tk.Button(root, text = 'Stop', font = ('calibri',12), command = lambda :plot_stop())
    stop.place(x = 493, y = 30)

    baud_label = tk.Label(root, text = 'Set correct baud rate:')
    baud_label.place(x = 5, y = 5)

    baud_entry = tk.Entry(root, text = '')
    baud_entry.place(x = 5, y = 25)

    baud_set = tk.Button(root, text = 'Set', command = lambda : set_baud_rate())
    baud_set.place(x = 5, y = 50)



    turn_off_btn = tk.Button(root, text = 'TURN OFF', command = lambda: turn_off_fcn())
    turn_off_btn.place(x = 5, y = 450)

    root.resizable(False, False)


    #Start serial plot

    if  start_plot:
      s.reset_input_buffer()


    root.after(1, plot_data)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()



t1 = Thread(target=fun1)
t2 = Thread(target=fun2)


t1.start()
t2.start()