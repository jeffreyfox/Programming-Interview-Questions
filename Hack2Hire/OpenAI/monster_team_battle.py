# Simulate a deterministic, turn-based monster battle between two ordered teams of monsters. The system should execute the fight step by step and produce a complete, chronological battle log that describes every event.

# You are given the following definitions for Monster and Team:

# class Monster { 
#     String name;   // Unique identifier of the monster.
#     int health;   // Initial hit points.
#     int attack;   // Damage inflicted when attacking.
#     ...
# }
# class Team {
#     String label;           // Team identifier, either "A" or "B".
#     List<Monster> monsters; // Monsters listed in spawn order.
# }
# Implement the method simulateBattle(teamA, teamB) that runs the battle simulation and returns a list of event strings according to the rules below:

# The active monster of a team is the first monster in its list whose health is greater than 0.

# Round Flow:

# Attack: Team A's active monster attacks Team B's active monster, dealing damage equal to its attack value. Record an "[ATTACK]" event.
# Apply Damage: Reduce the defender's health by the damage amount. If the defender's health becomes less than or equal to 0, it dies immediately.
# Counterattack: If the defender survives, it immediately counterattacks the original attacker using its own attack value. Record another "[ATTACK]" event.
# Cleanup: Whenever a monster's health becomes less than or equal to 0, immediately log a "[DEATH]" event. The next surviving monster in that team becomes the new active monster.

# Termination: The battle ends as soon as one team has no monsters remaining with health greater than 0. At that moment, record a "[RESULT]" event declaring the winning team.

# Event Formats

# Attack Event: "[ATTACK] <attacker_team>:<attacker_name> -> <defender_team>:<defender_name> | DMG=<damage> | HP:<before> -> <after>"

# Death Event: "[DEATH] <team>:<monster_name> defeated | NEXT=<next_monster_label_or_NONE>" where the value of "NEXT" is either "<label>:<name>" or "NONE".

# Result Event: "[RESULT] WINNER=<team>"

# You may assume a monster of team A always starts the first attack.

# Constraints:

# Team size is less than 104
# 1 ≤ health, attack ≤ 109
# Example:

# Input:
# ["Monster", "Monster", "Team", "Team", "simulateBattle"]
# [["Dragon", 10, 5], ["Goblin", 12, 3], ["A", monster1], ["B", monster2], [teamA, teamB], []]

# Output:
# [
#   "[ATTACK] A:Dragon -> B:Goblin | DMG=5 | HP:12 -> 7",
#   "[ATTACK] B:Goblin -> A:Dragon | DMG=3 | HP:10 -> 7",
#   "[ATTACK] A:Dragon -> B:Goblin | DMG=5 | HP:7 -> 2",
#   "[ATTACK] B:Goblin -> A:Dragon | DMG=3 | HP:7 -> 4",
#   "[ATTACK] A:Dragon -> B:Goblin | DMG=5 | HP:2 -> 0",
#   "[DEATH] B:Goblin defeated | NEXT=NONE",
#   "[RESULT] WINNER=A"
# ]

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Team:
    def __init__(self, label, monsters):
        self.label = label
        self.monsters = monsters
        self.activeIdx = 0

    def getActive(self):
        if self.activeIdx < len(self.monsters):
            return self.monsters[self.activeIdx]
        return None

    def advanceAndNextLabel(self):
        self.activeIdx = self.activeIdx + 1
        if self.activeIdx < len(self.monsters):
            return self.label + ":" + self.monsters[self.activeIdx].name
        return "NONE"

    def hasAlive(self):
        return self.activeIdx < len(self.monsters)

