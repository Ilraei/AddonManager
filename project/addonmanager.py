import os, zipfile, shutil

exedir = os.getcwd()
zip_dir = exedir + "\\Zips"
addon_dir = exedir + "\\Addons"
wow_txt = exedir + "\\WOW.txt"
wow_dir = "a"
print(wow_dir)
with open(wow_txt, 'r') as SNAKE:	# holy shit this is dumb
	wow_dir = SNAKE.read()			# you have to have 3 lines	
										# to read a file as a variable.

def directory_setup():
	if not os.path.exists(exedir + "\\Zips"):
		os.makedirs(exedir + "\\Zips")
		print("Created Zip Directory!")
	if not os.path.exists(exedir + "\\Addons"):
		os.makedirs(exedir + "\\Addons")
		print("Created Addons Directory!")
directory_setup()

def zip_function():
	os.chdir(zip_dir)
	for item in os.listdir(zip_dir):
		if item.endswith(".zip"):
			zip_files = os.path.abspath(item)
			zip_object = zipfile.ZipFile(zip_files)
			zip_object.extractall(addon_dir)
			zip_object.close()
			os.remove(zip_files)
zip_function()