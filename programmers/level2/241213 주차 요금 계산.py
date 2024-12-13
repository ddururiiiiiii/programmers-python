from math import ceil

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees

    car = {}
    using_time = {}

    for record in records:
        time, number, io = record.split()
        hour, minute = map(int,time.split(":"))
        time = hour * 60 + minute

        if io == "IN":
            car[number] = time
        else :
            if number in using_time:
                using_time[number] += (time - car[number])
            else:
                using_time[number] = time - car[number]
            del car[number]

    for number, time in car.items():
        if number in using_time:
            using_time[number] += 1439 - time
        else:
            using_time[number] = 1439 - time

    for number, time in sorted(using_time.items(), key = lambda x:x[0]):
        answer.append(default_fee+ max(0,ceil((time-default_time)/unit_time)) * unit_fee)

    return answer