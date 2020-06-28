from itertools import (
    permutations # list を受け取り、序列のジェネレータを返す関数. 第二引数に整数を渡せばその個数を選んだ並び替え.
    combinations　# list と整数を受け取り、その個数での組み合わせのジェネレータを返す関数.
    product # list を複数受け取り、直積のジェネレータを返す関数.
)

def isPrime(x):
    i = int(x**0.5)
    for j in range(2, i + 1):
        if x % j == 0:
            return False
    return True
