from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_set import DataSet
    from .ediscovery_review_set_query import EdiscoveryReviewSetQuery

from .data_set import DataSet

@dataclass
class EdiscoveryReviewSet(DataSet):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryReviewSet"
    # Represents queries within the review set.
    queries: Optional[List[EdiscoveryReviewSetQuery]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryReviewSet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryReviewSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .data_set import DataSet
        from .ediscovery_review_set_query import EdiscoveryReviewSetQuery

        from .data_set import DataSet
        from .ediscovery_review_set_query import EdiscoveryReviewSetQuery

        fields: Dict[str, Callable[[Any], None]] = {
            "queries": lambda n : setattr(self, 'queries', n.get_collection_of_object_values(EdiscoveryReviewSetQuery)),
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
        writer.write_collection_of_object_values("queries", self.queries)
    

