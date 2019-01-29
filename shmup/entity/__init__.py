"""
Container and reference for all actors and entities
*hitbox collision function
*Player type alias
*Lists each of Enemy, Token, and Projectile types for setup and spawning purposes
todo load in and finish enemies
todo executive decisions: Drop entityhandler and use Scene as Observer?
"""
import shmup.entity.actor.player as player

# Type aliases
Player = player.Player

Enemy = list()

Powerup = list()

Projectiles = list()

Explosion = list()


def hit_collide(a, b):
    """
    Check if two sprites hitboxes are interacting

    Args:
        a (Sprite): Sprite A to be collided. Must have hitbox field
        b (Sprite): Sprite B to check Collision. Must have hitbox field

    Returns:
        True is hitboxes are colliding, Fale otherwise
    """
    if a.hitbox.collide(b.hitbox):
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

    for powerup in Powerup:
        powerup.setup(observer)

    for projectile in Projectiles:
        projectile.setupC(observer)

    for exp in Explosion:
        exp.setup(observer)
