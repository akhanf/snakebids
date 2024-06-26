"""
This type stub file was generated by pyright.
"""

if False: ...
__all__ = [
    "ScalarString",
    "LiteralScalarString",
    "FoldedScalarString",
    "SingleQuotedScalarString",
    "DoubleQuotedScalarString",
    "PlainScalarString",
    "PreservedScalarString",
]

class ScalarString(str):
    __slots__ = ...
    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def replace(self, old: Any, new: Any, maxreplace: SupportsIndex = ...) -> Any: ...
    @property
    def anchor(self) -> Any: ...
    def yaml_anchor(self, any: bool = ...) -> Any: ...
    def yaml_set_anchor(self, value: Any, always_dump: bool = ...) -> None: ...

class LiteralScalarString(ScalarString):
    __slots__ = ...
    style = ...
    def __new__(cls, value: Text, anchor: Any = ...) -> Any: ...

PreservedScalarString = LiteralScalarString

class FoldedScalarString(ScalarString):
    __slots__ = ...
    style = ...
    def __new__(cls, value: Text, anchor: Any = ...) -> Any: ...

class SingleQuotedScalarString(ScalarString):
    __slots__ = ...
    style = ...
    def __new__(cls, value: Text, anchor: Any = ...) -> Any: ...

class DoubleQuotedScalarString(ScalarString):
    __slots__ = ...
    style = ...
    def __new__(cls, value: Text, anchor: Any = ...) -> Any: ...

class PlainScalarString(ScalarString):
    __slots__ = ...
    style = ...
    def __new__(cls, value: Text, anchor: Any = ...) -> Any: ...

def preserve_literal(s: Text) -> Text: ...
def walk_tree(base: Any, map: Any = ...) -> None:
    """
    the routine here walks over a simple yaml tree (recursing in
    dict values and list items) and converts strings that
    have multiple lines to literal scalars

    You can also provide an explicit (ordered) mapping for multiple transforms
    (first of which is executed):
        map = ruamel.yaml.compat.ordereddict
        map['\n'] = preserve_literal
        map[':'] = SingleQuotedScalarString
        walk_tree(data, map=map)
    """
    ...
