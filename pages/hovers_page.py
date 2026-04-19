class HoversPage:
    FIGURES = ".figure"
    FIGURE_CAPTION = ".figcaption h5"
    PROFILE_LINK = ".figcaption a"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/hovers")

    def hover_over_figure(self, index):
        self.page.locator(self.FIGURES).nth(index).hover()

    def get_figure_caption(self, index):
        return self.page.locator(self.FIGURES).nth(index).locator(self.FIGURE_CAPTION)

    def get_profile_link(self, index):
        return self.page.locator(self.FIGURES).nth(index).locator(self.PROFILE_LINK)
