import arcade

class CMIGame(arcade.Window):

    WIDTH = 1024

    def __init__(self):
        super().__init__(self.WIDTH, 768, "Pierwsz Gra CMI")

        self.player_list = None
        self.wall_list = None

        arcade.set_background_color(arcade.csscolor.AQUA)

    def setup(self):

        self.player_list = arcade.SpriteList()

        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_jump.png"
        player_sprite = arcade.Sprite(image_source)
        player_sprite.center_x = 64
        player_sprite.center_y = 160
        self.player_list.append(player_sprite)

        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        wall_source = ":resources:images/tiles/grassMid.png"
        for x in range(0, self.WIDTH+128, 128):
            wall = arcade.Sprite(wall_source)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        wall_source = ":resources:images/tiles/boxCrate.png"
        wall = arcade.Sprite(wall_source, scale=0.5)
        wall.center_x = 512
        wall.center_y = 128
        self.wall_list.append(wall)

    def on_draw(self):
        self.clear()

        self.player_list.draw()
        self.wall_list.draw()


def main():
    game = CMIGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()