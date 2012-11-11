
# http://stackoverflow.com/questions/5773028/how-to-recursively-check-an-answer-in-a-boggle-type-game

def paths(grid, x, y, l):
    """Returns a list of positions that the required letter is at"""

    positions = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    return [p for p in positions if p in grid and grid[p] == l]

def match_word(grid, pos, word, path):
    """Returns true if the word was found in the grid starting from pos"""
    if len(word) == 0: return path
    pos_paths = paths(grid, pos[0], pos[1], word[0])
    if len(pos_paths) == 0 : return False

    return [match_word(grid, the_pos, word[1:], path + [the_pos]) for the_pos in pos_paths]

def word_found(grid, word, current_path):
    """returns true if the word is in the grid"""
    return [match_word(grid, key, word[1:], current_path + [key]) for (key, val) in dict.iteritems(grid) if val == word[0]]

def make_grid(input_string):
	grid = dict()
	for index in range(0,16):
		letter = input_string[index]
		grid[idx_to_coords(index)] = letter
	return grid

def idx_to_coords(idx):
	i = idx/4
	j = idx%4
	return (i,j)

def unwrap(l):
	if len(l) == 1:
		return unwrap(l[0])
	else:
		return l

def boggle_search(gamedata, word):
	locations = list()
	grid = make_grid(gamedata)
	results = word_found(grid, word, [])
	for ans in results:
		locations.append(unwrap(ans))
	return locations

input_string = "FJPYIELUGSFAPTTS"
input_string = "FJPYIELUGSFAPTIG"

grid = make_grid(input_string)
word = "FIG"
results = word_found(grid, word, [])

all = list()
for ans in results:
	all.append(unwrap(ans))

print all
