from typing import Iterable, Optional, Tuple, Union, final
from pygame.surface import Surface
from ._common import RectValue

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
    def set_windowed(self) -> None: ...
    def set_fullscreen(self, desktop:bool = False) -> None: ...
    def focus(self, input_only: bool = False) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def restore(self) -> None: ...
    def maximize(self) -> None: ...
    def minimize(self) -> None: ...
    def set_modal_for(self, parent :Window) -> None: ...
    def update_from_surface(self, *rects :RectValue) -> None: ...

    def set_icon(self,icon:Surface) -> None: ...
    def set_grab(self,enable :bool) -> None: ...
    def get_grab(self) -> bool: ...
    def set_title(self,title :str) -> None: ...
    def get_title(self) -> str: ...
    def set_resizable(self,enable :bool) -> None: ...
    def get_resizable(self) -> bool: ...
    def set_borderless(self,enable :bool) -> None: ...
    def get_borderless(self) -> bool: ...
    def get_window_id(self) -> int: ...
    def set_size(self, size :Iterable[int]) -> None: ...
    def get_size(self) -> Tuple[int, int]: ...
    def set_position(self, position :Iterable[int]) -> None: ...
    def get_position(self) -> Tuple[int, int]: ...
    def set_opacity(self,opacity :float) -> None: ...
    def get_opacity(self) -> float: ...
    def get_display_index(self) -> int: ...
    def get_surface(self) -> Surface: ...
    def set_always_on_top(self,enable :bool) -> None: ...
    def get_always_on_top(self) -> bool: ...
    def get_wm_info(self) -> dict: ...

    @classmethod
    def from_display_module(cls) -> Window: ...
    @classmethod
    def from_existing_window(cls) -> Window: ...
    

WindowType = Window
