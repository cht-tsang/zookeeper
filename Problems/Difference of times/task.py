# put your python code here
hour1 = int(input())
minute1 = int(input())
second1 = int(input())

hour2 = int(input())
minute2 = int(input())
second2 = int(input())

time1 = ((hour1 * 60) * 60) + (minute1 * 60) + second1
time2 = ((hour2 * 60) * 60) + (minute2 * 60) + second2

print(time2 - time1)
