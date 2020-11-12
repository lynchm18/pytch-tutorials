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
        x_curr = self.x_position
        self.change_x(self.speed)
        x_new = self.x_position
        x_diff = x_curr - x_new
        assert x_diff == -self.speed, "should have moved the correct amount Right"

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        x_curr = self.x_position
        self.change_x(-self.speed)
        x_new = self.x_position
        x_diff = x_curr - x_new
        assert x_diff == self.speed, "should have moved the correct amount Left"

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        y_curr = self.y_position
        self.change_y(self.speed)
        y_new = self.y_position
        y_diff = y_curr - y_new
        assert y_diff == -self.speed, "should have moved the correct amount Up"

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        y_curr = self.y_position
        self.change_y(-self.speed)
        y_new = self.y_position
        y_diff = y_curr - y_new
        assert y_diff == self.speed, "should have moved the correct amount Down"


class Star(pytch.Sprite):
    Costumes = ["star.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-100, 100)
        self.set_size(0.4)
