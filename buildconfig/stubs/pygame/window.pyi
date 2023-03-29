from typing import Iterable, Optional, Tuple, Union, final
from pygame.surface import Surface

WINDOWPOS_UNDEFINED: int
WINDOWPOS_CENTERED: int
def get_windows() -> Tuple[Window, ...]: ... 
def get_grabbed_window() -> Optional[Window]: ...

@final
class Window:
    def __init__(
        self,
        title: str = "pygame",
        size: Iterable[int] = (640, 480),
        position: Union[int, Iterable[int]] = WINDOWPOS_UNDEFINED,
        fullscreen: bool = False,
        fullscreen_desktop: bool = False,
        ) -> None: ...
    def destroy(self) -> None: ...
    def set_icon(self,icon:Surface) -> None: ...
    def set_grab(self,enable :bool) -> None: ...
    def get_grab(self) -> bool: ...

WindowType = Window