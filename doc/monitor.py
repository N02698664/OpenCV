import os
import pyinotify

wm = pyinotify.WatchManager() #create a watch manager
mask = pyinotify.IN_CREATE #watched event

class CVProcessing(ProcessEvent):
    def process_IN_CREATE(self, event):
        execfile("hello_world.py")  #specialized event processor for any new file created
                                    #in the watched directory
        
notifier = pyinotify.Notifier(wm, CVProcessing()) #creates a notification object

wdd = wm.add_watch('/home/pi/OpenCV', mask, rec=False) #creates a watch on the OpenCV folder

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
