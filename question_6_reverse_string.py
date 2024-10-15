# This program is used to reverse a string.

def string_reverse(str1):
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    index = len(str1) 
    
    # Execute a while loop 
    while index > 0:
        # Concatenate the character of 'str1' to 'rstr1'
        rstr1 += str1[index - 1]
        
        # Decrement the 'index' by 1 for the next iteration
        index -= 1
    
    # Return the reversed string stored in 'rstr1'
    return rstr1

def main():    
    str1 = '12345abcde'  # Define str1 here
    print("String reverse for \'12345abcde\' is", string_reverse(str1))

# Don't change the code below!
if __name__ == "__main__":
    main()
