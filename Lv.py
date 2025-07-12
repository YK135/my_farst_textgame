from random import randint

from Skill import *

class LV_():
    def __init__(self, ply):
        self.player=ply

    def Lv_up(player):
        # 1. 이전 스탯 저장
        player.lv += 1
        player.skill=Ply_Skill()

        before = {
            "maxhp": player.maxhp,
            "maxmp": player.maxmp,
            "stg": player.stg,
            "sp": player.sp,
            "arm": player.arm,
            "sparm": player.sparm,
            "luc": player.luc
        }

        base_lv = player.lv

        # 2. 스탯 상승
        player.exp -= 100
        player.maxhp += 20 + (base_lv * 3)
        player.hp += 20 + (base_lv * 3)
        player.maxmp += 5 + (base_lv // 4)
        player.mp += 5 + (base_lv // 4)
        player.stg   += 1.5 + (base_lv // 5)
        player.sp    += 2 + (base_lv // 5)
        player.arm   += 1.5
        player.sparm += 1.2
        player.luc   += (base_lv % 2)

        # 3. 변화 출력
        print(f"\n📈 {player.name} 레벨업! (Lv.{base_lv-1} → Lv.{base_lv})")
        after = {
            "maxhp": player.maxhp,
            "maxmp": player.maxmp,
            "stg": player.stg,
            "sp": player.sp,
            "arm": player.arm,
            "sparm": player.sparm,
            "luc": player.luc
        }

        name_map = {
            "maxhp": "HP",
            "maxmp": "MP",
            "stg": "힘",
            "sp": "마력",
            "arm": "방어력",
            "sparm": "마법방어력",
            "luc": "행운"
        }

        for stat in before:
            b = round(before[stat], 2)
            a = round(after[stat], 2)
            print(f"{name_map[stat]}: {b} → {a}")

    def Get_exp(self, player):
        getexp = randint(45, 60)
        print(f"{getexp}의 경험치를 획득!!\n")
        player.exp += getexp

        if player.exp >= player.maxexp:
            print("레벨이 올랐습니다 + 1\n")
            LV_.Lv_up(player)
        else:
            return player.exp