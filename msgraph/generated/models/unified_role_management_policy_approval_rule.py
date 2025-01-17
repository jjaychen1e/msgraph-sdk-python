from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_settings import ApprovalSettings
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

@dataclass
class UnifiedRoleManagementPolicyApprovalRule(UnifiedRoleManagementPolicyRule):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"
    # The settings for approval of the role assignment.
    setting: Optional[ApprovalSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyApprovalRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyApprovalRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyApprovalRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .approval_settings import ApprovalSettings
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        from .approval_settings import ApprovalSettings
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        fields: Dict[str, Callable[[Any], None]] = {
            "setting": lambda n : setattr(self, 'setting', n.get_object_value(ApprovalSettings)),
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
        writer.write_object_value("setting", self.setting)
    

