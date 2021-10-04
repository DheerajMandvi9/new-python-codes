class Stack:
    """Class to represent a sequential static stack in Python3"""

    def __init__(self, maximum):
        self.max = maximum  # The maximum stack size
        self._stack = [None] * maximum  # Empty stack
        self._size = 0  # The size of stack

    @property
    def max(self):
        """Getters to max stack size"""
        return self._max

    @max.setter
    def max(self, maximum):
        """Setters to max stack size"""
        if isinstance(maximum, int):
            self._max = maximum
        else:
            raise Exception("The type must be an integer")

    def push(self, elem):
        """Adds an element at the top of a stack"""
        if self._size == self.max:
            raise Exception("Full stack")
        self._stack[self._size] = elem
        self._size += 1

    def pop(self):
        """Removes the topmost element of a stack"""
        if self._size == 0:
            raise Exception("Empty stack")
        elem, self._stack[self._size-1] = self._stack[self._size-1], None
        self._size -= 1
        return elem

    def top(self):
        """Returns the element on the top of the stack but does not remove it"""
        if self._size == 0:
            raise Exception("Empty stack")
        return self._stack[self._size-1]

    def empty(self):
        """Returns true if the stack is empty, otherwise, it returns false"""
        if self._size == 0:
            return True
        return False

    def length(self):
        """Returns the size of stack"""
        return self._size

    def __del__(self):
        """Destructor method"""

    def __str__(self):
        """Method for representing the stack, excluding NoneType objects (user)"""
        rep = "\033[1;34m" + "top ->  " + "\033[0;0m"
        if self._size == 0:
            rep += "None"
            return rep
        for i in range(self._size-1, -1, -1):
            if self._stack[i] == None:
                pass
            elif i == self._size-1:
                rep += f"{str(self._stack[i]).rjust(2)}"
            elif i == 0:
                rep += f"\n{str(self._stack[i]).rjust(10)}"
            else:
                rep += f"\n{str(self._stack[i]).rjust(10)}"
        return rep

    def __repr__(self):
        """Method for representing the stack, excluding NoneType objects (developer)"""
        return str(self)
