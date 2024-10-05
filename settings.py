# settings.py

# Screen dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors (R, G, B)
BACKGROUND_COLOR = (30, 30, 30)
PLAYER_COLOR = (0, 255, 0)
FLAIL_COLOR = (255, 0, 0)
CHAIN_COLOR = (200, 200, 200)
PARTICLE_COLOR = (255, 255, 0)
HEALTH_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)
POWERUP_COLOR = (0, 255, 255)

# Enemy colors
ENEMY_COLORS = {
    'basic': (255, 0, 0),
    'fast': (255, 165, 0),
    'tough': (139, 0, 139),
}

# Frame rate
FPS = 60

# Game settings
PLAYER_SPEED = 5
PLAYER_MAX_HEALTH = 5
FLAIL_SPEED = 5
FLAIL_INITIAL_LENGTH = 50
FLAIL_GROWTH = 5
PARTICLE_COUNT = 20

# Enemy settings
ENEMY_TYPES = ['basic', 'fast', 'tough']
ENEMY_SPAWN_INTERVAL = 3000  # milliseconds
ENEMY_BASE_SPEED = 2
ENEMY_SPEED_INCREMENT = 0.2
ENEMY_HEALTH = {
    'basic': 1,
    'fast': 1,
    'tough': 3,
}

# Level settings
LEVEL_UP_TIME = 20000  # milliseconds
MAX_LEVEL = 5

# Power-up settings
POWERUP_TYPES = ['speed', 'invincibility', 'health']
POWERUP_SPAWN_INTERVAL = 10000  # milliseconds
POWERUP_DURATION = 5000  # milliseconds
