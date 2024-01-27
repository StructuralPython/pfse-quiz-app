from textual import widgets
from components.titles import Header1, Header2, Header3
from validators import EmailValidator

TAB_CONTENT = {
    # TAB
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

    # TAB   
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
        ),

        widgets.Label(
            "Looking at the last 12 months as a whole, what percentage of your "
            "time is spent on either *manual data entry* or *manual click and drag*"
            ),
        widgets.RadioSet(
            *(
                "0 - 20%",
                "21 - 50%",
                "51 - 80%",
                "80 - 100%",
            ),
            id="percentage_manual_spreadsheet",
        ),
        widgets.Label(
            "Approximately how many different commercial engineering software "
            "packages do you use in a 'typical' month?"
            ),
        widgets.RadioSet(
            *(
                "1 - 2",
                "3 - 5",
                "5 - 8",
                "8+",
            ),
            id="number_of_commercial_software"
        ),
        widgets.Label(
            "Of the engineering software packages you use, how does your level of productivity _feel_ to you when you use them?"
        ),
        widgets.RadioSet(
            *(
                "Our software does exactly what I need almost all of the time. It requires little setup and I can execute designs profitably.",
                "Our software does a few things well but it requires some setup time. I find myself having to manually manipulate results. Could be better.",
                "Our software does one thing well and requires significant setup. The outputs are not in a suitable format for design. I need to do a lot of unprofitable work.",
            )
        ),

    ],
    "Your Internal Conversations": [
        Header1("# Your internal conversations"),
        widgets.Label(
            "With what frequency do you say to yourself, 'There MUST be a better way!'?"
        ),
        widgets.RadioSet(
            *(
                "Never, I have the best way",
                "2-3 times ever in my career to date",
                "2-3 times a year",
                "2-3 times a month",
                "2-3 times a week",
                "2-3 times a day!"
            )
        ),
        widgets.Label(
            "Which statements reflect your internal monologue while you are working? Select all that apply."
        ),
        widgets.SelectionList(
            *(
                ()
            )
        )
    ],
    "Your Learning Style": [],
    "Results": []
}