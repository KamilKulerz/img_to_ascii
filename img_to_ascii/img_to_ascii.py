from .imageHandler import AsciiGrayscaleImageHandler
from .imageTranslator import AsciiGrayscaleTranslator


def main() -> None:
    TRANSLATION_TABLE = " :=*%"
    # TRANSLATION_TABLE = " .:-=+*#%@"
    # TRANSLATION_TABLE = " ░▒▓"
    # TRANSLATION_TABLE = """ .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
    # TRANSLATION_TABLE = """ .\'`^~+_-?][}{1)(rxnuvczQ0OZmwqo*#M%B@$"""

    INPUT_FILE_PATH = "input/lena1.png"

    agt = AsciiGrayscaleTranslator(TRANSLATION_TABLE)

    agh = AsciiGrayscaleImageHandler(agt, INPUT_FILE_PATH)

    agh.save_to_file("output/out1.txt", vertical_spacing=3)


if __name__ == "__main__":
    main()
