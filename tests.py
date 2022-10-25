import unittest
from libsff import Document, Balloon, Out
from random import randint
from time import perf_counter


def create_random_content() -> list:
    uwu = []
    for _ in range(randint(1, 3)):
        uwu.append("ş" * randint(50, 100))
    return uwu


def create_random_sffx():
    with open("testimg.jpg", "rb") as file:
        imagefile = file.read()

    docasd = Document.create_blank()

    for _ in range(100):
        has_image = randint(0, 1)

        docasd.add_balloon(
            Balloon(
                tl_content=create_random_content(),
                btype=randint(0, 4),
                has_img=has_image,
                balloon_img=imagefile if has_image else b"",
                img_type="jpg"
            )
        )
    
    return docasd


def timer(func):  
    def wrap(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
          
        print(f"Test {func.__name__} took {end-start} seconds.")
        return result
    return wrap


class TestCreateEmpty(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.doc = create_random_sffx()

    @timer
    def test_create_empty(self):
        docasd = Document.create_blank()
        self.assertTrue(
            isinstance(docasd, Document) and docasd.balloon_count == 0
        )

    @timer
    def test_open_sff(self):
        self.doc = Document.create_from_sff("test.sffx")
        self.assertIsInstance(
           self.doc, Document
        )

    @timer
    def test_save_sffx(self):
        self.assertTrue(
            self.doc.save_sff("test", Out.RAW)
        )

    @timer
    def test_save_sffg(self):
        self.assertTrue(
            self.doc.save_sff("test", Out.GZIP)
        )

    @timer
    def test_save_sffl(self):
        self.assertTrue(
            self.doc.save_sff("test", Out.LZMA)
        )

    @timer
    def test_save_txt(self):
        self.assertTrue(
            self.doc.save_sff("test", Out.TXT)
        )


if __name__ == "__main__":
    # create_random_sffx()
    unittest.main()