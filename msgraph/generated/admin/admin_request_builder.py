from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.o_data_errors.o_data_error import ODataError
    from .edge.edge_request_builder import EdgeRequestBuilder
    from .service_announcement.service_announcement_request_builder import ServiceAnnouncementRequestBuilder
    from .sharepoint.sharepoint_request_builder import SharepointRequestBuilder

class AdminRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AdminRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/admin{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[AdminRequestBuilderGetRequestConfiguration] = None) -> Optional[Admin]:
        """
        Get admin
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Admin]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.admin import Admin

        return await self.request_adapter.send_async(request_info, Admin, error_mapping)
    
    async def patch(self,body: Optional[Admin] = None, request_configuration: Optional[AdminRequestBuilderPatchRequestConfiguration] = None) -> Optional[Admin]:
        """
        Update admin
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Admin]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.admin import Admin

        return await self.request_adapter.send_async(request_info, Admin, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AdminRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get admin
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[Admin] = None, request_configuration: Optional[AdminRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update admin
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def edge(self) -> EdgeRequestBuilder:
        """
        Provides operations to manage the edge property of the microsoft.graph.admin entity.
        """
        from .edge.edge_request_builder import EdgeRequestBuilder

        return EdgeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_announcement(self) -> ServiceAnnouncementRequestBuilder:
        """
        Provides operations to manage the serviceAnnouncement property of the microsoft.graph.admin entity.
        """
        from .service_announcement.service_announcement_request_builder import ServiceAnnouncementRequestBuilder

        return ServiceAnnouncementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sharepoint(self) -> SharepointRequestBuilder:
        """
        Provides operations to manage the sharepoint property of the microsoft.graph.admin entity.
        """
        from .sharepoint.sharepoint_request_builder import SharepointRequestBuilder

        return SharepointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AdminRequestBuilderGetQueryParameters():
        """
        Get admin
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AdminRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AdminRequestBuilder.AdminRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AdminRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

