def addZeno(philoList):
    list = philoList[:]
    list.append('Zeno')
    return list

philosophers = [
    'Socrates',
    'Plato',
    'Aristotle'
]

morePhilosophers = addZeno(philosophers)

print(philosophers)
print(morePhilosophers)