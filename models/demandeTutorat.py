# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime

from . import etudiant
from odoo import models, fields, api

class DemandeTutorat(models.Model):
    _name = "tutorat.demande"
    _description = "demande de tutorat"
    titre = fields.Char("Titre de demande", required=True)
    desDemande = fields.Char(string="Description demande", required=True)
    date= fields.Datetime(string="Date de Creation",default=lambda self: datetime.now())
    etat = fields.Selection([('valid','Valide'),('enAttente','en attente')
                             ],default='enAttente',string="état",tracking=True)
    def action_confirm(self):
        self.etat='valid'
    idProjet=fields.One2many('tutorat.projet','titre')
    



   