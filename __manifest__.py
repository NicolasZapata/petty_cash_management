{
  'name': 'Petty Cash Management',
  'version': '1.0',
  'description': 'Petty Cash Management',
  'summary': '',
  'author': 'Grupo Quanam Colombia SAS',
  'website': 'grupoquanam.com.co',
  'license': 'LGPL-3',
  'category': '',
  'depends': [
    'hr',
    'hr_expense',
    'account'
  ],
  'data': [
    'views/petty_cash_view.xml',
    'security/ir.model.access.csv',
    'views/hr_expense_views.xml',
  ],
  # 'demo': [
  #   ''
  # ],
  'auto_install': False,
  'application': False,
  'assets': {
    'web.assets_backend': [
      'petty_cash_management/static/src/scss/petty_cash.scss'
    ]
  }
}