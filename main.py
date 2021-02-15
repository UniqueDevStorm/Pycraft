from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enable = False
window.exit_button.visible = False

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='brick'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=1.0
        )

app.run()