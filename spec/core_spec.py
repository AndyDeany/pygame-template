"""File containing unit tests for the pygametemplate.core module."""
import os
import traceback
from datetime import datetime

from expects import *
import pygame

from spec.helper import game
from pygametemplate.core import path_to, log, load_image, load_font


with description("pygametemplate.core"):
    with context(".path_to()"):
        global joined_path_to

        def joined_path_to(*path_elements):
            return os.path.join(os.getcwd(), *path_elements)

        with it("should give a path to a given file in the root directory"):
            expected_path = joined_path_to("file.txt")
            expect(path_to("file.txt")).to(equal(expected_path))

        with it("should give a path to a file embedded in further folders"):
            expected_path = joined_path_to("folder", "file.txt")
            expect(path_to("folder/file.txt")).to(equal(expected_path))

        with it("should load a file when given it's location using multiple arguments"):
            expected_path = joined_path_to("folder", "file.txt")
            expect(path_to("folder", "file.txt")).to(equal(expected_path))

            expected_path = joined_path_to("folder", "deeper_folder", "file.txt")
            expect(path_to("folder/deeper_folder", "file.txt")).to(equal(expected_path))

    with context(".log()"):
        try:
            os.remove("log.txt")    # Clean starting environment
        except Exception:   # TODO: Change to FileNotFoundError (python3 only)
            pass

        with it("should log a non-fatal error correctly"):
            extended_error_message = "example extended error message"
            try:
                raise ValueError("example raised error message")
            except ValueError:
                log(extended_error_message, fatal=False)
                datetime_logged = datetime.utcnow()
                expected_traceback = traceback.format_exc()

            summary_line_regex = r"%s.\d{6} - %s" % (str(datetime_logged).split(".")[0],
                                                     extended_error_message)
            with open("log.txt", "r") as log_file:
                expect(log_file.readline()).to(match(summary_line_regex))
                expect(log_file.read()).to(equal(expected_traceback + "\n"))

            os.remove("log.txt")

        # The below test is currently untestable properly.
        # with it("should log a fatal error correctly"):
        #     pass

    with context(".load_image()"):
        global check_images_equal

        def check_images_equal(actual, expected):
            expect(type(actual)).to(equal(type(expected)))
            expect(actual.get_size()).to(equal(expected.get_size()))
            expect(actual.get_alpha()).to(equal(expected.get_alpha()))

        with it("should load a .png image correctly"):
            image = load_image("test")
            test_png_path = path_to("assets/images/test.png")
            expected_image = pygame.image.load(test_png_path).convert_alpha()
            check_images_equal(image, expected_image)

        with it("should load a .ico image correctly"):
            image = load_image("test", file_extension=".ico")
            test_ico_path = path_to("assets/images/test.ico")
            expected_image = pygame.image.load(test_ico_path).convert_alpha()
            check_images_equal(image, expected_image)

        with it("should load a non-fixed-alpha .png image correctly"):
            image = load_image("test", fade_enabled=True)
            test_png_path = path_to("assets/images/test.png")
            expected_image = pygame.image.load(test_png_path).convert()
            check_images_equal(image, expected_image)

        with it("should raise an error when the given image name isn't found"):
            expect(lambda: load_image("non_existant")).to(raise_error(IOError))

    with context(".load_font()"):
        pass
