import pytch
import random


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]
    @pytch.when_green_flag_clicked
    def checkRender(self):
        assert self.Backdrops == ["clouds.jpg"], "Background Image not defined Properly"
        print("Background Rendered successfully!")


class Bird(pytch.Sprite):
    Costumes = ["bird.png"]
    Sounds = ["honk.wav"]
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

    @pytch.when_green_flag_clicked
    def check_catch(self):
        pytch.wait_seconds(0.1)
        while True:
            if self.touching(Star):
                self.start_sound("honk")
                self.say_for_seconds("Got you!", 2)


class Star(pytch.Sprite):
    Costumes = ["star.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-100, 100)
        self.set_size(0.4)
        while True:
            self.show()
            destination_x = random.randint(-240, 240)
            destination_y = random.randint(-180, 180)
            self.glide_to_xy(destination_x, destination_y, 2)

    @pytch.when_green_flag_clicked
    def check_caught(self):
        while True:
            if self.touching(Bird):
                self.hide()

    @pytch.when_green_flag_clicked
    def testMovement(self):
        pytch.wait_seconds(10)
        x_start = self.x_position
        y_start = self.y_position
        pytch.wait_seconds(2)
        assert self.x_position != x_start, "star should have moved X"
        assert self.y_position != y_start, "star should have moved Y"
        print("Star Successfully Moved!")
