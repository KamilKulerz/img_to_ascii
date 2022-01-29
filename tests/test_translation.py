import pytest
from imageTranslator import AsciiGrayscaleTranslator


@pytest.mark.parametrize(
    "in1, out1",
    [
        (0, " "),
        (25, " "),
        (26, "."),
        (51, "."),
        (52, ":"),
        (77, ":"),
        (78, "-"),
        (103, "-"),
        (104, "="),
        (129, "="),
        (130, "+"),
        (155, "+"),
        (156, "*"),
        (181, "*"),
        (182, "#"),
        (207, "#"),
        (208, "%"),
        (233, "%"),
        (234, "@"),
        (255, "@"),
    ],
)
def test_translation(in1, out1):
    agt = AsciiGrayscaleTranslator(" .:-=+*#%@")
    assert agt._single_translation(in1) == out1
