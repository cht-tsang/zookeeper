deposit = int(input())

years = 0
while deposit < 700000:
    deposit += (deposit * (7.1 / 100))
    years += 1

print(years)
