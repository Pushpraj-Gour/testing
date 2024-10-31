def helper2(data,batch_size):
    batches = []
    for i in range(0,len(data),batch_size):
        batches.append(data[i:i+batch_size])

    return batches

def sir_function(l: list, batch_size: int, max_batch_size=-1):			
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

def helper(data,batch_size):
    
    total_element = len(data)
    if total_element%batch_size==0:  # Perfect Batches
        batches = helper2(data,batch_size)
    
    else:  # Last Batch Problem
        
        last_batch_element = total_element%batch_size
        total_batches = (total_element//batch_size) +1

        if last_batch_element<=(total_batches-1) and last_batch_element<=(batch_size//2): 
        	# We will pop the last batch and redistribute it's element to the remaining batches
            batches = sir_function(data,batch_size)

        else:
            # We will redistrubte elements by changing batch size----> keeping total number of batches same
            adj_batch_size = (total_element//total_batches) + 1
            batches = helper2(data,adj_batch_size)

    return batches

	
def test_helper_1():

    assert helper([1, 2, 3, 4, 5, 6, 7], 2) == [[1, 2, 3], [4, 5], [6, 7]]
    assert helper([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3, 4], [5, 6, 7]]
    assert helper([1, 2, 3, 4, 5, 6, 7], 4) == [[1, 2, 3, 4], [5, 6, 7]]         
    assert helper([1, 2, 3, 4, 5, 6, 7], 6) == [[1, 2, 3, 4, 5, 6, 7]]
    assert helper([1, 2, 3, 4, 5, 6, 7], 7) == [[1, 2, 3, 4, 5, 6, 7]]  
    assert helper([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert helper([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    assert helper([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    assert helper([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]

    # Address this distribution. Ideally, it should be: 8, 8, 7
    # assert helper(list(range(1, 24)), 10) == [list(range(1, 11)), list(range(11, 21)), list(range(21, 24))]
    assert helper(list(range(1,24)),10) == [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23]]

    assert helper([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
    assert helper(list(range(1, 30)), 7) == [[1, 2, 3, 4, 5, 6, 7, 8],
                                             [9, 10, 11, 12, 13, 14, 15],
                                             [16, 17, 18, 19, 20, 21, 22],
                                             [23, 24, 25, 26, 27, 28, 29]]
    
    assert helper([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
    assert helper([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]  
    assert helper(list(range(1, 16)), 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15]]

test_helper_1()
