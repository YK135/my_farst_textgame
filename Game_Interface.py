import msvcrt
import sys

from Player_Class import *
from Enemy_Class import *

def GameEmdKey():
    printed = 0
    while True:

        if printed==0:
            print("******************************\n"\
            "*     게임을 종료합니까?     *\n"\
            "*                            *\n"\
            "*    확인[Y]   아니요[N]     *\n"\
            "******************************\n")
            printed = 1

        elif printed==1:
            if msvcrt.kbhit():
                key=msvcrt.getch() 

                if key in [b'n', b'\x1b']:
                    return
                elif key in [b'y', b'\x0d']:
                    sys.exit()

def Trun_interface():
    print("\n*********************************\n"\
          "* 1. 앞으로 나아간다    2. 상태 *\n"\
          "* 3. 아이템             4. 종료 *\n"\
          "*********************************\n")

def Rest_Area():
    print("\n*********************************************\n"\
          "*                 쉼터 발견                 *\n"\
          "*   1. 쉬어간다(Hp회복)     2. 수련한다     *\n" \
          "*********************************************\n")

def Battle_interface():
    print("************************\n"\
          "* 1. 공격      2. 스킬 *\n"\
          "* 3. 아이템    4. 상태 *\n"\
          "************************\n")

def Player_Deth():
    
    print("\n##### 플레이어가 쓰러졌습니다... #####\n")

    print("##################################\n"\
          "#     다시 도전하시겠습니까?     #\n"\
          "#                                #\n"
          "#     예(Y)        아니오(N)     #\n"\
          "##################################\n")