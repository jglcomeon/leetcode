def demo2(source):
    inBlock = False
    res = []
    for line in source:
        i = 0
        if not inBlock:
            new_line = []
        while i < len(line):
            if line[i:i+2] == '/*' and not inBlock:
                inBlock = True
                i += 1
            elif line[i:i+2] == '*/' and inBlock:
                inBlock = False
                i += 1
            elif line[i:i+2] == "//" and not inBlock:
                break
            elif not inBlock:
                new_line.append(line[i])
            i += 1
        if new_line and not inBlock:
            res.append("".join(new_line))
    for i in res:
        print(i)



if __name__ == '__main__':
    source = []

    t = input().strip()
    while t != '}':
        source.append(t)
        t = input().strip()
    source.append('}')
    demo2(source)
