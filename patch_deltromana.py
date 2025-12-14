import tkinter, os, snfi
import tkinter.filedialog, requests
from tkinter import ttk, PhotoImage, Canvas

foldel = r"C:\Program Files (x86)\Steam\steamapps\common\DELTARUNE"

m = tkinter.Tk()

m.geometry("640x480")
cad = ttk.Frame(m, padding=10)
butoninceput = ttk.Button(m, text="Instalează", width=12, command=snfi.patching)
# imagine = PhotoImage(file="tenna_sprite_installer.png")
# imaginepgr = tkinter.Label(m, imagine)                       DE ADAUGĂT IMAGINE ÎN STÂNGA PROGRAMULUI
# imaginepgr.pack()
butoninceput.place(x=540, y=410)

m.title("Mod DELTARUNE Română")
if os.path.exists(foldel):
  pass # n-am ce să pun aici că butonul începe patch-uirea, deci n-are sens să o fac automat fără voința utilizatorului
else:
  mesnuex = tkinter.Label(m, text="Nu s-a găsit folderul unde e instalat DELTARUNE. Alege unde ai instalat jocul și apasă\nbutonul.")
  jocfol = tkinter.filedialog.askdirectory(title="Selectează folderul cu DELTARUNE")



m.mainloop()