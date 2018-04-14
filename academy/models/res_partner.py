
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    genero = fields.Selection([("F","Female"),("M","Man"),("G","Gay")])
    birthdate = fields.Date("Fecha cumpleano")

