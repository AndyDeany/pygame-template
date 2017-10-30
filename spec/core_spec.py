"""File containing unit tests for the pygametemplate.core module."""
import os
import traceback
from datetime import datetime

import pygame

from spec.helper import *
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
        except FileNotFoundError:
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
            with open("log.txt", "r", encoding="utf-8") as log_file:
                expect(log_file.readline()).to(match(summary_line_regex))
                expect(log_file.read()).to(equal(expected_traceback + "\n"))

            os.remove("log.txt")

        # The below test is currently untestable properly.
        # with it("should log a fatal error correctly"):
        #     pass

    with context(".load_image()"):
        with before.all:
            def check_images_equal(actual, expected):
                expect(type(actual)).to(equal(type(expected)))
                expect(actual.get_size()).to(equal(expected.get_size()))
                expect(actual.get_alpha()).to(equal(expected.get_alpha()))
            self.check_images_equal = check_images_equal

        with it("should load a .png image correctly"):
            image = load_image("test")
            test_png_path = path_to("assets/images/test.png")
            expected_image = pygame.image.load(test_png_path).convert_alpha()
            self.check_images_equal(image, expected_image)

        with it("should load a .ico image correctly"):
            image = load_image("test", file_extension=".ico")
            test_ico_path = path_to("assets/images/test.ico")
            expected_image = pygame.image.load(test_ico_path).convert_alpha()
            self.check_images_equal(image, expected_image)

        with it("should load a non-fixed-alphas .png image correctly"):
            image = load_image("test", fix_alphas=False)
            test_png_path = path_to("assets/images/test.png")
            expected_image = pygame.image.load(test_png_path).convert()
            self.check_images_equal(image, expected_image)

        with it("should raise an error when the given image name isn't found"):
            expect(lambda: load_image("non_existant")).to(raise_error(IOError))

    with context(".load_font()"):
        with before.all:
            def check_fonts_equal(actual, expected):
                expect(actual.get_bold()).to(equal(expected.get_bold()))
                expect(actual.get_italic()).to(equal(expected.get_italic()))
                expect(actual.get_underline()).to(equal(expected.get_underline()))

                expect(actual.get_height()).to(equal(expected.get_height()))
                expect(actual.get_linesize()).to(equal(expected.get_linesize()))

                expect(actual.get_ascent()).to(equal(expected.get_ascent()))
                expect(actual.get_descent()).to(equal(expected.get_descent()))

                sample_strings = (
                    "hello", "goodbye",
                    "What's the time, Mr Wolf?",
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Morbi fringilla dignissim nisl, nec tincidunt felis faucibus sed. "
                    "Pellentesque laoreet odio justo, ac commodo diam eleifend vitae. "
                    "Donec viverra ipsum diam, non euismod ex semper non. "
                    "Proin fermentum lorem vitae felis vehicula suscipit. "
                    "Nulla eu condimentum nisi, ut viverra neque. "
                    "Ut condimentum mattis ligula, id maximus lacus congue in. "
                    "Donec nec tempus leo, nec rhoncus leo. "
                    "Donec condimentum semper sapien at ultricies. "
                    "Integer fermentum velit vel mauris posuere sollicitudin. "
                    "Cras lobortis metus a varius iaculis. "
                    "Aliquam feugiat, diam a hendrerit facilisis, "
                    "lacus diam molestie purus, nec sagittis leo magna ac lorem. "
                    "Nam tristique tortor at suscipit tincidunt. "
                    "Interdum et malesuada fames ac ante ipsum primis in faucibus. "
                    "Etiam eget urna ut purus pulvinar egestas. "
                    "Morbi quis malesuada tellus. "
                    "Donec vestibulum, lorem vel ullamcorper scelerisque, "
                    "lectus odio euismod arcu, et auctor urna augue non lectus.",
                    "Phew, it worked :)"
                )
                for string in sample_strings:
                    expect(actual.size(string)).to(equal(expected.size(string)))
            self.check_fonts_equal = check_fonts_equal

        with it("should load a .ttf font correctly"):
            test_font_path = path_to("assets/fonts/chewy.ttf")
            expected_font = pygame.font.Font(test_font_path, 12)
            self.check_fonts_equal(load_font("chewy", 12), expected_font)

        with it("should raise an error when the given font name isn't found"):
            expect(lambda: load_font("non_existant", 12)).to(raise_error(IOError))
