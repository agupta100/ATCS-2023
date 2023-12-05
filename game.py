import pygame
import sys

class MazeGame:
    def __init__(self, maze):
        self.maze = maze
        self.player_position = (0, 1)

    def move_player(self, move):
        x, y = self.player_position
        if move == "up" and x > 0 and self.maze[x - 1][y] != 1:
            x -= 1
        elif move == "down" and x < len(self.maze) - 1 and self.maze[x + 1][y] != 1:
            x += 1
        elif move == "left" and y > 0 and self.maze[x][y - 1] != 1:
            y -= 1
        elif move == "right" and y < len(self.maze[0]) - 1 and self.maze[x][y + 1] != 1:
            y += 1
        self.player_position = (x, y)

    def is_game_over(self):
        return self.maze[self.player_position[0]][self.player_position[1]] == 2

def draw_maze(screen, maze):
    block_size = 30
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            color = (0, 0, 0) if maze[i][j] == 1 else (255, 255, 255)
            pygame.draw.rect(screen, color, (j * block_size, i * block_size, block_size, block_size))
            if maze[i][j] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (j * block_size + block_size // 2, i * block_size + block_size // 2), block_size // 2)

def main():
    pygame.init()

    # Define the maze (1 represents walls, 0 represents open path, and 2 represents the finish)
    maze = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 0, 1, 1, 1],
    ]

    game = MazeGame(maze)

    width, height = len(maze[0]) * 30, len(maze) * 30
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Game")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.move_player("up")
                elif event.key == pygame.K_DOWN:
                    game.move_player("down")
                elif event.key == pygame.K_LEFT:
                    game.move_player("left")
                elif event.key == pygame.K_RIGHT:
                    game.move_player("right")

        if game.is_game_over():
            print("Congratulations! You reached the finish!")
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        draw_maze(screen, maze)

        pygame.draw.circle(screen, (0, 255, 0), (game.player_position[1] * 30 + 15, game.player_position[0] * 30 + 15), 15)

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
