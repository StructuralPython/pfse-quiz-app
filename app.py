from textual import on
from textual.app import App, ComposeResult
import textual.validation as validation
import textual.widgets as widgets

from validators import EmailValidator
from components.titles import Header1, Header2, Header3




class FormsApp(App):
    """
    A Textual app for a form questionnaire
    """
    BINDINGS = [
        ('d', 'toggle_dark', 'Toggle dark mode'),
    ]
    CSS_PATH = "forms.tcss"

    TABS = {
        "About You":
            [
                Header1("# About You"),
                widgets.Markdown(
                    "Tell me a bit about yourself. Your personal information "
                    "is not stored unless, at the end, you choose to sign up "
                    "for the PfSE Async Course waiting list."
                ),
                widgets.Input(placeholder="Type your name here...", id="name_input"),
                widgets.Input(
                    placeholder="Type your email address...", 
                    id="email_input",
                    validators=[EmailValidator()],
                    validate_on=['submitted'],
                    ),
                widgets.RadioSet(
                    *(
                        "0-2 years", 
                        "2-5 years", 
                        "5-10 years", 
                        "10-15 years", 
                        "15-20 years", 
                        "20+ years"
                    ),
                    id="years_experience",
                ),
            ],
        "Your Daily Work": [
            widgets.Label("Do you use a spreadsheet application in your work?"),
            widgets.RadioSet(
                *(
                    "Daily",
                    "1-3 times per week",
                    "Occasionally (1-3 times per month)",
                ),
                id="use_spreadsheets"
            ),
            widgets.Label("What do you typically use spreadsheets for?"),
            widgets.SelectionList(
                ("Design calculations", 0),
                ("Tabulating loads (either manually or with a template)", 1),
                ("Post-processing (manipulating analysis results prior to design)", 2),
                ("Pre-processing (defining model geometry or element properties prior to analysis)", 3),
                ("Intermediate data storage or processing between apps", 4),
                ("Reporting or design documentation", 5),
                ("Other data manipulation (e.g. material take-offs, correlating sensor data, etc.)", 6),
            )
        ],
        "Your Internal Conversations": [],
        "Your Learning Style": [],
        "Results": []
    }

    def compose(self) -> ComposeResult:
        """
        Creates the child widgets for the app
        """
        yield widgets.Header()
        yield widgets.Markdown("# Python for Structural Engineers: Self-qualification test")
        with widgets.TabbedContent():
            for tab_name, tab_content in self.TABS.items():
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