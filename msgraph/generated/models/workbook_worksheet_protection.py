from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

from .entity import Entity

@dataclass
class WorkbookWorksheetProtection(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Sheet protection options. Read-only.
    options: Optional[WorkbookWorksheetProtectionOptions] = None
    # Indicates if the worksheet is protected.  Read-only.
    protected: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookWorksheetProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheetProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookWorksheetProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

        from .entity import Entity
        from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "options": lambda n : setattr(self, 'options', n.get_object_value(WorkbookWorksheetProtectionOptions)),
            "protected": lambda n : setattr(self, 'protected', n.get_bool_value()),
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
        writer.write_object_value("options", self.options)
        writer.write_bool_value("protected", self.protected)
    

