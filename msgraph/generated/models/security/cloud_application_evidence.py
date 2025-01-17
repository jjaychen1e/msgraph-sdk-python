from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class CloudApplicationEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.cloudApplicationEvidence"
    # Unique identifier of the application.
    app_id: Optional[int] = None
    # Name of the application.
    display_name: Optional[str] = None
    # Identifier of the instance of the Software as a Service (SaaS) application.
    instance_id: Optional[int] = None
    # Name of the instance of the SaaS application.
    instance_name: Optional[str] = None
    # The identifier of the SaaS application.
    saas_app_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudApplicationEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudApplicationEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudApplicationEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "instanceId": lambda n : setattr(self, 'instance_id', n.get_int_value()),
            "instanceName": lambda n : setattr(self, 'instance_name', n.get_str_value()),
            "saasAppId": lambda n : setattr(self, 'saas_app_id', n.get_int_value()),
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
        writer.write_int_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("instanceId", self.instance_id)
        writer.write_str_value("instanceName", self.instance_name)
        writer.write_int_value("saasAppId", self.saas_app_id)
    

