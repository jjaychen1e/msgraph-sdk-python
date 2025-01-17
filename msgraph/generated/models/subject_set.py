from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_rule_members import AttributeRuleMembers
    from .connected_organization_members import ConnectedOrganizationMembers
    from .external_sponsors import ExternalSponsors
    from .group_members import GroupMembers
    from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
    from .internal_sponsors import InternalSponsors
    from .requestor_manager import RequestorManager
    from .single_service_principal import SingleServicePrincipal
    from .single_user import SingleUser
    from .target_application_owners import TargetApplicationOwners
    from .target_manager import TargetManager

@dataclass
class SubjectSet(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectSet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeRuleMembers".casefold():
            from .attribute_rule_members import AttributeRuleMembers

            return AttributeRuleMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectedOrganizationMembers".casefold():
            from .connected_organization_members import ConnectedOrganizationMembers

            return ConnectedOrganizationMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalSponsors".casefold():
            from .external_sponsors import ExternalSponsors

            return ExternalSponsors()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupMembers".casefold():
            from .group_members import GroupMembers

            return GroupMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.ruleBasedSubjectSet".casefold():
            from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet

            return RuleBasedSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalSponsors".casefold():
            from .internal_sponsors import InternalSponsors

            return InternalSponsors()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.requestorManager".casefold():
            from .requestor_manager import RequestorManager

            return RequestorManager()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleServicePrincipal".casefold():
            from .single_service_principal import SingleServicePrincipal

            return SingleServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleUser".casefold():
            from .single_user import SingleUser

            return SingleUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetApplicationOwners".casefold():
            from .target_application_owners import TargetApplicationOwners

            return TargetApplicationOwners()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetManager".casefold():
            from .target_manager import TargetManager

            return TargetManager()
        return SubjectSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_rule_members import AttributeRuleMembers
        from .connected_organization_members import ConnectedOrganizationMembers
        from .external_sponsors import ExternalSponsors
        from .group_members import GroupMembers
        from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
        from .internal_sponsors import InternalSponsors
        from .requestor_manager import RequestorManager
        from .single_service_principal import SingleServicePrincipal
        from .single_user import SingleUser
        from .target_application_owners import TargetApplicationOwners
        from .target_manager import TargetManager

        from .attribute_rule_members import AttributeRuleMembers
        from .connected_organization_members import ConnectedOrganizationMembers
        from .external_sponsors import ExternalSponsors
        from .group_members import GroupMembers
        from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
        from .internal_sponsors import InternalSponsors
        from .requestor_manager import RequestorManager
        from .single_service_principal import SingleServicePrincipal
        from .single_user import SingleUser
        from .target_application_owners import TargetApplicationOwners
        from .target_manager import TargetManager

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

