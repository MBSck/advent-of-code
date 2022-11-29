from pathlib import Path
import re

def steer(path_to_input: Path) -> int:
    """Steers the submarine"""
    with open(path_to_input, 'r') as f:
        input_lst = [re.sub('\n', '', i) for i in (f.readlines())]

    horizontal = sum([int(i[~0]) for i in input_lst if "forward" in i])
    depth = sum([int(i[~0]) for i in input_lst if "down" in i])-sum([int(i[~0]) for i in input_lst if "up" in i])

    return depth*horizontal


if __name__ == "__main__":
    print(steer("test.txt"))
    print(steer("input.txt"))

