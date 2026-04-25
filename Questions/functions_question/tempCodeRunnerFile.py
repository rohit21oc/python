def charCount(String):
    my_dict = dict()
    for ch in String:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
        print(my_dict)

my_dict = charCount("hello world")
