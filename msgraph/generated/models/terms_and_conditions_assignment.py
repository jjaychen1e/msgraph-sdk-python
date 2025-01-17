from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
    from .entity import Entity

from .entity import Entity

@dataclass
class TermsAndConditionsAssignment(Entity):
    """
    A termsAndConditionsAssignment entity represents the assignment of a given Terms and Conditions (T&C) policy to a given group. Users in the group will be required to accept the terms in order to have devices enrolled into Intune.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Assignment target that the T&C policy is assigned to.
    target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TermsAndConditionsAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditionsAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TermsAndConditionsAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_object_value("target", self.target)
    

