from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teams_app import TeamsApp
    from .teams_app_definition import TeamsAppDefinition
    from .teams_app_permission_set import TeamsAppPermissionSet
    from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

from .entity import Entity

@dataclass
class TeamsAppInstallation(Entity):
    # The set of resource-specific permissions consented to while installing or upgrading the teamsApp.
    consented_permission_set: Optional[TeamsAppPermissionSet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The app that is installed.
    teams_app: Optional[TeamsApp] = None
    # The details of this version of the app.
    teams_app_definition: Optional[TeamsAppDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppInstallation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppInstallation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userScopeTeamsAppInstallation".casefold():
            from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

            return UserScopeTeamsAppInstallation()
        return TeamsAppInstallation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teams_app import TeamsApp
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_permission_set import TeamsAppPermissionSet
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

        from .entity import Entity
        from .teams_app import TeamsApp
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_permission_set import TeamsAppPermissionSet
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

        fields: Dict[str, Callable[[Any], None]] = {
            "consentedPermissionSet": lambda n : setattr(self, 'consented_permission_set', n.get_object_value(TeamsAppPermissionSet)),
            "teamsApp": lambda n : setattr(self, 'teams_app', n.get_object_value(TeamsApp)),
            "teamsAppDefinition": lambda n : setattr(self, 'teams_app_definition', n.get_object_value(TeamsAppDefinition)),
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
        writer.write_object_value("consentedPermissionSet", self.consented_permission_set)
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_object_value("teamsAppDefinition", self.teams_app_definition)
    

