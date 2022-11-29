from pathlib import Path

def count_depth_increase(path_to_file: Path) -> int:
    """Counts the depth increase of the submarine"""
    with open(path_to_file) as f:
        input_lst = [int(i) for i in f.readlines()]

    return len([True for x, y in zip(input_lst, input_lst[1:]) if y > x])


if __name__ == "__main__":
    print(count_depth_increase("test.txt"))
    print(count_depth_increase("input.txt"))

