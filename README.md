Wanted to make a GPS tracker with an old phone. No SIM/service needed.

You'll need an android phone and the Tasker app. For opsec, probably don't use your real google account etc when setting up this phone.

1. Go to the play store and install Tasker (https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)
2. Open Tasker and allow the priviledges that it requests. **There's a Tasker Permissions app for PC/Mac** (https://github.com/joaomgcd/Tasker-Permissions/releases)
3. Place the xml file on your device
4. Open the 3-dot menu in tasker and select 'Data > Restore > User Local Backup' and select the xml file you loaded
5. This will install 3 tasks 'GPS Log', 'Set Home' and 'Set Away'
6. Run 'Set Away' by tapping it, then press the play button on the bottom left of the screen. This will set the %Away variable to true and start the GPS Log task. When the task is running it will grab Date, Time, Lat, Long, Map URL and Speed every 15 seconds and write them to a file in Download called 'gps.log'
7. When done run 'Set Home' to set the %Away variable to false and stop the 'GPS Log' task
8. You can now export the the gps.log file to another machine and run 'log_parser.py' which generates an HTML file which is a map of the area, with each point marked on the map with all info except the URL. It also draws a line between all the points to see the path that was traveled

This may get more attention from me at some point. I just wanted a dead simple way to track something of interest. There's a lot that could be done to improve it but I have a lot of irons in the fire rn. Hopefully someone gets some use out of it