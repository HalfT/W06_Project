from directing.director import Director
from services.video_service import VideoService


def main():

    """
    Calls on director to start game
    starts the video service
    
    """

    video_service = VideoService()
    director = Director(video_service)
    director.start_game()



if __name__ == "__main__":
    main()

