import math

FILE_YAKOBY = './Yakoby.txt'
EPS = 10**(-4)
MAX_ITERTIONS = 500

def norma(curr, prev):
    return math.sqrt(sum([z**2 for z in list(map(lambda x, y: x - y, curr, prev))]))

def yakoby():
    with open(FILE_YAKOBY) as file:
        slay = [list(map(float, x)) for x in [line for line in list(map(str.split, file.readlines()))]]

    for i in range(len(slay)):
        for j in range(len(slay[i])):
            if i != j:
                slay[i][j] /= (-slay[i][i] if j != (len(slay[i]) - 1) else slay[i][i])
        slay[i].pop(i)

    counter = 0
    prev_solution = [row[-1] for row in slay]
    while True:
        curr_solution = []
        for i in range(len(slay)):
            tmp = 0
            prev_solution_tmp = prev_solution[0:i] + prev_solution[i+1:]
            for j in range(len(slay[i]) - 1):
                tmp += slay[i][j] * prev_solution_tmp[j]
            else:
                tmp += slay[i][j+1]
            curr_solution.append(tmp)
        counter += 1
        print(f'iter {counter}',curr_solution)
        if norma(curr_solution, prev_solution) < EPS or counter > MAX_ITERTIONS:
            break
        else:
            prev_solution = curr_solution
    print(f'Your solution is {curr_solution}')

if __name__ == "__main__":
    yakoby()
