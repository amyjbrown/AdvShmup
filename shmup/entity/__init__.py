"""
Container and reference for all actors and entities
*hitbox collision function
*Player type alias
*Lists each of Enemy, Token, and Projectile types for setup and spawning purposes
"""
import shmup.entity.actor.player as player
import shmup.entity.projectile as projectile
import shmup.entity.actor.asteroid as asteroid
import shmup.entity.powerup as powerup

# import shmup.entity.powerup as powerup

# Type aliases
Player = player.Player
Bullet = projectile.Bullet
Asteroid = asteroid.Asteroid
HealthToken = powerup.Health
HighPointToken = powerup.HighPoint
# Setup loops
Enemy = [Asteroid]

Powerups = [HealthToken, HighPointToken]

Projectiles = [Bullet
               ]

Particles = []


def hit_collide(a, b):
    """
    Check if two sprites hitboxes are interacting

    Args:
        a (Sprite): Sprite A to be collided. Must have hitbox field
        b (Sprite): Sprite B to check Collision. Must have hitbox field

    Returns:
        True is hitboxes are colliding, Fale otherwise
    """
    if a.hitbox.colliderect(b.hitbox):
        return True
    return False


def setup(observer):
    """
    Call to initialize image attributes for all game entities

    Args:
        observer (Scene): Scene object that will act as the Entities observer

    Returns:
        None
    """
    Player.setup(observer)

    for enemy in Enemy:
        enemy.setup(observer)

    for powerup in Powerups:
        powerup.setup(observer)

    for projectile in Projectiles:
        projectile.setup(observer)

    for p in Particles:
        p.setup(observer)
