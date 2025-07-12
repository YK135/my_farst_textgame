import Lv
import Skill

class Player():
    def __init__(self, name, lv, maxexp, exp, maxhp, hp, maxmp, mp, stg, arm, sparm, sp, spd, luc):
        self.name=name
        self.lv=lv
        self.maxexp=maxexp
        self.exp=exp
        self.maxhp=maxhp
        self.hp=hp
        self.maxmp=maxmp
        self.mp=mp
        self.stg=stg
        self.arm=arm
        self.sparm=sparm
        self.sp=sp
        self.spd=spd
        self.luc=luc

    def Show_Staters(self):
        print(f"\n이  름 : {self.name}\n")
        print(f"LV : {self.lv}         경험치 : {self.maxexp}/{self.exp}")
        print(f"HP : {self.maxhp} / {self.hp}")
        print(f"MP : {self.maxmp} / {self.mp}")
        print(f"힘   : {self.stg}")
        print(f"방어력 : {self.arm}")
        print(f"마법 방어력 : {self.sparm}")
        print(f"마력 : {self.sp}")
        print(f"행운 : {self.luc}\n")
