from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class RegistryKeyEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.registryKeyEvidence"
    # Registry hive of the key that the recorded action was applied to.
    registry_hive: Optional[str] = None
    # Registry key that the recorded action was applied to.
    registry_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegistryKeyEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegistryKeyEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RegistryKeyEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "registryHive": lambda n : setattr(self, 'registry_hive', n.get_str_value()),
            "registryKey": lambda n : setattr(self, 'registry_key', n.get_str_value()),
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
        writer.write_str_value("registryHive", self.registry_hive)
        writer.write_str_value("registryKey", self.registry_key)
    

