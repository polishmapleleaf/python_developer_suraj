import sys
import csv
import os


def load_csv(file_path):
    if not os.path.isfile(file_path):
        print(f" Error: '{file_path}' is not a valid file.\nFiles in directory '{os.path.dirname(file_path) or '.'}':")
        for f in os.listdir(os.path.dirname(file_path) or '.'):
            print(f"- {f}")
        sys.exit(1)

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]



def apply_changes(data, changes):
    for change in changes:
        try:
            x, y, value = change.split(",", 2)
            x = int(x)
            y = int(y)
            if y < 0 or y >= len(data):
                print(f"Skipping change '{change}': Row {y} is out of bounds.")
                continue
            if x < 0 or x >= len(data[y]):
                print(f"Skipping change '{change}': Column {x} is out of bounds in row {y}.")
                continue
            print(f"Applying change: data[{y}][{x}] = '{value}'")
            data[y][x] = value
        except ValueError:
            print(f"Skipping invalid change format: '{change}' (expected format: X,Y,value)")


def display_csv(data):
    print("\n Modified CSV content:\n" + "-" * 25)
    for row in data:
        print(",".join(row))
    print("-" * 25)


def save_csv(data, dst_path):
    try:
        with open(dst_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f" File saved successfully to '{dst_path}'")
    except Exception as e:
        print(f"Error saving file to '{dst_path}': {e}")



def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)

    src_path = sys.argv[1]
    dst_path = sys.argv[2]
    changes = sys.argv[3:]
    data = load_csv(src_path)
    apply_changes(data, changes)
    display_csv(data)
    save_csv(data, dst_path)

if __name__ == '__main__':
    main()