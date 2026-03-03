# You are building a chat system that supports human users and automated bots. Users can send messages to a shared channel, which may contain multiple users and multiple bots. Bots can respond to specific commands.

# The system must be extensible so new bot types can be added without modifying existing logic. For simplicity, you can assume there's only one shared channel in the system.

# You need to implement the ChatApp class, which is responsible for managing channels and processing messages. When a user sends a message, the message should first be added to the channel's message log. After that, each bot may react to the message and add its own output to the same log.

# The system must support the following three bot types:

# AwayBot: Records that a user is away in that specific channel

# Triggered when a message starts with "/away ".
# Adds the message: "AwayBot: <user> is away: <reason>".
# TacoBot: Gives tacos from one user to another

# Triggered with the command: "/givetaco @<recipient> <count>".

# If <count> is not provided, it defaults to 1.

# Tracks taco totals per user, per channel.

# Adds a message reflecting the updated count, using the correct singular or plural form, such as:

# "TacoBot: @<giver> gave @<recipient> 1 taco. @<recipient> now has 1 taco."
# "TacoBot: @<giver> gave @<recipient> 2 tacos. @<recipient> now has 3 tacos."
# MeetBot: Sets up a one-on-one meeting and marks the involved users as away

# Triggered by: "/meet <targetUser>".

# This bot works together with AwayBot in the following way:

# If <targetUser> is currently away, AwayBot must output its away message first, for example: "AwayBot: <targetUser> is away: <reason>".
# After the optional AwayBot output, MeetBot adds its own message: "MeetBot: Google Meet with @<sender>, and <targetUser> starting at /abc-def-123".
# Finally, it marks both the <sender> and <targetUser> as away in that channel, using the reason "@<user> may be in a meeting right now".
# Implement the ChatApp class:

# ChatApp() Initializes the chat system.
# void sendMessage(String name, String text) A user specified by name sends a message with text content to the channel. This action may trigger responses from one or more bots.
# List<String> getMessages() Returns a list of all messages from the channel, in the exact order they were processed. This includes both user-sent messages and bot-generated responses.
# Constraints:

# Bot command messages (e.g., "/away", "/meet", "/givetaco") are guaranteed to be in a valid format if they match the command prefix.
# The total number of calls to sendMessage will be between 0 and 1000.
# Example:

# Input:
# ["ChatApp", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "sendMessage", "getMessages"]

# [[], ["general", "Alice", "Hello"], ["general", "Bob", "Hi"], ["general", "Alice", "Nice job on your presentations"], ["general", "Cindy", "/givetaco @justin"], ["general", "Bob", "/givetaco @justin 2"], ["general", "Alice", "Bob let's meet"], ["general", "Bob", "/meet Alice"], ["general", "David", "/away out for lunch"], ["general", "Emily", "Anyone around?"], ["general", "Frank", "/meet David"], []]

# Output:
# [null, null, null, null, null, null, null, null, null, null, null,
#   ["Alice: Hello",
#    "Bob: Hi",
#    "Alice: Nice job on your presentations",
#    "Cindy: /givetaco @justin",
#    "TacoBot: @Cindy gave @justin 1 taco. @justin now has 1 taco.",
#    "Bob: /givetaco @justin 2",
#    "TacoBot: @Bob gave @justin 2 tacos. @justin now has 3 tacos.",
#    "Alice: Bob let's meet",
#    "Bob: /meet Alice",
#    "MeetBot: Google Meet with @Bob, and Alice starting at /abc-def-123",
#    "David: /away out for lunch",
#    "AwayBot: David is away: out for lunch",
#    "Emily: Anyone around?",
#    "Frank: /meet David",
#    "AwayBot: David is away: out for lunch",
#    "MeetBot: Google Meet with @Frank, and David starting at /abc-def-123"]]

# Explanation:

# ChatApp chatApp = new ChatApp();
# chatApp.sendMessage("Alice", "Hello"); // Message added.
# chatApp.sendMessage("Bob", "Hi");
# chatApp.sendMessage("Alice", "Nice job on your presentations");
# chatApp.sendMessage("Cindy", "/givetaco @justin"); // Triggers TacoBot. @justin's "general" count is 1.
# chatApp.sendMessage("Bob", "/givetaco @justin 2"); // Triggers TacoBot. @justin's "general" count is 3.
# chatApp.sendMessage("Alice", "Bob let's meet");
# chatApp.sendMessage("Bob", "/meet Alice"); // Triggers MeetBot. Alice is not away.
# chatApp.sendMessage("David", "/away out for lunch"); // Triggers AwayBot. David is now away.
# chatApp.sendMessage("Emily", "Anyone around?");
# chatApp.sendMessage("Frank", "/meet David"); Triggers MeetBot. David is away, so AwayBot responds first, then MeetBot.
# chatApp.getMessages(); // Returns the 16 messages from the "general" channel as shown above.

from typing import List, Dict, Set, Callable, Any, Type
from collections import defaultdict

