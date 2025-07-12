from collections import Counter

class Item_():
    def __init__(self, ply, item_list):
        self.player=ply
        self.item=item_list

    def HP_Potion_S(player):
        print("HP_S 포션을 사용하였다! +50\n")
        total_HP = player.hp + 50
        
        if total_HP > player.maxhp :
            player.hp = player.maxhp
        else:
            player.hp = total_HP
        
    def HP_Potion_M(player):
        print("HP_M 포션을 사용하였다! +100\n")
        total_HP = player.hp + 100
        
        if total_HP > player.maxhp :
            player.hp = player.maxhp
        else:
            player.hp = total_HP
    
    def HP_Potion_L(player):
        print("HP_L 포션을 사용하였다! +150\n")
        total_HP = player.hp + 150
        
        if total_HP > player.maxhp :
            player.hp = player.maxhp
        else:
            player.hp = total_HP
    
    def MP_Potion_S(player):
        print("MP_S 포션을 사용하였다! +20\n")
        total_mp = player.mp + 20
        
        if total_mp > player.maxmp :
            player.mp = player.maxmp
        else:
            player.mp = total_mp
    
    def MP_Potion_M(player):
        print("MP_M 포션을 사용하였다!\n +40")
        total_mp = player.mp + 40
        
        if total_mp > player.maxmp :
            player.mp = player.maxmp
        else:
            player.mp = total_mp
    
    def MP_Potion_L(player):
        print("MP_L 포션을 사용하였다!\n +60")
        total_mp = player.mp + 60
        
        if total_mp > player.maxmp :
            player.mp = player.maxmp
        else:
            player.mp = total_mp
        
    def show_item(self):
        if not self.item:
            print("보유 아이템이 없습니다\n")
            return

        print("아이템 목록:")

        # 아이템 개수 세기

        item_count = Counter(self.item)  # ✅ 꼭 self.item 사용

        for idx, (name, count) in enumerate(item_count.items()):
            print(f"{idx} - {name} x{count}")

    def use_item(self, item):
        item_effects = {
            "HP_S_potion": Item_.HP_Potion_S,
            "HP_M_potion": Item_.HP_Potion_M,
            "HP_L_potion": Item_.HP_Potion_L,
            "MP_S_potion": Item_.MP_Potion_S,
            "MP_M_potion": Item_.MP_Potion_M,
            "MP_L_potion": Item_.MP_Potion_L
        }

        if item in item_effects:
            item_effects[item](self.player)  # 아이템 효과 실행
            self.item.remove(item)           # 인벤토리에서 제거
        else:
            print("잘못된 입력입니다.\n")