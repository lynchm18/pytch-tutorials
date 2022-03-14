import pytch


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]
    @pytch.when_green_flag_clicked
    def checkRender(self):
        assert self.Backdrops == ["clouds.jpg"], "Background Image not defined Properly"
        print("Background Rendered successfully!")


class Bird(pytch.Sprite):
    Costumes = ["bird.png"]
    speed = 3

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0, 0)
        self.set_size(0.3)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.change_x(self.speed)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.change_x(-self.speed)

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        self.change_y(self.speed)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        self.change_y(-self.speed)
