def charCount(String):
    my_dict = dict()
    for ch in String:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    for k,v in my_dict.items():
        print(f"{k} occurs : {v} times")

my_dict = charCount("hello world")

