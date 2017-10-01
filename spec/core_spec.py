"""File containing unit tests for the pygametemplate.core module."""
import os
import traceback
from datetime import datetime

from expects import *

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
                time_logged = datetime.utcnow()
                expected_traceback = traceback.format_exc()

            details = (time_logged, extended_error_message, expected_traceback)
            expected_logged_error = "{} - {}.\n{}\n".format(*details)

            with open("log.txt", "r", encoding="utf-8") as log_file:
                expect(log_file.read()).to(equal(expected_logged_error))

            os.remove("log.txt")

        # The below test is currently untestable properly.
        # with it("should log a fatal error correctly"):
        #     pass

    with context(".load_image()"):
        pass

    with context(".load_font()"):
        pass
