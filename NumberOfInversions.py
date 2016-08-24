"""
    Count Number of Inversions in array using Divide and Conqure Paradigm
    ********* Using MergeSort Trick, We can count inversions in O(nlog(n)) Time ! *****
"""

def countInversions(array):
    if(len(array) == 1):
        return (array,0)
    x = countInversions(array[0:len(array)/2])
    y = countInversions(array[len(array)/2:])
    z = mergeAndCount(x[0],y[0])
    return (z[0],(x[1]+y[1]+z[1]))


def mergeAndCount(a1,a2):
    mergedArray = []
    NumberOfInversions = 0
    # Please note that we remove elements from sub arrays that's why we get rid of pointers
    while(len(a1)>0 and len(a2)>0):
        if(a1[0] > a2[0]):
            mergedArray.append(a2[0])
            a2.remove(a2[0])
            NumberOfInversions = NumberOfInversions + (len(a1)) # we need to count what is still in a1
        else:
            mergedArray.append(a1[0])
            a1.remove(a1[0])

    if(len(a1)>0):
        mergedArray.extend(a1)

    if(len(a2)>0):
        mergedArray.extend(a2)

    return (mergedArray,NumberOfInversions)

# Testing By Example :)

x = [1,3,5,2,4,6]
y = countInversions(x)
print "Sorted Array is => ",y[0]
print "Number of Inversions is => ", y[1]
