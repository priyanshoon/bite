from generate_page import generate_pages_recursive
from generate_page import generate_page
import shutil
import os


def copy_static_to_public():
    # delete everything to public first
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_static_to_public_helper("static", "public")


def copy_static_to_public_helper(src, dst):
    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)

        if os.path.isfile(src_path):
            print(f"copying... [{src_path} -> {dst_path}]")
            shutil.copy(src_path, dst_path)
        else:
            os.mkdir(dst_path)
            copy_static_to_public_helper(src_path, dst_path)


def main():
    copy_static_to_public()
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
