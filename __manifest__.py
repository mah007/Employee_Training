# -*- coding: utf-8 -*-
{
    'name': "Employee's Training Management",

'summary': """
        Employee's Training Management for Employees""",

    'description': """
        Add couses to your company emloeyees and set a track on it 
    """,


    'author': "Mahmoud Abdel Latif",
    'website': "http://www.mah007.com",

    
    'category': 'Employees',
    'version': '11.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','mail','hr'],

    # always loaded
    'data': [

        'security/training_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sequence.xml',
        'views/training_employee.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
