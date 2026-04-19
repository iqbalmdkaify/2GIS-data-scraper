from dataclasses import dataclass
from typing import List, Literal, TypeAlias

StrOrNull: TypeAlias = str | Literal["null"]
DataList: TypeAlias = List[StrOrNull]


@dataclass
class ColumnData:
    title: DataList
    type: DataList
    address: DataList
    rating: DataList
