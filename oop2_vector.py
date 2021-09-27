from math import hypot


class Vector:
    # 特殊方法一般只有解释器才会调用（eg. x.__bool__）
    # 唯一例外的是__init__方法，因为一般子类会去调用超类的构造器

    def __init__(self, x=0, y=0):
        # 构造函数和属性定义
        self.x = x
        self.y = y

    def __repr__(self):
        # 实现print函数，也可以实现__str__函数
        # 但推荐使用本函数，因为__str__会自动被替代
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)
        # Return the Euclidean distance, sqrt(x*x + y*y).

    def __bool__(self):
        # Vector(0, 0)不是向量
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


vec1 = Vector(1, 2)
vec2 = Vector(3, 4)
vec3 = Vector(0, 0)
print(vec1)
print(abs(vec2))
print(bool(vec1))
print(bool(vec3))
print(vec1 * -3)

# 为什么是len而不是普通方法：
# 当len(x)中的x是一个内置类型的实例时，那么len(x)的速度会非常快，
# 背后的原因是CPython会直接从一个C结构体中读取对象长度，完全不需要调用任何方法，
# 在str、list、memoryview等类型上，该方法必须高效。

