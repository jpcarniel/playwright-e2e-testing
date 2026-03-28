# Page Object for the Hovers page (/hovers)


class HoversPage:
    FIGURES = ".figure"
    FIGURE_CAPTION = ".figcaption h5"
    PROFILE_LINK = ".figcaption a"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/hovers")

    def hover_over_figure(self, index):
        """Hover over a specific avatar by index (0-based)."""
        self.page.locator(self.FIGURES).nth(index).hover()

    def get_figure_caption(self, index):
        """Get the caption text locator for a specific figure."""
        return self.page.locator(self.FIGURES).nth(index).locator(self.FIGURE_CAPTION)

    def get_profile_link(self, index):
        """Get the profile link locator for a specific figure."""
        return self.page.locator(self.FIGURES).nth(index).locator(self.PROFILE_LINK)
