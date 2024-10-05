# settings.py

# Initial screen dimensions (can be resized)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors (R, G, B)
BACKGROUND_COLOR = (30, 30, 30)
PLAYER_COLOR = (0, 255, 0)
FLAIL_COLOR = (255, 0, 0)
CHAIN_COLOR = (200, 200, 200)
HEALTH_COLOR = (255, 0, 0)
HEALTH_RECHARGE_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)
POWERUP_COLOR = (0, 255, 255)
ENERGY_BALL_COLOR = (255, 255, 255)
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
PLAYER_MAX_HEALTH = 100  # Health percentage
PLAYER_HEALTH_REGEN_RATE = 0.05  # Health regenerated per frame
PLAYER_RADIUS = 15  # Fixed player radius
FLAIL_BASE_LENGTH = 100  # Base length of the flail chain
FLAIL_SPEED = 5
FLAIL_BASE_RADIUS = 10
FLAIL_MAX_RADIUS = 30
FLAIL_GROWTH_RATE = 0.02  # Radius increase per score point

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
    'basic': 10,
    'fast': 15,
    'tough': 25,
}

# Power-up settings
POWERUP_TYPES = ['shield', 'double_score']
POWERUP_DURATION = 5000  # milliseconds

# Energy ball settings
ENERGY_BALL_RECHARGE_AMOUNT = 20  # Health percentage restored
ENERGY_BALL_SPAWN_INTERVAL = 8000  # milliseconds

# UI settings
FONT_NAME = None  # Use default font

# Audio settings
MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.5
