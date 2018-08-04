
def write(filename, dataArr):
    f = open(filename, "w+")
    if (f):
        f.write(getSubject(dataArr[0]) + "\n")

        for line in arr2Str(dataArr):
            f.write(line + "\n")

        f.close()

        return True
    else:
        return False

def arr2Str(dataArr):
    for d in dataArr:
        arr = []

        for sub in d:
            if ( isinstance(d[sub], list) ):
                arr.append( ", ".join(d[sub]))
            else:
                arr.append(d[sub])
        yield "\"" + "\",\"".join( [x.replace('"', '\\"') for x in arr] ) + '"'        


def getSubject(dataArr):
    return ",".join( dataArr.keys() )