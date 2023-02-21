# CS331 Assignment 2 v1.1, 09/15/2022

# In this assignment, you are asked to implement methods in the ArrayList class.

class ArrayList:

    # Please implement each of the following methods. Here, I've only implemented the construction method.
    # Consider self.array as an array instead of a list. Do not use the build-in methods of a list.
    # You may use only the following list/array methods in implementation:
    # 1. get the length of an array/list, for example: l = len(array)
    # 2. get the value at index i or values between indices i to j, for example: b = array[i], array1 = array[i:j]
    # 3. set value at index i or values between indices i to j, for example: array[i] = c, array [1:3] = [4,6]

    def __init__(self, n: int):
        # An ArrayList has two attributes:
        # 1. an array of with n slots
        # 2. an integer called "size" that represent the number of items in the ArrayList (initially it equals to 0)
        self.array = [None] * n
        self.size = 0

    def getsize(self) -> int:
        # Return the number of items in the ArrayList
        return self.size
        pass

    def getarray(self) -> []:
        # Return self.array
        return self.array
        pass

    def isEmpty(self) -> bool:
        # Return whether the size of the ArrayList is 0.
        if self.size == 0:
            return True
        else:
            return False
        pass

    def isFull(self) -> bool:
        # Return whether the size of the ArrayList equals to the length of self.array.
        if self.size == len(self.array):
            return True
        else:
            return False
        # This method is called in append().
        pass

    def doubleSize(self):
        # Create a new array and copy all items in self.array to the new array.
        self.arrayNew = [None] + self.array
        # The new array has doubled length compared to self.array.
        self.size = self.size * 2
        # Assign the new array to be self.array.
        self.array = self.arrayNew
        # This method is called in append() if self.array is full.
        # Do not return anything.
        pass

    def index(self, i):
        # Return the item in the self.array at index i.
        return self.array[i]
        pass

    def slice(self, i, j) -> []:
        # Return items in self.array[i : j] as an array
        tempArray = []
        for x in range(i, j):
            tempArray.append(x)
            self.array = tempArray
        return self.array
        pass

    def linearSearch(self, item) -> int:
        # Use linear search algorithm to find the location of item in self.array.

        # If the item is not there, return -1.
        # You may consider the items in the ArrayList are int.
        # Remind that, items are stored from index 0 to index self.size - 1.
        pass

    def binarySearch(self, item) -> int:
        # Use binary search algorithm to find the location of item in the sorted self.array.
        left = 0
        right = len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == item:
                return mid
            elif self.array[mid] > item:  # item is smaller than mid, look left
                right = mid - 1

            else:  # self.array[mid] < item, item is greater than mid, look right
                left = mid + 1
        # If the item is not there, return -1.
        return -1
        # You may consider the items in the ArrayList are int.
        # Remind that, items are stored from index 0 to index self.size - 1.
        pass

    def pop(self):
        # Return the last item in an ArrayList.
        return self.array[self.size - 1]
        # That item will be no longer in the ArrayList after pop().
        self.array.remove[self.size - 1]
        # Remind that, the size of the ArrayList will be reduced by 1 after pop().
        self.size = self.size - 1
        pass

    def pop_i(self, i):
        # Return the item in an ArrayList at index i.
        return self.array[i]
        # That item will be no longer in the ArrayList after pop_i().
        self.array.remove[i]
        # Remind that, the size of the ArrayList will be reduced by 1 after pop_i();
        self.size = self.size - 1
        # and all items after index i need to be moved one spot to the left.
        j = self.size - 1
        while j > i:
            self.array[j] = self.array[j-1]
            j = j-1
        pass

    def remove(self, item):
        # Assume that item is in the ArrayList.
        # Find the item and remove it from the ArrayList.
        self.array.pop(item)
        # Do not return anything.
        # Remind that, the size of the ArrayList will be reduced by 1 after remove();
        self.size = self.size - 1
        # and all items after the item need to be moved one spot to the left.
        j = self.size - 1
        i = 0
        while j > i:
            self.array[j] = self.array[j - 1]
            j = j - 1
        pass

    def max(self):
        # Return the item with maximum value.
        for x in self.array:
            if x > x + 1:
                max = x
            else:
                max = x + 1
        # You may consider the items in the ArrayList are int.
        return max
        pass

    def min(self):
        # Return the item with minimum value.
        x = 0
        for x in self.array:
            if x < x + 1:
                min = x
            else:
                min = x + 1
        # You may consider the items in the ArrayList are int.
        return min
        pass

    def append(self, item):
        # Append item to the next available spot in the ArrayList.
        # Remind that, check whether self.array is full first;
        if self.array:
            self.array.append(item)
            self.size = self.size + 1
        # if it is full, call doubleSize() to enlarge it.
        else:
            self.array.doubleSize()
        # Remind that, the size of the ArrayList will be increased by 1 after append().
        # Do not return anything.
        pass

    def insert(self, i, item):
        # Insert item at index i.
        # Remind that, you also need to check whether self.array is full first.
        if self.array:
            return self.array
        else:
            self.array.insert(i, item)
            self.size = self.size() + 1
        # Remind that, the size of the ArrayList will be increased by 1 after insert().
        # Do not return anything.
        pass

    def bubbleSort(self):
        # Use bubble sort algorithm to sort items in self.array.
        # You may consider the items in the ArrayList are int.
        # Remind that, items are stored from index 0 to index self.size - 1.
        # Do not return anything.
        n = len(self.array)
        temp = 0
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    swapped = True
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            if not swapped:
                return
        pass

    def mergesort(self, p: int, r: int):
        # Use merge sort algorithm to sort items in self.array[p:r+1].
        # You may consider the items in the ArrayList are int.
        # Users will call self.mergesort(0, self.size - 1) to merge sort the whole ArrayList.
        # Do not return anything.
        if p >= r:
            return

        m = (p + r) // 2
        self.mergesort(p, m)
        self.mergesort(m+1, r)
        self.merge(p, r, m)
        pass

    def merge(self, p: int, q: int, r: int):
        # This is a helper method for mergesort(p, r).
        # Merge the sorted self.array[p: q+1] and sorted self.array[q+1: r+1] into
        # sorted self.array[p: r+1].
        # Do not return anything.
        self.array[p: r + 1] = self.array[p: q + 1] + self.array[q + 1: r + 1]
        pass

    def __iter__(self):
        # return an AL_iterator object as the iterator for ArrayList.
        # The iterator object should iterate on self.array, starts at index 0, end at index self.size
        yield self.AL_iterator(self.array, 0, len(self.array))
        for x in self.array:
            yield x
        pass

    class AL_iterator:
        # This is a helper class that's used to create ArrayList iterator object.
        # Here, I've only implemented the construction method.

        def __init__(self, array, start, end):
            # ArrayList iterator has four attributes:
            # 1. an array it iterates on: array
            # 2. starting index: start
            # 3. ending index: end
            # 4. a pointer that point the current location
            self.array = array
            self.start = start
            self.end = end
            self.pointer = start

        def __iter__(self):
            # return the ArrayList iterator object itself
            yield AL_iterator()
            pass

        def __next__(self):
            # If self.pointer is smaller than self.end, then return the next item in self.array,
            if self.pointer < self.end:
                return self.array[pointer + 1]
            # and increase the pointer at the same time.
                self.pointer += 1
            # Else, raise the StopIteration() exception
            else:
                raise StopIteration()
            pass


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################

