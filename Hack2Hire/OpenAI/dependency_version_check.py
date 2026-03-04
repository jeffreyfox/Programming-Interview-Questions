# A software company is managing its product releases. They maintain a list of all software versions, sorted in ascending chronological order. A new, critical feature was supported in one of these versions, and if a version has the feature, all subsequent versions also support it.

# You are given this sorted list of version strings, versions. Each version string follows the "MAJOR.MINOR.PATCH" format (e.g., "103.3.2"), and you must use the provided VersionChecker API to identify the first version with the feature.

# You are given the VersionChecker API:

# /* This is a provided API class. */
# class VersionChecker {
#     /**
#      * @param version A version string.
#      * @return true if the version is supported, false otherwise.
#      */
#     public boolean isSupported(String version);
# }
# Implement the Solution class:

# Solution(VersionChecker checker) Initializes your solution with the provided checker API.

# String findEarliestSupported(List<String> versions) Find and return the earliest version string in the list that is supported, following the rules:

# You must use the isSupported method from VersionChecker class to check each version.
# It is guaranteed that at least one version in the list is supported.
# Your implementation should minimize the number of calls to isSupported.
# Constraints:

# 1 ≤ versions.length ≤ 
# 10
# 5
# 10 
# 5
 
# Each version string is in the format "MAJOR.MINOR.PATCH".
# 0 ≤ MAJOR, MINOR, PATCH ≤ 
# 10
# 5
# 10 
# 5
#  , and no part will have leading zeros.
# The versions list is sorted in ascending order.
# Example:

# Input:
# ["Solution", "findEarliestSupported"]
# ["VersionChecker("103.3.2")", ["101.1.2", "101.1.3", "101.2.1", "102.0.1", "103.3.2", "103.3.3"]]

# Output:
# [null, "103.3.2"]

# Explanation:

# checker = new VersionChecker("103.3.2") // Creates a version checker that can determine whether a given version is supported, and the earliest version string is unknown to you.
# solution = new Solution(checker);
# solution.findEarliestSupported([["101.1.2", "101.1.3", "101.2.1", "102.0.1", "103.3.2", "103.3.3"]); // Returns "103.3.2", determined by making a series of isSupported calls.

from typing import List
from functools import cmp_to_key


# External API that checks if a version supports a specific feature.
# You should NOT directly access the `minSupportedVersion`.
class VersionChecker:
    def __init__(self, minSupportedVersion: str):
        self.minSupportedVersion = minSupportedVersion
        self.callCount = 0

    def isSupported(self, version: str) -> bool:
        self.callCount += 1
        return self.compareVersions(version, self.minSupportedVersion) >= 0

    def getCallCount(self) -> int:
        return self.callCount

    def compareVersions(self, v1: str, v2: str) -> int:
        parts1 = v1.split(".")
        parts2 = v2.split(".")

        for i in range(3):
            num1 = int(parts1[i])
            num2 = int(parts2[i])
            if num1 != num2:
                return (num1 > num2) - (num1 < num2)
        return 0


class Solution:
    def __init__(self, checker: VersionChecker):
        self.checker = checker

    # basically binary search, but we need to sort the versions first
    def findEarliestSupported(self, versions: List[str]) -> str:
        versions.sort(key=cmp_to_key(self.checker.compareVersions))
        lo, hi = 0, len(versions) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            supported = self.checker.isSupported(versions[mid])
            if supported:
                hi = mid-1
            else:
                lo = mid+1
        return versions[lo] 

    @staticmethod
    def main():
        Solution.test1()
        Solution.test2()
        Solution.test3()
        Solution.test4()
        Solution.test5()

    @staticmethod
    def test1():
        print("===== Test 1 =====")
        versions = ["101.1.2", "101.1.3", "101.2.1", "102.0.1", "103.3.2", "103.3.3"]
        checker = VersionChecker("103.3.2")
        solution = Solution(checker)
        result = solution.findEarliestSupported(versions)
        print(result)  # Expected: 103.3.2
        print("Total calls: " + str(checker.getCallCount()))

    @staticmethod
    def test2():
        print("\n===== Test 2 =====")
        versions = ["1.0.0", "1.0.1", "1.1.0", "2.0.0"]
        checker = VersionChecker("1.1.0")
        solution = Solution(checker)
        result = solution.findEarliestSupported(versions)
        print(result)  # Expected: 1.1.0
        print("Total calls: " + str(checker.getCallCount()))

    @staticmethod
    def test3():
        print("\n===== Test 3 =====")
        versions = ["3.1.5", "12.0.3", "15.8.22", "30.6.108", "45.2.7", "67.15.0", "89.3.45",
                   "100.20.5", "150.0.99", "200.10.15"]
        checker = VersionChecker("67.15.0")
        solution = Solution(checker)
        result = solution.findEarliestSupported(versions)
        print(result)  # Expected: 67.15.0
        print("Total calls: " + str(checker.getCallCount()))

    @staticmethod
    def test4():
        print("\n===== Test 4 =====")
        versions = ["0.0.1", "0.0.2", "0.1.0", "1.0.0"]
        checker = VersionChecker("0.0.1")
        solution = Solution(checker)
        result = solution.findEarliestSupported(versions)
        print(result)  # Expected: 0.0.1
        print("Total calls: " + str(checker.getCallCount()))

    @staticmethod
    def test5():
        print("\n===== Test 5 =====")
        versions = ["10.0.0", "20.0.0", "30.0.0", "40.0.0", "50.0.0"]
        checker = VersionChecker("50.0.0")
        solution = Solution(checker)
        result = solution.findEarliestSupported(versions)
        print(result)  # Expected: 50.0.0
        print("Total calls: " + str(checker.getCallCount()))


if __name__ == "__main__":
    Solution.main()