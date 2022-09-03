import flet
from flet import (
    alignment, 
    border, 
    border_radius, 
    colors, 
    Container, 
    ElevatedButton,
    ListView, 
    GridView, 
    Page, 
    Row, 
    Text, 
    TextField
)


class MainApp:
    def __init__(self):
        self._main_page = None

    def render_page(self, page: Page):
        self._main_page = page

        self._main_page.add(
            Row(controls=[
                TextField(label="Your name"),
                ElevatedButton(text="Render List", on_click=self.render_list_view),
                ElevatedButton(text="Render Grid", on_click=self.render_grid_view)
            ])
        )

    def button_clicked(self, e):
        self._main_page.add(Text("Clicked!"))

    def render_list_view(self, e):
        lv = ListView(expand=True, spacing=10)
        for i in range(20):
            lv.controls.append(Text(f"Line {i}"))
        self._main_page.add(lv)

    def render_grid_view(self, e):
        r = Row(wrap=True, scroll="always", expand=True)
        self._main_page.add(r)
        for i in range(20):
            r.controls.append(
                Container(
                    Text(f"Item {i}"),
                    width=100,
                    height=100,
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    border=border.all(1, colors.AMBER_400),
                    border_radius=border_radius.all(5),
                )
            )
        self._main_page.update()

def main(page: Page):
    app = MainApp()
    app.render_page(page)

flet.app(target=main, view=flet.WEB_BROWSER)
