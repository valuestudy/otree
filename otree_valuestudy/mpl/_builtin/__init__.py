# This file is auto-generated.
# It's used to aid autocompletion in code editors.

import otree.api
from .. import models
from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page, Currency as c, currency_range



class Page(otree.api.Page):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()

    @staticmethod
    def vars_for_template(player):
        # Example configuration and choices
        choices = [(i, 'F' + str(i), 'P' + str(i)) for i in range(1, 6)]  # Adjust as necessary

        # Preparing IDs for pie charts
        formatted_choices = [
            (i, f, p, f"pie_a_{i}", f"pie_b_{i}") for i, f, p in choices
        ]

        return {
            'choices': formatted_choices,
            'small_pies': Constants.small_pies,
            'large_pies': Constants.large_pies,
            'one_choice_per_page': Constants.one_choice_per_page,
            'progress_bar': Constants.progress_bar,
            'page': 'current_page_number',  # Adjust according to actual logic
            'total': 'total_number_of_pages',  # Adjust according to actual logic
            'progress': 'calculated_progress'  # Adjust according to actual logic
        }



class WaitPage(otree.api.WaitPage):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()


class Bot(otree.api.Bot):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()
