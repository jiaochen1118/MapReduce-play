import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    mr.emit_intermediate(key,1)

def reducer(key,list_of_values):
    total = 0
    for v in list_of_values:
	total += v
    mr.emit((key,total))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
