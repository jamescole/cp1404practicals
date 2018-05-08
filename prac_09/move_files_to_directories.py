
import os, shutil


def main():

    version_one()


def version_one():

    os.chdir("FilesToSort")
    for dir_name, sub_dirs, filenames in os.walk('.'):
        for filename in filenames:
            if filename[0] != '.': # if not a hidden file
                extension = os.path.splitext(filename)[1][1:]
                if not os.path.exists(extension):
                    os.mkdir(extension)
                print(filename, os.path.join(extension, filename))
                shutil.move(filename, os.path.join(extension, filename))


if __name__ == '__main__':
    main()
