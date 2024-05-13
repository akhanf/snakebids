import collections
from upath import UPath as Path
from upath import UPath as Path
from upath.implementations.local import PosixUPath, WindowsUPath, FilePath

from typing import Any, OrderedDict

from ruamel.yaml import YAML, Dumper


def get_yaml_io():
    """Return yaml loader/dumper configured for snakebids."""
    yaml = YAML()

    # Represent any PathLikes as str.
    def path2str(dumper: Dumper, data: Path):
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str",
            str(data),
        )

    def to_dict(dumper: Dumper, data: OrderedDict[Any, Any]):
        return dumper.represent_dict(dict(data))

    yaml.representer.add_representer(Path, path2str)
    yaml.representer.add_representer(FilePath, path2str)
    yaml.representer.add_representer(PosixUPath, path2str)
    yaml.representer.add_representer(WindowsUPath, path2str)
    yaml.representer.add_representer(collections.OrderedDict, to_dict)
    yaml.representer.add_representer(OrderedDict, to_dict)
    return yaml
