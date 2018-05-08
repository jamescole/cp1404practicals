
import os
import shutil
from pathlib import Path


def main():

    # version_one()

    version_two()


def version_one():
    """
    For the files in ./FilesToSort, create a directory for each unique file extension, with the same name
    as that extension, and move all files with that extension into it.
    """

    os.chdir("FilesToSort")
    for dir_name, sub_dirs, filenames in os.walk('.'):
        for filename in filenames:
            if filename[0] != '.':  # if not a hidden file
                extension = os.path.splitext(filename)[1][1:]
                if not os.path.exists(extension):
                    os.mkdir(extension)
                print(filename, os.path.join(extension, filename))
                shutil.move(filename, os.path.join(extension, filename))


def version_two():
    """
    For each unique file extension found in ./FilesToSort, ask the user what directory name to put
    the files with that extension there in.  Create these directories as subdirectories and move the
    files into them.
    """

    directory_path = "./FilesToSort"

    # categorise the extensions
    unique_extensions = get_unique_extensions(directory_path)
    directories_for_extensions = {}
    for extension in unique_extensions:
        prompt = "What category would you like to sort {} files into? ".format(extension)
        category = input(prompt)
        if category not in directories_for_extensions:
            directories_for_extensions[category] = []
        directories_for_extensions[category].append(extension)

    # create the chosen directories and move the files into the appropriate directories
    path = Path(directory_path)
    for directory in directories_for_extensions:
        if not os.path.exists(directory):
            os.mkdir(os.path.join(path, directory))
        for extension in directories_for_extensions[directory]:
            for file_path in list(path.glob("*.{}".format(extension))):
                shutil.move(file_path, os.path.join(path, directory, file_path.name))


def get_unique_extensions(directory_path):

    unique_extensions = []
    for dir_name, sub_dirs, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename[0] != '.':  # if not a hidden file
                extension = os.path.splitext(filename)[1][1:]
                if extension not in unique_extensions:
                    unique_extensions.append(extension)

    return unique_extensions


if __name__ == '__main__':
    main()

