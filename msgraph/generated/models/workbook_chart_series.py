from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_point import WorkbookChartPoint
    from .workbook_chart_series_format import WorkbookChartSeriesFormat

from .entity import Entity

@dataclass
class WorkbookChartSeries(Entity):
    # Represents the formatting of a chart series, which includes fill and line formatting. Read-only.
    format: Optional[WorkbookChartSeriesFormat] = None
    # Represents the name of a series in a chart.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a collection of all points in the series. Read-only.
    points: Optional[List[WorkbookChartPoint]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartSeries:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartSeries
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartSeries()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_point import WorkbookChartPoint
        from .workbook_chart_series_format import WorkbookChartSeriesFormat

        from .entity import Entity
        from .workbook_chart_point import WorkbookChartPoint
        from .workbook_chart_series_format import WorkbookChartSeriesFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartSeriesFormat)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(WorkbookChartPoint)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("format", self.format)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("points", self.points)
    

