# Task #2

# Composition
class Person:
    def __init__(self):
        right_arm = Arm('Right')
        left_arm = Arm('Left')
        self.rl_arms = [right_arm.rl_arm, left_arm.rl_arm]


class Arm:
    def __init__(self, rl_arm):
        self.rl_arm = rl_arm


arms = Person()
print(arms.rl_arms)


# Aggregation
class CellPhone:
    def __init__(self, screen):
        self.screen = screen

    def get_model_screen(self):
        """Return screen model"""
        print(f'Screen model: {self.screen.screen_type}')


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


screen_1 = Screen('ips_1144')
galaxy_a1 = CellPhone(screen_1)

screen_2 = Screen('oled_2285')
note_10 = CellPhone(screen_2)

screen_3 = Screen('amoled_1337')
mi_9 = CellPhone(screen_3)

screen_4 = Screen('tft_8229')
mi10t = CellPhone(screen_4)

galaxy_a1.get_model_screen()
mi10t.get_model_screen()
