# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime

from . import etudiant
from odoo import models, fields, api

class DemandeTutorat(models.Model):
    _name = "tutorat.demande"
    _description = "demande de tutorat"
    idEt = fields.Char(string="Matricule", required=True)    
    nomEt = fields.Char(string="Nom", required=True) 
    prenomEt = fields.Char(string="Prenom", required=True)  
    titre = fields.Char("Titre de demande", required=True)
    desDemande = fields.Char(string="Description demande", required=True)
    date= fields.Datetime(string="Date de Creation",default=lambda self: datetime.now())
    etat = fields.Selection([('valid','Valide'),('enAttente','en attente')
                             ],default='enAttente',string="état",tracking=True)
    etudiantid=fields.Char('Etudiant',  default=lambda self: self.env.user.name)
    idProjet=fields.One2many('tutorat.projet','titre')
    def action_confirm(self):
        self.etat='valid'
    
    
    


   