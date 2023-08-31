"""
__call__ 메서드는 함수의 인스턴스를 변수에 저장해두고 f(...) 형태로 __call__ 메서드를 호출할 수 있다.
forward 메서드는 상속받은 클래스에서 구현한다.
"""

from step01 import Variable
import numpy as np

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x**2

if __name__ == "__main__":
    # 1
    """
    x = Variable(np.array(10))
    f = Function()
    y = f(x)
    print(y.data)
    print(type(y))
    """

    # 2
    x = Variable(np.array(10))
    f = Square()
    y = f(x)
    print(y.data)
    print(type(y))


