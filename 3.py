def binarySearch(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	          else:
	            return binarySearch(alist[midpoint+1:],item)
	
testlist = [0, 2, 6, 8, 13, 17, 18, 32, 49]
print(binarySearch(testlist, 90))
print(binarySearch(testlist, 13))
