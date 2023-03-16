import arcade

HEIGHT = 768
WIDTH = 1024
SPEED = 5
JUMP = 20
GRAVITY = 2

class CMIGame(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Pierwsz Gra CMI")

        self.scene = None
        self.physics = None
        self.player_sprite = None
        self.camera = None
        self.coinCounter = 0

        self.coinSound = None

        arcade.set_background_color(arcade.csscolor.AQUA)

    def setup(self):

        self.camera = arcade.Camera(self.width, self.height)

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("player")
        self.scene.add_sprite_list("wall", use_spatial_hash=True)

        self.coinSound = arcade.load_sound(":resources:/sounds/coin2.wav")

        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 160
        self.scene.add_sprite("player", self.player_sprite)

        wall_source = ":resources:images/tiles/grassMid.png"
        for x in range(0, WIDTH + 128, 128):
            wall = arcade.Sprite(wall_source)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("wall", wall)

        wall_source = ":resources:images/tiles/boxCrate.png"
        wall = arcade.Sprite(wall_source, scale=0.5)
        wall.center_x = 512
        wall.center_y = 128
        self.scene.add_sprite("wall", wall)

        wall = arcade.Sprite(wall_source, scale=0.5)
        wall.center_x = 512+64
        wall.center_y = 128+64
        self.scene.add_sprite("wall", wall)

        wall = arcade.Sprite(wall_source, scale=0.5)
        wall.center_x = 512+128
        wall.center_y = 128+128
        self.scene.add_sprite("wall", wall)

        for x in range(64, WIDTH, 128):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.25)
            coin.center_x = x
            coin.center_y = 102
            self.scene.add_sprite("coins", coin)

        #self.physics = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("wall"))
        self.physics = arcade.PhysicsEnginePlatformer(self.player_sprite, self.scene.get_sprite_list("wall"), gravity_constant=GRAVITY)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            if self.physics.can_jump():
                self.player_sprite.change_y = JUMP
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.show_score()

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        self.camera.move_to((screen_center_x, screen_center_y))

    def get_coin(self):
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["coins"])

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.coinCounter += 1
            arcade.play_sound(self.coinSound)

    def show_score(self):
        arcade.draw_text(f"Punkty: {self.coinCounter}", 10, HEIGHT - 18 - 10, arcade.csscolor.RED, 18)

    def on_update(self, delta_time: float):
        self.physics.update()
        self.get_coin()
        #self.center_camera_to_player()

def main():
    game = CMIGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()