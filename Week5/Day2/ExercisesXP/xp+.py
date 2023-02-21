# Exercise 1 : Family

class Family:
    def __init__(self, members: list, last_name: str):
        self.last_name = last_name
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
        
    def born(self, **kwargs):
        self.members.append({'name':kwargs,'age':kwargs,'gender':kwargs,'is_child':kwargs})
        return print(f'Congratulation family {self.last_name}')

    def is_18(self, name):
        every_member_name = []
        for i in range(0,len(self.members)):
            if self.members[i]['name']:
                every_member_name.append(name)
        if name not in every_member_name:
            return False
        else:
            return True
            
    def family_presentation(self):        
        every_member_name = []
        for i in range(0,len(self.members)):
            if self.members[i]['name']:
                every_member_name.append(self.members[i]['name'])
        every_member_name_str = ' ,'.join(every_member_name)
        return print(f'The {self.last_name} family and his members: {every_member_name_str}')

daniel_info = [{'name':'Daniel','age':1,'gender':'Male','is_child':True}]
daniel = Family(daniel_info, 'Ripari')

print(daniel.is_18('Daniel'))
daniel.family_presentation()


# Exercise 2 : TheIncredibles Family

class TheIncredibles(Family):
    def __init__(self, members: list, last_name: str):
        super().__init__(members, last_name)
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]

    def use_power(self):
        for i in range(0,len(self.members)):
            try:
                if self.members[i]['age'] >= 18:
                    print(self.members[i]['power'])
            except ValueError:
                print('they are not over 18 years old')

    def incredible_presentation(self):
        every_power = []
        for i in range(0,len(self.members)):
            if self.members[i]['name']:
                every_power.append(self.members[i]['power'])
        every_power_str = ' ,'.join(every_power)
        print(f'{self.family_presentation()} and his respective powers: {every_power_str}')



jack = TheIncredibles({'name':'Baby Jack','age':1,'gender':'Male','is_child':True,'power':'Unknown Power'}, 'Increibles')

TheIncredibles.born(jack)
jack.incredible_presentation()