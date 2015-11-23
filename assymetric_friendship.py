import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate((key,value),(value,key))

def reducer(key,list_of_value):
    mr.emit((value,value))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
    
