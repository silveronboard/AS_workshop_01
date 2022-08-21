import re

filepath=r'c:\Users\pxgeo2.geo\Downloads\RS2201630P210100.WGS84.p190'
with open(filepath,'r') as f:
    for sp in range (7100, 8400):
        header = ""
        for line in f.readlines():
            if "H2600  " + str(sp) +" 1 " in line:
                #print(line)
                header += line
        headersize = len(header.split('\n'))
        if headersize != 64:
            print(sp, headersize)
            print(header)


