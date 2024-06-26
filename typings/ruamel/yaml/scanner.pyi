"""
This type stub file was generated by pyright.
"""

from ruamel.yaml.error import MarkedYAMLError
from ruamel.yaml.tokens import *
from ruamel.yaml.compat import _debug

if False: ...
__all__ = ["Scanner", "RoundTripScanner", "ScannerError"]
_THE_END = ...
_THE_END_SPACE_TAB = ...
_SPACE_TAB = ...
if _debug != 0:
    def xprintf(*args: Any, **kw: Any) -> Any: ...

class ScannerError(MarkedYAMLError): ...

class SimpleKey:
    def __init__(
        self,
        token_number: Any,
        required: Any,
        index: int,
        line: int,
        column: int,
        mark: Any,
    ) -> None: ...

class Scanner:
    def __init__(self, loader: Any = ...) -> None:
        """Initialize the scanner."""
        ...

    @property
    def flow_level(self) -> int: ...
    def reset_scanner(self) -> None: ...
    @property
    def reader(self) -> Any: ...
    @property
    def scanner_processing_version(self) -> Any: ...
    def check_token(self, *choices: Any) -> bool: ...
    def peek_token(self) -> Any: ...
    def get_token(self) -> Any: ...
    def need_more_tokens(self) -> bool: ...
    def fetch_comment(self, comment: Any) -> None: ...
    def fetch_more_tokens(self) -> Any: ...
    def next_possible_simple_key(self) -> Any: ...
    def stale_possible_simple_keys(self) -> None: ...
    def save_possible_simple_key(self) -> None: ...
    def remove_possible_simple_key(self) -> None: ...
    def unwind_indent(self, column: Any) -> None: ...
    def add_indent(self, column: int) -> bool: ...
    def fetch_stream_start(self) -> None: ...
    def fetch_stream_end(self) -> None: ...
    def fetch_directive(self) -> None: ...
    def fetch_document_start(self) -> None: ...
    def fetch_document_end(self) -> None: ...
    def fetch_document_indicator(self, TokenClass: Any) -> None: ...
    def fetch_flow_sequence_start(self) -> None: ...
    def fetch_flow_mapping_start(self) -> None: ...
    def fetch_flow_collection_start(self, TokenClass: Any, to_push: Text) -> None: ...
    def fetch_flow_sequence_end(self) -> None: ...
    def fetch_flow_mapping_end(self) -> None: ...
    def fetch_flow_collection_end(self, TokenClass: Any) -> None: ...
    def fetch_flow_entry(self) -> None: ...
    def fetch_block_entry(self) -> None: ...
    def fetch_key(self) -> None: ...
    def fetch_value(self) -> None: ...
    def fetch_alias(self) -> None: ...
    def fetch_anchor(self) -> None: ...
    def fetch_tag(self) -> None: ...
    def fetch_literal(self) -> None: ...
    def fetch_folded(self) -> None: ...
    def fetch_block_scalar(self, style: Any) -> None: ...
    def fetch_single(self) -> None: ...
    def fetch_double(self) -> None: ...
    def fetch_flow_scalar(self, style: Any) -> None: ...
    def fetch_plain(self) -> None: ...
    def check_directive(self) -> Any: ...
    def check_document_start(self) -> Any: ...
    def check_document_end(self) -> Any: ...
    def check_block_entry(self) -> Any: ...
    def check_key(self) -> Any: ...
    def check_value(self) -> Any: ...
    def check_plain(self) -> Any: ...
    def scan_to_next_token(self) -> Any: ...
    def scan_directive(self) -> Any: ...
    def scan_directive_name(self, start_mark: Any) -> Any: ...
    def scan_yaml_directive_value(self, start_mark: Any) -> Any: ...
    def scan_yaml_directive_number(self, start_mark: Any) -> Any: ...
    def scan_tag_directive_value(self, start_mark: Any) -> Any: ...
    def scan_tag_directive_handle(self, start_mark: Any) -> Any: ...
    def scan_tag_directive_prefix(self, start_mark: Any) -> Any: ...
    def scan_directive_ignored_line(self, start_mark: Any) -> None: ...
    def scan_anchor(self, TokenClass: Any) -> Any: ...
    def scan_tag(self) -> Any: ...
    def scan_block_scalar(self, style: Any, rt: Optional[bool] = ...) -> Any: ...
    def scan_block_scalar_indicators(self, start_mark: Any) -> Any: ...
    def scan_block_scalar_ignored_line(self, start_mark: Any) -> Any: ...
    def scan_block_scalar_indentation(self) -> Any: ...
    def scan_block_scalar_breaks(self, indent: int) -> Any: ...
    def scan_flow_scalar(self, style: Any) -> Any: ...

    ESCAPE_REPLACEMENTS = ...
    ESCAPE_CODES = ...
    def scan_flow_scalar_non_spaces(self, double: Any, start_mark: Any) -> Any: ...
    def scan_flow_scalar_spaces(self, double: Any, start_mark: Any) -> Any: ...
    def scan_flow_scalar_breaks(self, double: Any, start_mark: Any) -> Any: ...
    def scan_plain(self) -> Any: ...
    def scan_plain_spaces(self, indent: Any, start_mark: Any) -> Any: ...
    def scan_tag_handle(self, name: Any, start_mark: Any) -> Any: ...
    def scan_tag_uri(self, name: Any, start_mark: Any) -> Any: ...
    def scan_uri_escapes(self, name: Any, start_mark: Any) -> Any: ...
    def scan_line_break(self) -> Any: ...

