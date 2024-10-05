# settings.py

# Screen dimensions (Adjustable)
WINDOW_WIDTH = 800  # You can change this value
WINDOW_HEIGHT = 600  # You can change this value

# Colors (R, G, B)
BACKGROUND_COLOR = (30, 30, 30)
PLAYER_COLOR = (0, 255, 0)
FLAIL_COLOR = (255, 0, 0)
CHAIN_COLOR = (200, 200, 200)
HEALTH_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)
POWERUP_COLOR = (0, 255, 255)
BUTTON_COLOR = (50, 50, 200)
BUTTON_HOVER_COLOR = (100, 100, 250)

# Enemy colors
ENEMY_COLORS = {
    'basic': (255, 0, 0),
    'fast': (255, 165, 0),
    'tough': (139, 0, 139),
}

# Frame rate
FPS = 60

# Game settings
PLAYER_BASE_SPEED = 5
PLAYER_MAX_HEALTH = 5
PLAYER_RADIUS = 15  # Fixed player radius
FLAIL_BASE_LENGTH = 50
FLAIL_MAX_LENGTH = 200
FLAIL_GROWTH_RATE = 0.5  # Length increase per score point
FLAIL_SPEED = 5

# Enemy settings
ENEMY_TYPES = ['basic', 'fast', 'tough']
ENEMY_BASE_SPEED = 2
ENEMY_SPEED_MULTIPLIER = {
    'basic': 1.0,
    'fast': 1.5,
    'tough': 2.0,
}
ENEMY_HEALTH = {
    'basic': 1,
    'fast': 1,
    'tough': 3,
}
ENEMY_DAMAGE = {
    'basic': 1,
    'fast': 1,
    'tough': 2,
}

# Power-up settings
POWERUP_TYPES = ['shield', 'double_score']
POWERUP_DURATION = 5000  # milliseconds

# UI settings
FONT_NAME = None  # Use default font
