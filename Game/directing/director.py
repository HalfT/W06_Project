import pygame
from pygame.locals import *
import random


class Director:

    """A person who Directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
    _video_service (VideoService): For providing video output.

    
    
    """

    def __init__(self, video_service):

        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """

        self._video_service = video_service

    def start_game(self,):

        """Starts the game and runs the main game loop.

        args:
            size: sets the size of the window
            lanes: sets the lanes for the cars to move around
            running: true or false for the program to run in the while loop
            cars: sets up cars for the game
            counter: help with progress of the game
            speed: ups the speed as we go
            stage: after the counter gets to a point adds a stage to up the difficulty of the game.
        """

        size = width, height = (1800, 1200)
        road_w = int(width/3)
        lane6 = 1800 - road_w/4
        lane5 = 1500 - road_w/4
        lane4 = 1200 - road_w/4
        lane3 = 900 - road_w/4
        lane2 = 600 - road_w/4
        lane1 = 300 - road_w/4
        lane0 = -300 - road_w/4
        speed = 1
        running = True
            
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Alien Dodge")
        screen.fill((60, 220, 0))

        pygame.display.update()

        car = pygame.image.load("Game\pics\player.png")
        car_loc = car.get_rect()
        car_loc.center = lane4, height*0.8

        car2 = pygame.image.load("Game\pics\lien1.png")
        car2_loc = car2.get_rect()
        car2_loc.center = lane1, height*0.2

        car3 = pygame.image.load("Game\pics\lien2.png")
        car3_loc = car3.get_rect()
        car3_loc.center = lane0, height*0.2

        car4 = pygame.image.load("Game\pics\lien3.png")
        car4_loc = car4.get_rect()
        car4_loc.center = lane0, height*0.2

        car5 = pygame.image.load("Game\pics\lien4.png")
        car5_loc = car5.get_rect()
        car5_loc.center = lane0, height*0.2

        car6 = pygame.image.load("Game\pics\lien5.png")
        car6_loc = car6.get_rect()
        car6_loc.center = lane0, height*0.2

        counter = 0
        stage = 1


        while running:
            counter += 1

            if counter == 1000:
                speed += 0.15
                counter = 0
                stage += 1
                print("level up", stage)

            car2_loc[1] += speed
            if car2_loc [1] > height:
                number = random.randint(0,5)
                if number == 0:
                    car2_loc.center = lane1, -200
                elif number == 1:
                    car2_loc.center = lane2, -200
                elif number == 2:
                    car2_loc.center = lane3, -200
                elif number == 3:
                    car2_loc.center = lane4, -200
                elif number == 4:
                    car2_loc.center = lane5, -200
                elif number == 5:
                    car2_loc.center = lane6, -200

            if stage > 1:
                car3_loc[1] += speed
                if car3_loc [1] > height:
                    number2 = random.randint(0,5)
                    if number2 == 0:
                        car3_loc.center = lane1, -200
                    elif number2 == 1:
                        car3_loc.center = lane2, -200
                    elif number2 == 2:
                        car3_loc.center = lane3, -200
                    elif number2 == 3:
                        car3_loc.center = lane4, -200
                    elif number2 == 4:
                        car3_loc.center = lane5, -200
                    elif number2 == 5:
                        car3_loc.center = lane6, -200

            if stage > 2:
                car4_loc[1] += speed
                if car4_loc [1] > height:
                    number3 = random.randint(0,5)
                    if number3 == 0:
                        car4_loc.center = lane1, -200
                    elif number3 == 1:
                        car4_loc.center = lane2, -200
                    elif number3 == 2:
                        car4_loc.center = lane3, -200
                    elif number3 == 3:
                        car4_loc.center = lane4, -200
                    elif number3 == 4:
                        car4_loc.center = lane5, -200
                    elif number3 == 5:
                        car4_loc.center = lane6, -200

            if stage > 3:
                car5_loc[1] += speed
                if car5_loc [1] > height:
                    number4 = random.randint(0,5)
                    if number4 == 0:
                        car5_loc.center = lane1, -200
                    elif number4 == 1:
                        car5_loc.center = lane2, -200
                    elif number4 == 2:
                        car5_loc.center = lane3, -200
                    elif number4 == 3:
                        car5_loc.center = lane4, -200
                    elif number4 == 4:
                        car5_loc.center = lane5, -200
                    elif number4 == 5:
                        car5_loc.center = lane6, -200

            if stage > 4:
                car6_loc[1] += speed
                if car6_loc [1] > height:
                    number5 = random.randint(0,5)
                    if number5 == 0:
                        car6_loc.center = lane1, -200
                    elif number5 == 1:
                        car6_loc.center = lane2, -200
                    elif number5 == 2:
                        car6_loc.center = lane3, -200
                    elif number5 == 3:
                        car6_loc.center = lane4, -200
                    elif number5 == 4:
                        car6_loc.center = lane5, -200
                    elif number5 == 5:
                        car6_loc.center = lane6, -200


            if car_loc[0] == car2_loc[0]:
                if car2_loc [1] > car_loc[1] - 50:
                    if car2_loc[1] < car_loc[1] + 50:
                        print("Game Over")
                        break

            if car_loc[0] == car3_loc[0]:
                if car3_loc [1] > car_loc[1] - 50:
                    if car3_loc[1] < car_loc[1] + 50:
                        print("Game Over")
                        break        

            if car_loc[0] == car4_loc[0]:
                if car4_loc [1] > car_loc[1] - 50:
                    if car4_loc[1] < car_loc[1] + 50:
                        print("Game Over")
                        break
            
            if car_loc[0] == car5_loc[0]:
                if car5_loc [1] > car_loc[1] - 50:
                    if car5_loc[1] < car_loc[1] + 50:
                        print("Game Over")
                        break
            
            if car_loc[0] == car6_loc[0]:
                if car6_loc [1] > car_loc[1] - 50:
                    if car6_loc[1] < car_loc[1] + 50:
                        print("Game Over")
                        break
            
            for event in pygame.event.get():
                if event.type == quit:
                    running = False
                
                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        car_loc = car_loc.move([-int(road_w/2), 0])
                    if event.key in [K_d, K_RIGHT]:
                        car_loc = car_loc.move([int(road_w/2), 0])

           

            pygame.draw.rect(
            screen,
            (50, 50, 50),
            (0, 0, width, height)
            )


            
            screen.blit(car, car_loc)
            screen.blit(car2, car2_loc)
            screen.blit(car3, car3_loc)
            screen.blit(car4, car4_loc)
            screen.blit(car5, car5_loc)
            screen.blit(car6, car6_loc)
            pygame.display.update()


        self._video_service.close_window()
