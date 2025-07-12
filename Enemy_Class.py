from random import *

goblin = [] # 고블린 리스트 생성
bet = [] # 박쥐 리스트 생성

class Unit():
    def __init__(self, name, lv, hp, mp, stg, arm, sparm, sp, spd, luc):
        self.name=name
        self.lv=lv
        self.hp=hp
        self.mp=mp
        self.stg=stg
        self.arm=arm
        self.sparm=sparm
        self.sp=sp
        self.spd=spd
        self.luc=luc

def Make_Goblin(x):
    base_goblin=Unit("고블린", 1, 75, 0, 2, 6, 0, 0, 5, 5)
    goblin.insert(0, base_goblin)
    base=goblin[0]
    x_lv=x*3
    
    if x==0:
        goblin.insert(0, base_goblin)
        return goblin[0]
    elif x!=0:
        lvunit=Unit(
            "고블린",
            x_lv,
            base.hp + 25 * (x_lv-1),
            0,
            base.stg + 2 * (x_lv-1),
            base.arm + 1.5 * (x_lv-1),
            base.sparm + 1.2 * (x_lv-1),
            base.sp,
            base.spd + 2 * (x_lv-1),
            base.luc + 1.2 * (x_lv-1)
            )
        goblin.insert(x, lvunit)

def Make_Bet(x):
    base_bet=Unit("박쥐", 1, 15, 5, 5, 5, 0, 0, 7, 0) # 1렙 박쥐 스탯
    bet.insert(0, base_bet)
    base=bet[0]
    x_lv=x*3
    
    if x==0:
        bet.insert(0, base_bet)
    elif x!=0:
        lvunit=Unit(
            "박쥐",
            x_lv,
            base.hp + 25 * (x_lv-1),
            0,
            base.stg + 2 * (x_lv-1),
            base.arm + 1.5 * (x_lv-1),
            base.sparm + 1.2 * (x_lv-1),
            base.sp,
            base.spd + 2 * (x_lv-1),
            base.luc + 1.2 * (x_lv-1)
            )
        bet.insert(x, lvunit)