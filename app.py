from textual import on
from textual.app import App, ComposeResult
import textual.validation as validation
import textual.widgets as widgets

from validators import EmailValidator
from components.titles import Header1, Header2, Header3
from layout import TAB_CONTENT




class FormsApp(App):
    """
    A Textual app for a form questionnaire
    """
    BINDINGS = [
        ('d', 'toggle_dark', 'Toggle dark mode'),
    ]
    CSS_PATH = "forms.tcss"


    def compose(self) -> ComposeResult:
        """
        Creates the child widgets for the app
        """
        yield widgets.Header()
        yield widgets.Markdown("# Python for Structural Engineers: Self-qualification test")
        with widgets.TabbedContent():
            for tab_name, tab_content in TAB_CONTENT.items():
                with widgets.TabPane(tab_name):
                    for content_item in tab_content:
                        yield content_item
        yield widgets.Button("Next", id="advance")
        yield widgets.RichLog()
        yield widgets.Footer()

    def action_toggle_dark(self) -> None:
        """
        Toggle dark mode
        """
        self.dark = not self.dark

    @on(widgets.Input.Submitted)
    def accept_email_addy(self, event: widgets.Input.Submitted):
        input = self.query_one("#email_input", widgets.Input) # Specify widget id with this special str style
        rich_log = self.query_one(widgets.RichLog)
        # rich_log.write(event.input)
        if event.input.id == "email_input" and not event.validation_result.is_valid:
            rich_log.write(event.validation_result.failure_descriptions)
        else:
            rich_log.write(input.value)





if __name__ == "__main__":
    app = FormsApp()
    app.run()