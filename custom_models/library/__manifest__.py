{
    'name': "library",
    'summary': "library management tool",
    'author': "Evaldas Melianas",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security\ir.model.access.csv',
        'wizard\create_report_view.xml',
        'views\library_view.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