class TacoBot:
    def __init__(self):
        self.counts: Dict[str, int] = {}

    def trigger(self, giver: str, receiver: str, count: int) -> str:
        self.counts[receiver] = self.counts.get(receiver, 0) + count
        word1 = "tacos" if count > 1 else "taco"
        receiverCount = self.counts[receiver]
        word2 = "tacos" if receiverCount > 1 else "taco"
        return (
            f"TacoBot: @{giver} gave @{receiver} {count} {word1}. "
            f"@{receiver} now has {self.counts[receiver]} {word2}."
        )

class AwayBot:
    def __init__(self):
        self.awayDict: Dict[str, str] = {}

    def setIsAway(self, user: str, reason: str) -> None:
        self.awayDict[user] = reason

    def isAway(self, user: str) -> bool:
        return user in self.awayDict

    def printMessage(self, user: str) -> str:
        return f"AwayBot: {user} is away: {self.awayDict[user]}"

class MeetBot:
    def __init__(self):
        pass

    def trigger(self, sender: str, targetUser: str) -> str:
        return (
            f"MeetBot: Google Meet with @{sender}, and {targetUser}"
            " starting at /abc-def-123"
        )
        

class ChatApp:
    def __init__(self):
        self.awayBot = AwayBot()
        self.tacoBot = TacoBot()
        self.meetBot = MeetBot()
        self.messages: list[str] = []

    def sendMessage(self, name: str, text: str):
        self.messages.append(f"{name}: {text}")
        if text.startswith("/givetaco"):
            tmp = text.split(" ")
            recipient = tmp[1][1:] # strips leading @
            count = 1
            if len(tmp) == 3:
                count = int(tmp[2])
            message = self.tacoBot.trigger(name, recipient, count) 
            self.messages.append(message)
        elif text.startswith("/away"):
            reason = text[6:] # strips '/away '
            self.awayBot.setIsAway(name, reason)
            self.messages.append(self.awayBot.printMessage(name))
        elif text.startswith("/meet"):
            targetUser = text[6:]
            if self.awayBot.isAway(targetUser):
                self.messages.append(self.awayBot.printMessage(targetUser))
            self.messages.append(self.meetBot.trigger(name, targetUser))
            self.awayBot.setIsAway(name, f"@{name} may be in a meeting right now")
            self.awayBot.setIsAway(targetUser, f"@{targetUser} may be in a meeting right now")
        

    def getMessages(self) -> List[str]:
        return self.messages

def test1():
    print("===== Test 1 =====")
    app = ChatApp()

    app.sendMessage("Alice", "Hello")
    app.sendMessage("Bob", "Hi")
    app.sendMessage("Alice", "Nice job on your presentations")
    app.sendMessage("Cindy", "/givetaco @justin")
    app.sendMessage("Bob", "/givetaco @justin 2")
    app.sendMessage("Alice", "Bob let's meet")
    app.sendMessage("Bob", "/meet Alice")
    app.sendMessage("David", "/away out for lunch")
    app.sendMessage("Emily", "Anyone around?")
    app.sendMessage("Frank", "/meet David")

    # print(app.getMessages())
    messages = app.getMessages()
    # print(messages)
    assert messages == ["Alice: Hello",
    "Bob: Hi",
    "Alice: Nice job on your presentations",
    "Cindy: /givetaco @justin",
    "TacoBot: @Cindy gave @justin 1 taco. @justin now has 1 taco.",
    "Bob: /givetaco @justin 2",
    "TacoBot: @Bob gave @justin 2 tacos. @justin now has 3 tacos.",
    "Alice: Bob let's meet",
    "Bob: /meet Alice",
    "MeetBot: Google Meet with @Bob, and Alice starting at /abc-def-123",
    "David: /away out for lunch",
    "AwayBot: David is away: out for lunch",
    "Emily: Anyone around?",
    "Frank: /meet David",
    "AwayBot: David is away: out for lunch",
    "MeetBot: Google Meet with @Frank, and David starting at /abc-def-123"]
    print("Pass")

def test2():
    print("\n===== Test 2 =====")
    app = ChatApp()

    app.sendMessage("Alice", "/away on vacation")
    app.sendMessage("Bob", "/away sick today")
    app.sendMessage("Charlie", "/meet Alice")
    app.sendMessage("David", "Hello everyone")
    app.sendMessage("Eve", "/meet Bob")

    # print(app.getMessages())
    messages = app.getMessages()
    # print(messages)
    assert messages == ["Alice: /away on vacation",
    "AwayBot: Alice is away: on vacation",
    "Bob: /away sick today",
    "AwayBot: Bob is away: sick today",
    "Charlie: /meet Alice",
    "AwayBot: Alice is away: on vacation",
    "MeetBot: Google Meet with @Charlie, and Alice starting at /abc-def-123",
    "David: Hello everyone",
    "Eve: /meet Bob",
    "AwayBot: Bob is away: sick today",
    "MeetBot: Google Meet with @Eve, and Bob starting at /abc-def-123"]
    print("Pass")

if __name__ == "__main__":
    test1()
    test2()