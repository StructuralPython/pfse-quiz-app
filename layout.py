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
            "Do you already have some thoughts about what the better way might be?"
        ),
        widgets.RadioSet(
            *(
                "Yes",
                "Kind of, but nothing really concrete",
                "Not yet"
            )
        ),
        widgets.Label(
            "Is there something holding you back from building the kind engineering workflow you want?"
        ),
        widgets.SelectionList(
            *(
                ("Lack of time", 0),
                ("Lack of funding", 1),
                ("Lack of skills", 2),
                ("Lack of support or help", 3),
                ("Lack of ideas", 4),
                ("Lack of community", 5),
            )
        )
    ],
    "Your Learning Style": [
        widgets.Label(
            "From courses you have taken in the past, what traits have made courses most enjoyable for you?"
        ),
        widgets.SelectionList(
            *(
                ("The course material was highly relevant", 0),
                ("The instructor taught well", 1),
                ("The course was well-structured", 2),
                ("I could access the course materials in the order that I wanted", 3),
            )
        )
        widgets.RadioSet(
            *(
                "No",
                "Yes",
            )
        ),
        widgets.Label(
            "What "
        ),
        widgets.Label(
            "When you take any course, what kind of behaviours reflect how you are as a student?"
        ),
        widgets.SelectionList(
            *(
                ("I like to work methodically through the course material as it is presented", 0),
                ("I like to see all material upfront and do that parts that interest me most", 1),
                ("I like to hear the opinions of others and focus on the parts they recommend", 2),
                ("I tend to follow the advice of the instructor.", 3),
                ("I tend to follow my own advice", 4),
            )
        ),

    ],
    "Results": []
}