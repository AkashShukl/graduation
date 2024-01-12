# Problem

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The number of ways that you will miss your graduation ceremony.

# Solution

### Findings

To determine eligibility for attending classes on the Nth Day, it is crucial not to have been absent for four or more consecutive days.

The total number of possible combinations for attending classes over N days is given by 2^N.
However, not all combinations are valid.
Illustrating this with a straightforward example of 5 days and a maximum allowance of 4 absences:

`0 represents Absent`

`1 represents Present`

`01000` represents student is present on 2nd day and absent on rest of the days

Out of `2^5 = 32` possible combinations, only 29 are valid, where the student is allowed to attend on the Nth day.

For instance:

`00010` is a valid combination

`10000` is not a valid combination

To determine the number of ways a student may miss their graduation ceremony:

Out of the 29 valid ways, the student will miss the ceremony if they are absent on the Nth Day.

For example, in the sequence `11110`, the student attends classes on the first four days but misses the ceremony on the fifth day.

Out of the 29 valid combinations, 14 ways result in missing the graduation ceremony:

00010
00100
00110
01000
01010
01100
01110
10000
10010
10100
10110
11000
11010
11100
11110

- To find out "The number of ways to attend classes over N days."
  using the above observation, we can write a recursive function to calculate the valid ways of attending

      	`def ways(days = 5, missedday = 0, maxAllowedMissDays = 4)`

- To find out "The number of ways that you will miss your graduation ceremony."
  we can fix  missedday to 1 as it is certain that candidate will not be presenet on Nth day.

  This is because it is certain that the candidate will not be present on the Nth day, and decisions for the last day have already been made.

  So this probelms is reduced to find valid ways to attend college in N-1 days with maxAllowedMissDays to be reduced by 1 , we can also say to initialize missedDay to 1,

      `def ways(days = 5-1, missedday = 1, maxAllowedMissDays = 4)`



# Instructions
 Required Python version 3.8 +
 - run main.py
	 `python main.py`
- run tests
	`python test.py`

	