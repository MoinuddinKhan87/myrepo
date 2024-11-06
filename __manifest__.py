# -*- coding: utf-8 -*-
# A prdouct of DX-8, module resricted as per the license.

{
    'name': 'Auto Logout User',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Automatic logout user within specific time in case if user is idle""",
    'description': """Set the timer under user's profile. The user will logout automatically, if the user
     remains idle within specified time under user profile  """,
    'depends': ['base'],
    'data': [
        'views/res_users_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            '/autologout_user/static/src/xml/systray.xml',
            '/autologout_user/static/src/js/systray.js',
            '/autologout_user/static/src/css/systray.css'
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
