from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_home_screen_folder_page import IosHomeScreenFolderPage
    from .ios_home_screen_item import IosHomeScreenItem

from .ios_home_screen_item import IosHomeScreenItem

@dataclass
class IosHomeScreenFolder(IosHomeScreenItem):
    """
    A folder containing pages of apps and web clips on the Home Screen.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosHomeScreenFolder"
    # Pages of Home Screen Layout Icons which must be applications or web clips. This collection can contain a maximum of 500 elements.
    pages: Optional[List[IosHomeScreenFolderPage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosHomeScreenFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosHomeScreenFolder
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosHomeScreenFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_home_screen_folder_page import IosHomeScreenFolderPage
        from .ios_home_screen_item import IosHomeScreenItem

        from .ios_home_screen_folder_page import IosHomeScreenFolderPage
        from .ios_home_screen_item import IosHomeScreenItem

        fields: Dict[str, Callable[[Any], None]] = {
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(IosHomeScreenFolderPage)),
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
        writer.write_collection_of_object_values("pages", self.pages)
    