print("We start with an empty testList with 4 available slots.")
testList = ArrayList(4)
testList.append(10)
testList.append(4)
testList.append(5)
testList.append(9)
string1 = "After appending 4 items, the testList should be full now, and your result is "
if testList.isFull():
    string1 = string1 + "correct."
else:
    string1 = string1 + "wrong."
print(string1)
testList.append(8)
testList.append(2)
testList.append(3)
testList.append(1)
testList.append(6)
testList.append(7)
print("After appending another 6 items, "
      "there should be 10 items in the list now, and your result says", testList.getsize(), ".")
print("The testList should have 16 slots in total at this moment, "
      "and your result says", len(testList.getarray()), ".")
print("The whole testList is currently", testList.getarray(), ".")
testList.remove(10)
testList.insert(2, 11)
print("After removing number 10 and inserting number 11 to the 3rd slot, "
      "the testList becomes" , testList.slice(0,testList.getsize()), ".")
print("The maximum number in the list is", testList.max(), ", and the minimum is", testList.min(), ".")
testList1 = testList
testList.bubbleSort()
print("If we bubble sort the testList, we get",
      testList.slice(0,testList.getsize()), "; then we can use binary "
                                       "search to find number 11 is at slot number", testList.binarySearch(11)+1, ".")
testList1.mergesort(0,testList1.getsize()-1)
print("Now we rewind the sorting procedure "
      "and re-sort the testList using mergesort, we also get", testList.slice(0,testList.getsize()), ".")
print("We pop out the item at the 4th slot, it is number",
      testList1.pop_i(3),"; the testList becomes", testList.slice(0,testList.getsize()), ".")
tl_iter = testList1.__iter__()
print("Using the iterator of testList, we can print out items in testList one by one:")
for item in testList1:
    print(item)

