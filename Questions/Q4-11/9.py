"""
write a python program to convert a temperature into Farhenheit to celcius 
The formula is: Celcius = (Farhenheit - 32) * 5/9.
"""
f = float(input("Enter temperature: "))

cel = (f-32) * 5/9;

print(f"celcius of {f} is {cel}")