class Solution:
    def simulateBattle(self, teamA, teamB):
        # This part is added by me
        result = []
        while teamA.hasAlive() and teamB.hasAlive():
            monsterA = teamA.getActive()
            monsterB = teamB.getActive()
            # A attack B
            dmg = monsterA.attack
            hpB = monsterB.health
            hpBNew = max(0, hpB - dmg)
            monsterB.health = hpBNew
            msg = (
                f"[ATTACK] A:{monsterA.name} -> B:{monsterB.name} | "
                f"DMG={dmg} | HP:{hpB} -> {hpBNew}"
            )
            result.append(msg)
            if hpBNew == 0:
                newLabel = teamB.advanceAndNextLabel()
                result.append(f"[DEATH] B:{monsterB.name} defeated | NEXT={newLabel}")
                continue

            # now B attacks A
            monsterB = teamB.getActive()
            dmg = monsterB.attack
            hpA = monsterA.health
            hpANew = max(0, hpA - dmg)
            monsterA.health = hpANew
            msg = (
                f"[ATTACK] B:{monsterB.name} -> A:{monsterA.name} | "
                f"DMG={dmg} | HP:{hpA} -> {hpANew}"                
            )
            result.append(msg)
            if hpANew == 0:
                newLabel = teamA.advanceAndNextLabel()
                result.append(f"[DEATH] A:{monsterA.name} defeated | NEXT={newLabel}")

        if teamA.hasAlive():
            result.append("[RESULT] WINNER=A")
        else:
            result.append("[RESULT] WINNER=B")
        return result

def test1():
    print("===== Test 1 =====")

    solution = Solution()
    monster1 = Monster("Dragon", 10, 5)
    monster2 = Monster("Goblin", 12, 3)
    teamA = Team("A", [monster1])
    teamB = Team("B", [monster2])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:Dragon -> B:Goblin | DMG=5 | HP:12 -> 7",
      "[ATTACK] B:Goblin -> A:Dragon | DMG=3 | HP:10 -> 7",
      "[ATTACK] A:Dragon -> B:Goblin | DMG=5 | HP:7 -> 2",
      "[ATTACK] B:Goblin -> A:Dragon | DMG=3 | HP:7 -> 4",
      "[ATTACK] A:Dragon -> B:Goblin | DMG=5 | HP:2 -> 0",
      "[DEATH] B:Goblin defeated | NEXT=NONE",
      "[RESULT] WINNER=A"
    ]
    assert log == expected

def test2():
    print("===== Test 2 =====")

    solution = Solution()
    monster1 = Monster("Warrior", 5, 4)
    monster2 = Monster("Goblin", 3, 1)
    monster3 = Monster("Orc", 10, 2)
    teamA = Team("A", [monster1])
    teamB = Team("B", [monster2, monster3])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:Warrior -> B:Goblin | DMG=4 | HP:3 -> 0",
      "[DEATH] B:Goblin defeated | NEXT=B:Orc",
      "[ATTACK] A:Warrior -> B:Orc | DMG=4 | HP:10 -> 6",
      "[ATTACK] B:Orc -> A:Warrior | DMG=2 | HP:5 -> 3",
      "[ATTACK] A:Warrior -> B:Orc | DMG=4 | HP:6 -> 2",
      "[ATTACK] B:Orc -> A:Warrior | DMG=2 | HP:3 -> 1",
      "[ATTACK] A:Warrior -> B:Orc | DMG=4 | HP:2 -> 0",
      "[DEATH] B:Orc defeated | NEXT=NONE",
      "[RESULT] WINNER=A",
    ]
    assert log == expected

def test3():
    print("===== Test 3 =====")

    solution = Solution()
    monster1 = Monster("Knight", 10, 3)
    monster2 = Monster("Mage", 6, 5)
    monster3 = Monster("Goblin", 4, 2)
    monster4 = Monster("Troll", 15, 4)
    monster5 = Monster("Dragon", 8, 6)
    teamA = Team("A", [monster1, monster2])
    teamB = Team("B", [monster3, monster4, monster5])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:Knight -> B:Goblin | DMG=3 | HP:4 -> 1",
      "[ATTACK] B:Goblin -> A:Knight | DMG=2 | HP:10 -> 8",
      "[ATTACK] A:Knight -> B:Goblin | DMG=3 | HP:1 -> 0",
      "[DEATH] B:Goblin defeated | NEXT=B:Troll",
      "[ATTACK] A:Knight -> B:Troll | DMG=3 | HP:15 -> 12",
      "[ATTACK] B:Troll -> A:Knight | DMG=4 | HP:8 -> 4",
      "[ATTACK] A:Knight -> B:Troll | DMG=3 | HP:12 -> 9",
      "[ATTACK] B:Troll -> A:Knight | DMG=4 | HP:4 -> 0",
      "[DEATH] A:Knight defeated | NEXT=A:Mage",
      "[ATTACK] A:Mage -> B:Troll | DMG=5 | HP:9 -> 4",
      "[ATTACK] B:Troll -> A:Mage | DMG=4 | HP:6 -> 2",
      "[ATTACK] A:Mage -> B:Troll | DMG=5 | HP:4 -> 0",
      "[DEATH] B:Troll defeated | NEXT=B:Dragon",
      "[ATTACK] A:Mage -> B:Dragon | DMG=5 | HP:8 -> 3",
      "[ATTACK] B:Dragon -> A:Mage | DMG=6 | HP:2 -> 0",
      "[DEATH] A:Mage defeated | NEXT=NONE",
      "[RESULT] WINNER=B",
    ]
    assert log == expected

