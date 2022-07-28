from typing import ClassVar

class ANDROID_VERSIONS:
    __members__: ClassVar[dict] = ...  # read-only
    UNKNOWN: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_601: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_700: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_710: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_712: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_800: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_810: ClassVar[ANDROID_VERSIONS] = ...
    VERSION_900: ClassVar[ANDROID_VERSIONS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def code_name(version: ANDROID_VERSIONS) -> str: ...
def version_string(version: ANDROID_VERSIONS) -> str: ...
