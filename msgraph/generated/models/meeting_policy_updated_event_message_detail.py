from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet

from .event_message_detail import EventMessageDetail

@dataclass
class MeetingPolicyUpdatedEventMessageDetail(EventMessageDetail):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.meetingPolicyUpdatedEventMessageDetail"
    # Initiator of the event.
    initiator: Optional[IdentitySet] = None
    # Represents whether the meeting chat is enabled or not.
    meeting_chat_enabled: Optional[bool] = None
    # Unique identifier of the meeting chat.
    meeting_chat_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingPolicyUpdatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingPolicyUpdatedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MeetingPolicyUpdatedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
            "meetingChatEnabled": lambda n : setattr(self, 'meeting_chat_enabled', n.get_bool_value()),
            "meetingChatId": lambda n : setattr(self, 'meeting_chat_id', n.get_str_value()),
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
        writer.write_object_value("initiator", self.initiator)
        writer.write_bool_value("meetingChatEnabled", self.meeting_chat_enabled)
        writer.write_str_value("meetingChatId", self.meeting_chat_id)
    

