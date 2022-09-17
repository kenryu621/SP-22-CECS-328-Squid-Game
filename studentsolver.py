import copy


def solve(x, n):
    if x <= 0 or n <= 0 or x > n:
        return 0
    elif x == n:
        return 1
    else:
        going = [[[] for row in range(x)]]
        temp_num = 0
        working_attempt = len(going)
        while temp_num != n:
            temp_num += 1
            for i in range(working_attempt):
                for z in range(len(going[i])-1, -1, -1):
                    temporary = copy.deepcopy(going[i])
                    temporary[z].append(temp_num)
                    if len(temporary[z]) == 1 or ((temporary[z][-1] + temporary[z][-2]) ** (1/2)).is_integer() is True:
                        curr = copy.deepcopy(temporary)
                        if sorted(curr) not in going:
                            going.append(sorted(curr))
                    temporary[z].pop(-1)
            for j in range(working_attempt):
                going.pop(0)
            working_attempt = len(going)
        for i in range(len(going)-1, -1, -1):
            if [] in going[i]:
                going.pop(i)
    return len(going)
