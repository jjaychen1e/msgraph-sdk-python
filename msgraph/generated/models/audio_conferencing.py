from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AudioConferencing(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The conference id of the online meeting.
    conference_id: Optional[str] = None
    # A URL to the externally-accessible web page that contains dial-in information.
    dialin_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tollFreeNumber property
    toll_free_number: Optional[str] = None
    # List of toll-free numbers that are displayed in the meeting invite.
    toll_free_numbers: Optional[List[str]] = None
    # The tollNumber property
    toll_number: Optional[str] = None
    # List of toll numbers that are displayed in the meeting invite.
    toll_numbers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AudioConferencing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudioConferencing
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AudioConferencing()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "conferenceId": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "dialinUrl": lambda n : setattr(self, 'dialin_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tollFreeNumber": lambda n : setattr(self, 'toll_free_number', n.get_str_value()),
            "tollFreeNumbers": lambda n : setattr(self, 'toll_free_numbers', n.get_collection_of_primitive_values(str)),
            "tollNumber": lambda n : setattr(self, 'toll_number', n.get_str_value()),
            "tollNumbers": lambda n : setattr(self, 'toll_numbers', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_str_value("dialinUrl", self.dialin_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tollFreeNumber", self.toll_free_number)
        writer.write_collection_of_primitive_values("tollFreeNumbers", self.toll_free_numbers)
        writer.write_str_value("tollNumber", self.toll_number)
        writer.write_collection_of_primitive_values("tollNumbers", self.toll_numbers)
        writer.write_additional_data_value(self.additional_data)
    

