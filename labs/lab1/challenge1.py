"""
Challenge 1: Simple Statistics with Python's built-in list data structure

You are given a list of exam scores.
Use your knowledge to calculate the following statistics:

1. Average score
2. Maximum score
3. Minimum score
4. Median score
5. Standard deviation
"""

EXAM_SCORES: list[int] = [
    90,
    95,
    85,
    88,
    92,
    100,
    75,
    85,
    90,
    92,
    85,
    95,
    90,
    85,
    80,
    95,
    100,
    85,
    90,
    92,
]


def average_score(scores: list[int]) -> float:
    """Calculate the average score of the exam scores."""
    raise NotImplementedError


def max_score(scores: list[int]) -> int:
    """Calculate the maximum score of the exam scores."""
    raise NotImplementedError


def min_score(scores: list[int]) -> int:
    """Calculate the minimum score of the exam scores."""
    raise NotImplementedError


def median_score(scores: list[int]) -> int:
    """Calculate the median score of the exam scores."""
    raise NotImplementedError


def standard_deviation(scores: list[int]) -> float:
    """Calculate the standard deviation of the exam scores."""
    raise NotImplementedError


def main():
    """Display the statistics of the exam scores."""
    print(f"Average score: {average_score(EXAM_SCORES)}")
    print(f"Max score: {max_score(EXAM_SCORES)}")
    print(f"Min score: {min_score(EXAM_SCORES)}")
    print(f"Median score: {median_score(EXAM_SCORES)}")
    print(f"Standard deviation: {standard_deviation(EXAM_SCORES)}")


if __name__ == "__main__":
    main()
