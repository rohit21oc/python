"palindrome function that takes a string as an argument and returns True if the string is a palindrome, and False otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization)."

def is_palindrome(String):
    if String == String[:: -1]:
        return True
    else:        
        return False
    
is_palindrome = is_palindrome("Sigma")

if is_palindrome == True:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")