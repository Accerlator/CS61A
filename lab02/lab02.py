
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    # def g(x):
    #     def f(y):
    #         return func(x,y)
    #     return f
    # return g
    ##上面是不用匿名函数的写法，下面用匿名函数来写
    return lambda x:(lambda y:func(x,y))



def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def count_sum(n):
        i = 1
        res = 0
        while i <= n:
            if condition(n,i):
                res = res + 1
            i = i + 1
        return res

    return count_sum


def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def decision(n):
        if f(g(n)) == g(f(n)):
            return True
        else:
            return False
    return decision


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    # def decision(n):##n决定了迭代函数多少层
    #     times = n // 3##迭代几个来回
    #     remain = n % 3
    #     res = lambda x:x
    #     for i in range(times):
    #         res = f1(f2(f3(res)))
    #     if remain == 2:
    #         res = f1(f2(res))
    #     else:
    #         res = f1(res)
    #     return res这里是因为复合函数的写法有问题


    # def decision(n):
    #     times = n // 3##迭代几个来回
    #     remain = n % 3
    #     res1,res2,res3,res4,t = 0,0,0,0,0
    #     def get_result(num):
    #         t = num
    #         nonlocal res1,res2,res3,res4
    #         if times != 0:
    #             for i in range(times):
    #                 res1 = f1(t)
    #                 res2 = f2(res1)
    #                 res3 = f3(res2)
    #                 t = res3
    #         else:
    #             res3 = num
    #         if remain == 1:
    #             res = f1(res3)
    #             return res
    #         elif remain == 2:
    #             res4 = f1(res3)
    #             res = f2(res4)
    #             return res
    #         elif remain == 0 and times != 0:
    #             return res3
    #         elif remain == 0 and times == 0:
    #             return num
    #     return get_result
    # return decision
    # 上面这个可以过评测，但是代码写得很臃肿，下面是比较简单也好看的写法
    def decision(n):
        times = n // 3
        remain = n % 3
        def get_result(num):
            t = num
            for i in range(times):
                t = f3(f2(f1(t)))
            if remain == 1:
                t = f1(t)
            elif remain == 2:
                t = f2(f1(t))
            return t
        return get_result
    return decision


    

