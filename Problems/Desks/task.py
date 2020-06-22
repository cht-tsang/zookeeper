# put your python code here
input_one = abs(int(input()))
input_two = abs(int(input()))
input_three = abs(int(input()))

desk_one = (input_one // 2) + (input_one % 2)
desk_two = (input_two // 2) + (input_two % 2)
desk_three = (input_three // 2) + (input_three % 2)

total = desk_one + desk_two + desk_three

print(total)