def test4():
    print("===== Test 4 =====")

    solution = Solution()
    monster1 = Monster("Dragon", 20, 5)
    teamA = Team("A", [monster1])
    teamB = Team("B", [])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[RESULT] WINNER=A"
    ]
    assert log == expected

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()

# Follow-up:
# In this follow-up, the monster battle simulator is enhanced so that each monster now has types and weaknesses. These additional attributes introduce damage multipliers that can significantly influence how battles unfold.

# class Monster { 
#     String name;
#     int health;
#     int attack;

#     String type; // The monster's elemental category (e.g., "Fire", "Water").
#     List<String> weakness; // A list of types this monster is vulnerable to.
#     ...
# }
# Implement the method simulateBattle(teamA, teamB) that executes the battle simulation and returns a list of event strings based on the updated rules described below:

# New Damage Rule

# When an attacker hits a defender, the final damage depends on the interaction between their types:

# If the defender's weakness list includes the attacker's type, the damage is doubled.
# If the attacker's weakness list includes the defender's type, the damage is halved (floor division toward 0).
# Otherwise, the damage remains unchanged.
# All adjusted damage values must be correctly reflected in the "[ATTACK]" event logs.

# Constraints:

# Team size is less than 104
# 1 ≤ health, attack ≤ 109
# type and weakness strings are non-empty and consist of alphanumeric characters.
# Example:

# Input:
# ["Monster", "Monster", "Team", "Team", "simulateBattle"]
# [["FireMon", 20, 10, "Fire", ["Water"]], ["GrassMon", 15, 5, "Grass", ["Fire"]], ["A", monster1], ["B", monster2], [teamA, teamB]]

# Output:
# [
#   "[ATTACK] A:FireMon -> B:GrassMon | DMG=20 | HP:15 -> 0",
#   "[DEATH] B:GrassMon defeated | NEXT=NONE",
#   "[RESULT] WINNER=A"
# ]

class Monster:
    def __init__(self, name, health, attack, type, weakness):
        self.name = name
        self.health = health
        self.attack = attack
        self.type = type
        self.weakness = weakness

class Team:
    def __init__(self, label, monsters):
        self.label = label
        self.monsters = monsters
        self.activeIdx = 0

    def getActive(self):
        if self.activeIdx < len(self.monsters):
            return self.monsters[self.activeIdx]
        return None

    def advanceAndNextLabel(self):
        self.activeIdx = self.activeIdx + 1
        if self.activeIdx < len(self.monsters):
            return self.label + ":" + self.monsters[self.activeIdx].name
        return "NONE"

    def hasAlive(self):
        return self.activeIdx < len(self.monsters)

