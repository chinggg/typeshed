from typing import Any, ClassVar, Iterable, Iterator, List, overload

class ARCHITECTURES:
    __members__: ClassVar[dict] = ...  # read-only
    ARM: ClassVar[ARCHITECTURES] = ...
    ARM64: ClassVar[ARCHITECTURES] = ...
    INTEL: ClassVar[ARCHITECTURES] = ...
    MIPS: ClassVar[ARCHITECTURES] = ...
    NONE: ClassVar[ARCHITECTURES] = ...
    PPC: ClassVar[ARCHITECTURES] = ...
    RISCV: ClassVar[ARCHITECTURES] = ...
    SPARC: ClassVar[ARCHITECTURES] = ...
    SYSZ: ClassVar[ARCHITECTURES] = ...
    X86: ClassVar[ARCHITECTURES] = ...
    XCORE: ClassVar[ARCHITECTURES] = ...
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

class Binary(Object):
    class VA_TYPES:
        __members__: ClassVar[dict] = ...  # read-only
        AUTO: ClassVar[Binary.VA_TYPES] = ...
        RVA: ClassVar[Binary.VA_TYPES] = ...
        VA: ClassVar[Binary.VA_TYPES] = ...
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

    class it_relocations:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...

    class it_sections:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...

    class it_symbols:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, index) -> Any: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> Any: ...
    name: str
    def __init__(self, *args, **kwargs) -> None: ...
    def get_content_from_virtual_address(self, virtual_address: int, size: int, va_type: Binary.VA_TYPES = ...) -> List[int]: ...
    def get_function_address(self, function_name: str) -> int: ...
    def get_symbol(self, *args, **kwargs) -> Any: ...
    def has_symbol(self, symbol_name: str) -> bool: ...
    def offset_to_virtual_address(self, offset: int, slide: int = ...) -> int: ...
    @overload
    def patch_address(self, address: int, patch_value: List[int], va_type: Binary.VA_TYPES = ...) -> None: ...
    @overload
    def patch_address(self, address: int, patch_value: int, size: int = ..., va_type: Binary.VA_TYPES = ...) -> None: ...
    def remove_section(self, name: str, clear: bool = ...) -> None: ...
    def xref(self, virtual_address: int) -> List[int]: ...
    @property
    def abstract(self) -> object: ...
    @property
    def concrete(self) -> object: ...
    @property
    def ctor_functions(self) -> Any: ...
    @property
    def entrypoint(self) -> int: ...
    @property
    def exported_functions(self) -> Any: ...
    @property
    def format(self) -> EXE_FORMATS: ...
    @property
    def has_nx(self) -> bool: ...
    @property
    def header(self) -> Any: ...
    @property
    def imagebase(self) -> int: ...
    @property
    def imported_functions(self) -> Any: ...
    @property
    def is_pie(self) -> bool: ...
    @property
    def libraries(self) -> Any: ...
    @property
    def relocations(self) -> Binary.it_relocations: ...
    @property
    def sections(self) -> Any: ...
    @property
    def symbols(self) -> Binary.it_symbols: ...

class DictStringVersion:
    def __init__(self) -> None: ...
    def items(self) -> ItemsView[DictStringVersion]: ...
    def keys(self) -> KeysView[DictStringVersion]: ...
    def values(self) -> ValuesView[DictStringVersion]: ...
    def __bool__(self) -> bool: ...
    @overload
    def __contains__(self, arg0: str) -> bool: ...
    @overload
    def __contains__(self, arg0: object) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> str: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: str) -> None: ...

class ENDIANNESS:
    __members__: ClassVar[dict] = ...  # read-only
    BIG: ClassVar[ENDIANNESS] = ...
    LITTLE: ClassVar[ENDIANNESS] = ...
    NONE: ClassVar[ENDIANNESS] = ...
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

class EXE_FORMATS:
    __members__: ClassVar[dict] = ...  # read-only
    ELF: ClassVar[EXE_FORMATS] = ...
    MACHO: ClassVar[EXE_FORMATS] = ...
    PE: ClassVar[EXE_FORMATS] = ...
    UNKNOWN: ClassVar[EXE_FORMATS] = ...
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

