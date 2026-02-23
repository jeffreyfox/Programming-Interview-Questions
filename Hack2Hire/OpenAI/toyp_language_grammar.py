class Node:
    def __init__(self, value=None, tuple=None):
        if tuple is not None:
            self._tuple = tuple
            self._isTuple = True
        else:
            self._value = value  # for primitive or generic types
            self._isTuple = False

    def __str__(self):
        if self._isTuple:
            return "[" + ','.join(str(node) for node in self._tuple) + "]"
        return self._value


class Function:
    def __init__(self, params, returnType):
        self._params = params
        self._returnType = returnType

    def __str__(self):
        param_str = "[" + ','.join(str(node) for node in self._params) + "]"
        return_type_str = str(self._returnType)
        return param_str + " -> " + return_type_str


class Solution:
    @staticmethod
    def main():
        Solution.nodeTest()
        Solution.functionTest()

    @staticmethod
    def nodeTest():
        print("===== Node Test =====")

        node1 = Node("int")
        print(node1)  # Expected: "int"

        node2 = Node("char")
        print(node2)  # Expected: "char"

        node3 = Node("float")
        print(node3)  # Expected: "float"

        node4 = Node("T1")
        print(node4)  # Expected: "T1"

        node7 = Node(tuple=[Node("int"), Node("T1"), Node("char")])
        print(node7)  # Expected: "[int,T1,char]"

        node8 = Node(tuple=[Node("float"), Node("T3")])
        print(node8)  # Expected: "[float,T3]"

        node9 = Node(tuple=[Node("int"), Node("char"),
                           Node(tuple=[Node("int"), Node("T1")])])
        print(node9)  # Expected: "[int,char,[int,T1]]"

        node10 = Node(tuple=[Node("int"),
                            Node(tuple=[Node("char"), Node(tuple=[Node("float"), Node("T1")])])])
        print(node10)  # Expected: "[int,[char,[float,T1]]]"

        node11 = Node(tuple=[Node(tuple=[Node("int"), Node("char")]),
                            Node(tuple=[Node("T1"), Node("T2")]),
                            Node(tuple=[Node("float"), Node("T3")])])
        print(node11)  # Expected: "[[int,char],[T1,T2],[float,T3]]"

        node12 = Node(tuple=[Node("int")])
        print(node12)  # Expected: "[int]"

        node13 = Node(tuple=[])
        print(node13)  # Expected: "[]"

        node14 = Node(tuple=[Node(tuple=[Node("int")])])
        print(node14)  # Expected: "[[int]]"

    @staticmethod
    def functionTest():
        print("\n===== Function Test =====")

        func1 = Function([Node("int"), Node("T1"),
                         Node(tuple=[Node("int"), Node("T2")])], Node("T1"))
        print(func1)  # Expected: "[int,T1,[int,T2]] -> T1"

        func2 = Function([Node("char"), Node("float")], Node("int"))
        print(func2)  # Expected: "[char,float] -> int"

        func3 = Function(
            [Node(tuple=[Node("int"), Node("char")]), Node("T1"),
             Node(tuple=[Node("float"),
                        Node(tuple=[Node("T2"), Node("T3")])])],
            Node(tuple=[Node("int"), Node("T1")]))
        print(func3)  # Expected: "[[int,char],T1,[float,[T2,T3]]] -> [int,T1]"
        
        func4 = Function([Node("int")], Node("char"))
        print(func4)  # Expected: "[int] -> char"

        func5 = Function([], Node("int"))
        print(func5)  # Expected: "[] -> int"

        func6 = Function([Node("int"), Node(tuple=[])], Node("T1"))
        print(func6)  # Expected: "[int,[]] -> T1"

        func7 = Function([Node("int")], Node(tuple=[]))
        print(func7)  # Expected: "[int] -> []"


if __name__ == "__main__":
    Solution.main()