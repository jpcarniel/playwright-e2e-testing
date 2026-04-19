from playwright.sync_api import expect


class TestHovers:
    def test_should_display_name_when_hovering_over_first_avatar(self, hovers_page):
        hovers_page.visit()
        hovers_page.hover_over_figure(0)

        expect(hovers_page.get_figure_caption(0)).to_be_visible()
        expect(hovers_page.get_figure_caption(0)).to_contain_text("user1")

    def test_should_display_name_when_hovering_over_second_avatar(self, hovers_page):
        hovers_page.visit()
        hovers_page.hover_over_figure(1)

        expect(hovers_page.get_figure_caption(1)).to_be_visible()
        expect(hovers_page.get_figure_caption(1)).to_contain_text("user2")

    def test_should_display_name_when_hovering_over_third_avatar(self, hovers_page):
        hovers_page.visit()
        hovers_page.hover_over_figure(2)

        expect(hovers_page.get_figure_caption(2)).to_be_visible()
        expect(hovers_page.get_figure_caption(2)).to_contain_text("user3")

    def test_should_have_correct_profile_links(self, hovers_page):
        hovers_page.visit()

        for i in range(3):
            hovers_page.hover_over_figure(i)
            expect(hovers_page.get_profile_link(i)).to_have_attribute(
                "href", f"/users/{i + 1}"
            )
