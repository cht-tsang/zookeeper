# put your python code here
length = int(input())
width = int(input())
height = int(input())

edge_sum = 4 * (length + width + height)

print(edge_sum)

surface = 2 * ((length * width) + (width * height) + (height * length))

print(surface)

volume = length * width * height

print(volume)
