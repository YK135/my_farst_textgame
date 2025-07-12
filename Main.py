from random import randint
import msvcrt
import sys

from Player_Class import *
from Explain import Explain
from Lv import *
from Skill import *
from Item import *
from Enemy_Class import *
from Action_Class import *
from Game_Interface import *

#Explain()

#GameStart()

plname=input("이름을 입력하세요. ------> ")

ply=Player(plname, 1, 100, 0, 200, 200, 25, 25, 5, 7, 5, 5, 10, 15) 
# 이름, 레벨, 경험치 통, 현재 경험치, 최대 체력, 현재 체력, 최대 mp, 현재 mp, 공격력, 방어력, 마방, 마력, 스피드, 행운
pl_item=["HP_S_potion"]
player_item=Item_(ply, pl_item)
item_list=["HP_S_potion", "HP_M_potion", "HP_L_potion",
           "MP_S_potion", "MP_M_potion", "MP_L_potion"]

def Game_restart():
    global ply, goblin

    # 플레이어 이름 다시 입력받기 (선택적으로 기존 이름 유지할 수도 있음)
    plname = input("\n[재시작] 이름을 다시 입력하세요 ------> ")
    ply = Player(plname, 1, 50, 0, 200, 200, 25, 25, 8, 10, 10, 5, 10, 15)

    print("\n게임을 다시 시작합니다!\n")
    Trun(0)

def Game_over():
    if ply.hp > 0:
        return  # 체력이 남아 있으면 아무 일도 하지 않음
    
    Player_Deth()
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key in [b'y', b'Y', b'1']:
                Game_restart()
                break
            elif key in [b'n', b'N', b'\x1b']:  # ESC 포함
                print("게임을 종료합니다.")
                sys.exit()
      
def Trun(tn): # 턴 진행
    printed=0   
    while True:
        rd=randint(1, 16)
        rd_e=randint(1, 2)
        e_lv=int(ply.lv//3 + 1)
        Game_over() # 플레이어의 체력이 없으면 게임 종료

        if printed==0 :
            Trun_interface()
            printed=1
        # ^^^ 문장을 한 번만 출력하기 위해

        elif printed==1 :
            if tn<50:

                if msvcrt.kbhit():
                    key=msvcrt.getch() 

                    if key in [b'4', b'\x1b']:
                        GameEmdKey()
                        printed=0

                    elif key==b'1':
                        print("앞으로 나아갑니다.\n")

                        if 1<=rd and rd<=7:
                            if rd_e==1:
                                print("고블린이다!\n")
                                Make_Goblin(e_lv)
                                battel=Act(ply, goblin[e_lv], pl_item)
                                battel.action()
                            elif rd_e == 2:
                                print("슬라임이다!\n")
                                Make_Bet(e_lv)
                                battel=Act(ply, bet[e_lv], pl_item)
                                battel.action()

                        elif 8<=rd and rd<=10:
                            rd_item = randint(0, 5)
                            get=item_list[rd_item]
                            print(f"{get}아이템 획득!\n")
                            pl_item.append(get)

                        elif 11<=rd and rd<=12:
                            Rest_Area()
                            key=msvcrt.getch()

                            if key==b'1':
                                if ply.maxhp<ply.hp+int(ply.maxhp*(1/3)) or ply.hp==ply.maxhp:
                                    print(f"{ply.maxhp-ply.hp}회복\n")
                                    ply.hp=ply.maxhp
                                else:
                                    print(f"{int(ply.maxhp*(1/3))}회복\n")
                                    ply.hp=ply.hp+int(ply.maxhp*(1/3))

                            elif key==b'2':
                                LV_.Get_exp(ply.lv, ply)
                                print("경험치 획득\n") 

                            else:
                                print("잘못된 선택입니다.\n") 
                                rd=11                          

                        else:
                            print("\n")

                        tn+=1
                        print("\n현재 진행 턴 수 : {0}  (남은 턴 수 : {1})\n".format(tn, 50-tn))

                    elif key==b'2':
                        ply.Show_Staters()  
                        printed=0

                    elif key==b'3':
                        player_item.show_item()
                        print("사용할 아이템 번호를 선택하세요. (ESC: 취소)")

                        key = msvcrt.getch()

                        if key == b'\x1b':  # ESC 입력 시 취소
                            printed = False
                            continue

                        try:
                            idx = int(key.decode())

                            if idx < 0 or idx >= len(pl_item):
                                print("잘못된 번호입니다.\n")
                            else:
                                selected_item = pl_item[idx]
                                player_item.use_item(selected_item)
                        except (ValueError, IndexError):
                            print("잘못된 입력입니다.\n")

                        printed=0  

            elif tn==50:
                print("~~~구현중~~~")
                break

Trun(0)