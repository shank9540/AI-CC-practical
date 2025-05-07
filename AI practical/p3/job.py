def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  # sort by profit
    max_deadline = max(job[1] for job in jobs)
    result = [None] * max_deadline
    total_profit = 0

    for job in jobs:
        id, deadline, profit = job
        for i in range(deadline - 1, -1, -1):
            if result[i] is None:
                result[i] = id
                total_profit += profit
                break

    return result, total_profit

jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
scheduled_jobs, profit = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", profit)
