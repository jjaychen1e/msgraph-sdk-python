from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .request_schedule import RequestSchedule
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
    from .unified_role_schedule_base import UnifiedRoleScheduleBase

from .unified_role_schedule_base import UnifiedRoleScheduleBase

@dataclass
class UnifiedRoleAssignmentSchedule(UnifiedRoleScheduleBase):
    # If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
    activated_using: Optional[UnifiedRoleEligibilitySchedule] = None
    # Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
    assignment_type: Optional[str] = None
    # How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The period of the role assignment. It can represent a single occurrence or multiple recurrences.
    schedule_info: Optional[RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleAssignmentSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentSchedule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignmentSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .request_schedule import RequestSchedule
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        from .request_schedule import RequestSchedule
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        fields: Dict[str, Callable[[Any], None]] = {
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(UnifiedRoleEligibilitySchedule)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
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
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_str_value("assignmentType", self.assignment_type)
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

