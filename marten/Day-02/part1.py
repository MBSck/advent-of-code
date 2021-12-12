from pathlib import Path
import re

def steer(path_to_input: Path) -> int:
    """Steers the submarine"""
    with open(path_to_input, 'r') as f:
        input_lst = [re.sub('\n', '', i) for i in (f.readlines())]

    down = 


if __name__ == "__main__":
    print(steer("test.txt"))
    print(steer("input.txt"))

