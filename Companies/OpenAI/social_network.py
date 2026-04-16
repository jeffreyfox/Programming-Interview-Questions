import copy

class SocialNetwork:
    def __init__(self):
        """Initialize an empty social network."""
        self.users: set[str] = set()
        self.user_to_followees: dict[str, set[str]] = {}
        self.user_to_followers: dict[str, set[str]] = {}

    def add_user(self, user_id: str) -> None:
        """
        Add a user to the network.
        Raises ValueError if the user already exists.
        """
        self.users.add(user_id)
        self.user_to_followees[user_id] = set()
        self.user_to_followers[user_id] = set()

    def follow(self, follower: str, followee: str) -> None:
        """
        Make `follower` follow `followee`.
        Raises ValueError if a user does not exist.
        Notes: A user cannot follow themselves. Duplicate follows do nothing.
        """
        if follower not in self.users:
            raise ValueError(f"Follower {follower} does not exist")
        
        if followee not in self.users:
            raise ValueError(f"Followee {followee} does not exist")

        if follower == followee:
            raise ValueError("A user cannot follow themselves")

        self.user_to_followers[followee].add(follower)
        self.user_to_followees[follower].add(followee)

    def create_snapshot(self) -> 'Snapshot':
        """
        Create a snapshot of the current network state.
        This object must be immutable (it cannot change).
        """
        return Snapshot(self.user_to_followers, self.user_to_followees)

class Snapshot:
    def __init__(self, user_to_followers, user_to_followees):
        self.user_to_followers = copy.deepcopy(user_to_followers)
        self.user_to_followees = copy.deepcopy(user_to_followees)
        
    def is_following(self, follower: str, followee: str) -> bool:
        """
        Check if `follower` is following `followee` in this snapshot.
        Returns True or False.
        """
        return (
            follower in self.user_to_followees
            and followee in self.user_to_followees[follower]
        )

    def get_following(self, user_id: str) -> list[str]:
        """
        Get a list of people that `user_id` follows.
        """
        if user_id not in self.user_to_followees:
            return []
        return list(self.user_to_followees[user_id])

    def get_followers(self, user_id: str) -> list[str]:
        """
        Get a list of people who follow `user_id`.
        """
        if user_id not in self.user_to_followers:
            return []
        return list(self.user_to_followers[user_id])


def test_1():
    network = SocialNetwork()

    network.add_user("A")
    network.add_user("B")
    network.add_user("C")

    network.follow("A", "B")
    network.follow("B", "C")

    # Take a picture of the network state right now
    snapshot1 = network.create_snapshot()

    assert snapshot1.is_following("A", "B") == True
    assert snapshot1.is_following("B", "C") == True
    assert snapshot1.is_following("A", "C") == False   # A does not follow C

    # Add a new follow AFTER taking the snapshot
    network.follow("A", "C")

    # The old snapshot should NOT show the new follow
    assert snapshot1.is_following("A", "C") == False

    # A new snapshot shows the new follow
    snapshot2 = network.create_snapshot()
    assert snapshot2.is_following("A", "C") == True

def test_2():
    network = SocialNetwork()

    # Setup users and follows...
    network.add_user("A")
    network.add_user("B")
    network.add_user("C")
    network.add_user("D")

    network.follow("A", "B")
    network.follow("A", "C")
    network.follow("B", "C")
    network.follow("D", "A")

    snapshot = network.create_snapshot()

    print(snapshot.get_following("A"))    # ["B", "C"]
    print(snapshot.get_followers("C"))    # ["A", "B"]

test_1()
test_2()