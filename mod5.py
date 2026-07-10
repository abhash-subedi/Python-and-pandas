import numpy as np

array = np.array(range(1, 11))
celsius_temp = np.array([0, 10, 15, 20, 25, 30])


# The question asked for a function to be created
# which can tell various attributes of a given array
def calc_properties(arr: np.ndarray) -> str:
    """Calculate the various attributes of a given NumPy array."""
    return (
        f"The sum is {arr.sum()}, the min is {arr.min()}, "
        f"the max is {arr.max()}, and the mean is {arr.mean()}"
    )


# The question asked for a function which turns a list
# of celsius temperatures to fahrenheit
def celsius_to_fahrenheit(arr: np.ndarray) -> np.ndarray:
    """Turn an array of Celsius temperatures to Fahrenheit."""
    return arr * 9 / 5 + 32


# The question asked to compare summing a million numbers
# with standard Python and with NumPy
def sum_million() -> int:
    """Sum a million numbers with standard Python and compare against NumPy."""
    million_nums = range(0, 1000001)
    million_nums_np = np.array(range(0, 1000001))

    total_sum = 0
    # For i in range(len(million_nums)):
    #     total_sum += i
    # total_sum = million_nums_np.sum()
    # print(total_sum)

    # I noticed that with NumPy the calculation was much faster and
    # it was more simple to implement
    return million_nums_np.sum()


def main() -> None:
    """Execute main logic."""
    print(sum_million())


if __name__ == "__main__":
    main()