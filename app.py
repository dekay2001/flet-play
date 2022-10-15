import os

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

import fs.utils as futil

TEST_FILE = os.path.join(os.getcwd(), 'data', 'test.json')
INTRO_TEXT = f'Write a key and value to write to {TEST_FILE}'

class MainApp:
    def __init__(self):
        self._main_page = None

    def render_page(self, page: Page):
        self._main_page = page
        self._key = TextField(label='Enter a key')
        self._value = TextField(label='Enter a value')
        self._feedback = TextField(label="Your name is Dan")
        self._display_json = TextField(label="", max_lines=50)

        self._main_page.add(
            Row(controls=[
                Text(INTRO_TEXT, size=20, color="pink600", italic=True)
            ])
        )
        self._main_page.add(
            Row(controls=[
                self._key,
                self._value
            ])
        )
        self._main_page.add(
            Row(controls=[
                self._feedback
            ])
        )
        self._main_page.add(
            Row(controls=[self._display_json])
        )
        self._main_page.add(
            Row(controls=[
                ElevatedButton(text="Render List", on_click=self.render_list_view),
                ElevatedButton(text="Render Grid", on_click=self.render_grid_view),
                ElevatedButton(text="Write Name File", on_click=self.write_name_to_file)
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

    def write_name_to_file(self, e):
        file = futil.LocalJsonFile(TEST_FILE)
        key = self._key.value
        value = self._value.value
        content_written = f'{key}: {value}'
        file.write(key, value)
        self._display_json.value = file.pretty_content
        self._display_feedback_message(content_written)

    def _display_feedback_message(self, message):
        self._feedback.value = message
        self._main_page.update()

def main(page: Page):
    app = MainApp()
    app.render_page(page)

# flet.app(target=main, view=flet.WEB_BROWSER)
flet.app(target=main)
