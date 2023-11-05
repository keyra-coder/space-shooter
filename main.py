@namespace
class SpriteKind:
    asteroid = SpriteKind.create()

def on_a_pressed():
    global shipfire
    shipfire = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        ship,
        0,
        -100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(ard, effects.halo, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.asteroid, on_on_overlap)

projectile: Sprite = None
shipfire: Sprite = None
ship: Sprite = None
ard: Sprite = None
ard = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . e e e . . . . 
            . . . . . . e e e . f e e . . . 
            . . . . . e e . b b f . e . . . 
            . . . . . e b b e b f f e e e . 
            . . . . e c c b b b f f f e e . 
            . . . . e . c c c c f f b e e . 
            . . . . e e c c c c b b b b e . 
            . . . . . e c c c c 5 5 b b b . 
            . . . . . e c f f f f 5 b b . . 
            . . . . . f f f f 5 5 5 b b . . 
            . . . . . . f f f e e b b b . . 
            . . . . . . . . b b b b . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.asteroid)
effects.star_field.start_screen_effect()
ship = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 2 . . . . . . . . 
            . . . . . . 2 1 2 . . . . . . . 
            . . . . . . 1 1 1 . . . . . . . 
            . . . 2 . . 1 1 1 . . 2 . . . . 
            . . . 8 . 1 1 1 1 1 . 8 . . . . 
            . . . 8 1 1 1 1 1 1 1 8 8 . . . 
            . . 8 8 1 1 1 1 1 1 1 8 8 . . . 
            . . 8 8 1 1 1 1 1 1 1 8 8 . . . 
            . . 8 8 . 1 1 1 1 1 1 8 8 . . . 
            . 4 8 8 1 4 4 4 4 4 1 8 8 4 . . 
            4 1 8 . . . 4 4 4 . . . 8 1 4 . 
            4 1 1 . . . . . 4 . . . . 1 . 4
    """),
    SpriteKind.player)
controller.move_sprite(ship, 100, 100)
ship.set_position(78, 98)
ship.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global projectile
    ard.set_position(randint(0, 160), randint(-20, 0))
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . e e e . . . . 
                    . . . . . . e e e . f e e . . . 
                    . . . . . e e . b b f . e . . . 
                    . . . . . e b b e b f f e e e . 
                    . . . . e c c b b b f f f e e . 
                    . . . . e . c c c c f f b e e . 
                    . . . . e e c c c c b b b b e . 
                    . . . . . e c c c c 5 5 b b b . 
                    . . . . . e c f f f f 5 b b . . 
                    . . . . . f f f f 5 5 5 b b . . 
                    . . . . . . f f f e e b b b . . 
                    . . . . . . . . b b b b . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        ard,
        randint(-100, 100),
        randint(0, 100))
game.on_update_interval(1000, on_update_interval)
