import pytch


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]


class Bird(pytch.Sprite):
    Costumes = ["bird.png"]

    start_shown = False

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0, 0)
        self.show()
