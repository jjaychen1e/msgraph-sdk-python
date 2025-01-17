from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

from .entity import Entity

@dataclass
class PlannerAssignedToTaskBoardTaskFormat(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Dictionary of hints used to order tasks on the AssignedTo view of the Task Board. The key of each entry is one of the users the task is assigned to and the value is the order hint. The format of each value is defined as outlined here.
    order_hints_by_assignee: Optional[PlannerOrderHintsByAssignee] = None
    # Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.
    unassigned_order_hint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerAssignedToTaskBoardTaskFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerAssignedToTaskBoardTaskFormat
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerAssignedToTaskBoardTaskFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

        from .entity import Entity
        from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

        fields: Dict[str, Callable[[Any], None]] = {
            "orderHintsByAssignee": lambda n : setattr(self, 'order_hints_by_assignee', n.get_object_value(PlannerOrderHintsByAssignee)),
            "unassignedOrderHint": lambda n : setattr(self, 'unassigned_order_hint', n.get_str_value()),
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
        writer.write_object_value("orderHintsByAssignee", self.order_hints_by_assignee)
        writer.write_str_value("unassignedOrderHint", self.unassigned_order_hint)
    

