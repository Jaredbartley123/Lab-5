def split(word):
    return[char for char in word]


print("Welcome to the Caesar cypher generator!")
string = str(input("Please enter a sentence: "))
num = int(input("Please enter the amount you would like to shift by: "))

while num > 25 or num < 0:
    num = int(input("Please enter a number between 0 and 25: "))
    
    

string = split(string)

for i in range (len(string)):
    if string[i].isalpha() : 
        
        string[i] = ord(string[i]) + num
        
        string[i] = chr(string[i])
        

for i in range (len(string)):
    print(string[i], end = "")
    




    
