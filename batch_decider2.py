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

def create_batches(l: list, batch_size: int, max_batch_size=-1):			
	# A batch can be batch_size or max_batch_size
	
	assert max_batch_size == -1 or max_batch_size == batch_size + 1
	if max_batch_size == -1:
		max_batch_size = batch_size + 1
	
	batches = []
	for i in range(0, len(l), batch_size):
		batches.append(l[i:i + batch_size])

	size_of_last_batch = len(batches[-1])

	increased_capacity_per_batch = max_batch_size - batch_size
	if size_of_last_batch <= increased_capacity_per_batch * (len(batches) - 1):			# If possible, distribute the last batch to the previous batches
		batches = []
		cur_size = size_of_last_batch
		cur_batch_size = max_batch_size

		i = 0
		while (i < len(l)):
			batches.append(l[i:i + cur_batch_size])
			i += cur_batch_size

			cur_size -= increased_capacity_per_batch
			if cur_size == 0:
				cur_batch_size = batch_size


	return batches

def test_create_batches_1():
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 2) == [[1, 2, 3], [4, 5], [6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3, 4], [5, 6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 4) == [[1, 2, 3, 4], [5, 6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 5) == [[1, 2, 3, 4, 5], [6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 6) == [[1, 2, 3, 4, 5, 6, 7]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 7) == [[1, 2, 3, 4, 5, 6, 7]]


	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
	assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]

	# Address this distribution. Ideally, it should be: 8, 8, 8
	assert create_batches(list(range(1, 24)), 10) == [list(range(1, 11)), list(range(11, 21)), list(range(21, 24))]

def test_create_batches_2():
	assert create_batches([1, 2, 3, 4, 5, 6, 7], 2, 4) == [[1, 2, 3], [4, 5], [6, 7]]
	
	# assert create_batches([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3, 4], [5, 6, 7]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7], 4) == [[1, 2, 3, 4], [5, 6, 7]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7], 5) == [[1, 2, 3, 4, 5], [6, 7]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7], 6) == [[1, 2, 3, 4, 5, 6, 7]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7], 7) == [[1, 2, 3, 4, 5, 6, 7]]


	# assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
	# assert create_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]


test_create_batches_1()
# test_create_batches_2()