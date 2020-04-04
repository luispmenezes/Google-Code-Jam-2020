def main():
    t = int(input())

    for t_idx in range(1, t + 1):
        n = int(input())

        result = []

        latest_start_time = [9999, 9999]
        activities = []

        for n_idx in range(n):
            activities.append((n_idx,) + tuple(map(int, input().split())))
            result.append('')

        activities.sort(key=lambda tup: tup[1], reverse=True)

        for activity in activities:
            person_idx = 0

            if latest_start_time[1] < latest_start_time[0]:
                person_idx = 1

            if activity[2] <= latest_start_time[person_idx]:
                result[activity[0]] = "C" if person_idx == 0 else "J"
                latest_start_time[person_idx] = activity[1]
            elif activity[2] <= latest_start_time[int(not person_idx)]:
                result[activity[0]] = "C" if int(not person_idx) == 0 else "J"
                latest_start_time[int(not person_idx)] = activity[1]
            else:
                result = list("IMPOSSIBLE")
                break

        print('Case #%d: %s' % (t_idx, ''.join(result)))


if __name__ == '__main__':
    main()
