import tkinter as tk
import tkinter.ttk as tkk

window = tk.Tk()
window.geometry("470x500")
window.resizable(width=False,height=False)
window.title("BCRDH Segregation App")
window.iconbitmap("c:/Users/yoits/OneDrive/Desktop/BCRDH.ico")

logo = tk.PhotoImage(file = "c:/Users/yoits/OneDrive/Desktop/BCRDH.gif", width=100, height=100)
label = tk.Label(image = logo, justify="right", anchor="nw")
label.grid(column=1, row=1,padx=20, pady=20)

Label_Intro = tk.Label(window, text="BCRDH \nFile Segregator  ", bd=5, font=("Helvetica Bold", 20), justify="left", anchor="nw")
Label_Intro.grid(column=2, row=1)
# Label_Intro = tk.Label(window, text="File Segregator for Ingestion", font=("Helvetica", 12), justify="left", anchor="nw")
# Label_Intro.grid(column=2, row=2)
Label_Intro = tk.Label(window, text=" \n \n ", bd=5, font=("Helvetica", 13), justify="left", anchor="nw")
Label_Intro.grid(column=1, row=2, padx=20)


Label_Intro = tk.Label(window, text="Source Location", bd=5, font=("Helvetica", 13), justify="left", anchor="nw")
Label_Intro.grid(column=1, row=3, padx=20)
txt = tk.Entry(window,width=40)
txt.grid(column=2, row=3)

Label_Intro = tk.Label(window, text="Destination", bd=5, font=("Helvetica", 13))
Label_Intro.grid(column=1, row=4, padx=20)
txt = tk.Entry(window,width=40)
txt.grid(column=2, row=4)

progress = tkk.Progressbar(window, orient="horizontal", length=410, mode='determinate')

def bar():
    import time
    progress['value'] = 20
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    window.update_idletasks()
    time.sleep(1)
    progress['value'] = 100


progress.grid(column=1, row=7, padx=20, columnspan=3)

button_Start = tk.Button(window, text="Start", command=bar, width=10, height=1, bg="#00C68C", fg="Black",  font=("Arial Bold", 12),  relief="flat" )
button_Start.grid(column=1, row=5, pady=20)
# tk.Button(window, text='Start', command=bar).pack(pady=10)

Label_Intro = tk.Label(window, text=" \n ", bd=5, font=("Helvetica", 13), justify="left", anchor="nw")
Label_Intro.grid(column=1, row=6, padx=20)

window.mainloop()