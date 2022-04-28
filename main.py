from flappy import run, user_play
import os

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "CONFIG.txt")
    # the 2ed parameter
    # None for no visulization
    # other for visulization
    run(config_path)
    # user_play()