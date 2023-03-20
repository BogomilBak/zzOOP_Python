from .room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([x.guests for x in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}\n"\
                 f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"
