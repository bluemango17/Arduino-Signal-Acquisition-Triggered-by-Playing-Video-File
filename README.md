# Acquisition detector
This python script was made as an idea to synchronize start of playing video file with start of acquisition of (EEG) data from arduino microcontroller.
It is realized as an intership project on University of Belgrade, School of Electrical Engineering, under the mentorship of professor PhD Nadica Miljković.

**Instalation**

"Generate log file" option in GOM player is used as an indicator that the video has started. watchodog python library is used to pick up changes in folder in which GOM player stores log files. In order for script to work, [GOM player](https://www.gomlab.com/download/) has to be installed and the -Generate log files- option in settings has to be [checked](http://prntscr.com/101xviy).

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

**Usage**

[GUI](http://prntscr.com/101zdd3)

To enter correct baud rate arduino code must be checked:

```
void setup() {
  Serial.begin(115200);
}
```

In this case 115200 is typed in Entry box and "Set" button is pressed. After that acquisition will start if "Start" button is pressed or if any video is played via GOM player.
Acuisition can be stopped in the same fashon, that is, if "Stop" button is pressed or GOM player is turned off. In that case plot pauses and can be resumed with start button or with playing video (via GOM player).

With every new acquisition start, new txt file is created with date and time as a title (when acquisition started), in which data from that acquisition session is being stored.

