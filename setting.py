import pygame

pygame.init()
pygame.font.init()

class Setting:
    def __init__(self):
        self.boardSize = 8
        self.windowIconSize = 30
        self.width = 1300
        self.height = 700
        self.resolution = (self.width, self.height)
        self.top_offset = 20
        self.spotSize = (self.height - self.top_offset) // self.boardSize
        self.horizontal_offset = self.width // 2 - (self.spotSize * (self.boardSize // 2))
        self.fps = 60
        self.CoordFont = pygame.font.SysFont("jaapokki", 18, bold=True)
        self.highlightOutline = 5
        self.themeIndex = -1
        # CHANGE THE AI DIFFICULTY
        self.AI_DEPTH = 3
        self.themes = [
            # DUSK THEME
            {"dark": (112, 102, 119), "light": (204, 183, 174), "outline": (0, 0, 0)}
        ]
        
Config = Setting()

