import std/strformat
import wNim
import osproc
import os
import httpclient

var foldel = r"C:\Program Files (x86)\Steam\steamapps\common\DELTARUNE\"

proc patching(folderprin: string) =
  let folderjoc = folderprin & "data.win"
  let process_chselect = execShellCmd(fmt"flips.exe --apply chapter_select.bps ""{folderjoc}"" ""{folderprin}data_ro.win""")

  for chapter in 1..4:
    let nrcapitol = $chapter
    let folderdepatch = fmt"chapter{nrcapitol}_windows\data.win"
    let folderpatchuit = fmt"chapter{nrcapitol}_windows\data_ro.win"
    let fisierbps = fmt"patch_files\chapter{nrcapitol}.bps"

    let fisiere = fmt"flips --apply {fisierbps} {folderdepatch} {folderpatchuit}"
    let patchpebune = execShellCmd(fisiere)
    if process_chselect != 0 or patchpebune != 0:
      echo "Pentru un motiv nu s-a putut aplica modul. Verifică versiunea jocului"

    try:
      var client = newHttpClient()
      let jsonuri = fmt"{foldel}\chapter{nrcapitol}\lang"
      client.downloadFile(fmt"https://raw.githubusercontent.com/ners-xd/DELTARUNE-RO/refs/heads/ch1-4/mod/chapter{nrcapitol}/lang_ro.json", jsonuri & r"\lang_ro.json")
    except:
      echo "Nu s-au putut descărca fișierele. Ce plm"



let app = App(wSystemDpiAware)
let frame = Frame(title="Mod DELTARUNE Română", size=(640, 480))
let panel = Panel(frame)
let mesaj = StaticText(panel, label="Bine ai venit la aplicația de instalare a traducerii DELTARUNE în limba română!")
let mesaj2 = StaticText(panel, label="Pentru a începe, apasă butonul pe care scrie 'Instalează' și totul va fi instalat rapid și automat.")

let butoninstalare = Button(panel, label="Instalează")
let butoninchidere = Button(panel, label="Ieși")

butoninchidere.wEvent_Button do ():
  frame.delete()
  echo "bag pula in programare tot primesc erori ce dracu. acuma nu mai primesc, dar atunci primeam. eram nervos ca tot imi dadea erori"

butoninstalare.wEvent_Button do ():
    if dirExists(foldel):
      echo "S-a găsit folderul!"
    else:
      let jocfol = FileDialog(frame, message="Alege unde ai instalat DELTARUNE").display()
      if jocfol.len != 0:
       foldel = jocfol[0]

    patching(foldel)

proc layout() =
  butoninstalare.setPosition(60, 410)
  butoninchidere.setPosition(150, 410)
  mesaj.setPosition(40, 30)
  mesaj2.setPosition(40, 45)

panel.wEvent_size do (): layout()

layout()
frame.center()
frame.show()
app.mainLoop()