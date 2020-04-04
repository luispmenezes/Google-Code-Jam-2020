def main():
    t = int(input())

    for t_idx in range(1, t + 1):
        s = input()
        new_s = ""
        current_depth = 0

        for n in s:
            new_depth = int(n)
            if new_depth > current_depth:
                new_s += "(" * (new_depth - current_depth)
            elif new_depth < current_depth:
                new_s += ")" * (current_depth - new_depth)
            new_s += n
            current_depth = new_depth

        new_s += ")" * current_depth

        print('Case #%d: %s' % (t_idx, new_s))


if __name__ == '__main__':
    main()
