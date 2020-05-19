#Importing libraries and frameworks
import tkinter as tk
import tkinter.ttk as tkk
import webbrowser
import os
import shutil
import time

#Creating window for the application
window = tk.Tk()
#Setting size
window.geometry("470x500")
window.resizable(width=False,height=False)
#Setting title and icon
window.title("BCRDH Segregation App")
window.iconbitmap("c:/Users/yoits/OneDrive/Desktop/BCRDH.ico")

#Adding logo
logo = tk.PhotoImage(file = "c:/Users/yoits/OneDrive/Desktop/BCRDH.gif", width=100, height=100)
labelLogo = tk.Label(image = logo, justify="right", anchor="nw")
labelLogo.grid(column=1, row=1,padx=20, pady=20)

#Creating Global variables source and destination
source=""
destination=""

#Application Description
Label_Intro = tk.Label(window, text="BCRDH \nFile Segregator  ", bd=5, font=("Helvetica Bold", 20), justify="left", anchor="nw")
Label_Intro.grid(column=2, row=1)

#printing space below
Space = tk.Label(window, text=" \n \n ", bd=5, font=("Helvetica", 13), justify="left", anchor="nw")
Space.grid(column=1, row=2, padx=20)

finishMessage = tk.Label(window, text="Finished Segregation", bd=5, font=("Helvetica", 13))

#Getting source and location from use
Label_Source = tk.Label(window, text="Source Location", bd=5, font=("Helvetica", 13), justify="left", anchor="nw")
Label_Source.grid(column=1, row=3, padx=20)
txt1 = tk.Entry(window,width=40)
txt1.grid(column=2, row=3)

Label_Dest = tk.Label(window, text="Destination", bd=5, font=("Helvetica", 13))
Label_Dest.grid(column=1, row=4, padx=20)
txt2 = tk.Entry(window,width=40)
txt2.grid(column=2, row=4)

#Initializing Progress bar for separation
progress = tkk.Progressbar(window, orient="horizontal", length=410, mode='determinate')
progress.grid(column=1, row=7, padx=20, columnspan=4)

#Creating start button
button_Start = tk.Button(window, text="Start", command=lambda: retrieve_input(), width=10, height=1, bg="#00C68C", fg="Black",  font=("Arial Bold", 12),  relief="flat" )
button_Start.grid(column=1, row=5, pady=20)
print(source+destination)
# tk.Button(window, text='Start', command=bar).pack(pady=10)

Label_Intro = tk.Label(window, text=" \n ", bd=5, font=("Helvetica", 13), justify="left", anchor="nw")
Label_Intro.grid(column=1, row=6, padx=20)

#Help link to WIki
link1 = tk.Label(window, text="Need help? Read Wiki Documentation here.", fg="blue", cursor="hand2")
link1.grid(column=2, row=5, padx=20)
link1.bind("<Button-1>", lambda e: callback("https://wiki.ok.ubc.ca/libokhist/Creating_Zipped_Bundles"))

def retrieve_input():
    global source
    global destination
    source = txt1.get()
    destination = txt2.get()
    print(source+destination)
    bar()

def callback(url):
    webbrowser.open_new(url)

def bar():

    progress['value'] = 5
    window.update_idletasks()
    time.sleep(1)

    global source
    global destination
    segregate(source, destination)
    progress['value'] = 100
    finishMessage.grid(column=1, row=8, padx=20, columnspan=3)

#Segregation Algorithm
def segregate(source, destination):
    source = source.replace('\\','/')
    destination = destination.replace('\\','/')
    # Changing current working directory
    os.chdir(source)
    # Get a list of files
    files = os.listdir(os.getcwd())
    new = 0
    size = 0
    newDestination = createDirectory(destination,new)
    new += 1
    progressValue = len(files)/10
    while files:
        progress['value'] = progressValue
        window.update_idletasks()

        file1 = source + "/" + files[0]
        file2 = source + "/" + files[1]
        size = size+os.path.getsize(file1)+os.path.getsize(file2)
        print(size)
        #while size is less than 2.5 GB
        if size <= 2684354560:
            shutil.move(file1, newDestination)
            shutil.move(file2, newDestination)
            del files[0:2]
            print(files)
        else:
            newDestination = createDirectory(destination, new)
            new += 1
            size=0
            print("seze: "+str(size))

def createDirectory(destination, new):
    os.chdir(destination)
    os.mkdir(str(new))
    destination = destination + "/" + str(new)
    return destination

window.mainloop()