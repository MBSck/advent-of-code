from pathlib import Path

def count_depth_increase_mean(path_to_file: Path) -> int:
    with open(path_to_file, 'r') as f:
        input_lst = [int(x) for x in f.readlines()]

    lst = [sum(x) for x in zip(input_lst, input_lst[1:], input_lst[2:])]

    return len([True for x, y in zip(lst, lst[1:]) if y > x])

if __name__ == "__main__":
    print(count_depth_increase_mean("test.txt"))
    print(count_depth_increase_mean("input.txt"))

