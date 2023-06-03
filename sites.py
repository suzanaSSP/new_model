import random
class Site:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Foreign_Site(Site):
    def __init__(self, x, y, quality) -> None:
        super().__init__(x, y)
        self.quality = quality