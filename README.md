## acquisition detector
This python script was made as an idea to synchrionize start of playing video file with start of acquisition of (EEG) data from arduino microcontroller.
It is realized as an intership project on University of Belgrade, School of Electrical Engineering, under the mentorship of professor PhD Nadica Miljković.

**Instalation**

-Generate log file- option in GOM player is used as an indicator that the video has started. watchodog python library is used to pick up changes in folder in which GOM player stores log files. In order for script to work, [GOM player](https://www.gomlab.com/download/) has to be installed and the -Generate log files- option in settings has to be [checked](http://prntscr.com/101xviy).

Libraries:

[watchdog](https://pypi.org/project/watchdog/)

[NumPy](https://numpy.org/install/)

[matplotlib](https://matplotlib.org/stable/users/installing.html)

[pySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html#installation)

[pyinstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html) (for application building)

If numpy causes trouble during build up:
```
pip install numpy==1.19.3
```

