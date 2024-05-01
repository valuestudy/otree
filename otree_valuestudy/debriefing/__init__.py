from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'debriefing'
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

    question31 = models.IntegerField(
        label="Dieser Cookie Banner ist unehrlich zu seinen Nutzern.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question32 = models.IntegerField(
        label="Dieser Cookie Banner versucht Nutzer zu einer Auswahl zu verleiten, die sie eigentlich nicht treffen wollen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question33 = models.IntegerField(
        label="Dieser Cookie Banner verwendet missverständliche Techniken, um Nutzer zu einer Auswahl zu verleiten, die sie eigentlich nicht treffen wollen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question34 = models.IntegerField(
        label="Es war kompliziert für mich, die Cookieauswahl zu treffen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question35 = models.IntegerField(
        label="Es war frustrierend für mich, die Cookieauswahl zu treffen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question36 = models.IntegerField(
        label="Es war einfach für mich, die Cookieauswahl zu treffen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question37 = models.IntegerField(
    label="Ich bereue meine Cookieauswahl.",
    choices=LIKERT_CHOICES,
    widget=widgets.RadioSelectHorizontal,
    )

    question38 = models.IntegerField(
        label="Ich würde meine Cookieauswahl ändern, wenn ich jetzt noch die Möglichkeit dazu hätte.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question39 = models.IntegerField(
        label="Ich bin zufrieden mit meiner Cookieauswahl.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question40 = models.IntegerField(
        label="Ich bin zufrieden mit meiner Cookieauswahl.",
        choices= [
            ('Preferred', 'Sie entspricht meinen Präferenzen'),
            ('Unbewusst', 'Ich habe unbewusst agiert.'),
            ('Tracked', 'Ich möchte gerne getrackt werden, etwa um personalisierte Werbungen zu erhalten.'),
            ('Schnell', 'Ich wollte schnellstmöglich weiterkommen.'),
            ('Egal', 'Es ist mir egal.  '),
        ],

        widget=widgets.RadioSelect,
    )

    pass


# PAGES
class success(Page):
    form_model = 'player'
    form_fields = []
    pass


class cookie_survey(Page):
    form_model = 'player'
    form_fields = ['question31', 'question32', 'question33','question34', 'question35', 'question36']

class cookie_survey2(Page):
    form_model = 'player'
    form_fields = ['question37', 'question38', 'question39']

class cookie_survey3(Page):
    form_model = 'player'
    form_fields = ['question40']

    

class debriefing (Page):
    form_model = 'player'
    form_fields = []
    pass


page_sequence = [  success, cookie_survey,  cookie_survey2, cookie_survey3, debriefing   ]
