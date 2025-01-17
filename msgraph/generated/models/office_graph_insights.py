from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .shared_insight import SharedInsight
    from .trending import Trending
    from .used_insight import UsedInsight

from .entity import Entity

@dataclass
class OfficeGraphInsights(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.
    shared: Optional[List[SharedInsight]] = None
    # Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.
    trending: Optional[List[Trending]] = None
    # Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.
    used: Optional[List[UsedInsight]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeGraphInsights:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OfficeGraphInsights
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OfficeGraphInsights()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .shared_insight import SharedInsight
        from .trending import Trending
        from .used_insight import UsedInsight

        from .entity import Entity
        from .shared_insight import SharedInsight
        from .trending import Trending
        from .used_insight import UsedInsight

        fields: Dict[str, Callable[[Any], None]] = {
            "shared": lambda n : setattr(self, 'shared', n.get_collection_of_object_values(SharedInsight)),
            "trending": lambda n : setattr(self, 'trending', n.get_collection_of_object_values(Trending)),
            "used": lambda n : setattr(self, 'used', n.get_collection_of_object_values(UsedInsight)),
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
        writer.write_collection_of_object_values("shared", self.shared)
        writer.write_collection_of_object_values("trending", self.trending)
        writer.write_collection_of_object_values("used", self.used)
    

