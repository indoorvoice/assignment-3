with open('filename') as f:
    data = [line.rstrip('/n' for line in open('filename'))]
# arena = [0 for x in range(999) for x in range(999)]

arena = [0 for x in range(10) for x in range(10)]


def occupy(s, v):
    """Switches a value from 0 to 1, representing a seat becoming occupied."""

    for row in range(s[0], v[0]):
        for col in range(s[1], v[1]):
            col = 1


def toggle(s, v):
    """Inverts between 0 and 1 for any value in range"""

    for row in range(s[0], v[0]):
        for col in range(s[1], v[1]):
            if col == 1:
                col = 0
            elif col == 0:
                col == 1
            else:
                print 'else activated'

def empty(s, v):
    """Switches a value from 1 to 0, representing a seat becoming empty."""

    for row in range(s[0], v[0]):
        for col in range(s[1], v[1]):