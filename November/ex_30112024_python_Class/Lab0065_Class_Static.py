# Static methods: is method that belongs to a class rather than an instance of the class.
# The advantage of static class is directly we can call, no need of object creation.



class O:
    @staticmethod
    def sum(a, b):
        return a + b

    def sub(self, a, b):
        return a - b

print("----------------------NonStatic-------------------------")
obj_O = O()
ans = obj_O.sub(20, 10)
print(ans)
print("----------------------Static------@staticmethod----------------")
#Direct call
print(O.sum(10,30))

