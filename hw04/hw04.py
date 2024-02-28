def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message != 'deposit' and message != 'withdraw':
            return 'Invalid message'
        if message == 'deposit':
            balance = balance + amount
            return balance
        if message == 'withdraw':
            if balance < amount:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    err_times = 0
    err_lists = []
    def bank(amount,password_):
        nonlocal balance, password,err_times
        if err_times == 3:
            return "Frozen account. Attempts: " + str(err_lists)
        if password_ != password:
            err_times = err_times + 1
            err_lists.append(password_)
            return 'Incorrect password'
        if balance < amount:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return bank

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    # res = {}
    # for i in t:
    #     if i not in res:
    #         res[i] = 1
    #         continue
    #     res[i] = res[i] + 1
    # ##这一步返回的是一个字典，其中包含了字母出现的次数
    # result = []
    # for j in res.items():
    #     if j[1] == k:
    #         result.append(j[0])
    # return next(iter(result))

    now,num = iter(t),1
    for item in t:
        if item == now:
            num = num + 1
            if num == k:
                return item
        else:
            num = 1
        now = item




def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    # used = []
    # for i in range(len(seq)):
    #     used.append(0)
    # ##used列表记录元素是否被使用过
    # tmp = []
    # ##tmp列表记录当前的排列
    # res = []
    # ##res为返回总的列表生成器
    # def helper(now):##now表示当前考虑的是第几位
    #     if sum(used) == len(seq):
    #         res.append(tmp)
    #         return
    #     for i in range(len(seq)):
    #         if used[i] == 0:
    #             tmp.append(seq[i])
    #             used[i] = 1
    #             helper(now + 1)
    #             used[i] = 0
    # helper(0)
    # yield 

    if len(seq) == 1:
        yield seq

    elif len(seq) > 0:
        now = seq[0]
        for x in permutations(seq[1:]):
            for index in range(len(seq)):
                tmp = list(x)
                tmp.insert(index,now)
                yield tmp

def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    # if type(withdraw(0,old_pass)) == str:
    #         return 'Incorrect password'
    #     ##不正常的情况返回值为字符串
    # password_list = []
    # password_list.append(old_pass)
    # password_list.append(new_pass)
    # def _withdraw_(amount,used_pass):
    #     nonlocal password_list
    #     if used_pass not in password_list:##添加新密码
    #         return 'Incorrect password'
    #     return withdraw(amount,old_pass)
    # return  _withdraw_
    _check_ = withdraw(0,old_pass)
    if type(_check_) == str:
        return _check_
    def check(amount,use_pass):
        if use_pass == new_pass:
            return withdraw(amount,old_pass)
        else:
            return withdraw(amount,use_pass)
    return check
def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def gen(n):##n记录当前的余数是多少
        k = naturals()
        while True:
            tmp = next(k)
            if tmp % m == n:
                res = tmp
                yield res
    for i in range(m):
        yield gen(i)  

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

