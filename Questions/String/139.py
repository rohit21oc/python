text = "python is good"
words = text.split(" ")
captalyze = " ".join(i.capitalize() for i in words)
print(captalyze)