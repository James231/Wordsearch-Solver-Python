
# Functions used to find the word in order of use

def find_word (wordsearch, word):
	"""Trys to find word in wordsearch and prints result"""
	# Store first character positions in array
	start_pos = []
	first_char = word[0]
	for i in range(0, len(wordsearch)):
		for j in range(0, len(wordsearch[i])):
			if (wordsearch[i][j] == first_char):
				start_pos.append([i,j])
	# Check all starting positions for word
	for p in start_pos:
		if check_start(wordsearch, word, p):
			# Word found
			return
	# Word not found
	print('Word Not Found')

def check_start (wordsearch, word, start_pos):
	"""Checks if the word starts at the startPos. Returns True if word found"""
	directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]
	# Iterate through all directions and check each for the word
	for d in directions:
		if (check_dir(wordsearch, word, start_pos, d)):
			return True

def check_dir (wordsearch, word, start_pos, dir):
	"""Checks if the word is in a direction dir from the start_pos position in the wordsearch. Returns True and prints result if word found"""
	found_chars = [word[0]] # Characters found in direction. Already found the first character
	current_pos = start_pos # Position we are looking at
	pos = [start_pos] # Positions we have looked at
	while (chars_match(found_chars, word)):
		if (len(found_chars) == len(word)):
			# If found all characters and all characters found are correct, then word has been found
			print('')
			print('Word Found')
			print('')
			# Draw wordsearch on command line. Display found characters and '-' everywhere else
			for x in range(0, len(wordsearch)):
				line = "";
				for y in range(0, len(wordsearch[x])):
					is_pos = False
					for z in pos:
						if (z[0] == x) and (z[1] == y):
							is_pos = True
					if (is_pos):
						line = line + " " + wordsearch[x][y]
					else:
						line = line + " -"
				print(line)
			print('')
			return True;
		# Have not found enough letters so look at the next one
		current_pos = [current_pos[0] + dir[0], current_pos[1] + dir[1]]
		pos.append(current_pos)
		if (is_valid_index(wordsearch, current_pos[0], current_pos[1])):
			found_chars.append(wordsearch[current_pos[0]][current_pos[1]])
		else:
			# Reached edge of wordsearch and not found word
			return

def chars_match (found, word):
	"""Checks if the leters found are the start of the word we are looking for"""
	index = 0
	for i in found:
		if (i != word[index]):
			return False
		index += 1
	return True

def is_valid_index (wordsearch, line_num, col_num):
	"""Checks if the provided line number and column number are valid"""
	if ((line_num >= 0) and (line_num < len(wordsearch))):
		if ((col_num >= 0) and (col_num < len(wordsearch[line_num]))):
			return True
	return False




##########################################################################################################
# Program Starts Here
##########################################################################################################

# import wordsearch
print('')
file = input('What file contains the wordsearch? (inc ext) ')
wordsearch = open(file).read().splitlines()

# Ask for word to look for
while (True):
	word = input('Enter a word to find (q to quit): ')
	if (word == 'q'):
		break;
	else:
		find_word(wordsearch, word)