class Solution:
    def damage(self, attacker: Monster, defender: Monster) -> int:
        dmg = attacker.attack
        if attacker.type in defender.weakness:
            dmg = dmg * 2
        if defender.type in attacker.weakness:
            dmg = dmg // 2 # floor division
        return dmg

    def simulateBattle(self, teamA, teamB):
        result = []
        while teamA.hasAlive() and teamB.hasAlive():
            monsterA = teamA.getActive()
            monsterB = teamB.getActive()
            # A attacks B
            dmg = self.damage(monsterA, monsterB)
            hpB = monsterB.health
            hpBNew = max(0, hpB - dmg)
            monsterB.health = hpBNew
            msg = (
                f"[ATTACK] A:{monsterA.name} -> B:{monsterB.name} | "
                f"DMG={dmg} | HP:{hpB} -> {hpBNew}"
            )
            result.append(msg)
            if hpBNew == 0:
                newLabel = teamB.advanceAndNextLabel()
                result.append(f"[DEATH] B:{monsterB.name} defeated | NEXT={newLabel}")
                continue

            # now B attacks A
            monsterB = teamB.getActive()
            dmg = self.damage(monsterB, monsterA)
            hpA = monsterA.health
            hpANew = max(0, hpA - dmg)
            monsterA.health = hpANew
            msg = (
                f"[ATTACK] B:{monsterB.name} -> A:{monsterA.name} | "
                f"DMG={dmg} | HP:{hpA} -> {hpANew}"                
            )
            result.append(msg)
            if hpANew == 0:
                newLabel = teamA.advanceAndNextLabel()
                result.append(f"[DEATH] A:{monsterA.name} defeated | NEXT={newLabel}")

        if teamA.hasAlive():
            result.append("[RESULT] WINNER=A")
        else:
            result.append("[RESULT] WINNER=B")
        return result

def test1():
    print("===== Test 1 =====")

    solution = Solution()
    monster1 = Monster("FireMon", 20, 10, "Fire", ["Water"])
    monster2 = Monster("GrassMon", 15, 5, "Grass", ["Fire"])
    teamA = Team("A", [monster1])
    teamB = Team("B", [monster2])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:FireMon -> B:GrassMon | DMG=20 | HP:15 -> 0",
      "[DEATH] B:GrassMon defeated | NEXT=NONE",
      "[RESULT] WINNER=A"
    ]
    assert log == expected

def test2():
    print("===== Test 2 =====")

    solution = Solution()
    monster1 = Monster("FireMon", 8, 9, "Fire", ["Water"])
    monster2 = Monster("WaterMon", 10, 6, "Water", [])
    teamA = Team("A", [monster1])
    teamB = Team("B", [monster2])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:FireMon -> B:WaterMon | DMG=4 | HP:10 -> 6",
      "[ATTACK] B:WaterMon -> A:FireMon | DMG=12 | HP:8 -> 0",
      "[DEATH] A:FireMon defeated | NEXT=NONE",
      "[RESULT] WINNER=B"
    ]
    assert log == expected

def test3():
    print("===== Test 3 =====")

    solution = Solution()
    monster1 = Monster("NormalA", 10, 5, "Normal", ["Fire"])
    monster2 = Monster("NormalB", 12, 3, "Normal", ["Water"])
    teamA = Team("A", [monster1])
    teamB = Team("B", [monster2])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:NormalA -> B:NormalB | DMG=5 | HP:12 -> 7",
      "[ATTACK] B:NormalB -> A:NormalA | DMG=3 | HP:10 -> 7",
      "[ATTACK] A:NormalA -> B:NormalB | DMG=5 | HP:7 -> 2",
      "[ATTACK] B:NormalB -> A:NormalA | DMG=3 | HP:7 -> 4",
      "[ATTACK] A:NormalA -> B:NormalB | DMG=5 | HP:2 -> 0",
      "[DEATH] B:NormalB defeated | NEXT=NONE",
      "[RESULT] WINNER=A"
    ]
    assert log == expected

