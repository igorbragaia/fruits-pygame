from fruits.background import Background
from fruits.scenes.scene import Scene
from fruits.menu import Menu
from fruits.world import Menu as MenuWorld


class MenuScene(Scene):
    def __init__(self, event_handler) -> None:
        super(MenuScene, self).__init__(event_handler,
                                        MenuWorld(),
                                        Background('MENU.png'))
        self._menu = Menu(self)
        self._event_handler.subscribe_entity(self._menu)

    def play(self) -> None:
        Scene.play(self)

    def stop(self) -> None:
        Scene.stop(self)

    def pause(self) -> None:
        Scene.pause(self)

    def _user_update(self, user_commands) -> None:
        if self.status() == Scene.ALIVE and self.user_commands_enabled():
            self._event_handler.process_events(user_commands)

    def _apply_physics(self, engine) -> None:
        if self.status() == Scene.ALIVE:
            engine.move_fruits()

    def _update_final_state(self) -> None:
        if self.status() == Scene.DONE:
            # Scene has received signal to terminate
            # Just enqueue next scene and return
            self._enqueue_next_scene()
            return
        # Update Match according to new world
        # TODO

    def _enqueue_next_scene(self):
        # TODO: Differentiate next scene of QUIT from next scene of end of match
        self._enqueued_scene = None

    def draw_background(self, screen) -> None:
        if self._background is not None and self._background.mesh.image is not None:
            self._background.mesh.draw_on(screen)

    def draw_world(self, screen) -> None:
        if self._world is not None:
            drawables = self._world.drawables
            for drawable in drawables:
                if drawable.mesh.image is not None:
                    drawable.mesh.draw_on(screen)
