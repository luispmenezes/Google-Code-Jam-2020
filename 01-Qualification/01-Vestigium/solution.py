def main():
    t = int(input())

    for t_idx in range(1, t + 1):
        k, c, r = 0, 0, 0

        n = int(input())
        c_map = {}
        for i in range(n):
            c_map[i] = {}

        for i in range(n):
            row = list(map(int, input().split()))
            r_map = {}
            k += row[i]
            for j in range(n):
                # Check Row
                if r_map is not None:
                    if row[j] in r_map:
                        r += 1
                        r_map = None
                    else:
                        r_map[row[j]] = True
                # Check Column
                if j in c_map:
                    if not row[j] in c_map[j]:
                        c_map[j][row[j]] = True
                    else:
                        c += 1
                        del c_map[j]

        print('Case #%d: %d %d %d' % (t_idx, k, r, c))


if __name__ == '__main__':
    main()
