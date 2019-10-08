from PIL import Image


class Pixel():
    def __init__(self, inValue, *args, **kwargs):
        self.value = inValue
        self.outline = None
