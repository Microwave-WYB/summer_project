"""
Challenge 2: Simple Statistics with Python's built-in list and dictionary data structures

You are given a list of health records.
Each record is a dictionary with the following keys:
- name: the name of the person
- height: the height of the person in meters
- weight: the weight of the person in kilograms

You need to implement a preprocessing function that converts the height and weight of the health
records to float.
Be careful with the records that have missing values (N/A), this means that the record is invalid.
It should not be included in the processed records.

You are required to calculate the following statistics:
1. Average height
2. Average weight
3. Average BMI
"""

HEALTH_RECORD: list[dict[str, str]] = [
    {
        "name": "Alice",
        "height": "1.6",
        "weight": "60.1",
    },
    {
        "name": "Bob",
        "height": "1.7",
        "weight": "70.4",
    },
    {
        "name": "Charlie",
        "height": "1.8",
        "weight": "80.3",
    },
    {
        "name": "David",
        "height": "1.74",
        "weight": "75",
    },
    {
        "name": "Eve",
        "height": "1.64",
        "weight": "62.8",
    },
    {
        "name": "Frank",
        "height": "N/A",
        "weight": "N/A",
    },
    {
        "name": "Grace",
        "height": "1.75",
        "weight": "65.5",
    },
    {
        "name": "Helen",
        "height": "1.78",
        "weight": "85",
    },
    {
        "name": "Ivy",
        "height": "1.68",
        "weight": "55",
    },
    {
        "name": "Jack",
        "height": "1.76",
        "weight": "75",
    },
    {
        "name": "Kate",
        "height": "N/A",
        "weight": "N/A",
    },
]


def preprocess(records: list[dict[str, str]]) -> list[dict[str, float]]:
    """
    Preprocess the health records by converting the height and weight to float.
    If the record has missing values (N/A), it should not be included in the processed records.
    """
    raise NotImplementedError


def average_height(records: list[dict[str, float]]) -> float:
    """Calculate the average height of the health records."""
    raise NotImplementedError


def average_weight(records: list[dict[str, float]]) -> float:
    """Calculate the average weight of the health records."""
    raise NotImplementedError


def bmi(height: float, weight: float) -> float:
    """Calculate the BMI of the person."""
    return weight / (height**2)


def average_bmi(records: list[dict[str, float]]) -> float:
    """Calculate the average BMI of the health records."""
    raise NotImplementedError


def main():
    """Display the statistics of the health records."""
    processed_records = preprocess(HEALTH_RECORD)
    print(f"Average height: {average_height(processed_records)}")
    print(f"Average weight: {average_weight(processed_records)}")
    print(f"Average BMI: {average_bmi(processed_records)}")


if __name__ == "__main__":
    main()
