# -*- coding: utf-8 -*-
import odoo
from odoo import models, fields, api

class Etudiant(models.Model):
    _name = "tutorat.etudiant"
    _description = "etudiant de l'ecole"

    idEtudiant = fields.Char(string="Matricule", required=True)    
    nomEtudiant = fields.Char(string="Nom", required=True) 
    prenomEtudiant = fields.Char(string="Prenom", required=True) 
    promo = fields.Char(string="Promo", required=True) 
    