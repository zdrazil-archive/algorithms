
table = [[] for x in range(10)]

def compute_hash(input):
    return len(input) % 10

def insert(input):
    position = compute_hash(input)
    table[position].append(input)

def remove(input):
    position = compute_hash(input)
    table[position].remove(input)
    
insert('tangerine')
insert('apple')
insert('momor')

print(table)
