import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    row = record[1]
    col = record[2]
    if record[0] == 'a':
       for k in range(0,5):
           mr.emit_intermediate((row,k),("a",col,record[3]))
    if record[0] == 'b':
       for k in range(0,5):
           mr.emit_intermediate((k,col),("b",row,record[3]))

def reducer(key,list_of_values):
    a = [0] * 5
    b = [0] * 5
    for v in list_of_values:
        if v[0] == 'a':
             a[v[1]] = v[2]
        else:
             b[v[1]] = v[2]
    sum = 0
    for i in range(0,5):
        sum += a[i] * b[i]
    mr.emit((key,sum))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
       
