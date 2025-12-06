import time
import numpy as np
from math import prod

start_time = time.perf_counter()

fp = '2025_day6_input.txt'

with open(fp, 'r') as file:
    lines = file.readlines()
    
    
rows = []

for line in lines:
	rows.append(line.strip().split())
      
def perform_op(numbers) -> int:
	if numbers[-1] == '+':
		return (numbers[0] + numbers[1] + numbers[2] + numbers[3])
	else:
		return (numbers[0] * numbers[1] * numbers[2] * numbers[3])
	
running_sum = 0

for i in range(len(rows[0])):
	numbers = (
		int(rows[0][i]),
		int(rows[1][i]),
		int(rows[2][i]),
		int(rows[3][i]),
		rows[4][i],
	)

	running_sum += perform_op(numbers)

time1 = time.perf_counter()

print(f'Part 1: {running_sum}\tTime: {(time1 - start_time):.6f}')

for i, line in enumerate(lines):
	lines[i] = line.strip()

rows = len(lines)
cols = len(lines[0])

digit_arr = np.zeros(shape=(rows, cols), dtype=str)


for i in range(cols):
	for j in range(rows):
		try:
			digit_arr[(j, i)] = lines[j][i]
		except:
			pass


digit_str = ''

digit_arr[(rows-1, cols-1)] = ' '

for i in range(cols-1, -1, -1):
	for j in range(rows):
		digit_str += digit_arr[(j, i)]


op_set = []
number_str = ''

running_sum = 0

for i, char in enumerate(digit_str):
	if char == ' ':
		if number_str == '':
			pass
		else:
			op_set.append(int(number_str))
		number_str = ''
	else:
		if char == '*':
			if number_str != '':
				op_set.append(int(number_str))
			number_str = ''
			result = prod(op_set)
			running_sum += result
			# print(f'mult {op_set} \t result: {result} \t\t running: {running_sum}')
			op_set = []
		elif char == '+':
			if number_str != '':
				op_set.append(int(number_str))
			number_str = ''
			result = sum(op_set)
			running_sum += result
			# print(f'add {op_set} \t result: {result} \t\t running: {running_sum}')
			op_set = []
		else:
			number_str += char

time2 = time.perf_counter()

print(f'Part 2: {running_sum}\tTime: {(time2-time1):.6f}')
