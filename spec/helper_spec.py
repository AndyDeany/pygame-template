from spec.helper import *

from pygametemplate import load_font
from pygametemplate.helper import wrap_text

font = load_font("test", 20)

with description("pygametemplate.helper"):
    with context(".load_class_assets()"):
        pass

    with context(".wrap_text()"):
        with it("should wrap valid text correctly"):
            text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Aliquam faucibus magna arcu, nec finibus lectus gravida "
                    "ultrices. Nam non nibh tellus. Pellentesque molestie "
                    "sagittis mi eget interdum. Vivamus semper metus vestibulum "
                    "metus interdum porttitor. Phasellus suscipit enim at "
                    "sollicitudin luctus. Nam ultrices quis leo a faucibus. "
                    "Mauris porta nibh ultrices quam bibendum, sed cursus velit "
                    "elementum. Etiam ultrices molestie sem vitae accumsan. "
                    "Maecenas dictum gravida nulla non blandit.")
            lines = wrap_text(text, font, 200)
            for index, line in enumerate(lines):
                # Check that the line isn't too long
                expect(font.size(line)[0]).to(be_below_or_equal(200))
                if not index + 1 == len(lines):
                    # Check that the line is as long as it could be
                    next_word = lines[index+1].split()[0]
                    joined_width = font.size(" ".join((line, next_word)))[0]
                    expect(joined_width).to(be_above(200))

        with it("should create a forced newline wherever \\n is present in the text"):
            text = "Lorem\nipsum\ndolor\nsit\namet."
            lines = wrap_text(text, font, 200)
            expect(lines).to(equal(["Lorem", "ipsum", "dolor", "sit", "amet."]))

        with it("should raise an error if the first word is too long to wrap"):
            text = "Supercalifragilisticexpialidocious."
            expect(lambda: wrap_text(text, font, 200)).to(raise_error(ValueError))

        with it("should raise an error if a word in the middle is too long to wrap"):
            text = "I am feeling supercalifragilisticexpialidocious today!"
            expect(lambda: wrap_text(text, font, 200)).to(raise_error(ValueError))

        with it("should raise an error if the last word is too long to wrap"):
            text = "My favourite word is supercalifragilisticexpialidocious!"
            expect(lambda: wrap_text(text, font, 200)).to(raise_error(ValueError))
