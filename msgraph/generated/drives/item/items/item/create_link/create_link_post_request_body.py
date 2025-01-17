from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CreateLinkPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The message property
    message: Optional[str] = None
    # The password property
    password: Optional[str] = None
    # The retainInheritedPermissions property
    retain_inherited_permissions: Optional[bool] = None
    # The scope property
    scope: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateLinkPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateLinkPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CreateLinkPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "retainInheritedPermissions": lambda n : setattr(self, 'retain_inherited_permissions', n.get_bool_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("message", self.message)
        writer.write_str_value("password", self.password)
        writer.write_bool_value("retainInheritedPermissions", self.retain_inherited_permissions)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

