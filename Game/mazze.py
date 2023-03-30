import random
import arcade

MOVE_STEP = 2

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Labiryntówka"

SPRITE_SCALING = 0.25

TILE_EMPTY=0
TILE_WALL=1

MAZE_WIDTH = 51
MAZE_HEIGHT = 51

MARGIN = 50

SPRITE_SIZE = int(128 * SPRITE_SCALING)

class MazzeGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)

        # Zmienne używane so przesuwania ekranu
        self.view_bottom = 0
        self.view_left = 0

        # Lista sprite
        self.players = None
        self.walls = None

        # Nasza postać
        self.player = None
        self.wall = None

        # Definicja fizyki
        self.physics = None

    def create_empty_grid(self, width, height, value=TILE_EMPTY):
        grid = []
        for row in range(height):
            grid.append([])
            for column in range(width):
                grid[row].append(value)
        return grid

    def create_outside_walls(self, maze):
        for row in range(len(maze)):
            maze[row][0] = TILE_WALL
            maze[row][len(maze) - 1] = TILE_WALL

        for column in range(1, len(maze[0]) - 1):
            maze[0][column] = TILE_WALL
            maze[len(maze[0]) - 1][column] = TILE_WALL

    # algorytm budujący labirynt
    def make_maze(self, maze, top, bottom, left, right):
        start_range = bottom + 2
        end_range = top - 1
        y = random.randrange(start_range, end_range, 2)

        for column in range(left + 1, right):
            maze[y][column] = TILE_WALL

        start_range = left + 2
        end_range = right - 1
        x = random.randrange(start_range, end_range, 2)

        for row in range(bottom + 1, top):
            maze[row][x] = TILE_WALL

        wall = random.randrange(4)
        if wall != 0:
            gap = random.randrange(left + 1, x, 2)
            maze[y][gap] = TILE_EMPTY

        if wall != 1:
            gap = random.randrange(x + 1, right, 2)
            maze[y][gap] = TILE_EMPTY

        if wall != 2:
            gap = random.randrange(bottom + 1, y, 2)
            maze[gap][x] = TILE_EMPTY

        if wall != 3:
            gap = random.randrange(y + 1, top, 2)
            maze[gap][x] = TILE_EMPTY

        if top > y + 3 and x > left + 3:
            self.make_maze(maze, top, y, left, x)

        if top > y + 3 and x + 3 < right:
            self.make_maze(maze, top, y, x, right)

        if bottom + 3 < y and x + 3 < right:
            self.make_maze(maze, y, bottom, x, right)

        if bottom + 3 < y and x > left + 3:
            self.make_maze(maze, y, bottom, left, x)

    def create_maze(self, width, height):
        maze = self.create_empty_grid(width, height)
        self.create_outside_walls(maze)
        self.make_maze(maze, height - 1, 0, 0, width - 1)
        return maze;

    def setup(self):

        self.players = arcade.SpriteList()
        self.walls = arcade.SpriteList()

        self.player = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", SPRITE_SCALING)
        self.player.center_y = 64
        self.player.center_x = 48

        self.players.append(self.player)

        maze = self.create_maze(MAZE_WIDTH, MAZE_HEIGHT)

        for row in range(MAZE_HEIGHT):
            for column in range(MAZE_WIDTH):
                if maze[row][column] == 1:
                    wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
                    wall.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                    self.walls.append(wall)

        self.physics = arcade.PhysicsEngineSimple(self.player, self.walls)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player.change_y = MOVE_STEP
        if key == arcade.key.DOWN:
            self.player.change_y = -MOVE_STEP
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVE_STEP
        if key == arcade.key.RIGHT:
            self.player.change_x = MOVE_STEP

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_draw(self):
        self.clear()

        self.player.draw()
        self.walls.draw()

    def update_camera(self):
        change = False

        left_boundary = self.view_left + MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            change = True

        right_boundary = self.view_left + SCREEN_WIDTH - MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            change = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            change = True

        bottom_boundary = self.view_bottom + MARGIN
        if self.player.top < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            change = True

        if change:
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                self.view_bottom, SCREEN_HEIGHT + self.view_bottom)


    def on_update(self, delta_time: float):
        self.physics.update()

        self.update_camera()

def main():
    game = MazzeGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()