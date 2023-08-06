import numpy as np

arr = [1, 2, 3, 7, 9]
window_size = 3

i = 0
moving_averages = []

while i < len(arr) - window_size + 1:
	window_average = round(np.sum(arr[
	i:i+window_size]) / window_size, 2)	
	moving_averages.append(window_average)
	i += 1

print(moving_averages)
