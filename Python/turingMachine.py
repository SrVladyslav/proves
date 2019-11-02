iteration = 0
state = 'A'
position = 0
data = ['0','1','1','1','1','1','']
#output of first data
print(f"Input data: ", data)

#algorithm
print(f"⋙State: ",state, f"⋙Position: ", position, f"⋙Data state: ", data)

def stateA():
	global position
	global state
	if data[position] == '1' or data[position] == '0':
		# same state
		position += 1 						# move right

	elif data[position] == '':
		state = 'B'   						# change state to B
		position -= 1						# move left
	print(f"⋙State: ",state, f"⋙Position: ", position, f"⋙Data state: ", data)

def stateB():
	global position
	global state
	if data[position] == '1':
		# same state
		data[position] = '0'				# change data to 0
		position -= 1						# move left
	elif data[position] == '0' or data[position] == '':
		state = 'C'   						# change state to C
		data[position] = '1'				# change data to 1
		position -= 1 						# move 
	print(f"⋙State: ",state, f"⋙Position: ", position, f"⋙Data state: ", data)

def stateC():
	print(f"Done! ⋙Output: " , data)


while True:
	if state == 'A': 
		stateA()
	elif state == 'B':
		stateB()
	else:
		stateC()
		break







		