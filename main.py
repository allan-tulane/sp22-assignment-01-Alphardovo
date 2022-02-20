"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<= 1:
      return x
    else: 
      return foo(x-1)+foo(x-2)
    pass

def longest_run(mylist, key):
    maxcount = 0
    count = 0
    for n in mylist:
        if n == key:
            count = count+1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
    return maxcount
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if not mylist:
      return Result(0, 0, 0, False)

    left, right = 0, len(mylist) - 1   # 0 1  2  3 4
    mid = (left + right) // 2
    cross_longest = 0

    # cross longest repeat
    if mylist[mid] == key:
        l = r = mid  
        while l >= 0 and mylist[l] == key:     
            l -= 1 
        while r < len(mylist) and mylist[r] == key:
            r += 1      
        cross_longest = r - l - 1  

    left_longest = longest_run_recursive(mylist[0:mid], key).longest_size
    right_longest = longest_run_recursive(mylist[mid + 1:], key).longest_size
    longest = max(left_longest, right_longest, cross_longest)

    res = Result(left_longest, right_longest, longest, all([num == key for num in mylist]))
    return res

    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
#    print(longest_run([2,12,12,8,12,12,12,0,12,1], 999))
#    print(longest_run([12,12,12,8,12,12,0,12,1], 12))
#    print(longest_run([6, 12, 12, 12, 12, 6, 6, 6], 12))

#test_longest_run()
