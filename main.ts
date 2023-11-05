namespace SpriteKind {
    export const asteroid = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    shipfire = sprites.createProjectileFromSprite(img`
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
        `, ship, 0, -100)
    music.play(music.createSoundEffect(WaveShape.Sine, 1901, 543, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.ashes, 200)
    music.play(music.createSoundEffect(WaveShape.Noise, 744, 1181, 126, 0, 200, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprites.destroy(otherSprite, effects.starField, 500)
    if (info.life() == 0) {
        game.gameOver(false)
        game.splash("Score:  " + info.score())
    }
})
let ard: Sprite = null
let shipfire: Sprite = null
let ship: Sprite = null
effects.starField.startScreenEffect()
ship = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(ship, 100, 100)
ship.setStayInScreen(true)
info.setLife(3)
info.setScore(0)
game.onUpdateInterval(2000, function () {
    ard = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . e e . . . . 
        . . . . . . . e e . f e e . . . 
        . . . . . e e . b b f . e . . . 
        . . . . . e b b e b f f e e e . 
        . . . b e c c b b b f f f e e . 
        . . . b e . c c c c f f b e e . 
        . . . . e e c c c c b b b b e . 
        . . . . . e c c c c 5 5 b b b . 
        . . . . b e c f f f f 5 b b . . 
        . . . . . f f f f 5 5 5 b b . . 
        . . . . . b f f f e e b b . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Enemy)
    ard.setPosition(randint(0, 160), randint(-20, 0))
    ard.setVelocity(randint(-50, 50), randint(0, 50))
})
