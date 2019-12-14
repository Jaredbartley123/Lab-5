word = "char"
strn = "character"

#found is a variable that stays true unless charcter is not available
found = True

#tells program where to start count after it has checked a character.
#keeps program from checking the previously checked characters.
start = 0

for ch in word:
	#strn.find (character to check, optional position value to start checking.)
	pos = strn.find(ch, start)
	#breaks program if letter is not found
	if pos < 0:
		found = False
		break
	#tells find function where letter was found and where to start again
	start = pos + 1

if found:
	print("Yes")
else:
	print("No")
