class A:
    def func(self):
        pass


class B:
    def func(self, number):
        pass


lst = [A(), B()]

for item in lst:
    item.func()

# Logically inconsistent code
