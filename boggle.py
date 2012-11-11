# Original implementation from stack overflow
# http://stackoverflow.com/questions/5773028/how-to-recursively-check-an-answer-in-a-boggle-type-game
# 
# Modified to return results (which are in a nested list structure), so unroll provides a way to unroll that list of lists
# into a flat list of answers.
# make_grid is a convenience to take the string and make a grid which the word_found method expects.
#

def paths(grid, x, y, l):
    """Returns a list of positions that the required letter is at"""

    positions = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    return [p for p in positions if p in grid and grid[p] == l]

def match_word(grid, pos, word, path):
    """Returns true if the word was found in the grid starting from pos"""
    if len(word) == 0: return path
    pos_paths = paths(grid, pos[0], pos[1], word[0])
    if len(pos_paths) == 0 : return False
    return [match_word(grid, the_pos, word[1:], path + [tuple(the_pos)]) for the_pos in pos_paths]

def word_found(grid, word, current_path):
    """returns true if the word is in the grid"""
    return [match_word(grid, key, word[1:], current_path + [tuple(key)]) for (key, val) in dict.iteritems(grid) if val == word[0]]

def make_grid(input_string):
	"""converts a string into a 4x4 grid"""
	grid = dict()
	for index in range(0,16):
		letter = input_string[index]
		grid[(index / 4, index % 4)] = letter
	return grid

def unroll(results, flat):
	""""flattens the list of lists into a single list of lists"""
	if any([x for x in results if isinstance(x, (bool, list))]):
		return [ unroll(x, flat) for x in results if x]
	else:
		if len(results) > 0:
			flat.add(frozenset(results))
			return results

def boggle_search(gamedata, word):
	"""Searches for word in gamedata and returns the set of locations the word is found"""
	locations = list()
	grid = make_grid(gamedata)
	results = word_found(grid, word, [])
	answers = set()
	locations = list()
	unroll(results, answers)
	for ans in answers:
		if len(ans) == len(word):
			locations.append(list(ans))
	return locations

# Ineresting game sets:
# FJPYIELUGSFAPTIG => Search for FIG
# VYAMYTTSTAHLMBSZ => Search for MATT
