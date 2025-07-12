from Game_Interface import *
from Damge import *

class Ply_Skill:
    def __init__(self):
        # 전체 스킬 목록: "이름": "습득 레벨"
        self.all_skills = {
            "셰이드 1": 3,
            "파이어볼 1": 5,
            "아이스 볼릿 1": 7,
            "셰이드 2": 10,
            "파이어볼 2": 13,
            "아이스 볼릿 2": 15,
            "파이어볼 3": 17,
            "아이스 볼릿 3": 21
        }
        # 실제 배운 스킬 (레벨 오르면 자동 추가됨)
        self.learned_skills = []

    def enemy_att(self, pl, en, x):
        if en.hp>0:
            pl.hp=Stg_massege_p(en.name, pl.name, pl.hp, x)
    
    def enemy_att_mp(player, enemy, y):
        if enemy.hp>0:
            Ply_Skill.enemy_att(player, enemy, y)

    def update_skills(self, lv):
        for skill, require_lv in self.all_skills.items():
            if require_lv <= lv and skill not in self.learned_skills:
                print(f"🎉 새로운 스킬 '{skill}'을(를) 배웠습니다!\n")
                self.learned_skills.append(skill)

    def show_skills(self):
        if not self.learned_skills:
            print("아직 배운 스킬이 없습니다.\n")
        else:
            print("스킬 목록\n")
            for i in range(0, len(self.learned_skills), 2):
                left = f"{i + 1}.{self.learned_skills[i]}"
                right = ""
                if i + 1 < len(self.learned_skills):
                    right = f"{i + 2}.{self.learned_skills[i + 1]}"
                print(f"{left:<20}{right}")     

    def try_skill(self, player, enemy, damage_to_player, selected_skill):  

            if selected_skill == "셰이드 1":
                damage = Shade(player.stg, player.luc,
                                enemy.arm, enemy.luc)
                print(f"{enemy.name}에게 {damage}의 데미지!\n")
                enemy.hp -= damage
                Ply_Skill.enemy_att(self, player, enemy, damage_to_player)

            elif selected_skill == "셰이드 2":
                damage = Shade_2(player.stg, player.luc,
                                enemy.arm, enemy.luc)
                print(f"{enemy.name}에게 {damage}의 데미지!\n")
                enemy.hp -= damage
                Ply_Skill.enemy_att(self, player, enemy, damage_to_player)

            elif selected_skill == "파이어볼 1":
                damage = Fierball1(player.sp, player.luc,
                                enemy .sparm, enemy.luc)
                if player.mp < 10:
                    print("mp가 부족합니다!\n")
                else:
                    print("\n파이어볼 1 을(를) 사용했다!\n"+"{0}".format(damage))
                    enemy.hp, player.mp = Magic_mp(player.mp, enemy.name,
                                                    enemy.hp, damage, 10)
                    Ply_Skill.enemy_att_mp(player, enemy, damage_to_player) 
            
            elif selected_skill == "파이어볼 2":
                damage = Fierball2(player.sp, player.luc,
                                enemy .sparm, enemy.luc)
                if player.mp < 13:
                    print("mp가 부족합니다!\n")
                else:
                    print("\n파이어볼 2 을(를) 사용했다!\n"+"{0}".format(damage))
                    enemy.hp, player.mp = Magic_mp(player.mp, enemy.name,
                                                    enemy.hp, damage, 13)
                    Ply_Skill.enemy_att_mp(player, enemy, damage_to_player)

            elif selected_skill == "파이어볼 3":
                damage = Fierball3(player.sp, player.luc,
                                enemy .sparm, enemy.luc)
                if player.mp < 15:
                    print("mp가 부족합니다!\n")
                else:
                    print("\n파이어볼 3 을(를) 사용했다!\n"+"{0}".format(damage))
                    enemy.hp, player.mp = Magic_mp(player.mp, enemy.name,
                                                    enemy.hp, damage, 15)
                    Ply_Skill.enemy_att_mp(player, enemy, damage_to_player)

            elif selected_skill == "아이스 볼릿 1":
                damage = Frozebolt1(player.sp, player.luc,
                                enemy .sparm, enemy.luc)
                if player.mp < 7:
                    print("mp가 부족합니다!\n")
                else:
                    print("\n아이스 볼릿 1 을(를) 사용했다!\n"+"{0}".format(damage))
                    enemy.hp, player.mp = Magic_mp(player.mp, enemy.name,
                                                    enemy.hp, damage, 7)
                    Ply_Skill.enemy_att_mp(player, enemy, damage_to_player)

            elif selected_skill == "아이스 볼릿 2":
                damage = Frozebolt2(player.sp, player.luc,
                                enemy .sparm, enemy.luc)
                if player.mp < 15:
                    print("mp가 부족합니다!\n")
                else:
                    print("\n아이스 볼릿 1 을(를) 사용했다!\n"+"{0}".format(damage))
                    enemy.hp, player.mp = Magic_mp(player.mp, enemy.name,
                                                    enemy.hp, damage, 15)
                    Ply_Skill.enemy_att_mp(player, enemy, damage_to_player)

            elif selected_skill == "아이스 볼릿 3":
                damage = Frozebolt3(player.sp, player.luc,
                                enemy .sparm, enemy.luc)
                if player.mp < 25:
                    print("mp가 부족합니다!\n")
                else:
                    print("\n아이스 볼릿 1 을(를) 사용했다!\n"+"{0}".format(damage))
                    enemy.hp, player.mp = Magic_mp(player.mp, enemy.name,
                                                    enemy.hp, damage, 25)
                    Ply_Skill.enemy_att_mp(player, enemy, damage_to_player)

            else:
                print("해당 스킬은 아직 구현되지 않았습니다.\n")