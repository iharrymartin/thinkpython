import uuid
with open('wordschpt11.txt') as fd:
    words = fd.read().splitlines()
result = dict()
def dictionary():
    for line in wordschpt11:
        result[line] = uuid.uuid4()
    return result
print dictionary()
