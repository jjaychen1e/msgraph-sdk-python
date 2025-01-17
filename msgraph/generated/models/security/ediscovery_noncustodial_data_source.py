from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_source import DataSource
    from .data_source_container import DataSourceContainer
    from .ediscovery_index_operation import EdiscoveryIndexOperation

from .data_source_container import DataSourceContainer

@dataclass
class EdiscoveryNoncustodialDataSource(DataSourceContainer):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryNoncustodialDataSource"
    # User source or SharePoint site data source as non-custodial data source.
    data_source: Optional[DataSource] = None
    # Operation entity that represents the latest indexing for the non-custodial data source.
    last_index_operation: Optional[EdiscoveryIndexOperation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryNoncustodialDataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryNoncustodialDataSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryNoncustodialDataSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .data_source import DataSource
        from .data_source_container import DataSourceContainer
        from .ediscovery_index_operation import EdiscoveryIndexOperation

        from .data_source import DataSource
        from .data_source_container import DataSourceContainer
        from .ediscovery_index_operation import EdiscoveryIndexOperation

        fields: Dict[str, Callable[[Any], None]] = {
            "dataSource": lambda n : setattr(self, 'data_source', n.get_object_value(DataSource)),
            "lastIndexOperation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(EdiscoveryIndexOperation)),
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
        writer.write_object_value("dataSource", self.data_source)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
    

