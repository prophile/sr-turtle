from game_object import GameObject
from vision import create_marker_info_by_type, MARKER_TOKEN_SILVER, MARKER_TOKEN_GOLD, MARKER_ARENA

class Token(GameObject):
    grabbable = True
    GOLD = 'gold'
    SILVER = 'silver'

    def __init__(self, arena, colour, number):
        GameObject.__init__(self, arena)
        self.marker_info = create_marker_info_by_type({self.GOLD: MARKER_TOKEN_GOLD,
                                                       self.SILVER: MARKER_TOKEN_SILVER}[colour], number)
        self.grabbed = False
        self.colour = colour

    def grab(self):
        self.grabbed = True

    def release(self):
        self.grabbed = False

    @property
    def surface_name(self):
        return 'sr/token_{1}{0}.png'.format('_grabbed' if self.grabbed else '', self.colour)

class WallMarker(GameObject):
    surface_name = 'sr/wall_marker.png'

    def __init__(self, arena, number, location=(0,0), heading=0):
        GameObject.__init__(self, arena)
        self.marker_info = create_marker_info_by_type(MARKER_ARENA, number)
        self.location = location
        self.heading = heading

