def in_size(row):
    for left in range(1, row + 1):
        end = '\n' if left == row else '\t'
        print('%d * %d = %d' % (left, row, row * left), end=end)


for count in range(1, 10):
    in_size(count)
