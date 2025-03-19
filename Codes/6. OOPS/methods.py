class Youtube :
    def __init__(self,username,subs):
        self.username = username
        self.subs = subs
        print(f'total subs right now = {self.subs}')

    def subscribe(self,name):
        self.subs += 1
        print(f'{name} just subscribe , now total subs = {self.subs}')

ch = Youtube('vraj',12)
ch.subscribe(
    'meow'
)