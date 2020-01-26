nums = [
1,0,0,3,
1,1,2,3,
1,3,4,3,
1,5,0,3,
2,10,1,19,
1,19,9,23,
1,23,6,27,
2,27,13,31,
1,10,31,35,
1,10,35,39,
2,39,6,43,
1,43,5,47,
2,10,47,51,
1,5,51,55,
1,55,13,59,
1,59,9,63,
2,9,63,67,
1,6,67,71,
1,71,13,75,
1,75,10,79,
1,5,79,83,
1,10,83,87,
1,5,87,91,
1,91,9,95,
2,13,95,99,
1,5,99,103,
2,103,9,107,
1,5,107,111,
2,111,9,115,
1,115,6,119,
2,13,119,123,
1,123,5,127,
1,127,9,131,
1,131,10,135,
1,13,135,139,
2,9,139,143,
1,5,143,147,
1,13,147,151,
1,151,2,155,
1,10,155,0,
99,2,14,0,0
]


# create a way to separate the list into 4 chunks at a time
def chunks(a, z, inputLst):
    chunk = inputLst[a:z]
    return chunk

# process one chunk, move on to the next, break if we hit 99 in index 0
def opCode(inputLst):
    a = 0
    z = 4
    while z < len(inputLst):
        chunk = chunks(a, z, inputLst)
        if chunk[0] == 1:
            inputLst[chunk[3]] = inputLst[chunk[1]] + inputLst[chunk[2]]
        elif chunk[0] == 2:
            inputLst[chunk[3]] = inputLst[chunk[1]] * inputLst[chunk[2]]
        elif chunk[0] == 99:
            print(f'item at {a} was 99')
            break
        a += 4
        z += 4
        print(chunk)
        print(f'step {z//4-1}')


# run function

def findNounVerb(inputLst):
    # copy input to a new list
    testLst = inputLst.copy()
    for i in range(0, 98):
        for j in range(0, 98):
            testLst[1] = i
            testLst[2] = j
            solution = [i, j]
            #print(solution)
            #print(inputLst)
            opCode(testLst)
            if testLst[0] == 19690720:
                return 100 * solution[0] + solution[1]
            else:
                # copy clean list into new list
                testLst = inputLst.copy()
                #print(testLst)
                pass


print(findNounVerb(nums))
