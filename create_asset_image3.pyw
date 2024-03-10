import tkinter as tk
from tkinter import ttk
import os, shutil
#import _thread
#from pathlib import path

path = os.chdir('C:\\Users\\Anwender\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')
#path = os.chdir('C:\\Users\\Anwender\\Desktop\\testordner')
files = os.listdir(".")

def Ordner_auslesen():
    textfield.config(state='normal')
    textfield.delete(1.0, 'end')
    textarray = []
    for i in range(0,len(files)):       #Achtung: Indizierung beginnt bei 0 und endet bei n-1
        filename = files[i]
        #print(filename)
        text_new=filename+'\n'
        textarray.append(filename)
        textfield.insert('end', text_new)
    print(i)
    textfield.config(state='disabled')

def neuer_Ordner():
    textfield2.config(state='normal')
    textfield2.delete(1.0, 'end')
    if not os.path.exists("C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe"):
        os.makedirs("C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe")
        textfield2.insert('end', "Neuer Ordner angelegt")
    else:
        textfield2.insert('end', "Ordner existiert bereits. Kopiere Dateien...")
    button2.config(state='normal')
    button3.config(state='normal')
    
    path = os.chdir("C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe")
    new_folder = os.listdir(".")
    path = os.chdir('C:\\Users\\Anwender\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')
    files_raw = os.listdir(".")
    for f in files_raw:
        file_cct = f+'.jpg'
        if f in new_folder or file_cct in new_folder:
            hint = '\n'+'Datei '+f+' exisitiert bereits.'
            textfield2.insert('end', hint)
        else:
            shutil.copy(f, "C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe")
    textfield2.config(state='disabled')

def Dateien_umbenennen():
    path = os.chdir("C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe")
    files_raw = os.listdir(".")
    textfield.delete(1.0, 'end')
    textfield2.config(state='normal')
    textfield2.delete(1.0, 'end')
    for i in range(0,len(files_raw)):
        filename = files_raw[i]
        '''if os.path.isfile(filename+'.jpg'):
            hint = '\n'+'Datei '+filename+' exisitiert bereits'
            textfield2.insert('end', hint)
        else:'''
        if filename[-4] != '.':
             os.rename(os.getcwd()+'\\'+str(filename),os.getcwd()+'\\'+str(filename)+'.jpg')
             text2 = filename+'.jpg '+'\n'
             textfield2.insert('end', text2)
        else:
             Alert = "Die Datei "+filename+" wurde schon ins .jpg Format umgewandelt"+'\n'
             textfield2.insert('end', Alert)
    textfield2.config(state='disabled')

def Ordner_oeffnen():
    path = "C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe"
    if os.path.exists("C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe"):
        path = os.path.realpath(path)
        os.startfile(path)
    else:
        textfield2.config(state='normal')
        textfield2.delete(1.0, 'end')
        textfield2.insert('end', "Ordner exisitert nicht. Bitte auf 'Dateien kopieren oder Speicherort"+'\n'+"anlegen und kopieren' klicken!")
        textfield2.config(state='disabled')

def Hilfe():
    textfield.config(state='normal')
    textfield.delete(1.0, 'end')
    textfield.insert('end', instructions)
    textfield.config(state='disabled')

def Developer():
    path = os.chdir("C:\\Users\\Anwender\\Desktop\\Windows Startbildschirm-Hintergründe")
    textfield2.config(state='normal')
    textfield2.delete(1.0, 'end')
    filename_dev = '5e2afdc70c60b7ac3564993ef7d6a4680e033221c8c2c226154ea5d009910c57'
    istrue = os.path.isfile(filename_dev)
    textfield2.insert('end', istrue)
    textfield2.config(state='disabled')

root = tk.Tk()
root.title('Create Asset Immage')

# An oberster Stelle steht die Möglichkeit, den Ordnerinhalt anzuzeigen
frame_oben = tk.Frame(root)
frame_oben.pack( side = 'top' )
button = tk.Button(master=frame_oben, text="Ordnerinhalt aufzählen", command = Ordner_auslesen, width=34, bg='#C7DDF2')
button.pack( side = 'left' )
button_instructions = tk.Button(master=frame_oben, text="Hilfe", command = Hilfe, width=34, bg='#C7DDF2')
button_instructions.pack( side = 'right')
button_create = tk.Button(master=root, text="Dateien kopieren oder Speicherort anlegen und kopieren", command = neuer_Ordner, width=70, bg='#C7DDF2')
button_create.pack( side = 'top' )

# Das erste Frame beinhaltet nur das Text-Widget
frame = tk.Frame(root)
frame.pack( side = 'top' )
# Das zweite Frame beinhaltet die Knöpfe, welche zum unteren Feld gehören
frame2 = tk.Frame(root)
frame2.pack()
# Das dritte Frame beinhaltet das untere Text-Widget
frame3 = tk.Frame()
frame3.pack( side = 'bottom' )

textfield = tk.Text(master=frame, height=15, width=70)
scrollbar1 = tk.Scrollbar(master=frame, orient='vertical')
scrollbar2 = tk.Scrollbar(master=frame3, orient='vertical')
label_text2 = tk.Label(master=frame2, width=70, text='Ausgabe neue Dateien')
button2 = tk.Button(master=frame2, text='Dateien umwandeln', state='disabled', command = Dateien_umbenennen, width=70, bg='#C7DDF2')
button3 = tk.Button(master=frame2, text="Ordner öffnen", command = Ordner_oeffnen, width=70, bg='#C7DDF2')
textfield2 = tk.Text(master=frame3, height = 15, width = 70)

instructions = "Ordnerinhalt aufzählen: "+'\n'+"Mit diesem Befehl werden alle temporären Dateien des Quell-"+'\n'+"verzeichnisses angezeigt."
instructions +='\n'*2+"Dateien kopieren oder Speicherort anlegen und kopieren: "+'\n'+"Die Dateien des Quellverzeichnisses müssen zunächst in einen separatenOrdner kopiert werden, um Komplikationen mit Windows zu vermeiden,"+'\n'+"nachdem die Dateien umgewandelt wurden. "
instructions +="Sofern noch kein Ordner"+'\n'+"besteht, erzeuge einen neuen Ordner, in welchem die .jpg-Dateien"+'\n'+"abgelegt werden."
instructions +='\n'*2+"Dateien umwandeln: "+'\n'+"Sofern ein Verzeichnis vorliegt, können die Rohdateien aus dem Quell-"+'\n'+"verzeichnis hiermit zu .jpg-Dateien umgewandelt werden."
instructions +='\n'*2+"Ordner öffnen:"+'\n'+"Mit diesem Befehl kann der Ordner geöffnet werden, in welchem sich dieneuen .jpg-Dateien nun befinden. Sollte dieser Ordner (noch) nicht"+'\n'+"existieren, muss dieser zunächst mit 'Dateien kopieren oder Speicher-"+'\n'+"ort anlegen und kopieren' angelegt werden."

scrollbar1.pack(side='right', fill='y')
scrollbar2.pack(side='right', fill='y')
scrollbar1.config(command=textfield.yview)
scrollbar2.config(command=textfield2.yview)
textfield.pack()
textfield.delete(1.0, 'end')
textfield.insert('end', instructions)
textfield.config(state='disabled')
button2.pack()
button3.pack()
label_text2.pack()
textfield2.pack()
textfield2.config(state='disabled')
button_developer = tk.Button(master=root, text="Entwicklerhilfe", command = Developer, width = 70, bg='#C7DDF2')
#button_developer.pack()
root.mainloop()
