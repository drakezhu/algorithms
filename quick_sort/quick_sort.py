



def q_sort(ray):

	if len(ray) <= 1:
		return ray
	# elif len(ray) == 2:
	# 	print (ray)
	# 	if ray[0] >= ray[1]:
	# 		swap(ray,0,1)
	# 	return ray

	#print (ray)
	pivot = ray[0]
	L = 1
	R = len(ray) - 1
	while L <= R:
		if ray[L] < pivot:
			L += 1
		elif ray[R] > pivot:
			R -= 1
		else:
			swap(ray,L,R)
			L += 1
			R -= 1
		#print (ray)
	swap(ray,0,R)


	return q_sort(ray[0:R]) + [ray[R]] + q_sort(ray[L:])

	
	#return q_sort(ray[0:R]) + q_sort(ray[L:])

def swap(ray, i, j):
	temp = ray[i]
	ray[i] = ray[j]
	ray[j] = temp






