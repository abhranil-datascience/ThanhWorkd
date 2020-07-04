from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Introduction(Page):
    form_model = 'player'

class Decision1(Page):
    form_model = 'player'
    form_fields = ['decision1']

class Confidence1(Page):
    form_model = 'player'
    form_fields = ['confidence1']

class End(Page):
    form_model = 'player'


page_sequence = [Decision1, Confidence1]
