# Problem Prompt:
# Initially, there is a Robot at position (0, 0).
# Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string.
# And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.

def judgeCircle(moves):
	x = 0
	y = 0

	if moves:
		for m in moves:
			if m == 'U':
				y += 1
			elif m == 'D':
				y -= 1
			elif m == 'L':
				x -= 1
			elif m == 'R':
				x += 1
			else:
				x += 1.5
				y += 1.5
		if x==0 and y ==0:
			return True

	return False

# Test cases
moves = ['', ' ', 'HKJGKJ', 'D', 'UD', 'DU', 'UDL', 'UDR', 'LR', 'RL', 'LLRURD', 'LRD', 'LLD', 'RD', 'UD']

for i in range(len(moves)):
	print judgeCircle(moves[i])
