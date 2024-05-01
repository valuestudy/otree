from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'paternalism'
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

KNOWLEDGE_CHOICES = [

            ['Wahr', 'Wahr'],
            ['Falsch', 'Falsch'],
            ['Weiß nicht', 'Weiß nicht'],
        ]
    


class Player(BasePlayer):


        frage1r = models.IntegerField(
            label="Der Staat sollte ungesunde Lebensmittel verbieten.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage2r = models.IntegerField(
            label="Der Staat sollte uns konsequent vor Drogenmissbrauch schützen.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage3 = models.IntegerField(
            label="Wann und wie viel ich für die Rente spare, möchte ich vollständig selbst entscheiden.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage4 = models.IntegerField(
            label="Jeder sollte selbst entscheiden dürfen, ob er einen Fahrradhelm trägt.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage5 = models.IntegerField(
            label="Der Staat übertreibt es mit der großen Anzahl von Bauvorschriften.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage6r = models.IntegerField(
            label="Alte Fahrzeuge mit geringer Energieeffizienz sollten mittelfristig ihre Betriebslizenz entzogen bekommen.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage7 = models.IntegerField(
            label="Jeder sollte das Recht haben, Dinge zu tun, die ihm selbst schaden können.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage8r = models.IntegerField(
            label="Verhaltensweisen, die Menschen selbst gefährden, sollten verboten sein.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage9 = models.IntegerField(
            label="Niemand weiß besser als ich selbst, was gut für mich ist.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage10r = models.IntegerField(
            label="Die wichtigste Aufgabe des Staates besteht darin, mich umfassend vor Gefahren jeder Art zu schützen.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

        frage11r = models.IntegerField(
            label="Ich würde gerne sehen, dass der Staat uns Bürger von mehr Aufgaben und Verantwortlichkeiten entlastet.",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )


# FUNCTIONS


# PAGES
class Paternalism_survey(Page):
    form_model = 'player'
    form_fields = ['frage1r', 'frage2r', 'frage3', 'frage4', 'frage5', 'frage6r', ]


class Paternalism_survey2(Page):
    form_model = 'player'
    form_fields = ['frage7', 'frage8r','frage9', 'frage10r', 'frage11r']



page_sequence = [ Paternalism_survey, Paternalism_survey2
                        ]
