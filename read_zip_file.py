import re
import os
import subprocess
import sys
import zipfile
from typing import List


def read_file(path: str, new_dir: str) -> List[str]:
    """
    Reads a file provided in {@code: path} (and if required, stores the output in {@code: new_dir}

    If {@code: path} does not contain ".7z" or ".zip", it opens it.
    Otherwise {@code path} is divided into two substring: Path from char at index 0 until ".7z" (or ".zip") (inclusive)
    and path from "-7z" (or ".zip") (exclusive) until last char.
    Paths containing ".7z" or ".zip" with whitespaces, need to be extracted.
    Paths containing ".zip" but no whitespaces do not need to be extracted.

    :param path File path (without white-spaces)
    :param new_dir path of the directory where the read zip file is expected to be stored

    :return String of the read file

    """
    path = path.replace("/", "\\")

    if ".7z" not in path and ".zip" not in path:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                return file.read().splitlines()
        except PermissionError:
                print(f"PermissionError:\t{path}")
    elif path.__contains__(".7z") or path.__contains__(" "):
        print(f"Extracting:\t\t{path}")
        # Divide path into two: path until .7z (inclusive) and path from .7z (exclusive) to a2l file
        path_groups = re.search(r"^(.*(?:\.7z|\.zip))\\(.*)", path)
        zip_path = path_groups.group(1)
        file_path = path_groups.group(2).replace(os.sep, '/')
        a2l_file_name = re.search(r".*\\(.*\.\w+)$", path).group(1)   # TODO try-catch block needed

        # 1. Make directory in which we store unzipped files (only if it exists)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        try:
            with open(zip_path, "r") as f:
                pass
        except PermissionError:
            print(f"PermissionError: {path}")
            return None

        # 2 Path to our extracted file (extraction done in #3)
        new_path = os.path.join(new_dir, a2l_file_name)

        # 3. Extract file to the new directory new_dir (if it already exists we do not extract)
        if not os.path.isfile(new_path):
            subprocess.call(r'7z e ' + "\"" + zip_path + "\"" + ' -o' + new_dir + ' ' + file_path)

        with open(new_path, "r") as f:
            data = f.read().splitlines()

        return data
    else:
        print(f"Accessing zip file:\t{path}")
        path_groups = re.search(r"^(.*\.zip.*?)\\(.*)", path)
        start_path = path_groups.group(1)
        sub_path = path_groups.group(2).replace(os.sep, '/')

        try:
            zip_file = zipfile.ZipFile(start_path, "r")
            data = zip_file.read(sub_path).decode("utf-8", errors='ignore').splitlines()
            return data
        except PermissionError:
            print(f"PermissionError:\t{path}")
            return None
        except zipfile.BadZipFile:
            print(f"Invalid zip file:\t{path}")
            return None


if __name__ == "__main__":
    # Example:
    # print(read_file(r'resources\test.zip\test.txt', 'output'))

    if ".7z" in sys.argv[1] or ' ' in sys.argv[1]:
        if len(sys.argv) < 3:
            print("Please provide at least two arguments:\n"
                  "1. Path of the file within a zip-file\n"
                  "2. Directory of extracted files")
        else:
            print(read_file(sys.argv[1], sys.argv[2]))
    else:
        if len(sys.argv) < 2:
            print("Please provide at least one argument:\n"
                  "1. Path of the file within a zip-file")
        else:
            print(read_file(sys.argv[1], None))
