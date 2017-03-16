f = open('README.md','r')
print(f.read(20)) # read size
for line in f:
    print(line, end=' ')

