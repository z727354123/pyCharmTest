# range(0)
rangeA = range(0)
rangeB = range(1)

if rangeB:
    print('rangeB = True')
else:
    print('rangeB = False')
if rangeA:
    print('rangeA = True')
else:
    print('rangeA = False')
    print('\n----------\n')

# list []
listA = []
listB = [1]

if listB:
    print('listB = True')
else:
    print('listB = False')
if listA:
    print('listA = True')
else:
    print('listA = False')
    print('\n----------\n')


# tuple []
tupleA = ()
tupleB = 1,

print(type(tupleA))
print(type(tupleB))
if tupleB:
    print('tupleB = True')
else:
    print('tupleB = False')
if tupleA:
    print('tupleA = True')
else:
    print('tupleA = False')
    print('\n----------\n')
