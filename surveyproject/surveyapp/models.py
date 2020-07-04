from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Nguyen Huu Ky Thanh'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'surveyapp'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision1 = models.StringField(
        choices=['a', 'b', 'c', 'd'],
        widget=widgets.RadioSelect,
    )

    confidence1 = models.StringField(
        label="",
        choices=["Very confident", "Somewhat confident", "Not confident", "Just a wild guess"],
        widget=widgets.RadioSelect,
    )
