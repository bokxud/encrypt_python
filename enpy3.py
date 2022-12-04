import os, sys, time, base64



def banner ():
	pass
	
	

user_file = input("You File Path: ")
try:
	file = open(user_file,"r")
	f = file.read()
except FileNotFoundError:
	print ("file not found")

file_encode = f.encode()
file_encypt = base64.b64encode(file_encode)
encypt_str = str(file_encypt)
target_enc_str = encypt_str[1:]

target_final_str = "## encrypted by - BDKR28-encrypter v1.0\n## made by - Mr. BDKR28\n## GitHub: https://github.com/bokxud\n## copyright ©️ reserved - 2022\n\nimport base64\nexec(base64.b64decode("+target_enc_str+"))"

target_file = user_file.replace(".py","-Encypted.py")

enc_file = open (target_file, "w")
enc_file.write(target_final_str)
enc_file.close()

print ("DONE")
print ("File save as " + target_file)