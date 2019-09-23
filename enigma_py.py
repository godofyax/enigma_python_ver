import sys

alphet_to_num = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,
				"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
num_to_alphet = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",
				19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}
def read_file(filename):
	global alphet_to_num
	f = open(filename, "r")
	lines = f.readlines()
	string = ""
	for line in lines:
		line.strip('\n')
		string = string+line
	lst = list(string)
	file = [alphet_to_num[char] for char in lst]
	return file

def rotate(rotor, outside_rotor):
	n_r = rotor[1:len(rotor)]
	n_r.append(rotor[0])
	n_outside_rotor = outside_rotor[1:len(outside_rotor)]
	n_outside_rotor.append(outside_rotor[0])
	return n_r, n_outside_rotor

def init_rotor(rotor, outside_rotor, start):
	pos = 0
	stop = rotor[start]
	while rotor[pos] != stop:
		#print(rotor[pos])
		#count += 1
		rotor, outside_rotor = rotate(rotor, outside_rotor)

	#print(count)
	#print(rotor)
	return rotor, outside_rotor

def main():
	global alphet_to_num
	plugboard = read_file('plugboard_my.txt')
	RIII_outside = plugboard
	RII_outside = plugboard
	RI_outside = plugboard
	rotorI = read_file('Rotor_I_web.txt')
	rotorII = read_file('Rotor_II_web.txt')
	rotorIII = read_file('Rotor_III_web.txt')
	reflector = read_file('reflector_web.txt')
	start = read_file('Rotor_start_web.txt')
	arrow = read_file('Rotor_arrow_web.txt')
	arrow[0] = rotorIII[arrow[0]]
	arrow[1] = rotorII[arrow[1]]
	arrow[2] = rotorI[arrow[2]]

	rotorIII, RIII_outside = init_rotor(rotorIII, RIII_outside, start[0])
	rotorII, RII_outside = init_rotor(rotorII, RII_outside, start[1])
	rotorI, RI_outside = init_rotor(rotorI, RI_outside, start[2])
	print(rotorIII)
	print(rotorII)
	print(rotorI)
	print(RIII_outside)
	print(RII_outside)
	print(RI_outside)
	print(reflector)

	def encode(input):
		output = list()
		global num_to_alphet
		nonlocal plugboard, rotorI, rotorII, rotorIII, reflector, arrow, RIII_outside, RII_outside, RI_outside
		for char in input:
			rotorIII, RIII_outside = rotate(rotorIII, RIII_outside)

			if rotorII[1] == arrow[1] and rotorIII[0] != arrow[0]:
				rotorII, RII_outside = rotate(rotorII, RII_outside)
				rotorI, RI_outside = rotate(rotorI, RI_outside)
			if rotorIII[0] == arrow[0]:
				rotorII, RII_outside = rotate(rotorII, RII_outside)

			'''
			print(rotorIII)
			print(rotorII)
			print(rotorI)
			print(RIII_outside)
			print(RII_outside)
			print(RI_outside)
			print(reflector)
			'''
			plug = plugboard[char]
			
			RIII = RIII_outside.index(rotorIII[plug])
			
			RII = RII_outside.index(rotorII[RIII])
			
			RI = RI_outside.index(rotorI[RII])
			
			ref = reflector[RI]
			'''
			print("plug:", num_to_alphet[plug])
			print("RIII:", num_to_alphet[rotorIII[plug]])
			print("RIII_out:", num_to_alphet[RIII])
			print("RII:", num_to_alphet[rotorII[RIII]])
			print("RII_out:", num_to_alphet[RII])
			print("RI", num_to_alphet[rotorI[RII]])
			print("RI_out", num_to_alphet[RI])
			print("reflector:", num_to_alphet[ref])
			'''
			b_RI = rotorI.index(RI_outside[ref])
			
			b_RII = rotorII.index(RII_outside[b_RI])
			
			b_RIII = rotorIII.index(RIII_outside[b_RII])
			out = plugboard[b_RIII]
			'''
			print("back rotorI:", num_to_alphet[b_RI])
			print("back rotorII:", num_to_alphet[b_RII])
			print("back rotorIII:", num_to_alphet[b_RIII])
			print("output:", num_to_alphet[out])
			'''
			output.append(out)
		return output



	input = [alphet_to_num[char] for char in list(sys.argv[1])]
	code = encode(input)
	output = [num_to_alphet[num] for num in code]
	print(output)
#print(plugboard_txt[alphet_to_num["E"]])
if __name__ == "__main__":
	main()