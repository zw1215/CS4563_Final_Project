file = open("X_train.txt", 'r')
outfile = open("cleaned_X_train.txt", 'w')
for line in file:
    line = line.strip()
    newline = ''
    for char in line:
        if char != ' ':
            newline += char
        else:
            newline += ", "
    newline += '\n'
    outfile.write(newline)

file.close()
outfile.close()
