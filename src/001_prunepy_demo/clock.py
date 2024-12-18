import threading

from prune import Prune, notify


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

class Clock:
    def __init__(self) -> None:
        self.seconds_deg = 0
        self.minutes_deg = 0
        self.hours_deg = 0
        # Si on veut on peut passer des arguments derrière le temps, ce sera envoyé à event
        # set_interval(self.refresh_clock, 1000)

    @notify
    def refresh_clock(self):
        self.seconds_deg += 360/60
        self.minutes_deg += 360/(60*60)
        self.hours_deg += 360/(60*60*12)

    @notify
    def set_hour(self, hour:str):
        self.hours_deg = 360/12 * int(hour)

    @notify
    def set_minute(self, minute:str):
        self.minutes_deg = 360/60 * int(minute)

    @notify
    def set_second(self, second:str):
        self.seconds_deg = 360/60 * int(second)

clock = Clock()
prune = Prune(clock=clock)



