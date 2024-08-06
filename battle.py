class Monster:

    # コンストラクタ
    def __init__(self, init_hp):
        if (init_hp > 0):
            self.hp = init_hp
        else:
            print("体力は0以上です")
            self.hp = 1

    def damage(self, points):
        self.hp -= points
        if (self.hp < 0):
            return False
        else:
            return True


class Wizard(Monster):
    def __init__(self, init_hp, init_mp):
        super().__init__(init_hp)
        self.mp = init_mp

    def damage(self, points):
        points /= 2
        return super().damage(points)

    def magic(self):
        self.mp -= 10


goblin = Monster(50)


print("ゴブリンが現れた　体力：" + str(goblin.hp))
print("主人公の攻撃！")
goblin_life = goblin.damage(20)
if (goblin_life):
    print("ゴブリンの体力は" + str(goblin.hp) + "になった")
else:
    print("ゴブリンは倒れた")

print("主人公の攻撃！")
goblin_life = goblin.damage(30)
if (goblin_life):
    print("ゴブリンの体力は" + str(goblin.hp) + "になった")
else:
    print("ゴブリンは倒れた")


wizard1 = Wizard(150, 70)

print("魔法使いが現れた　体力：" + str(wizard1.hp) + "/魔法：" + str(wizard1.mp))
print("主人公の攻撃！")
wizard_life = wizard1.damage(10)
print(wizard1.hp)
if (wizard_life):
    print("魔法使いの体力は" + str(wizard1.hp) + "になった")
else:
    print("魔法使いは倒れた")
print("魔法使いは魔法を使った")
wizard1.magic()
print("魔法使いの魔法は" + str(wizard1.mp) + "になった")
