alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
plain_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
	encrypt = ""
	alphabet_position = 0
	for i in plain_text:
		alphabet_position = alphabet.index(i) + shift_amount
		if alphabet_position > 25:
			alphabet_position = alphabet_position - 26
		if i == " ":
			encrypt += " "
		else:
			encrypt += alphabet[alphabet_position]
	return encrypt
encrypt_data = encrypt(plain_text, shift_amount)
print(f"The encoded text is {encrypt_data}")