World = {
    'garden': {
        'name': 'Garden',
        'description': 'A beautiful garden with a pond and a waterfall.',
        'items': ['Cheesy Gordita Crunch'],
        'exits': []
    },
    'ghetto': {
        'name': 'Ghetto',
        'description': 'A dirty ghetto with a lot of crime.',
        'items': ['a gun'],
        'hazards': ['police'],
        'exits': ['prision'],
        'locked': True,
        'required_action': 'shoot the gun'
    },
    'panda express': {
        'name': 'Panda Express',
        'description': 'A restaurant with a lot of orange chicken.',
        'items': ['an entree of orange chicken'],
        'hazards': ['giant pandas'],
        'exits': ['ghetto']
    },
    'prision':{
        'name': 'Prision',
        'description': 'A dirty prision with a lot of criminals.',
        'items': ['a bar of soap','key'],
        'hazards': ['big fella on top bunk'],
        'exits': ['Warden\'s Office']
    },
    'wardens office':{
        'name': 'Warden\'s Office',
        'description': 'A dirty warden\'s office with a lot of paperwork.',
        'items': ['+10 health'],
        'hazards': ['guards'],
        'exits': ['portal to the garden'],
        'locked': True,
        'required_item': 'key'

    }
}

