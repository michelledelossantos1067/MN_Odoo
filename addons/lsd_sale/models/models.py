# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LsdSale(models.Model):
    _name = 'lsd_sale.lsd_sale'
    _description = 'lsd_sale.lsd_sale'

    nombre = fields.Char(string='Nombre',required=True)
    apellido = fields.Char(string='Apellido',required=True)
    email = fields.Char(string='Email',required=True)
    cedula = fields.Char(string='Cedula',required=True)
    telefono = fields.Char(string='Telefono',required=True)


class Compra(models.Model):
    _name = 'lsd_sale.compra'
    _description = 'Compra de productos de la tienda lsd_sale'

    pantalones = fields.Float(string='Pantalones',required=True)
    blusas = fields.Float(string='Blusas',required=True)
    vestidos = fields.Float(string='Vestidos',required=True)



