"""import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Messaggio","Questo è un messagio d'esempio")

root = tk.Tk()

label= tk.Label(root, text="Benvenuti a tkinter!") 
label.pack()

button = tk.Button(root,text="Quit", command=root.destroy)
button.pack() 

check = tk.Checkbutton(root,text="controllo")
check.pack()

radio1 = tk.Radiobutton(root,
text="Opzione 1", value="Opzione1")
radio2 = tk.Radiobutton(root,
text="Opzione 2", value="Opzione2")
radio1.pack()
radio2.pack()

entry = tk.Entry(root)
entry.insert(0, "Inserisci deltesto qui")
entry.pack()

entry = tk.Entry(root)
entry.insert(0, "Inserisci del testo qui")
entry.pack()

textArea = tk.Text(root,width=20,height=5)
textArea.pack()

lb = tk.Listbox(root)
lb.insert(1, "Opzione 1")
lb.insert(2, "Opzione 1")
lb.insert(3, "Opzione 1")
lb.pack()

combo = ttk.Combobox(root,values=["Opzione 1","Opzione 2", "Opzione 3"])
combo.set("Seleziona un'opzione")
combo.pack()

frame = tk.Frame(root)
frame.pack()

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Sonodentro al frame!")
label.pack()

button = tk.Button(root,text="Mostra Messaggio",command=show_message)
button.pack()

label1 = tk.Label(frame, text="Riga1, Colonna 1")
label2 = tk.Label(frame, text="Riga1, Colonna 2")
label1.pack(side="left", fill="y",expand="true")
label2.pack(side="right")   

root.title("Calcolatrice")
root.mainloop()"""

x=0
c=0
r=1
while x!=9:
    x=x+1
    if c<3:
        c=c+1
    else:
        c=1
        r=r+1
    print(x,c,r)