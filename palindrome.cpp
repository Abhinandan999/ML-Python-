def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    original = x
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10  # Reduce x by removing the last digit
    
    # Check if the original number is equal to the reversed number
    return original == reversed_num


# Test cases
print(is_palindrome(121))   # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(10))    # Output: False
