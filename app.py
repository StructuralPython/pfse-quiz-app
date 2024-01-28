from textual import on
from textual.app import App, ComposeResult
import textual.validation as validation
import textual.widgets as widgets

from validators import EmailValidator
from components.titles import Header1, Header2, Header3
from layout import TAB_CONTENT

tab_ids = [f"tab-{idx + 1}" for idx, _ in enumerate(TAB_CONTENT.keys())]

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
        with widgets.TabbedContent(id="quiz_tabs"):
            for tab_name, tab_content in TAB_CONTENT.items():
                with widgets.TabPane(tab_name, name=tab_name):
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


    @on(widgets.Button.Pressed, "#advance")
    # @on(widgets.TabbedContent.TabActivated)
    def advance_tabs(self, event: widgets.Button.Pressed):
        tab_status = self.query_one(widgets.TabbedContent)
        rich_log = self.query_one(widgets.RichLog)
        advance_button = self.query_one("#advance", widgets.Button)
        rich_log.write("Pressed")
        rich_log.write(tab_status)
        rich_log.write(advance_button.label)
        # tab_status.disabled = False
        current_tab = tab_status.active
        next_tab = None
        if advance_button.Pressed and current_tab != tab_ids[-1]:
            current_tab_idx = tab_ids.index(f"{current_tab}")
            next_tab_idx = current_tab_idx + 1
            next_tab = tab_ids[next_tab_idx]
            tab_status.active = next_tab
            advance_button.label = "Next"
        else:
            rich_log.write("Submitted!")
            # tab_status.disabled = True
        if next_tab == tab_ids[-1]:
            advance_button.label = "Submit"

            

    # @on(widgets.TabbedContent.TabActivated)
    # def show_tab(self, event: widgets.TabbedContent.TabActivated):
    #     rich_log = self.query_one(widgets.RichLog)
    #     rich_log.write(event.tab)









if __name__ == "__main__":
    app = FormsApp()
    app.run()