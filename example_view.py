from pygametemplate import View, load_font


class ExampleView(View):

    font = load_font("test", 20)
    background_colour = (0, 0, 0)
    text_colour = (255, 255, 255)
    coords = (100, 100)

    def load(self):
        pass

    def unload(self):
        pass

    def logic(self):
        self.text = self.font.render("This is an example :)", True, self.text_colour)

    def draw(self):
        self.game.screen.fill(self.background_colour)
        self.game.screen.blit(self.text, self.coords)
