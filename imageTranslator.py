from abc import ABC
import math
import numpy as np
import numpy.typing as npt


class ImageTranslator(ABC):
    def _single_translation(self, inp: int) -> str:
        ...

    def translate_image(self, img: npt.NDArray) -> npt.NDArray:
        ...


class AsciiGrayscaleTranslator(ImageTranslator):
    """translator of np array image values to ascii characters"""

    def __init__(self, translation_table: str) -> None:
        super().__init__()
        self._translation_table = translation_table

    def _single_translation(self, inp: int) -> str:
        """translation of image values to ascii characters"""
        divisor = math.ceil(255 / len(self._translation_table))
        return self._translation_table[int(inp / divisor)]

    def translate_image(self, img: npt.NDArray) -> npt.NDArray:
        """translates full image and returns np array with corresponding ascii values"""
        func_vec = np.vectorize(self._single_translation)
        result = func_vec(img)
        return result
