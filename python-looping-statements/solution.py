def countdown_with_skip(start: int) -> list:
    """
    Using a while loop, count down from `start` to 1 (inclusive),
    appending each number to a list, but skip appending any
    number that is exactly 3 (use continue for this).
    Do not use break here.
    Return the resulting list.
    """
    l = []
    while start >= 1:
        if start != 3:
            l.append(start)
        start -= 1
    return l
    


def find_first_negative(numbers: list) -> int | None:
    """
    Using a while loop with an index variable, find and return
    the first negative number in `numbers`. Use break once found.
    If no negative number exists, use the loop's else clause to
    return None after the loop completes normally.
    """
    idx = 0
    while idx < len(numbers):
        if numbers[idx] < 0:
            return numbers[idx]
        idx += 1
    return None


def sum_with_index(numbers: list) -> dict:
    """
    Using a for loop with enumerate(), build and return a
    dictionary mapping each index to the running sum of all
    numbers up to and including that index.

    Example: sum_with_index([10, 20, 30])
    -> {0: 10, 1: 30, 2: 60}
    """
    d = {}
    for i in range(len(numbers)):
        if i == 0:
            d[i] = numbers[i]
        else:
            d[i] = numbers[i] + d[i - 1]
        
    return d
        


def manual_iteration_trace(items: list) -> list:
    """
    Without using a for loop, replicate what a for loop does
    internally: use iter() to get an iterator from `items`, then
    repeatedly call next() on it inside a while loop, catching
    StopIteration to know when to stop.

    Return a list of all elements retrieved this way, in order
    (it should exactly match the original `items` list).
    """
    itr = iter(items)
    l = []
    while True:
        try:
            l.append(next(itr))
        except StopIteration:
            break
    return l
