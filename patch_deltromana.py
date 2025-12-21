import tkinter, os, snfi, requests
from tkinter import *
from tkinter import ttk
import PIL.Image, PIL.ImageTk

foldel = r"C:\Program Files (x86)\Steam\steamapps\common\DELTARUNE"

m = tkinter.Tk()

m.geometry("640x480")
cad = ttk.Frame(m, padding=10)
butoninceput = ttk.Button(m, text="Instalează", width=12, command=snfi.patching)
imagine = PIL.Image.open("tenna_sprite_installer.png")
imaginepgr = PIL.ImageTk.PhotoImage(imagine)
imgpgr = ttk.Label(m, image=imaginepgr)
imgpgr.pack()

textdetest = ttk.Label(m, text="Bine ai venit la aplicația oficială de instalare a traducerii DELTARUNE în limba română!\n"
                               "Pentru a începe, apasă butonul pe care scrie 'Instalează' și totul va fi instalat rapid și\nautomat", font=("Arial", 12))
textdetest.pack()

butoninceput.place(x=540, y=410)

m.title("Mod DELTARUNE Română")
if os.path.exists(foldel):
  pass # n-am ce să pun aici că butonul începe patch-uirea, deci n-are sens să o fac automat fără voința utilizatorului
else:
  mesnuex = tkinter.Label(m, text="Nu s-a găsit folderul unde e instalat DELTARUNE. Alege unde ai instalat jocul și apasă\nbutonul.")
  jocfol = tkinter.filedialog.askdirectory(title="Selectează folderul cu DELTARUNE")



m.mainloop()