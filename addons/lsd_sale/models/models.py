# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lsd_sale(models.Model):
    _name = 'lsd_sale.lsd_sale'
    _description = 'lsd_sale.lsd_sale'

    nombre = fields.Char(String='Nombre')
    apellido = fields.Char(String='Apellido')
    email = fields.Char(String='Email')
    cedula = fields.Char(String='Cedula')

