
# python version 3.8 +


from math import comb
from collections import defaultdict


class Graduation:
    def __init__(self, days: int, max_consecutive_days_to_miss: int):
        """
        Initialize the Graduation class with the number of days and the maximum number of consecutive days that can be missed.
        """
        self.days = days
        self.max_consecutive_days_to_miss = max_consecutive_days_to_miss
        self.memo = defaultdict(int)

    def calculate_ways(self, curr_day: int, days_missed: int) -> int:
        """
        Calculate the number of valid ways to attend classes over N days such that allowed to attend graduation ceremony.
        """
        if curr_day == 0 and days_missed < self.max_consecutive_days_to_miss:
            return 1
        if days_missed >= self.max_consecutive_days_to_miss:
            return 0

        # attend class on curr_day. reset the missed days back to 0
        attend = self.calculate_ways(curr_day-1, 0)

        # don't attend class on curr_day. Increment the days_missed
        not_attend = self.calculate_ways(curr_day-1, days_missed+1)

        return attend + not_attend

    def calculate_ways(self, curr_day: int, days_missed: int) -> int:
        if curr_day == 0 and days_missed < self.max_consecutive_days_to_miss:
            return 1
        if days_missed >= self.max_consecutive_days_to_miss:
            return 0

        if (curr_day, days_missed) in self.memo:
            return self.memo[(curr_day, days_missed)]

        attend = self.calculate_ways(curr_day-1, 0)
        not_attend = self.calculate_ways(curr_day-1, days_missed+1)

        self.memo[(curr_day, days_missed)] = attend + not_attend
        return self.memo[(curr_day, days_missed)]

    def number_of_ways_to_attend(self) -> str:
        """
        Returns number of ways to miss ceremony /number of ways to attend classes over N days
        """
        ways_to_attend = self.calculate_ways(self.days, 0)
        ways_to_miss_ceremony = self.calculate_ways(self.days-1, 1)

        return f"{ways_to_miss_ceremony}/{ways_to_attend}"



g = Graduation(5, 4)
print(g.number_of_ways_to_attend())

g = Graduation(10, 4)
print(g.number_of_ways_to_attend())