names=["유투버1","유투버2","유투버3","유투버4"]
for name in names:
    with open("{}.txt".format(name),"w",encoding="utf8") as file:
        contents=("안녕하세요?\n"
        f"{name}님\n"
        "영상보고 연락드립니다\n"
        "회신부탁드려요")
        file.write(contents)
        file.close()

