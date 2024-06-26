import jsonpickle
from model.project import Project
import random
import string
import os.path
import getopt
import sys

#"n:f:"-опции, n - кол-во генерируемых данных, f - задает файл в который все должно помещаться.
#["number of groups", "file"] - подсказки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of project", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/project.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*1
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("name", 10), description=random_string("description", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))