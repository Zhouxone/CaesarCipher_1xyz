print("""
░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄░░
░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄░░
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀░░
░█▀▄░▀█▀░█▀█░░░▀▀█░█░█░█▀█░█░█
░█▀▄░░█░░█░█░░░▄▀░░█▀█░█░█░█░█
░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀
作者：周威龍
"""
)

字母表 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("你要加密（encode）或者 解密（decode）？").lower()
text = input("在這兒填一下,你想要寫的信息").lower()
shift = int(input("填一下， 你想要的偏移量"))


def encrypt(original_text, shift_amount,mode):
	cipher_text = ""
	if mode == "decode":
			shift_amount =  - shift_amount
	
	for letter in original_text:
		if letter in 字母表:
			pos = 字母表.index(letter)
			new_pos = (pos + shift_amount) % 26
			cipher_text += 字母表[new_pos]
			# print(f"'{letter}' → pos {pos} → new_pos {new_pos} → '{字母表[new_pos]}'")
		else:
			cipher_text += letter
	return cipher_text
output = encrypt(text, shift, direction)
print(f"結果：{output}")