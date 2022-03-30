# 网络通信，读取文件，批处理的时候，都有可能会遇到这种情况（计算时间比较长）
import time
def very_complex_compute(n):# 模拟非常复杂的计算过程，时间消耗就会较多
    time.sleep(3)
    return n**3

# def get_number(n):
#     numbers=[]
#     for i in range(n):
#         answer=very_complex_compute(i)
#         numbers.append(answer)
#
#     return numbers

def get_number(n): ### 注意，该函数，等同于上面的函数，属于简写
    return [very_complex_compute(i) for i in range(n)]

# print(get_number(4))   # 运行之后就会发现，得到结果需要好久

begin=time.time() #基督诞生以来，经过的所有秒数
for ans in get_number(3):
    now_=time.time()
    print("begin time:",int(begin))
    print("now time:",int(now_))
    print('used time={}'.format(now_-begin))
    print(ans)

# 可以看到，直到最后一个数字经过运算后，才会执行for循环内部的代码程序，这是由于get_number(3)是一个消耗时间很长的程序
# 所以，最终的used time都是一个数值