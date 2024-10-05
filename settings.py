# settings.py

# Screen dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

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
PLAYER_MIN_RADIUS = 10
PLAYER_MAX_RADIUS = 30
PLAYER_GROWTH_RATE = 0.05  # Increase per score point
PLAYER_SHRINK_RATE = 2     # Decrease per hit
FLAIL_SPEED = 5
FLAIL_LENGTH = 50

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
