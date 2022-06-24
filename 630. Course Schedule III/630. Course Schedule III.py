import heapq


def schedule_course(courses):
    courses.sort(key=lambda x: x[1])
    memo = [[-1] * (courses[-1][1] + 1) for _ in range(len(courses))]

    def schedule(i, time):
        if i == len(courses):
            return 0
        if memo[i][time] != -1:
            return memo[i][time]

        taken = 0
        if time + courses[i][0] <= courses[i][1]:
            taken = 1 + schedule(i + 1, time + courses[i][0])
        not_taken = schedule(i + 1, time)

        memo[i][time] = max(taken, not_taken)
        return memo[i][time]

    return schedule(0, 0)


def schedule_course_2(courses):
    courses.sort(key=lambda x: x[1])
    time, count = 0, 0
    for i in range(len(courses)):
        if time + courses[i][0] <= courses[i][1]:
            time += courses[i][0]
            count += 1
        else:
            max_i = i
            for j in range(i):
                if courses[j][0] > courses[max_i][0]:
                    max_i = j
            time -= courses[max_i][0] - courses[i][0]
            courses[max_i][0] = -1

    return count


def schedule_course_3(courses):
    courses.sort(key=lambda x: x[1])
    time, heap = 0, []
    for duration, end_time in courses:
        if time + duration <= end_time:
            time += duration
            heapq.heappush(heap, -duration)

        elif heap and -heap[0] > duration:
            time -= -heapq.heappop(heap) - duration
            heapq.heappush(heap, -duration)

    return len(heap)


courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print(schedule_course_3(courses))
