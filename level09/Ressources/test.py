f = open('./token', 'r')
content = f.read()
f.close()

i = 0
s= ''
for x in content:
	x = ord(x) - i
	x = x % 256
	s += chr(x)
	i += 1

print s