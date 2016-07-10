class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")


class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")


class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")


class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")

d = D()
# 进入D…
# 进入B…
# 进入C…
# 进入A…
# 离开A…
# 离开C…
# 离开B…
# 离开D…

