from imageTranslator import AsciiGrayscaleTranslator
from imageHandler import AsciiGrayscaleImageHandler


def main() -> None:
    agt = AsciiGrayscaleTranslator(" :=*%")

    # agt = AsciiGrayscaleTranslator(" .:-=+*#%@")
    # agt = AsciiGrayscaleTranslator(" ░▒▓")
    # agt = AsciiGrayscaleTranslator(""" .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$""")
    # agt = AsciiGrayscaleTranslator(""" .\'`^~+_-?][}{1)(rxnuvczQ0OZmwqo*#M%B@$""")

    agh = AsciiGrayscaleImageHandler(agt, "input/lena1.png")

    agh.save_to_file("output/out1.txt", 2)


if __name__ == "__main__":
    main()
