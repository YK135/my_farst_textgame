import msvcrt

from Damge import *
from Player_Class import *
from Skill import *
from Item import *
from Game_Interface import *
from Lv import *

pl_skill=Ply_Skill()
            
# Action_Class.py
class Act:
    def __init__(self, player, enemy, item_list):
        self.player = player
        self.enemy = enemy
        self.item = item_list

        if self.player.lv >= 3:
            pl_skill.update_skills(self.player.lv)

    def action(self):
        printed = False
        pl_item=Item_(self.player, self.item)
        pl_lv=LV_(self.player)

        while True:
            damage_to_enemy = stg_Attack(
            self.player.stg, self.player.luc,
            self.enemy.arm, self.enemy.luc)
            damage_to_player = stg_Attack(
                self.enemy.stg, self.enemy.luc,
                self.player.arm, self.player.luc)

            if self.enemy.hp <= 0:
                print(f"{self.enemy.name}을(를) 퇴치했습니다!\n")
                pl_lv.Get_exp(self.player)
                break

            if self.player.hp <= 0:
                print(f"{self.player.name}이(가) 쓰러졌다...\n")
                break

            if not printed:
                Battle_interface()
                printed = True

            if msvcrt.kbhit():
                key = msvcrt.getch()

                if key == b'1':  # 공격
                    self.enemy.hp=Stg_massege_e(self.enemy.name, self.enemy.hp, damage_to_enemy)
                    pl_skill.enemy_att(self.player, self.enemy, damage_to_player)

                    printed = False

                elif key == b'2':  # 스킬
                    if pl_skill.learned_skills:
                        pl_skill.show_skills()
                        print("사용할 스킬 번호를 입력하세요:")

                        key2 = msvcrt.getch()

                        if key2 == b'\x1b':
                            printed = False
                            continue

                        try:
                            idx = int(key2.decode())
                            selected_skill = pl_skill.learned_skills[idx-1]

                        except (IndexError, ValueError):
                            print("잘못된 스킬 번호입니다.\n")
                            return
                        print(f"선택된 스킬: {selected_skill}")
                        pl_skill.try_skill(self.player, self.enemy, damage_to_player, selected_skill)
                        printed = False

                    else:
                        print("아직 배운 스킬이 없습니다.\n")

                        printed = False

                elif key == b'3':
                    pl_item.show_item()
                    print("사용할 아이템 번호를 선택하세요. (ESC: 취소)")

                    key = msvcrt.getch()

                    if key == b'\x1b':  # ESC 입력 시 취소
                        printed = False
                        continue

                    try:
                        idx = int(key.decode())

                        if idx < 0 or idx >= len(self.item):
                            print("잘못된 번호입니다.\n")
                        else:
                            selected_item = self.item[idx]
                            pl_item.use_item(selected_item)
                    except (ValueError, IndexError):
                            print("잘못된 입력입니다.\n")

                    printed = False

                elif key == b'4':
                    Player.Show_Staters(self.player)
                    printed = False
                
                elif key == b'\x1b':
                    GameEmdKey()
                    printed = False
