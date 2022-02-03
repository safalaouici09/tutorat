# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ProjetTutorat(models.Model):
    _name = "tutorat.projet"
    _description = "Projet de tutorat "

    idProjet = fields.Char(string="Id Projet ", required=True)
    descProjet = fields.Char(string="Description",required=True)
    idEns =fields.Many2one('tutorat.enseignant',
     ondelete='cascade', string="Enseignant", required=True)
    titre = fields.Many2one('tutorat.demande',
     ondelete='cascade', string="demande de tutorat", required=True)
 
       