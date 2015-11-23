import sys
import MapReduce
mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for word in words:
        mr.emit_intermediate(word.lower(),key)

def reducer(key, list_of_value):
    mr.emit((key, list_of_value))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

