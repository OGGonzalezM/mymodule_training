# -*- coding: utf-8 -*-
{
    'name': "My testing module",

    # Short description
    'summary': """
        This is a module developed to train with Odoo
    """,

    'description': """
        The long descr is used to show all the details
    """,

    'author': "Soluciones4G - OGM",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Extra Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    # Views, XML, HTML
    # Datos XML, CSV
    'data': [
    ],

    'installable':True,
    'auto_install':False,
}