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
    from ........models.identity_governance.workflow_version import WorkflowVersion
    from ........models.o_data_errors.o_data_error import ODataError
    from .created_by.created_by_request_builder import CreatedByRequestBuilder
    from .last_modified_by.last_modified_by_request_builder import LastModifiedByRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder

class WorkflowVersionVersionNumberItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the versions property of the microsoft.graph.identityGovernance.workflow entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkflowVersionVersionNumberItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/versions/{workflowVersion%2DversionNumber}{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[WorkflowVersionVersionNumberItemRequestBuilderGetRequestConfiguration] = None) -> Optional[WorkflowVersion]:
        """
        Read the properties and relationships of a workflowVersion object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkflowVersion]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.identity_governance.workflow_version import WorkflowVersion

        return await self.request_adapter.send_async(request_info, WorkflowVersion, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[WorkflowVersionVersionNumberItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a workflowVersion object.
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
    
    @property
    def created_by(self) -> CreatedByRequestBuilder:
        """
        Provides operations to manage the createdBy property of the microsoft.graph.identityGovernance.workflowBase entity.
        """
        from .created_by.created_by_request_builder import CreatedByRequestBuilder

        return CreatedByRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by(self) -> LastModifiedByRequestBuilder:
        """
        Provides operations to manage the lastModifiedBy property of the microsoft.graph.identityGovernance.workflowBase entity.
        """
        from .last_modified_by.last_modified_by_request_builder import LastModifiedByRequestBuilder

        return LastModifiedByRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.identityGovernance.workflowBase entity.
        """
        from .tasks.tasks_request_builder import TasksRequestBuilder

        return TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkflowVersionVersionNumberItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a workflowVersion object.
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
    class WorkflowVersionVersionNumberItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WorkflowVersionVersionNumberItemRequestBuilder.WorkflowVersionVersionNumberItemRequestBuilderGetQueryParameters] = None

    

