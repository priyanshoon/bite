import shutil
import os

from textnode import TextNode, TextType


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
    dummy = TextNode("This is my website link", TextType.LINK, "https://priyanshoon.me")
    print(dummy)
    copy_static_to_public()


main()
