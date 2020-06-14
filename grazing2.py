def process(infile, outfile):
    with open(infile) as fin, open(outfile, 'w') as fout:
        K = int(fin.readline().strip())
        barren = set()
        for _ in range(K):
            singleBarren = tuple([int(__) for __ in fin.readline().strip().split()])
            barren.add(singleBarren)

        visited = set()
        visited.add((1, 1))
        dpReturn = dp((1, 1), visited, barren)
        fout.write("{}\n".format(dpReturn))


def dp(pos, visited, barren):
    if pos == (5, 5):
        if len(visited) + len(barren) != 25:
            return 0
        return 1

    # right, down, left, up
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    count = 0
    for d in dirs:
        posNew = (pos[0] + d[0], pos[1] + d[1])
        if posNew[0] > 5 or posNew[0] < 1 or posNew[1] > 5 or posNew[1] < 1:
            continue
        if posNew in barren:
            continue
        if posNew in visited:
            continue

        visited.add(posNew)
        count += dp(posNew, visited, barren)
        visited.remove(posNew)
    return count


def verify(index, outfile, testfile):
    out_data = [line.strip() for line in open(outfile)]
    test_data = [line.strip() for line in open(testfile)]
    print('{}. {}'.format(
        index,
        'success' if out_data == test_data else 'failure'
    ))


for i in range(1, 11):
    infile = '{}.in'.format(i)
    outfile = '{}.out'.format(i)
    testfile = '{}.out.test'.format(i)
    process(infile, testfile)
    verify(i, outfile, testfile)