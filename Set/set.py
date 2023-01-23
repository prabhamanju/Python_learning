s = set('HackerRank')
print(s)
s.add('H')
print(s)
"""
If we want to add a single element(uniq) to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.
"""
s.add('HackerRank')
print(s)