class Player():
    
    def __init__(self, hp=100, cash=0):
        self.hp = hp;
        self.zombieKillCount = 0;
        self.cash = cash;
        
class Zombie():
    '''This is Zombie Parent Class. Different Zombies inherit from this class'''
    
    def __init__(self, hp):
        self.hp = hp;
        
class RunnerZombie(Zombie):
    
    def __init__(self, hp):
        Zombie.__init__(self, hp);
        
class Bullet():
    
    def __init__(self, speed):
        pass

        

    
        