from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ref.ref_request_builder import RefRequestBuilder

class AccessPackageItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /identityGovernance/entitlementManagement/accessPackages/{accessPackage-id}/incompatibleAccessPackages/{accessPackage-id1}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}/incompatibleAccessPackages/{accessPackage%2Did1}", path_parameters)
    
    @property
    def ref(self) -> RefRequestBuilder:
        """
        Provides operations to manage the collection of identityGovernance entities.
        """
        from .ref.ref_request_builder import RefRequestBuilder

        return RefRequestBuilder(self.request_adapter, self.path_parameters)
    

