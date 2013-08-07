#Uses the split function on each line in text file, this produces a list of words in that line. It then takes the length of the list to get the word count for that line. This is added to total word count for each line processed.

#Tally of words in file.
totalwords = 0

with open(raw_input('What is the address of the file?: ')) as f:
	for lines in f:
		totalwords =  totalwords + len(lines.split())

print totalwords
