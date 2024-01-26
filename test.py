import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a + b
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a + b + c

obj = A()
print(obj.add(1,2,3))
print(obj.add(1,2))