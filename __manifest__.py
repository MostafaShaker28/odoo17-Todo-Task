{
    'name': 'To Do',
    'version': '1.0',
    'depends': ['base' , 'mail'],
    'data': [
        'views/base_menu.xml' ,
        'views/todo_task_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
