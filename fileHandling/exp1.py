filename = input("Enter the filename: ")
filename = filename+".txt"

with open(filename, "w") as f:
    while True:
        sentence = input("Enter sentence (or 'q' or 'Q' to stop): ")
        if sentence == "q" or sentence == "Q":
            break
        f.write(sentence + "\n")
        
print(sentence)