def test4():
    print("===== Test 4 =====")

    solution = Solution()
    monster1 = Monster("Archer", 12, 6, "Grass", ["Fire"])
    monster2 = Monster("Mage", 20, 4, "Water", ["Grass"])
    monster3 = Monster("FireSprite", 10, 4, "Fire", ["Water"])
    monster4 = Monster("StoneGolem", 18, 5, "Normal", [])
    teamA = Team("A", [monster1, monster2])
    teamB = Team("B", [monster3, monster4])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:Archer -> B:FireSprite | DMG=3 | HP:10 -> 7",
      "[ATTACK] B:FireSprite -> A:Archer | DMG=8 | HP:12 -> 4",
      "[ATTACK] A:Archer -> B:FireSprite | DMG=3 | HP:7 -> 4",
      "[ATTACK] B:FireSprite -> A:Archer | DMG=8 | HP:4 -> 0",
      "[DEATH] A:Archer defeated | NEXT=A:Mage",
      "[ATTACK] A:Mage -> B:FireSprite | DMG=8 | HP:4 -> 0",
      "[DEATH] B:FireSprite defeated | NEXT=B:StoneGolem",
      "[ATTACK] A:Mage -> B:StoneGolem | DMG=4 | HP:18 -> 14",
      "[ATTACK] B:StoneGolem -> A:Mage | DMG=5 | HP:20 -> 15",
      "[ATTACK] A:Mage -> B:StoneGolem | DMG=4 | HP:14 -> 10",
      "[ATTACK] B:StoneGolem -> A:Mage | DMG=5 | HP:15 -> 10",
      "[ATTACK] A:Mage -> B:StoneGolem | DMG=4 | HP:10 -> 6",
      "[ATTACK] B:StoneGolem -> A:Mage | DMG=5 | HP:10 -> 5",
      "[ATTACK] A:Mage -> B:StoneGolem | DMG=4 | HP:6 -> 2",
      "[ATTACK] B:StoneGolem -> A:Mage | DMG=5 | HP:5 -> 0",
      "[DEATH] A:Mage defeated | NEXT=NONE",
      "[RESULT] WINNER=B"
    ]
    assert log == expected

def test5():
    print("===== Test 5 =====")

    solution = Solution()
    monster1 = Monster("Blaze", 14, 7, "Fire", ["Water"])
    monster2 = Monster("Aqua", 10, 5, "Water", ["Electric"])
    monster3 = Monster("Leaf", 12, 6, "Grass", ["Fire"])
    monster4 = Monster("Sprout", 13, 4, "Grass", ["Fire"])
    monster5 = Monster("Spark", 9, 7, "Electric", ["Grass"])
    monster6 = Monster("Wave", 16, 3, "Water", ["Electric"])
    monster7 = Monster("Rock", 18, 15, "Normal", ["Water"])
    teamA = Team("A", [monster1, monster2, monster3])
    teamB = Team("B", [monster4, monster5, monster6, monster7])

    log = solution.simulateBattle(teamA, teamB)
    print(log)
    expected = [
      "[ATTACK] A:Blaze -> B:Sprout | DMG=14 | HP:13 -> 0",
      "[DEATH] B:Sprout defeated | NEXT=B:Spark",
      "[ATTACK] A:Blaze -> B:Spark | DMG=7 | HP:9 -> 2",
      "[ATTACK] B:Spark -> A:Blaze | DMG=7 | HP:14 -> 7",
      "[ATTACK] A:Blaze -> B:Spark | DMG=7 | HP:2 -> 0",
      "[DEATH] B:Spark defeated | NEXT=B:Wave",
      "[ATTACK] A:Blaze -> B:Wave | DMG=3 | HP:16 -> 13",
      "[ATTACK] B:Wave -> A:Blaze | DMG=6 | HP:7 -> 1",
      "[ATTACK] A:Blaze -> B:Wave | DMG=3 | HP:13 -> 10",
      "[ATTACK] B:Wave -> A:Blaze | DMG=6 | HP:1 -> 0",
      "[DEATH] A:Blaze defeated | NEXT=A:Aqua",
      "[ATTACK] A:Aqua -> B:Wave | DMG=5 | HP:10 -> 5",
      "[ATTACK] B:Wave -> A:Aqua | DMG=3 | HP:10 -> 7",
      "[ATTACK] A:Aqua -> B:Wave | DMG=5 | HP:5 -> 0",
      "[DEATH] B:Wave defeated | NEXT=B:Rock",
      "[ATTACK] A:Aqua -> B:Rock | DMG=10 | HP:18 -> 8",
      "[ATTACK] B:Rock -> A:Aqua | DMG=7 | HP:7 -> 0",
      "[DEATH] A:Aqua defeated | NEXT=A:Leaf",
      "[ATTACK] A:Leaf -> B:Rock | DMG=6 | HP:8 -> 2",
      "[ATTACK] B:Rock -> A:Leaf | DMG=15 | HP:12 -> 0",
      "[DEATH] A:Leaf defeated | NEXT=NONE",
      "[RESULT] WINNER=B"
    ]
    assert log == expected

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()