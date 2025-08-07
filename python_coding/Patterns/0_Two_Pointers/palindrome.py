def check_if_palindrome(s):
    left=0
    right=len(s)-1

    while left<right:
        if s[left] != s[right]:
            print(f"{s} is not a palindrome string")
            return False
        left += 1
        right -= 1
    
    print(f"{s} is a palindrome string")
    return True

check_if_palindrome("racecar")
check_if_palindrome("raecar")
