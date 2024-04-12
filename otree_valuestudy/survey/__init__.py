from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# some variables 
LIKERT_CHOICES = [
        [1, 'Stimme gar nicht zu'],
        [2, 'Stimme eher nicht zu'],
        [3, 'Neutral'],
        [4, 'Stimme eher zu'],
        [5, 'Stimme voll zu'],
    ]


class Player(BasePlayer):


    education = models.StringField(
        label="Was ist Ihr höchster Bildungsabschluss?",
        choices=[
            ('NoDegree', 'Kein Abschluss'),
            ('MittlereReife', 'Mittlere Reife'),
            ('Abitur', 'Abitur'),
            ('University', 'Bachelor'),
            ('Master', 'Master'),
            ('Promotion', 'Promotion'),
        ],
        widget=widgets.RadioSelect,
    )

    age = models.IntegerField(
        label='What is your age?', min=13, max=125
        )

    gender = models.StringField(
        label="Geschlecht",
        choices=[
            ('männlich', 'männlich'),
            ('weiblich', 'weiblich'),
            ('divers', 'divers'),
            ('NA', 'möchte ich nicht angeben'),
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )


# SURVEY Preferences.html
    question1 = models.IntegerField(
        label="Es ist wichtig für mich, meine Privatsphäre im Internet zu schützen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question2 = models.IntegerField(
        label="Wenn ich Websites besuche, versuche ich normalerweise, so wenig Daten wie möglich preiszugeben.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question3 = models.IntegerField(
        label="Ich schätze personalisierte Werbung, die auf meinen vorherigen Online-Aktivitäten zugeschnitten sind.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

# SURVEY Preferences2.html

    question4 = models.IntegerField(
            label="...dass Online-Organisationen nicht sind, wer sie vorgeben zu sein?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question5 = models.IntegerField(
            label="...dass bei der Anmeldung oder bei Online-Einkäufen viele persönliche Informationen angeben werden müssen?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question6 = models.IntegerField(
            label="...dass Personen, die Sie nicht kennen, durch Ihre Online-Aktivitäten persönliche Informationen über Sie erhalten?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question7 = models.IntegerField(
            label="...über Online-Identitätsdiebstahl?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question8 = models.IntegerField(
            label="...dass eine Nachricht, die Sie jemandem online schicken, unberechtigterweise an andere weitergeleitet werden könnte?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question9 = models.IntegerField(
            label="...dass Informationen über Sie auf einem alten Computer gefunden werden könnten?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question10 = models.IntegerField(
            label="...dass Nachrichten, die Sie online erhalten, nicht von der Person stammen, die diese vorgibt zu sein?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

# FUNCTIONS


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['education', 'age', 'gender']


class Preferences(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question3']

class Preferences2(Page):
    form_model = 'player'
    form_fields = ['question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10']


page_sequence = [Demographics, Preferences, Preferences2 ]
