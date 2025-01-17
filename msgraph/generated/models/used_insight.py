from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .resource_reference import ResourceReference
    from .resource_visualization import ResourceVisualization
    from .usage_details import UsageDetails

from .entity import Entity

@dataclass
class UsedInsight(Entity):
    # Information about when the item was last viewed or modified by the user. Read only.
    last_used: Optional[UsageDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Used for navigating to the item that was used. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
    resource: Optional[Entity] = None
    # Reference properties of the used document, such as the url and type of the document. Read-only
    resource_reference: Optional[ResourceReference] = None
    # Properties that you can use to visualize the document in your experience. Read-only
    resource_visualization: Optional[ResourceVisualization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UsedInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsedInsight
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UsedInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization
        from .usage_details import UsageDetails

        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization
        from .usage_details import UsageDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "lastUsed": lambda n : setattr(self, 'last_used', n.get_object_value(UsageDetails)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(Entity)),
            "resourceReference": lambda n : setattr(self, 'resource_reference', n.get_object_value(ResourceReference)),
            "resourceVisualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(ResourceVisualization)),
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
        writer.write_object_value("lastUsed", self.last_used)
        writer.write_object_value("resource", self.resource)
    

