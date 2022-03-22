import pytch


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]
    @pytch.when_green_flag_clicked
    def checkRender(self):
        assert self.Backdrops == ["clouds.jpg"], "Background Image not defined Properly"
        print("Background Rendered successfully!")
