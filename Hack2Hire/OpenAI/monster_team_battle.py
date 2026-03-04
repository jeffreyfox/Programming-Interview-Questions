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