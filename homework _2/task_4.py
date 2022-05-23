from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def get_screen(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def get_keyboard(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def get_touchpad(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def get_webcam(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def get_ports(self):
        raise NotImplementedError("This method was not implemented")

    @abstractmethod
    def get_dynamics(self):
        raise NotImplementedError("This method was not implemented")


class HPLaptop(Laptop):
    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

    def get_screen(self):
        print(self.screen)

    def get_keyboard(self):
        print(self.keyboard)

    def get_touchpad(self):
        print(self.touchpad)

    def get_webcam(self):
        print(self.webcam)

    def get_ports(self):
        print(self.ports)

    def get_dynamics(self):
        print(self.dynamics)


hp250 = HPLaptop(screen='15,6", HD SVA eDP, WLED', keyboard='Full size textured',
                 touchpad='S145-15 SA469D-22HH, black', webcam='VGA, 480p',
                 ports='(2) USB 3.1, (1) USB 2.0, (1) HDMI 1.4b, (1) RJ-45/Ethernet',
                 dynamics='Built-in stereo speakers')


hp250.get_ports()
hp250.get_screen()
hp250.get_touchpad()
