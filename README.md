Documentation for ARBD testing APP

INTRO:

After a software update or installation of a new app, the TacRead Devices require manual testing in order to ensure that every app and all it’s features are functioning as expected. But this process could be automated since the testcases to be repeated every time was the same, saving time and increasing efficiency as compared to manual testing. We developed a linux-based app for the same.


APP SPECIFICATIONS:

Records and stores any number of test cases with all the relevant details such as the output, time lag between successive keystrokes.
Recorded testcases can be run anytime in the future.
The app executes each keystroke in the test case, compares
the output to the expected output in real time.
If these both are not matching, it asks the user whether to continue execution of the test case or not.
Suitable GUI, for the tester to run the app.


DESCRIPTION OF FUNCTIONING OF THE APP:

BEFORE RUNNING THE APP:

Make sure that srbda.py, alclinet.py, alserver.py, connect.py, executer6.py, are all existing in a common directory(dir1). Also if the app is being run for the first time make sure that there is a directory called ‘tacread’(which could be empty or not) inside dir1. If testcases were already recorded it would be found in this tacread directory.
Also make sure that python-uinput is installed in the arbd .


CONNECTING TO THE ARBD:

The app can be executed by executing the file srbda.py in the terminal at dir1. As of now of now we have tested the app in an ubuntu PC only, but it can be easily implemented for windows as well with minor changes.

On executing, the home screen opens in which four buttons can be found. We can click on CONNECT to connect to the Arbd. Before clicking on Connect ensure that the ARBD is functioning and is connected to through a usb or should be connected to the net (basically we must be able to SSH into it), or else it throws an error.
For changing the credentials of the ARBD such as userid, password, and ip adress ; go to CREDENTIALS option on the home menu and after editing click UPDATE.

What clicking on the connect button does internally:

It updates the alserver.py file with the latest updated credentials, establishes an ssh connection with the ARBD, through the ssh connection sends the file alserver.py to the arbd. Then it automatically executes the file alserver.py in the arbd and creates sockets (using socket module of python) in the alserver program in the arbd and in the srbda program in the laptop. 

Note here that the socket communication and ssh are independent of each other. The ssh connection is used only for transfering the file and executing it in the arbd and later for killing the process in arbd during Disconnection. 
The sockets created are used for interaction between the srbda.py program in PC and alserver.py in arbd, making use of TCP alone. The sockets get connected through a randomly generated port number. 

The functions for connecting is imported by the srbda.py file from alclient.py.
So now connection is established between the process behind srbda.py in the PC and the process behind alserver.py and they can interact as and when necessitated by the user.

After connection is established, the other buttons, namely RECORD, EXECUTE and DISCONNECT get enabled.

DISCONNECTING:

Clicking on Disconnect kills the process running in the ARBD and the connection will be broken.
If there is any bug during execution of the app, clicking on Disconnect and Connecting again (without having to re-executing srbda.py) usually solves the problem.



RECORDING TESTCASES:

On clicking RECORD a new window opens. On the right-hand side of it, all the existing testcases and the sub-directories can be seen.
To record a new testcase right click on the directory under which the testcase has to be stored. A new pop-up opens, showing “add testcase” and “add menu”. On clicking “add testcase” another pop-up opens in which the name of the testcase can be given.

To add a submenu, click on “add submenu” and give the submenu’s name in the new pop-up that appears.
The sub-menu can now be seen in the list on the right hand. Now right click on the sub-menu and repeat the process for adding a testcase.

After a testcase name is given, click on “start recording” and one can start giving keystrokes. As the keystrokes are being given the app displays all the keystrokes received and also the display on the arbd sequentially. 
To stop recording, click on “End Recording”. After parsing is done a pop-up menu shows up showing “RECORDING FINISHED”. It usually takes 2-3 seconds.

What happens internally:

The alserver.py captures the name of the latest log file in the arbd.
As lines are being updated in the log-file by the OS the alserver program looks for “BRF DATA” or “KEYBOARD EVENT RECEIVED” in the lines. If found it sends the lines to the srbda.py program in the PC which prints it on the screen as and when the lines are received. The lines are stored and parsed for printing.

After recording is stopped, all the lines are parsed again to store the time, and time-differences between all two successive lines as well as the uinput key code for the corresponding key. The parsed information is stored as a list in a .txt file with the name of the testcase.

For recording, the srbda.py imports functions from the alclient.py file, which contains code for communication between sockets for recording. 

The functions for parsing is imported by alclient.py from executer6.py

During parsing the keyword received from the logfile are converted to its equivalent keycode in uinput by the di() and ex() functions in executer6.py.

So to change any keycode definition according to uinput definitions the dictionaries dict6 in di() and dict7 in ex() has to be modified.

**Please note that since there were problem in getting the Key-codes for ‘windows’(super) key and some combinations like ‘ctrl’+’c’ , when the keycodes are found these can be updated easily as mentioned above.( other combinations such as ‘shift’ +1 ,etc. are working perfectly fine.)

After recording is finished the window for recording can be closed and other functions such as executing can be done. 



EXECUTING TESTCASES:

Click on “Execute” to get to the execution window. Select a testcase from the list on the right, right-click on it and click on “load testcases”. This loads all the BRF data lines and Keyboard event lines as recorded, sequentially.\

Now click on “Execute testcases”, to start execution.

NOTE: Before execution make sure that the intial condition in the arbd is same as shown in the loaded testcase. (This could not be done automatically because ,we don’t know the u-input keycode for windows key)

The program compares the new BRF data lines to the BRF data lines in the recorded testcases. If the line passed, the line turns green and ‘passes’ appears on the table. If the line failed, the line becomes red and ‘failed’ appears on the table. A pop-up appears asking the user to continue execution or not. If the user clicks on “Continue” the execution continues until the whole testcase has been executed or until when a new fail case appears. If the user clicks on “stop”, execution is stopped.

What happens internally:

The functions for execution are imported by srbda.py from alclient.py.

During execution the alserver.py program captures the name of the latest logfile in the arbd and reads from it. The lines obtained are used for comparision. Also a uinput device is defined by the alserver program.

All the keyboard event lines between two BRF data lines are sent by the alclient program in PC to alserver, at once. These keystrokes are executed after exactly the same time difference between each other as in the recorded case.
Execution of two keys at the same time (combo) is also handled.

After these many keyboard events are executed, the alserver program wats and reads for as many BRF data lines as expected. If the expected number of BRF data lines are not received, it waits for a maximum of 1 second. The newly recorded BRF data lines are sent back to the alclient program.

The comparison happens at the alclient program. It compares all the obtained BRF data lines to all the BRF Data lines before the next set of Keyboard Event lines. If there is at least one match, the line is “passed”.


 MAJOR MODULES USED:

POPEN(subprocess), multiprocessing, Tkinter, socket, uinput, paramiko




