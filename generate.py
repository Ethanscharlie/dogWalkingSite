import os
import shutil

BUILD_DIR = "build"

def main():
    make_build_dir()

def make_build_dir() -> None:
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)

    os.makedirs(BUILD_DIR)

if __name__ == '__main__':
    main()
