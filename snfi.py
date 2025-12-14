import pypatchergba, requests # type:ignore

foldel = r"C:\Program Files (x86)\Steam\steamapps\common\DELTARUNE"
locfin = foldel or jocfol
urljson = {
    "urlch1": "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter1/lang_ro.json",
    "urlch2": "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter2/lang_ro.json",
    "urlch3": "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter3/lang_ro.json",
    "urlch4": "https://rawgithubcontent.com/ners-xd/DELTARUNE-RO/blob/ch1-4/mod/chapter4/lang_ro.json"
}

desjson = {
    "ch1": "{locfin}/chapter1",
    "ch2": "{locfin}/chapter2",
    "ch3": "{locfin}/chapter3",
    "ch4": "{locfin}/chapter4"
}

def patching():
    global button_pressed
    button_pressed = True
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

    for url, json in urljson, desjson:
        try:
            r = requests.get()
            if r.status_code == 200:
                with open(desjson, "w").split('/', 1)[1] as file:
                    file.write(r.content)
        except Exception as e:
            print(f"Nu s-au putut descărca fișierele. Ce plm")