class Function(Symbol):
    class FLAGS:
        __members__: ClassVar[dict] = ...  # read-only
        CONSTRUCTOR: ClassVar[Function.FLAGS] = ...
        DEBUG: ClassVar[Function.FLAGS] = ...
        DESTRUCTOR: ClassVar[Function.FLAGS] = ...
        EXPORTED: ClassVar[Function.FLAGS] = ...
        IMPORTED: ClassVar[Function.FLAGS] = ...
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
    address: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    def add(self, flag: Function.FLAGS) -> Function: ...
    @property
    def flags(self) -> List[Function.FLAGS]: ...

class Header(Object):
    architecture: Any
    endianness: ENDIANNESS
    entrypoint: int
    modes: Set[MODES]
    object_type: OBJECT_TYPES
    def __init__(self) -> None: ...
    @property
    def is_32(self) -> bool: ...
    @property
    def is_64(self) -> bool: ...

class ItemsView(DictStringVersion):
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class KeysView(DictStringVersion):
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def __contains__(self, arg0: str) -> bool: ...
    @overload
    def __contains__(self, arg0: object) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class ListLangCodeItem:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: ListLangCodeItem) -> None: ...
    @overload
    def __init__(self, arg0: Iterable) -> None: ...
    def append(self, x: PE.LangCodeItem) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: PE.LangCodeItem) -> int: ...
    @overload
    def extend(self, L: ListLangCodeItem) -> None: ...
    @overload
    def extend(self, L: Iterable) -> None: ...
    def insert(self, i: int, x: PE.LangCodeItem) -> None: ...
    @overload
    def pop(self) -> PE.LangCodeItem: ...
    @overload
    def pop(self, i: int) -> PE.LangCodeItem: ...
    def remove(self, x: PE.LangCodeItem) -> None: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, x: PE.LangCodeItem) -> bool: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    @overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: ListLangCodeItem) -> bool: ...
    @overload
    def __getitem__(self, s: slice) -> ListLangCodeItem: ...
    @overload
    def __getitem__(self, arg0: int) -> PE.LangCodeItem: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: ListLangCodeItem) -> bool: ...
    @overload
    def __setitem__(self, arg0: int, arg1: PE.LangCodeItem) -> None: ...
    @overload
    def __setitem__(self, arg0: slice, arg1: ListLangCodeItem) -> None: ...

class MODES:
    __members__: ClassVar[dict] = ...  # read-only
    ARM: ClassVar[MODES] = ...
    M16: ClassVar[MODES] = ...
    M32: ClassVar[MODES] = ...
    M64: ClassVar[MODES] = ...
    MCLASS: ClassVar[MODES] = ...
    MIPS3: ClassVar[MODES] = ...
    MIPS32: ClassVar[MODES] = ...
    MIPS32R6: ClassVar[MODES] = ...
    MIPS64: ClassVar[MODES] = ...
    MIPSGP64: ClassVar[MODES] = ...
    NONE: ClassVar[MODES] = ...
    THUMB: ClassVar[MODES] = ...
    UNDEFINED: ClassVar[MODES] = ...
    V7: ClassVar[MODES] = ...
    V8: ClassVar[MODES] = ...
    V9: ClassVar[MODES] = ...
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

class OBJECT_TYPES:
    __members__: ClassVar[dict] = ...  # read-only
    EXECUTABLE: ClassVar[OBJECT_TYPES] = ...
    LIBRARY: ClassVar[OBJECT_TYPES] = ...
    NONE: ClassVar[OBJECT_TYPES] = ...
    OBJECT: ClassVar[OBJECT_TYPES] = ...
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

class Object:
    def __init__(self, *args, **kwargs) -> None: ...

class PLATFORMS:
    __members__: ClassVar[dict] = ...  # read-only
    ANDROID: ClassVar[PLATFORMS] = ...
    IOS: ClassVar[PLATFORMS] = ...
    LINUX: ClassVar[PLATFORMS] = ...
    OSX: ClassVar[PLATFORMS] = ...
    UNKNOWN: ClassVar[PLATFORMS] = ...
    WINDOWS: ClassVar[PLATFORMS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __eq__(self, arg0: int) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    @overload
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __ne__(self, arg0: int) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Relocation(Object):
    address: int
    size: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, address: int, size: int) -> None: ...
    def __eq__(self, arg0: Relocation) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, arg0: Relocation) -> bool: ...

