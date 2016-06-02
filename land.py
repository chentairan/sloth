
f1 = open('test.txt','w')
f2 = open('test.json')
line = f2.readline()
while line:
    if line == '    }\n':
        break
    xi = []
    yi = []
    ids = []
    line = f2.readline()
    line = f2.readline()
    lower = 0
    first = 1
    for i in range(0,27):
        line = f2.readline()
        line = f2.readline()

        line = f2.readline()
        line = line.split(': "')
        Id = line[1].strip('",\n')
        if Id == '28' and first:
            lower = i
            first = 0
        ids.append(int(Id))
        line = f2.readline()
        xs = line.split(': ')
        x = xs[1]
        x = x.strip(',\n')
        x = x.strip('"')
        line = f2.readline()
        ys = line.split(': ')
        y = ys[1]
        y = y.strip()
        y = y.strip('"')
        line = f2.readline()
        xi.append(x)
        yi.append(y)
    line = f2.readline()
    line = f2.readline()

    line = f2.readline()
    line = line.split(': "')
    name = line[1]
    name = name.strip('"\n')

    line = f2.readline()
    f1.write(name)
    print name
    upper = 0
    for i in range(0,27):
        if ids[upper] == i:
            f1.write(' ')
            f1.write(str((float(xi[upper]))))
            f1.write(' ')
            f1.write(str((float(yi[upper]))))
            upper = upper+1
        else:
            f1.write(' ')
            f1.write(str((float(xi[lower]))))
            f1.write(' ')
            f1.write(str((float(yi[lower]))))
            lower = lower+1
    f1.write('\n')
f1.close()
f2.close()

