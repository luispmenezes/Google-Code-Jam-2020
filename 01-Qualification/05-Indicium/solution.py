import math


def exists_in_column(matrix, n, j, value):
    for i in range(n):
        if matrix[i][j] == value:
            return True
    return False


def main():
    t = int(input())

    for t_idx in range(1, t + 1):
        input_params = list(map(int, input().split()))
        n = input_params[0]
        k = input_params[1]
        is_possible = True
        matrix = [[0 for i in range(n)] for j in range(n)]

        if k > (n * n) or k < n:
            is_possible = False
        else:
            # Fill Diag
            total = 0
            digit_counter = {k: 0 for k in range(1, n + 1)}
            for i in range(n):
                matrix[i][i] = math.ceil(float(k - total) / float(n - i))
                total += matrix[i][i]
                digit_counter[matrix[i][i]] += 1

            for digit in digit_counter:
                if digit_counter[digit] == n - 1:
                    is_possible = False

            # Fill Mat
            if is_possible:

                total_inserts = n
                possibilities = []
                while total_inserts < n * n:
                    for value in range(1, n + 1):
                        for i in range(n):
                            if value not in matrix[i]:
                                possible_places = []
                                for j in range(n):
                                    if matrix[i][j] == 0 and not exists_in_column(matrix, n, j, value):
                                        possible_places.append(j)
                                if len(possible_places) > 0:
                                    possibilities.append((possible_places, i, value))

                    possibilities.sort(key=lambda tup: len(tup[0]))

                    while len(possibilities) >= 1 and len(possibilities[0][0]) == 1:
                        matrix[possibilities[0][1]][possibilities[0][0][0]] = possibilities[0][2]
                        possibilities = possibilities[1:]
                        total_inserts += 1

                    if len(possibilities) >= 1:
                        if len(possibilities) >= 2 and total_inserts != n:
                            print("implementa-me porca")
                        matrix[possibilities[0][1]][possibilities[0][0][0]] = possibilities[0][2]
                        total_inserts += 1

        print("Case #%d: %s" % (t_idx, "POSSIBLE" if is_possible else "IMPOSSIBLE"))
        if is_possible:
            for i in range(n):
                print(*matrix[i])


if __name__ == '__main__':
    main()
