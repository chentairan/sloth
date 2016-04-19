
#f1 = open('/Users/wangchao/Downloads/AFLW_old/crop_land.txt')
f1 = open('land.txt')
f2 = open('mylabels.json','w')
f2.write('[\n')
for line in f1:
    line = line.split()
    name = line[0]
    print name
    f2.write('    {\n')
    f2.write('        "annotations": [\n')
    first = 0
    for i in range(1,20):
        if line[i*2]=='NaN':
            continue
        else:
            if first == 1:
                f2.write(',\n')
            first = 1
            f2.write('            {\n')
            f2.write('                "class": "FacePoint"')
            f2.write(',\n')
        it = i*2-1
        cmd = '                "'+'x'+'": "'+str(line[it])+'",\n'
        f2.write(cmd)
        it = i*2
        cmd = '                "'+'y'+'": "'+str(line[it])+'",\n'
        f2.write(cmd)
        cmd = '                "'+'ids'+'": "'+str(i-1)+'"\n'
        f2.write(cmd)
        f2.write('            }')

    f2.write('\n')
    f2.write('        ],\n')
    f2.write('        "class": "image",\n')
    path = '        "filename": "' +name+'"\n'
    f2.write(path)
    f2.write('    },\n')
f2.write(']')
f1.close()
f2.close()

