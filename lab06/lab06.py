this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    time = 0
    def helper(b):
        nonlocal time
        tmp = a + b + time
        time = time + 1
        return tmp
    return  helper

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    # times = 0
    # fab = []
    # def helper():
    #     nonlocal times,fab
    #     if times == 0:
    #         times = times + 1
    #         fab.append(0)
    #         return 0
    #     if times == 1:
    #         times = times + 1
    #         fab.append(1)
    #         return 1
    #     res = fab[len(fab)-1] + fab[len(fab)-2]
    #     fab.append(fab[len(fab)-1] + fab[len(fab)-2])
    #     return res
    # return helper
    ##上面的代码实现用了列表，课程要求不允许用列表
    fab0, fab1 = 0, 1
    def helper():
        nonlocal fab0,fab1
        ans = fab0
        fab0,fab1 = fab1,fab1 + fab0
        return ans
    return helper



def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    ##lst是传值还是传址
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            lst.insert(index + 1,elem)
            index = index + 1
        index = index + 1
    return lst

