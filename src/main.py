from textnode import TextNode, TextType


def main():
    dummy = TextNode("This is my website link", TextType.LINK, "https://priyanshoon.me")
    print(dummy)


main()
