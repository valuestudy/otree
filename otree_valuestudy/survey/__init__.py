from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass




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

    question1 = models.IntegerField(
        label="Es ist wichtig für mich, meine Privatsphäre im Internet zu schützen.",
        choices=[
            [1, 'Stimme gar nicht zu'],
            [2, 'Stimme eher nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme eher zu'],
            [5, 'Stimme voll zu']
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    question2 = models.IntegerField(
        label="Wenn ich Websites besuche, versuche ich normalerweise, so wenig Daten wie möglich preiszugeben.",
        choices=[
            [1, 'Stimme gar nicht zu'],
            [2, 'Stimme eher nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme eher zu'],
            [5, 'Stimme voll zu']
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    question3 = models.IntegerField(
        label="Ich schätze personalisierte Werbung, die auf meinen vorherigen Online-Aktivitäten zugeschnitten sind.",
        choices=[
            [1, 'Stimme gar nicht zu'],
            [2, 'Stimme eher nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme eher zu'],
            [5, 'Stimme voll zu']
        ],
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


page_sequence = [Demographics, Preferences ]
