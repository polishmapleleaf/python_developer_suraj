import csv
import json
import pickle
import os
import sys


class FileHandler:
    def __init__(self, path):
        self.path = path
        self.data = []

    def read(self):
        raise NotImplementedError

    def write(self, dst):
        raise NotImplementedError


class CSVHandler(FileHandler):
    def read(self):
        with open(self.path, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            self.data = [row for row in reader]
        return self.data

    def write(self, dst):
        with open(dst, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


class JSONHandler(FileHandler):
    def read(self):
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data

    def write(self, dst):
        with open(dst, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)


class PickleHandler(FileHandler):
    def read(self):
        with open(self.path, "rb") as f:
            self.data = pickle.load(f)
        return self.data

    def write(self, dst):
        with open(dst, "wb") as f:
            pickle.dump(self.data, f)


def get_handler(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return CSVHandler(path)
    elif ext == ".json":
        return JSONHandler(path)
    elif ext == ".pickle":
        return PickleHandler(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def apply_changes(data, changes):
    for change in changes:
        try:
            col, row, value = change.split(",", 2)
            col, row = int(col), int(row)
            data[row][col] = value
        except Exception as e:
            print(f"Could not apply change '{change}': {e}")
    return data


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> [changes...]")
        return

    src, dst, *changes = sys.argv[1:]


    if not os.path.isfile(src):
        print(f"Source file '{src}' not found.")
        directory = os.path.dirname(src) or "."
        print("\nFiles in the same directory:")
        for file in os.listdir(directory):
            print(" -", file)
        return


    try:
        handler = get_handler(src)
    except ValueError as e:
        print(e)
        return

    data = handler.read()
    if changes:
        data = apply_changes(data, changes)

    print("\nModified contents:")
    for row in data:
        print(row)

    try:
        dst_handler = get_handler(dst)
    except ValueError as e:
        print(e)
        return

    dst_handler.data = data
    dst_handler.write(dst)

    print(f"\nSaved modified file to: {dst}")


if __name__ == "__main__":
    main()
