"""
这题还算比较简单，直接用一个栈来存储一个递增的子数组（栈元素的第一项），第二项是原数组中在该元素前连续递减的数字数量，
加上自己。
在leetcode上毕竟慢，可能是测试的例子增多了。
"""
class StockSpanner:

    def __init__(self):
        self.stack = [(float("inf"), 0)]

    def next(self, price):
        count = 1
        while self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count


solve = StockSpanner()
prices = [100, 80, 60 ,70, 60, 75, 85]
for price in prices:
    print(solve.next(price))
