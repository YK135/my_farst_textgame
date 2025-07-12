from random import randint
from Skill import *

# 일반 공격 함수
def stg_Attack(a_stg, a_luc, b_arm, b_luc):  # a=공격자, b=방어자
    rd_1=randint(1, 10)
    pl_damge=int(rd_1) #추가 데미지
    rd=randint(1, pl_damge)

    # 행운으로 공격을 회피   
    dodge_roll = randint(1, 100)
    if dodge_roll <= b_luc:
        return 0
    
    # 기본 데미지 계산
    base_dmg = (a_stg * 100 / (100 + b_arm) * 10)+rd

    # 치명타 판정
    crit_roll = randint(1, 100)
    if crit_roll <= a_luc:
        base_dmg *= 1.5

    #print(f"최종 데미지: {int(base_dmg)}")
    return int(base_dmg)

def magic_Attack(a_sp, a_luc, b_sparm, b_luc):  # a=공격자, b=방어자
    rd_1=randint(1, 10)
    pl_damge=int(rd_1) #추가 데미지
    rd=randint(1, pl_damge)

    # 행운으로 공격을 회피   
    dodge_roll = randint(1, 100)
    if dodge_roll <= b_luc:
        return 0
    
    # 기본 데미지 계산
    base_dmg = (a_sp*100 / (100 + b_sparm) * 10)+rd

    # 치명타 판정
    crit_roll = randint(1, 100)
    if crit_roll <= a_luc:
        base_dmg *= 1.5

    #print(f"최종 데미지: {int(base_dmg)}")
    return int(base_dmg)

#플레이어의 mp의 상태에 따라 출력과 공격 계산
def Magic_mp(p_mp, e_n, e_hp, x, m_mp):
    if p_mp < m_mp:
        return e_hp, p_mp
    else:
        print(f"{e_n}에게 {x}의 데미지!\n")
        e_hp -= x
        p_mp -= m_mp
        return e_hp, p_mp

# 적에게 입힌 데미지 출력 
def Stg_massege_e(e_n, e_h, e_d):  
    print(f"{e_n}에게 물리공격!")
    if e_d == 0:
        print(f"{e_n}은 공격을 회피했다!\n")
    else:
        e_h -= e_d
        print(f"{e_n}에게 {e_d}의 데미지!\n")
    return e_h

# 플레이어한테 입힌 데미지 출력 
def Stg_massege_p(e_n, p_n, p_h, p_d):
    if p_d==0:
        print(f"{p_n}은 공격을 회피했다!\n")
    else:
        p_h-=p_d
        print(f"{e_n}은 {p_n}에게 {p_d}의 데미지!\n")
    return p_h

#셰이드 1~2 스킬 
def Shade(p_stg, p_luc, e_arm, e_luc):
    damege=int(stg_Attack(p_stg, p_luc, e_arm, e_luc)*0.7)
    damege2=int(stg_Attack(p_stg, p_luc, e_arm, e_luc)*0.7)
    print("\n셰이드 1 을(를) 사용하였다!")
    print("{0}\n{1}".format(damege, damege2))
    return int(damege + damege2)

def Shade_2(p_stg, p_luc, e_arm, e_luc):
    damege=int(stg_Attack(p_stg, p_luc, e_arm, e_luc)*0.7)
    damege2=int(stg_Attack(p_stg, p_luc, e_arm, e_luc)*0.7)
    damege3=int(stg_Attack(p_stg, p_luc, e_arm, e_luc)*0.7)
    print("\n셰이드 2 을(를) 사용했다!")
    print("{0}\n{1}\n{2}\n".format(damege, damege2, damege3))
    return int(damege + damege2 + damege3)

# 파이어볼 스킬 1~3
def Fierball1(p_sp, p_luc, e_sparm, e_luc):
    damege=int(magic_Attack(p_sp, p_luc, e_sparm, e_luc)*1.4)
    return damege

def Fierball2(p_sp, p_luc, e_sparm, e_luc):
    damege=int(magic_Attack(p_sp, p_luc, e_sparm, e_luc)*1.6)
    return damege

def Fierball3(p_sp, p_luc, e_sparm, e_luc):
    damege=int(magic_Attack(p_sp, p_luc, e_sparm, e_luc)*1.8)
    return damege

# 아이스 볼릿 1~3
def Frozebolt1(p_sp, p_luc, e_sparm, e_luc):
    damege=int(magic_Attack(p_sp, p_luc, e_sparm, e_luc)*1.5)
    return damege

def Frozebolt2(p_sp, p_luc, e_sparm, e_luc):
    damege=int(magic_Attack(p_sp, p_luc, e_sparm, e_luc)*1.7)
    return damege

def Frozebolt3(p_sp, p_luc, e_sparm, e_luc):
    damege=int(magic_Attack(p_sp, p_luc, e_sparm, e_luc)*2)
    return damege