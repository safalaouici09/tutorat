# -*- coding: utf-8 -*-
import odoo
from odoo import models, fields, api

class Etudiant(models.Model):
    _name = "tutorat.enseignant"
    _description = "Enseignant"

    idEns = fields.Char(string="Matricule", required=True)    
    nomEns = fields.Char(string="Nom", required=True) 
    prenomEns= fields.Char(string="Prenom", required=True) 
    idProjet=fields.One2many('tutorat.projet','idEns')
    