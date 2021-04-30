
class Stopwatch():

    def __init__(self, widget, _lap_count=0, stopwatch_time=0, stopwatch_lap=''):
        self.w = widget
        self._current_time = stopwatch_time
        self._lap_count = _lap_count
        self.w.stopwatch_label.setText(self.convert())
        self.w.stopwatch_textBrowser.setText(stopwatch_lap)


    def lap_btn(self):
        self._lap_count += 1
        self.w.stopwatch_textBrowser.append(' Lap' + str(self._lap_count) + '\t  ' + self.convert())


    def reset_btn(self):
        self._current_time = 0
        self._lap_count = 0
        self.w.stopwatch_label.setText('00:00.00')
        self.w.stopwatch_textBrowser.setText('')


    def start_stop_btn(self):
        # Starting counting
        if not self.w.stopwatch_lap_btn.isEnabled():
            self.w.stopwatch_lap_btn.setEnabled(True)
            self.w.stopwatch_timer.start(10)
        
        # Stop counting
        else:
            self.w.stopwatch_lap_btn.setEnabled(False)
            self.w.stopwatch_timer.stop()


    def convert(self):
        minute = int(self._current_time/60000)
        second = int((self._current_time%60000)/1000)
        decimal_second = int((self._current_time%1000)/10)
        fmt = '{:0>2d}:{:0>2d}.{:0>2d}'

        return fmt.format(minute, second, decimal_second)


    def display(self):
        self._current_time += 10
        self.w.stopwatch_label.setText(self.convert())

