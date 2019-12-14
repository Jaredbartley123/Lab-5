def check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("They are Anagrams")

    else:
        print("They are Not Anagrams")
        
print("Check if 2 words are anagrams!")

s1 = input("please enter a word: ")
s2 = input("please enter a second word: ")

check(s1, s2)
