from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from .service_principal_risk_detection import ServicePrincipalRiskDetection

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class ServicePrincipalRiskDetectionCollectionResponse(BaseCollectionPaginationCountResponse):
    # The value property
    value: Optional[List[ServicePrincipalRiskDetection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalRiskDetectionCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalRiskDetectionCollectionResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalRiskDetectionCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .service_principal_risk_detection import ServicePrincipalRiskDetection

        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .service_principal_risk_detection import ServicePrincipalRiskDetection

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(ServicePrincipalRiskDetection)),
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
        writer.write_collection_of_object_values("value", self.value)
    