class Section(Object):
    content: memoryview
    name: object
    offset: int
    size: int
    virtual_address: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def search(self, number: int, pos: int = ..., size: int = ...) -> int: ...
    @overload
    def search(self, str: str, pos: int = ...) -> int: ...
    @overload
    def search_all(self, number: int, size: int = ...) -> List[int]: ...
    @overload
    def search_all(self, str: str) -> List[int]: ...
    @property
    def entropy(self) -> float: ...
    @property
    def fullname(self) -> str: ...

class Symbol(Object):
    name: object
    size: int
    value: int
    def __init__(self) -> None: ...

class ValuesView(DictStringVersion):
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class bad_file(exception): ...
class bad_format(bad_file): ...
class builder_error(exception): ...
class conversion_error(exception): ...
class corrupted(exception): ...
class exception(Exception): ...
class integrity_error(exception): ...

class lief_errors:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    asn1_bad_tag: ClassVar[lief_errors] = ...
    build_error: ClassVar[lief_errors] = ...
    conversion_error: ClassVar[lief_errors] = ...
    corrupted: ClassVar[lief_errors] = ...
    data_too_large: ClassVar[lief_errors] = ...
    file_error: ClassVar[lief_errors] = ...
    file_format_error: ClassVar[lief_errors] = ...
    not_found: ClassVar[lief_errors] = ...
    not_implemented: ClassVar[lief_errors] = ...
    not_supported: ClassVar[lief_errors] = ...
    parsing_error: ClassVar[lief_errors] = ...
    read_error: ClassVar[lief_errors] = ...
    read_out_of_bound: ClassVar[lief_errors] = ...
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

class not_found(exception): ...
class not_implemented(exception): ...
class not_supported(exception): ...

class ok_t:
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...

class parser_error(exception): ...
class pe_bad_section_name(pe_error): ...
class pe_error(exception): ...
class read_out_of_bound(exception): ...
class type_error(exception): ...

@overload
def art_version(filename: str) -> int: ...
@overload
def art_version(raw: List[int]) -> int: ...
def breakp() -> object: ...
def current_platform() -> PLATFORMS: ...
def demangle(arg0: str) -> object: ...
@overload
def dex_version(filename: str) -> int: ...
@overload
def dex_version(raw: List[int]) -> int: ...
@overload
def hash(arg0: Object) -> int: ...
@overload
def hash(arg0: List[int]) -> int: ...
@overload
def hash(arg0: bytes) -> int: ...
@overload
def hash(arg0: str) -> int: ...
@overload
def is_art(filename: str) -> bool: ...
@overload
def is_art(raw: List[int]) -> bool: ...
@overload
def is_dex(filename: str) -> bool: ...
@overload
def is_dex(raw: List[int]) -> bool: ...
@overload
def is_elf(filename: str) -> bool: ...
@overload
def is_elf(raw: List[int]) -> bool: ...
@overload
def is_macho(filename: str) -> bool: ...
@overload
def is_macho(raw: List[int]) -> bool: ...
@overload
def is_oat(filename: str) -> bool: ...
@overload
def is_oat(raw: List[int]) -> bool: ...
@overload
def is_oat(elf: ELF.Binary) -> bool: ...
@overload
def is_pe(filename: str) -> bool: ...
@overload
def is_pe(raw: List[int]) -> bool: ...
@overload
def is_vdex(filename: str) -> bool: ...
@overload
def is_vdex(raw: List[int]) -> bool: ...
@overload
def oat_version(filename: str) -> int: ...
@overload
def oat_version(raw: List[int]) -> int: ...
@overload
def oat_version(elf: ELF.Binary) -> int: ...
@overload
def parse(raw: bytes, name: str = ...) -> Binary: ...
@overload
def parse(filepath: str) -> Binary: ...
@overload
def parse(raw: List[int], name: str = ...) -> Binary: ...
@overload
def parse(io: object, name: str = ...) -> Binary: ...
def shell() -> object: ...
def to_json(arg0: Object) -> str: ...
def to_json_from_abstract(arg0: Object) -> str: ...
@overload
def vdex_version(filename: str) -> int: ...
@overload
def vdex_version(raw: List[int]) -> int: ...
