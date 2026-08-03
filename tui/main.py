from textual.app import App, ComposeResult
from textual.widgets import Label, ListView, ListItem

class TUI(App):
    CSS_PATH = "main.tcss"

    def compose(self):
        yield ListView(
            ListItem(Label("Calendar")),
            ListItem(Label("Stacks")),
            ListItem(Label("Tasks")),
            ListItem(Label("Time log")),
        )