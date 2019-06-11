d={1:"class",
   2:[3,[4,5,[6,7]]]
   }
#print"d 1[0]:",d 1[0]
#print"d 2[1:5]:",d 2[1:5]
print(d.keys())
print(d[2] [1] [2] [1])


for k,v in d.items():
    print (k,v)
    if k == 2:
        print (v[1][2][1])
        # lists occupy more memory than dictionaries 