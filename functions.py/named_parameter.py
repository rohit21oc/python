def named_parameter(physics,math,english=0,hindi=0,chemistry=0):
    print(f"Your marks in physics : {physics}")
    print(f"Your marks in math : {math}")
    print(f"Your marks in english : {english}")
    print(f"Your marks in hindi : {hindi}")
    print(f"Your marks in chemistry : {chemistry}")
    total = physics+math+english+hindi+chemistry
    print(f"Your total marks is {total}")
# named_parameter(70,89,50,69,100)
named_parameter(physics = 70,math=95,hindi=90,english=83,chemistry=100)
named_parameter(-10,95,hindi=90,english=83,chemistry=100)
