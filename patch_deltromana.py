import tkinter, os
import tkinter.filedialog

foldel = r"C:\Program Files (x86)\Steam\steamapps\common\DELTARUNE"
m = tkinter.Tk()

m.title("Mod DELTARUNE Română")
if os.path.exists(foldel):
  print("Momentan nu se întâmplă nimic ca na. E mult e greu") # pun mai târziu că acum mi-e lene

else:
  textnuex = tkinter.Label(m, text="Nu s-a găsit folderul unde e instalat DELTARUNE. Alege unde ai instalat jocul.")
  jocfol = tkinter.filedialog.askdirectory(title="Selectează folderul cu DELTARUNE")
  

m.mainloop()