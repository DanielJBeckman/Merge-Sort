def Mergesort(Nlist):
	if len(Nlist)>1:
		mid = len(Nlist)//2
		left = Nlist[:mid]
		right = Nlist[mid:]
		
		Mergesort (left)
		Mergesort (right)
		
		i=0
		j=0
		k=0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				Nlist[k]=left[i]
				i+=1
			else:
				Nlist[k]=right[j]
				j+=1
			k+=1
			
		while i < len(left):
			Nlist[k]=left[i]
			i+=1
			k+=1
		
		while j < len(right):
			Nlist[k]=right[j]
			j+=1
			k+=1
	
op = open("Numbers.txt", "r")
Nlist = []

for val in op.read().split(): 
	Nlist.append(int(val))

	

op.close

Mergesort(Nlist)
print (Nlist)
