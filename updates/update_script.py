import os
import hashlib
import shutil
from pathlib import Path

def hash_file(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return None

def compare_directories(dir1, dir2):
    dir1, dir2 = Path(dir1), Path(dir2)
    all_files = set(dir1.rglob("*")) | set(dir2.rglob("*"))

    only_in_dir1 = []
    only_in_dir2 = []
    different_files = []

    for file in all_files:
        rel_path = file.relative_to(dir1 if file in dir1.rglob("*") else dir2)
        file1 = dir1 / rel_path
        file2 = dir2 / rel_path

        if file1.exists() and not file2.exists():
            only_in_dir1.append(str(rel_path))
            shutil.copy(file1, file2)
        elif file2.exists() and not file1.exists():
            only_in_dir2.append(str(rel_path))
        elif file1.is_file() and file2.is_file():
            if hash_file(file1) != hash_file(file2):
                different_files.append(str(rel_path))
                shutil.copy(file1, file2)

    print(f"Files only in {dir1}:")
    print("\n".join(only_in_dir1))

    print(f"Files only in {dir2}:")
    print("\n".join(only_in_dir2))

    print("Different files:")
    print("\n".join(different_files))

if __name__ == "__main__":
    dir1 = input("Enter directory with new files: ")
    dir2 = input("Enter directory to update: ")
    compare_directories(dir1, dir2)

