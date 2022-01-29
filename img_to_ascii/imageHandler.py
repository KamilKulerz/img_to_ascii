from abc import ABC

import cv2
import numpy.typing as npt

from .imageTranslator import ImageTranslator


class ImageHandler(ABC):
    def __init__(self, translator: ImageTranslator):
        self.translator = translator

    def _open_image(self) -> npt.NDArray:
        ...

    def get_image(self) -> npt.NDArray:
        ...

    def save_to_file(self, out_filpath: str, vertical_spacing: int) -> None:
        ...


class AsciiGrayscaleImageHandler(ImageHandler):
    """handler for images to translate and save array of ascii characters"""

    def __init__(self, translator: ImageTranslator, filepath: str):
        self.translator: ImageTranslator = translator
        self._filepath: str = filepath
        self.img: npt.NDArray = self.translator.translate_image(self._open_image())

    def _open_image(self) -> npt.NDArray:
        """opens image file and returns grayscale np array"""
        return cv2.imread(self._filepath, cv2.IMREAD_GRAYSCALE)

    def get_image(self) -> npt.NDArray:
        """returns image"""
        return self.img

    def save_to_file(self, out_filpath: str, vertical_spacing: int) -> None:
        """saves image to .txt file with indicated vertical_spacing, spacing skips lines"""
        if vertical_spacing < 2:
            raise ValueError("Spacing must be greater than 1")
        with open(out_filpath, "w", encoding="utf-8") as f:
            for i, row in enumerate(self.img):
                if i % vertical_spacing != 0:
                    f.write("".join(row) + "\n")
