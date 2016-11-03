from string import punctuation

def packetize(word):
	"""
	This function will split a word in packets of threes,
	and will pad any remaining letters
	"""
	i = 0
	packets = []
	while i+2 <= len(word)-1:
		packets.append(word[i:i+3])
		i += 3
		
	if i <= len(word)-1:
		packets.append(word[i:]+(3-len(word)+i)*"0")
		
	return packets

def partition(message):
	"""
	This function will remove all punctutations from a string,
	split it on spaces, and group them in packets of three.
	"""
	
	# Drop punctuations
	message = ''.join(char for char in message.lower() if char not in punctuation)
	
	# Separate by spaces
	message = message.split(" ")
	
	# Split into packets of three
	# Pad packets with less than three characters
	packets = []
	for word in message:
		if len(word) < 3:
			packets.append(word+(3-len(word))*"0")
		else:
			packets += packetize(word)
			
	return packets
	
	
def packets_to_hex(packets):
	"""
	This functions generates hex color codes
	for the packets
	"""
	hex_codes = []
	
	for packet in packets:
		string = "#"
		for char in packet:
			if char == "0":
				string += "00"
			else:
				x = hex(int(round((ord(char)-96) * 255 / 26)))[2:]
				string += "0"*(2-len(x)) + x
				
		hex_codes.append(string)
	
	return hex_codes
	
# print packets_to_hex(partition("awesome awesomee awesomeee"))