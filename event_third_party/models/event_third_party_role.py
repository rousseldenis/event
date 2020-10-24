# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class EventThirdPartyRole(models.Model):

    _name = 'event.third.party.role'
    _description = 'Event Third Party Role'

    name = fields.Char(
        required=True,
        index=True,
    )
