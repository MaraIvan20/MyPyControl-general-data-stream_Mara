pyControl is a system of software and hardware for controlling behavioural experiments based around the Micropython microcontroller.

For more information please see the Docs: http://pycontrol.readthedocs.io/

Repository contents:

gui              : Graphical user interface
com              : Serial communication and data logging
config           : Configuration files edited by user
data             : Behavioural data.
experiments      : Experiment definition files.
devices          : pyControl hardware classes (uploaded to pyboard).
pyControl        : pyControl framework        (uploaded to pyboard).
tasks            : Task definition files
tools            : Tools for importing and visualising pycontrol data
pyControl_GUI.py : Python script to launch the GUI.

Version: v1.6.2
---------------




The gui was adapted and tested to run on the task file test.py, simulating the changes that would normally take place
in the treadmill task based on the intertrial state,motion event, and the c variable.
For the new gui see gui_treadmilltask folder; some files in gui folder and the PyTreadmillTask.py were also modified, see comments #NEW!

