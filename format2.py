import csv


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)



#random_list_of_nums = ['Betty had some ','butter','but the ','butter','was bitter','so she bought another','butter to make','the bitter','butter better']
#quick_sort(random_list_of_nums)
#print(random_list_of_nums)

#print('a'>'Asbsnjdkdke')

csv_read=open('FP_Part-2_new.csv','r',newline='')
obj_r=csv.reader(csv_read)

csv_write=open('FP_Part-2_real_new.csv','w',newline='')
obj_w=csv.writer(csv_write)

for row in obj_r:
	quick_sort(row)
	l=list()
	k=0
	for i in range(0,len(row)):
		if(i!=0):
			if(row[i]==l[k]):
				continue
			else:
				k+=1	
		l.append(row[i])
	obj_w.writerow(l)
	
csv_write.close()			