OpenCV
======

Raspberry Pi / OpenCV project

This project is for the Embedded Linux class at SUNY New Paltz.
Original concept is to use the Raspberry Pi to process an image file uploaded into a monitored folder using pyinotify.
The results would be placed into the same folder when completed.
I plan to use the Python wrapper for OpenCV and eventually create the ability to upload a .txt file with parameters
to determine what is processed.


https://opencv-python-tutroals.readthedocs.org/en/latest/index.html


http://pyinotify.sourceforge.net/doc-v07/index.html


found in inotify-tools package in Ubuntu
Inotify is a great way to monitor file system changes, and with the great tool inotifywait ( found in inotify-tools package in Ubuntu) it’s even utilizeable in Bash scripts.

?
1
2
3
4
5
6
7
#!/bin/bash
while true; do
 
inotifywait -e create /home/user/pdfs  && \
./watermark_all.sh
 
done
Inotifywait creates an inotify watch on the directory /home/user/pdfs and waits until a file is created. In this event, inotifywait terminates and the ./watermark_all.sh script from above will be executed.

Great – Immediate results
