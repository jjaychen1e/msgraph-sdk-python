from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .learning_course_activity import LearningCourseActivity

from .learning_course_activity import LearningCourseActivity

@dataclass
class LearningSelfInitiatedCourse(LearningCourseActivity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The date time value on which the self-initiated course was started by the learner. Optional.
    started_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LearningSelfInitiatedCourse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LearningSelfInitiatedCourse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LearningSelfInitiatedCourse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .learning_course_activity import LearningCourseActivity

        from .learning_course_activity import LearningCourseActivity

        fields: Dict[str, Callable[[Any], None]] = {
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("startedDateTime", self.started_date_time)
    

