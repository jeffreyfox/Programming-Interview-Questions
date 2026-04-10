from typing import List, Optional, Dict, Tuple

class CreditSystem:
    def __init__(self, ):
        # [begin, end) interval -> credits
        self.creditIntervals: Dict[Tuple[int, int], int] = {}
        # timestamp -> credits
        self.creditSubstractions: Dict[int, int] = {}

    def grantCredit(self, id: str, amount: int, startTime: int, expirationTime: int) -> None:
        # Use += to accumulate instead of overwrite for duplicate intervals
        self.creditIntervals[(startTime, expirationTime)] += amount

    def subtract(self, amount: int, timestamp: int) -> None:
        # Use += to accumulate instead of overwrite for duplicate timestamps
        self.creditSubstractions[timestamp] += amount

    def getBalance(self, timestamp: int) -> int:
        result = 0
        # scans all intervals
        for interval, credit in self.creditIntervals.items():
            if self._isPointInInterval(timestamp, interval):
                result += credit
        # subtractions
        result -= self.creditSubstractions.get(timestamp, 0)
        return -1 if result < 0 else result

    def _isPointInInterval(self, timestamp: int, interval: Tuple[int, int]) -> bool:
        start, end = interval
        return start <= timestamp and timestamp < end

    
