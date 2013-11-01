import os
from pyinotify import WatchManager, Notifier, ThreadedNotifier, EventsCodes, ProcessEvent

wm = WatchManager()

class CVProcessing(ProcessEvent):
    def __init__(self):
        """
        Does nothing in this case, but you can as well implement this constructor
        and you don't need to explicitely call its base class constructor.
        """
        pass

    def process_IN_CREATE(event):
        """
        This method process a specific kind of event (IN_DELETE). event
        is an instance of Event.
        """
        python -m hello_world.py

mask = EventsCodes.IN_CREATE  # watched events
        
notifier = Notifier(wm, CVProcessing())

wdd = wm.add_watch('/users/pi/OpenCV', mask, rec=False)

while True:  # loop forever
    try:
        # process the queue of events, if any
        notifier.process_events()
        if notifier.check_events():
            # read notified events and enqeue them
            notifier.read_events()
    except KeyboardInterrupt:
        # destroy the inotify's instance on this interrupt (stop monitoring)
        notifier.stop()
        break
