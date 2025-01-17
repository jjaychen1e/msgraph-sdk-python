from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bucket_aggregation_definition import BucketAggregationDefinition

@dataclass
class AggregationOption(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The bucketDefinition property
    bucket_definition: Optional[BucketAggregationDefinition] = None
    # Computes aggregation on the field while the field exists in current entity type. Required.
    field: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of searchBucket resources to be returned. This is not required when the range is provided manually in the search request. Optional.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AggregationOption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AggregationOption
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AggregationOption()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .bucket_aggregation_definition import BucketAggregationDefinition

        from .bucket_aggregation_definition import BucketAggregationDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "bucketDefinition": lambda n : setattr(self, 'bucket_definition', n.get_object_value(BucketAggregationDefinition)),
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("bucketDefinition", self.bucket_definition)
        writer.write_str_value("field", self.field)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    

