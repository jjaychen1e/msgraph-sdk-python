from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .ios_managed_app_protection import IosManagedAppProtection
    from .managed_app_protection import ManagedAppProtection
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

from .managed_app_protection import ManagedAppProtection

@dataclass
class TargetedManagedAppProtection(ManagedAppProtection):
    """
    Policy used to configure detailed management settings targeted to specific security groups
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.targetedManagedAppProtection"
    # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
    assignments: Optional[List[TargetedManagedAppPolicyAssignment]] = None
    # Indicates if the policy is deployed to any inclusion groups or not.
    is_assigned: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TargetedManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TargetedManagedAppProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from .android_managed_app_protection import AndroidManagedAppProtection

            return AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from .ios_managed_app_protection import IosManagedAppProtection

            return IosManagedAppProtection()
        return TargetedManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_protection import ManagedAppProtection
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

        from .android_managed_app_protection import AndroidManagedAppProtection
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_protection import ManagedAppProtection
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TargetedManagedAppPolicyAssignment)),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_bool_value("isAssigned", self.is_assigned)
    

