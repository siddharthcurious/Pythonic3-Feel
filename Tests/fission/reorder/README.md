Method - 1 
1. Convert indexes in iterable list of tuples
2. Sort it on the basis of first value
3. Read the other key value from json iteratring tupled indexes and insert key value in list.
4. Convert it back in dictionary and dump into a file
 

$ python reorder.py --input input.json --output `pwd` --index indexes

input json - `{
  "k4": "value4",
  "k1": "v1",
  "k9": "value9",
  "k8": "value8",
  "k5": "value5",
  "k7": "value7",
  "k6": "dummyvalue",
  "k2": "value2",
  "k3": "value3",
  "k10": "any_value",
  "indexes": {
    "1": "k5",
    "7": "k8",
    "2": "k1",
    "8": "k3",
    "6": "k4",
    "0": "k2",
    "3": "k9",
    "4": "k6",
    "5": "k7",
    "9": "k10"
  }
}
`

##### Notes
 Since dictionary and json are orderless order can't be graunted. The value from json can be access using key value method(hashing function).
  
  
Method - 2

1. Convert indexes in iterable list of tuples
2. Sort it on the basis of first value
3. Read the other key value from json iteratring tupled indexes and insert key value in list.
4. Start making a single json string and write it to file
 

$ python reorder_2.py --input input.json --output `pwd` --index indexes

input json - `{
  "k4": "value4",
  "k1": "v1",
  "k9": "value9",
  "k8": "value8",
  "k5": "value5",
  "k7": "value7",
  "k6": "dummyvalue",
  "k2": "value2",
  "k3": "value3",
  "k10": "any_value",
  "indexes": {
    "1": "k5",
    "7": "k8",
    "2": "k1",
    "8": "k3",
    "6": "k4",
    "0": "k2",
    "3": "k9",
    "4": "k6",
    "5": "k7",
    "9": "k10"
  }
}
`