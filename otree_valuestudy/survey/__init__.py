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

    age = models.IntegerField(label='What is your age?', min=13, max=125)

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


# FUNCTIONS


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['education', 'age', 'gender']


class index(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Demographics, index ]
