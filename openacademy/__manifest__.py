# -*- coding: utf-8 -*-
{
    'name': "LG Cursos",

    'summary': """
        Sistema de Gestão de Cursos""",

    'description': """
        O sistema de gestão de cursos propõe gerir cursos de forma fácil 
        e com interface amigável para o usuário
    """,

    'author': "Luan Gomes",
    'website': "http://www.luangomes.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',                
        'views/views.xml',
        'views/openacademy.xml',
        'views/partner.xml',   
        'reports.xml',        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}