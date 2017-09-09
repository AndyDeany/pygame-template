from spec.helper import *

import os

with description("Game"):
    # Uses TestGame which inherits all of game's functions
    with it("should initialise correctly"):
        pass

    with context(".path_to()"):
        global joined_path_to

        def joined_path_to(*path_elements):
            return os.path.join(os.getcwd(), *path_elements)

        with it("should give a path to a given file in the root directory"):
            expected_path = joined_path_to("file.txt")
            expect(game.path_to("file.txt")).to(equal(expected_path))

        with it("should give a path to a file embedded in further folders"):
            expected_path = joined_path_to("folder", "file.txt")
            expect(game.path_to("folder/file.txt")).to(equal(expected_path))

        with it("should load a file when given it's location using multiple arguments"):
            expected_path = joined_path_to("folder", "file.txt")
            expect(game.path_to("folder", "file.txt")).to(equal(expected_path))

            expected_path = joined_path_to("folder", "deeper_folder", "file.txt")
            expect(game.path_to("folder/deeper_folder", "file.txt")).to(equal(expected_path))

    with context(".log()"):
        pass

    with context(".initialise_screen()"):
        pass

    with context(".load_image()"):
        pass

    with context(".load_font()"):
        pass

    with context(".display()"):
        pass

    with context(".inputs()"):
        pass

    with context(".update()"):
        pass

    with context(".runtime()"):
        pass

    with context(".check_quit()"):
        pass

    with context(".run()"):
        pass
