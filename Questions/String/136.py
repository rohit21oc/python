str = "erg ergsfee egeg   seff   re+265f 6rf "
space = 0
for sp in str:
    # if sp==" ":
        # space+=1
    if ord(sp)==32:
        space+=1
print(space)