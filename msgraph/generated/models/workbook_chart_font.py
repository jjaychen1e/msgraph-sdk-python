from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class WorkbookChartFont(Entity):
    # Represents the bold status of font.
    bold: Optional[bool] = None
    # HTML color code representation of the text color. E.g. #FF0000 represents Red.
    color: Optional[str] = None
    # Represents the italic status of the font.
    italic: Optional[bool] = None
    # Font name (e.g. 'Calibri')
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Size of the font (e.g. 11)
    size: Optional[float] = None
    # Type of underline applied to the font. The possible values are: None, Single.
    underline: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartFont:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartFont
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartFont()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "bold": lambda n : setattr(self, 'bold', n.get_bool_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "italic": lambda n : setattr(self, 'italic', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_float_value()),
            "underline": lambda n : setattr(self, 'underline', n.get_str_value()),
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
        writer.write_bool_value("bold", self.bold)
        writer.write_str_value("color", self.color)
        writer.write_bool_value("italic", self.italic)
        writer.write_str_value("name", self.name)
        writer.write_float_value("size", self.size)
        writer.write_str_value("underline", self.underline)
    

