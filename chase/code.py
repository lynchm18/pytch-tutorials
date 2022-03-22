import pytch


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]
    @pytch.when_green_flag_clicked
    def checkRender(self):
        assert self.Backdrops == ["clouds.jpg"], "Background Image not defined Properly"
        print("Background Rendered successfully!")


class Bird(pytch.Sprite):
    Costumes = ["bird.png"]

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0, 0)
        self.set_size(0.3)
