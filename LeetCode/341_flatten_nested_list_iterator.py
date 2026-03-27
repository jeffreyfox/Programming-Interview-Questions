# TAGS: stack,design

# Stack + lazy flattening: keep expanding the top until it’s an integer, then pop it.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st: list[NestedInteger] = list(reversed(nestedList))

    def _unravel(self) -> None:
        while self.st and not self.st[-1].isInteger():
            top = self.st.pop()
            self.st.extend(list(reversed(top.getList())))

    def next(self) -> int:
        self._unravel()
        return self.st.pop().getInteger()
        
    def hasNext(self) -> bool:
        self._unravel()
        return bool(self.st)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())