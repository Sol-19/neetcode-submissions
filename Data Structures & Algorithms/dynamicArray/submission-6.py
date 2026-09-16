# class DynamicArray:
#     def __init__(self, capacity: int):
#         if capacity < 0:
#             raise ValueError("Capacity cannot be negative")
#         else:
#             self.capacity = capacity
#             self.data = [0] * capacity

#     def get(self, i: int) -> int:
#         return self.data[i]

#     def set(self, i: int, n: int) -> None:
#         self.data[i] = n

#     def pushback(self, n: int) -> None:
#         size = self.getSize()
#         if size == self.capacity:
#             self.resize()
#         self.data[size] = n

#     def popback(self) -> int:
#         self.data.pop()

#     def resize(self) -> None:
#         for i in range(self.capacity):
#             self.data.append(0)
#         self.capacity*=2

#     def getSize(self) -> int:
#         size = 0
#         for i in self.data:
#             if i:
#                 size+=1
#         return size
        
#     def getCapacity(self) -> int:
#         return self.capacity



class DynamicArray:
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.capacity = capacity
        self.size = 0
        self.data = [0] * capacity

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.data[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        new_capacity = max(1, self.capacity * 2)
        for _ in range(new_capacity - self.capacity):
            self.data.append(0)
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
