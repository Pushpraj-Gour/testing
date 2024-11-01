def split_answer_into_body_and_conclusion(answer):
	body, conclusion = '', None
	for line in answer.splitlines(keepends=True):
		if conclusion is None:
			if 'Conclusion:' in line or 'Key Takeaways:' in line:
				conclusion = line
			else:
				body += line
		else:
			conclusion += line

	if conclusion is None:
		body, conclusion = '', None
		for line in answer.splitlines(keepends=True):
			if conclusion is None:
				if 'Conclusion' in line or 'Key Takeaways' in line:
					conclusion = line
				else:
					body += line
			else:
				conclusion += line
	
	if conclusion is None:
		body, conclusion = '', None
		for line in answer.splitlines(keepends=True):
			if conclusion is None:
				if 'conclusion' in line or 'key takeaways' in line:
					conclusion = line
				else:
					body += line
			else:
				conclusion += line

	if ':' in conclusion:
		conclusion = conclusion.split(':', 1)[1]
	elif 'In conclusion, ' in conclusion:
		conclusion = conclusion.split('In conclusion, ', 1)[1]
	
	return body, conclusion

# def create_batches(l: list, batch_size: int, max_batch_size=-1):			
# 	# A batch can be batch_size or max_batch_size
	
# 	assert max_batch_size == -1 or max_batch_size == batch_size + 1
# 	if max_batch_size == -1:
# 		max_batch_size = batch_size + 1
	
# 	batches = []
# 	for i in range(0, len(l), batch_size):
# 		batches.append(l[i:i + batch_size])

# 	size_of_last_batch = len(batches[-1])

# 	increased_capacity_per_batch = max_batch_size - batch_size
# 	if size_of_last_batch <= increased_capacity_per_batch * (len(batches) - 1):			# If possible, distribute the last batch to the previous batches
# 		batches = []
# 		cur_size = size_of_last_batch
# 		cur_batch_size = max_batch_size

# 		i = 0
# 		while (i < len(l)):
# 			batches.append(l[i:i + cur_batch_size])
# 			i += cur_batch_size

# 			cur_size -= increased_capacity_per_batch
# 			if cur_size == 0:
# 				cur_batch_size = batch_size


# 	return batches


def create_batches(l: list, batch_size: int, max_batch_size=-1):			
	# A batch can be batch_size or max_batch_size

	assert max_batch_size == -1 or max_batch_size == batch_size + 1
	if max_batch_size == -1:
		max_batch_size = batch_size + 1

	total_element = len(l)
	last_batch_size = total_element % batch_size

	if last_batch_size==0:  #Perfect fit
		batches = []
		for i in range(0, len(l), batch_size):
			batches.append(l[i:i + batch_size])

	else:
		# 1. Pop the last batch and distrubte its elements to the remaining batches
		# 2. rearrange the elements of last batch by keeping the number of batches same

		num_batches  = (total_element//batch_size) +1
		increased_capacity_per_batch = max_batch_size - batch_size

		if last_batch_size<=(num_batches-1) and last_batch_size<=(batch_size//2):

			batches = []
			cur_size = last_batch_size
			cur_batch_size = max_batch_size
			i = 0
			while (i < len(l)):
				batches.append(l[i:i + cur_batch_size])
				i += cur_batch_size
				cur_size -= increased_capacity_per_batch
				
				if cur_size == 0:
					cur_batch_size = batch_size
		else:

			adjusted_batch_size  = (total_element//num_batches)  # (15 element , 6 batch_size)--> adj_batch_size = 5  -->(5,5,5)

			if total_element%num_batches!=0:  #but if the num_batches can fit the elements but the batch_size but there is reminder while calculating adj_batch_size (e.g. 16 element, 6 batch_size)  --> adj_batch_size = 6 --> (6,5,5)
				adjusted_batch_size+=1

			batches = []
			i =0
			while i<len(l):
				batches.append(l[i:i+adjusted_batch_size ])
				num_batches-=1
				total_element-=adjusted_batch_size 
				i+=adjusted_batch_size 

				# Checking if the remaining element can be distributed equally to the remaining batches
				if (total_element>0 and total_element % num_batches==0):
					adjusted_batch_size  = total_element//num_batches 
	return batches

def test_helper_1():

	assert create_batches([1, 2, 3, 4, 5, 6, 7], 2) == [[1, 2, 3], [4, 5], [6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3, 4], [5, 6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 4) == [[1, 2, 3, 4], [5, 6, 7]]         
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 5) == [[1, 2, 3, 4], [5, 6, 7]]         
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 6) == [[1, 2, 3, 4, 5, 6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 7) == [[1, 2, 3, 4, 5, 6, 7]]  
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3) == [[1, 2, 3], [4 ,5 , 6], [7 ,8 ,9,], [10, 11]]  

	# Address this distribution. Ideally, it should be: 8, 8, 7
	# assert helper(list(range(1, 24)), 10) == [list(range(1, 11)), list(range(11, 21)), list(range(21, 24))]
	assert create_batches(list(range(1,24)),10) == [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23]]

	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
	assert create_batches(list(range(1, 30)), 7) == [[1, 2, 3, 4, 5, 6, 7, 8],
											 [9, 10, 11, 12, 13, 14, 15],
											 [16, 17, 18, 19, 20, 21, 22],
											 [23, 24, 25, 26, 27, 28, 29]]
	
	assert create_batches([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]  
	assert create_batches(list(range(1, 16)), 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15]]
	assert create_batches(list(range(1,16)),6) == [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
	assert create_batches(list(range(1,29)),10) == [list(range(1,11)),list(range(11,20)),list(range(20,29))]
	assert create_batches(list(range(1,27)),9) == [list(range(1,10)),list(range(10,19)),list(range(19,27))]
	assert create_batches(list(range(1,27)),8) == [list(range(1,10)),list(range(10,19)),list(range(19,27))]
	assert create_batches(list(range(1,17)),3) == [list(range(1,5)),
												list(range(5,8)),
												list(range(8,11)),	
												list(range(11,14)),
												list(range(14,17))]


test_helper_1()

data = create_batches(list(range(1,989)),100) 
for item in data:
	print(len(item),end=",")
print()

data = create_batches(list(range(1,89)),10) 
for item in data:
	print(len(item),end=",")
print()

data = create_batches(list(range(1,105)),30)
for item in data:
	print(len(item),end=",")
print()

data = create_batches(list(range(1,18)),15)
for item in data:
	print(len(item),end=",")
print()

data = create_batches(list(range(1,26)),8)
for item in data:
	print(len(item),end=",")
print()

data = create_batches(list(range(1,35)),7)
for item in data:
	print(len(item),end=",")
print()