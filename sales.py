# Application for testing skills with Odoo for Marcap Company Builder
from openerp import models, fields

# Ilusiones sales class 

class ILusiones_res_users_sale(models.Model):
    _name = 'res.users.sale'
    sale_date = fields.Datetime("Sale Date")
    #product_id = fields.Many2one('product.template', 'Product Sale')
    prepago_ids = fields.One2many('res.users.prepago', 'sale_id', "Sale type")
    plan_ids = fields.Many2one('res.users.plan', 'sale_id')
    activation_ids = fields.Many2one('res.users.activation', 'sale_id')
    user_id = fields.Many2one('res.users', 'Sale user')
    notes = fields.Text('Sale Notes')
    
class Ilusiones_res_sale_prepago(models.Model):
    _name = 'res.users.prepago'
    sale_id = fields.Many2one('res.users.sale')
    #fields
    product_id = fields.Many2one('product.template', 'Storable or Service')
    notes = fields.Text('Prepago Notes')
    price = fields.Float('Price')
    contract = fields.Integer('Contract')
    serieSelection = fields.Selection([('serie1', '12345'), ('serie2', '99897')], "Serie")
    type = fields.Text('Prepago', default='Prepago', readonly="true")
    
class Ilusiones_res_sale_plan(models.Model):
    _name = 'res.users.plan'
    sale_id = fields.Many2one('res.users.sale')
    #fields
    product_id = fields.Many2one('product.template', 'Storable or Service')
    month_rent = fields.Float('Month Price')
    notes = fields.Text('Plan Notes')
    
class Ilusiones_res_sale_activation(models.Model):
    _name = 'res.users.activation'
    sale_id = fields.Many2one('res.users.sale')
    #fields
    product_id = fields.Many2one('product.template', 'Storable or Service')
    serieSelection = fields.Selection([('serie1', '12345'), ('serie2', '99897')], "Serie")
    contract = fields.Integer('Contract')
    month_rent = fields.Float('Month Price')
    combo = fields.Selection([('none', 'Ninguno')])
    notes = fields.Text('Activation Notes')
    
    