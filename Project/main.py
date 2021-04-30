import sys
import os.path
from stopwatch import Stopwatch
from countdown import Countdown
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QSound
import atexit


def actionAbout(w_about):
    w_about.show()


def save(w, s, c, __file__):
    f = open(os.path.abspath(os.path.dirname(__file__)) + '/save/stopwatch_save.bin', 'wb+')

    f.write(str.encode(str(s._lap_count) + '\n'))
    f.write(str.encode(str(s._current_time) + '\n'))
    f.write(str.encode(w.stopwatch_textBrowser.toPlainText()))

    f.close()

    f = open(os.path.abspath(os.path.dirname(__file__)) + '/save/countdown_save.bin', 'wb+')

    f.write(str.encode(str(w.countdown_hours_spinBox.value()) + ':' + str(w.countdown_mins_spinBox.value()) + ':' + str(w.countdown_secs_spinBox.value()) + '\n'))
    f.write(str.encode(str(c.hours) + ':' + str(c.mins) + ':' + str(c.secs)))

    f.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    stopwatch_lap_count = 0
    stopwatch_current_time = 0
    stopwatch_lap = ''

    # Load UI file
    w = loadUi(os.path.abspath(os.path.dirname(__file__)) + '/ui/clock.ui')
    w_about = loadUi(os.path.abspath(os.path.dirname(__file__)) + '/ui/about.ui')

    # Set application icon
    w.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.dirname(__file__)) + '/image/clock.ico'))
    w_about.setWindowIcon(QtGui.QIcon(os.path.abspath(os.path.dirname(__file__)) + '/image/clock.ico'))

    try:
        # Read the operation history of stopwatch
        stopwatch_history = open(os.path.abspath(os.path.dirname(__file__)) + '/save/stopwatch_save.bin', 'rb')
        stopwatch_lines = stopwatch_history.readlines()
        stopwatch_lap_count = int(stopwatch_lines[0].decode().strip('\n'))
        stopwatch_current_time = int(stopwatch_lines[1].decode().strip('\n'))
        for i in range(2,len(stopwatch_lines)):
            stopwatch_lap += stopwatch_lines[i].decode() 

        # Initial the class of Stopwatch
        s = Stopwatch(w, stopwatch_lap_count, stopwatch_current_time, stopwatch_lap)
    except:
        # Initial the class of Stopwatch
        s = Stopwatch(w)
    
    try:
        # Read the operation history of countdown
        countdown_history = open(os.path.abspath(os.path.dirname(__file__)) + '/save/countdown_save.bin', 'rb')
        countdown_lines = countdown_history.readlines()
        countdown_set_time = countdown_lines[0].decode().strip('\n').split(':')
        countdown_current_time = countdown_lines[1].decode().split(':')
        for i in range(0, len(countdown_set_time)):
            countdown_set_time[i] = int(countdown_set_time[i])
            countdown_current_time[i] = int(countdown_current_time[i])
        # Initial the class of Countdown
        c = Countdown(w, countdown_set_time, countdown_current_time)
    except:
        # Initial the class of Countdown
        c = Countdown(w)

    # Declare timer for stopwatch and countdown
    w.stopwatch_timer = QTimer()
    w.countdown_timer = QTimer()

    # Load beep voice
    w.beep_sound = QSound(os.path.abspath(os.path.dirname(__file__)) + '/sound/Old-clock-ringing-sound-effect.wav')
    w.beep_sound.setLoops(10)

    # Connect to slot function of about widget
    w.actionAbout.triggered.connect(lambda: actionAbout(w_about))

    # Connect to slot function of stopwatch
    w.stopwatch_lap_btn.clicked.connect(s.lap_btn)
    w.stopwatch_reset_btn.clicked.connect(s.reset_btn)
    w.stopwatch_start_stop_btn.clicked.connect(s.start_stop_btn)
    w.stopwatch_timer.timeout.connect(s.display)

    # Connect to slot function of countdown
    w.countdown_reset_btn.clicked.connect(c.reset_btn)
    w.countdown_start_btn.clicked.connect(c.start_btn)
    w.countdown_pause_btn.clicked.connect(c.pause_btn)
    w.countdown_close_btn.clicked.connect(c.close_btn)
    w.countdown_hours_spinBox.valueChanged.connect(c.setCountdownTime)
    w.countdown_mins_spinBox.valueChanged.connect(c.setCountdownTime)
    w.countdown_secs_spinBox.valueChanged.connect(c.setCountdownTime)
    w.countdown_timer.timeout.connect(c.display)

    atexit.register(save, w, s, c, __file__)

    w.show()
    app.exec_()
