# 修改成迭代器
import time
def very_complex_compute(n):# 模拟非常复杂的计算过程，时间消耗就会较多
    time.sleep(3)
    return n**3

# def get_number(n):
#
#     for i in range(n):
#         answer=very_complex_compute(i)
#         yield answer  # 修改成迭代器，返回结果，继续运行代码

def get_number(n):

    # return [very_complex_compute(i) for i in range(n)] # 如果还是原来的方框，就不是迭代器
    return (very_complex_compute(i) for i in range(n)) # 把方框改成括弧，就实现了迭代器（省去了写yield关键字）


# print(get_number(4))   # 运行之后就会发现，得到结果需要好久

begin=time.time() #基督诞生以来，经过的所有秒数
for ans in get_number(3):
    now_=time.time()
    print("begin time:",int(begin))
    print("now time:",int(now_))
    print('used time={}'.format(now_-begin))
    print(ans)

# 可以看到，修改成迭代器之后，get_number(3)变成了一个迭代器，有一个结果，返回一个结果，for 循环就得以继续向下执行
# 所以，最终，不同的数值执行时间，used time是不同的