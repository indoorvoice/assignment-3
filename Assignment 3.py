#with open('filename') as f:
 #   data = [line.rstrip('/n' for line in open('filename'))]

for line in f:
    list_line = line.split() # make list of line elements
    csv_coord1, csv_coord2 = (line[1]).split(','), (line[3]).split(',') # separate coordinates
    x1, y1 = csv_coord1[0], csv_coord1[1] # assign initial coordinates for seating
    x2, y2 = csv_coord2[0], csv_coord2[1] # assign terminal coordinates for seating

# hard code for test, delete later
line = "empty 660,55 through 986,197"
line = line.split() # make list of line elements
csv_coord1, csv_coord2 = (line[1]).split(','), (line[3]).split(',')
print('1', csv_coord1)
print(csv_coord2)
x1, y1 = csv_coord1[0], csv_coord1[1]
x2, y2 = csv_coord2[0], csv_coord2[1]
print(x1, x2, y1, y2)

# arena = [[0 for x in range(999)] for x in range(999)]

# test with small array
arena = [[0 for x in range(10)] for x in range(10)]

#print(arena)

def occupy(s, v, array):
    """Switches a value from 0 to 1, representing a seat becoming occupied."""

    for row in range(s[0], s[1]):
        for col in range(v[0], v[1]):
            col = 1

def toggle(s, v, array):
    """Inverts between 0 and 1 for any value in range"""

    for row in range(s[0], s[1]):
        for col in range(v[0], v[1]):
            if col == 1:
                col = 0
            elif col == 0:
                col == 1
            else:
                print('else activated')
    return col


def empty(s, v, array):
    """Switches a value from 1 to 0, representing a seat becoming empty."""

    for row in range(s[0], v[0]):
        for col in range(s[1], v[1]):
            col = 0
    return col

occupy([0,9], [0,9], arena)

#print(arena)