import odoo
from odoo import models, fields, api

class responsableDE(models.Model):
    _name = "tutorat.responsablede"
    _description = "Responsable à l'ecole"
    idRespo = fields.Char(string="id", required=True)    
    nomRespo = fields.Char(string="Nom", required=True) 
    prenomRespo = fields.Char(string="Prenom", required=True) 