class RoundTripScanner(Scanner):
    def check_token(self, *choices: Any) -> bool: ...
    def peek_token(self) -> Any: ...
    def get_token(self) -> Any: ...
    def fetch_comment(self, comment: Any) -> None: ...
    def scan_to_next_token(self) -> Any: ...
    def scan_line_break(self, empty_line: bool = ...) -> Text: ...
    def scan_block_scalar(self, style: Any, rt: Optional[bool] = ...) -> Any: ...
    def scan_uri_escapes(self, name: Any, start_mark: Any) -> Any:
        """
        The roundtripscanner doesn't do URI escaping
        """
        ...

VALUECMNT = ...
KEYCMNT = ...

class CommentBase:
    __slots__ = ...
    def __init__(self, value: Any, line: Any, column: Any) -> None: ...
    def set_used(self, v: Any = ...) -> None: ...
    def set_assigned(self) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def info(self) -> str: ...

class EOLComment(CommentBase):
    name = ...
    def __init__(self, value: Any, line: Any, column: Any) -> None: ...

class FullLineComment(CommentBase):
    name = ...
    def __init__(self, value: Any, line: Any, column: Any) -> None: ...

class BlankLineComment(CommentBase):
    name = ...
    def __init__(self, value: Any, line: Any, column: Any) -> None: ...

class ScannedComments:
    def __init__(self: Any) -> None: ...
    def add_eol_comment(self, comment: Any, column: Any, line: Any) -> Any: ...
    def add_blank_line(self, comment: Any, column: Any, line: Any) -> Any: ...
    def add_full_line_comment(self, comment: Any, column: Any, line: Any) -> Any: ...
    def __getitem__(self, idx: Any) -> Any: ...
    def __str__(self) -> Any: ...
    def last(self) -> str: ...
    def any_unprocessed(self) -> bool: ...
    def unprocessed(self, use: Any = ...) -> Any: ...
    def assign_pre(self, token: Any) -> Any: ...
    def assign_eol(self, tokens: Any) -> Any: ...
    def assign_post(self, token: Any) -> Any: ...
    def str_unprocessed(self) -> Any: ...

class RoundTripScannerSC(Scanner):
    def __init__(self, *arg: Any, **kw: Any) -> None: ...
    def get_token(self) -> Any: ...
    def need_more_tokens(self) -> bool: ...
    def scan_to_next_token(self) -> None: ...
    def scan_empty_or_full_line_comments(self) -> None: ...
    def scan_block_scalar_ignored_line(self, start_mark: Any) -> Any: ...
