command = ""
yes = False
command = input("do you love me?>>>  ").lower()
while command != "no":
    if command == "yes":
        if yes:
            print("* i love you *---* i love you *---* i love you *")
        else:
            yes = True
            print("i realy love with you")
            continue

else:
    print("but i love you")
