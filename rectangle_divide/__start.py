import greatest_common_divisor as gcd
import rectangle_divide as rd
import json

filename = 'rectangle_divide_solution.json'

a=input()
b=input()
a=int(a)
b=int(b)
gcdn=gcd.gcd(a,b)
a,b=int(a/gcdn),int(b/gcdn)

with open(filename) as fobj:
    rd.solution = json.load(fobj)
print(rd.rectangle_divide(a, b))
with open(filename, 'w+') as fobj:
    json.dump(rd.solution, fobj)