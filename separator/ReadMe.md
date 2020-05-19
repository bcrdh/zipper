# separator
This app will separate files (TIFF, XML) in pairs into directories with sizes < 2.5 GB; preparing them to be zipped and ready for ingest. 

# How to use it
After opening the executable, the use must provide the following two inputs:
- Source: Location of the TIFF and XML files to be seperated.
- Destination: Location to store the separated files. 

The progress bar on the bottom will show the use the progress of the process. One completed, the progress bar will touch the end and a message saying "Finsihed Segregation" will be printed. 

# Libraries used
- tkinter: for GUI
- os: for file manipulation
- tkinter.tt: for progress bar display
- webbrowser: to open help link with default browser

# Methods used
There are 5 main functions defined in this program

### retrieve_input():
This is used to assist tkinter to get the user input for location of source and destination. 

### bar():
This functinon starts the progress bar and calls segregate(source, dest)
When finished, it prints a finshed message. 

### segregate(source, destination):
Using the source and destination provided by the use, the function iterates over all files and adds them to folders created for every 2.5 GB worht of files. When a new directory needs to be created, it is done using the function below.

### createDirectory(destination, new):
Creates a new directory for 2.5 GB and returnds a new destination for the files to be moved.
