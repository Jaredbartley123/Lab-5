def reverse(word):
    return word[::-1]


def isPalindrome(word):
    rev = reverse(word)

    if (word == rev):
        return True
    return False

s = input("Please enter a word: ")
s = s.replace(" ", "")
s = s.lower()
ans = isPalindrome(s)

if ans == 1:
    print("It's a palindrome")

else:
    print("It's not a palindrome")
