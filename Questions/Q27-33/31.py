""" Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000 

#First method

bill = int(input("Enter bill amount: "))
discount = 0;
if(bill>50000):
    discount = bill/100*30;
    print(f"You got 30% discount \nYour final bill is Rs. {bill-discount}");
elif(bill>=40000 and bill<=49999):
    discount = bill/100*25;
    print(f"You got 25% discount \nYour final bill is Rs. {bill-discount}");
elif(bill>=30000 and bill<=39999):
    discount = bill/100*20;
    print(f"You got 20% discount \nYour final bill is Rs. {bill-discount}");
elif(bill>=10000 and bill<=29999):
    discount = bill/100*10;
    print(f"You got 10% discount \nYour final bill is Rs. {bill-discount}");
elif(bill>=1 and bill<=9999):
    
    print(f"No discount \nYour final bill is Rs. {bill-discount}"); """

bill = int(input("Enter bill amount: "))
if bill>50000:
    discount = 30
elif bill>=40000 and bill>=49999:
    discount = 25;
elif bill>=30000 and bill>=39999:
    discount = 25;
elif bill>=10000 and bill>=19999:
    discount = 25;
elif bill>=1 and bill>=9999:
    discount = 0;

print(f"You got {discount}% discout");
final_bill = bill-(bill*30)/100
print(f"Yout final bill is{final_bill}") 