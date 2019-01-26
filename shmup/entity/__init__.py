"""
Container and reference for all actors and entities
*hitbox collision function
*Player type alias
*Lists each of Enemy, Token, and Projectile types for setup and spawning purposes
todo load in and finish enemies
todo executive decisions: Drop entityhandler and use Scene as Observer?
"""
import entity.actor.player

# Type aliases
Player = entity.actor.player.Player

Enemy = list()

Powerup = list()

Projectiles = list()

Explosion = None
