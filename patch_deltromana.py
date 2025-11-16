import tkinter, os, pypatchergba # type: ignore
import tkinter.filedialog, requests

foldel = r"C:\Program Files (x86)\Steam\steamapps\common\DELTARUNE"
locfin = foldel or jocfol
urljson = [
  {
  "url" : "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter1/lang_ro.json",
  "cale" : "{locfin}/chapter1"
  },
  {
  "url" : "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter2/lang_ro.json",
  "cale" : "{locfin}/chapter2"
  },
  {
  "url" : "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter3/lang_ro.json",
  "cale" : "{locfin}/chapter3"
  },
  {
  "url" : "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter4/lang_ro.json",
  "cale" : "{locfin}/chapter4"
  }
]

def patching():
  open(locfin)
  chselect = pypatchergba.apply_patch("data.win", "patch_files/chapter_select.bps")
  with open("data_ro.win", "wb") as f:
    f.write(chselect)
  
  ch1 = pypatchergba.apply_patch("chapter1/data.win")
  with open("data_ro.win", "wb") as f:
    f.write(ch1)
  
  ch2 = pypatchergba.apply_patch("chapter2/data.win")
  with open("data_ro.win", "wb") as f:
    f.write(ch2)
  
  ch3 = pypatchergba.apply_patch("chapter3/data.win")
  with open("data_ro.win", "wb") as f:
    f.write(ch3)

  ch4 = pypatchergba.applypatch("chapter4/data.win")
  with open("data_ro.win", "wb") as f:
    f.write(ch4)



m = tkinter.Tk()

m.title("Mod DELTARUNE Română")
if os.path.exists(foldel):
  print("Momentan nu se întâmplă nimic ca na. E mult e greu") # pun mai târziu că acum mi-e lene

else:
  mesnuex = tkinter.Label(m, text="Nu s-a găsit folderul unde e instalat DELTARUNE. Alege unde ai instalat jocul.")
  jocfol = tkinter.filedialog.askdirectory(title="Selectează folderul cu DELTARUNE")

  

m.mainloop()