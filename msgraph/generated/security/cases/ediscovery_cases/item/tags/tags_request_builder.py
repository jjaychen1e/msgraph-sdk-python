from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.o_data_errors import o_data_error
    from ......models.security import ediscovery_review_tag, ediscovery_review_tag_collection_response
    from .count import count_request_builder
    from .item import ediscovery_review_tag_item_request_builder
    from .microsoft_graph_security_as_hierarchy import microsoft_graph_security_as_hierarchy_request_builder

class TagsRequestBuilder():
    """
    Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TagsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/tags{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_ediscovery_review_tag_id(self,ediscovery_review_tag_id: str) -> ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            ediscovery_review_tag_id: Unique identifier of the item
        Returns: ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder
        """
        if ediscovery_review_tag_id is None:
            raise Exception("ediscovery_review_tag_id cannot be undefined")
        from .item import ediscovery_review_tag_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryReviewTag%2Did"] = ediscovery_review_tag_id
        return ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[TagsRequestBuilderGetRequestConfiguration] = None) -> Optional[ediscovery_review_tag_collection_response.EdiscoveryReviewTagCollectionResponse]:
        """
        Returns a list of ediscoveryReviewTag objects associated to this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_review_tag_collection_response.EdiscoveryReviewTagCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.security import ediscovery_review_tag_collection_response

        return await self.request_adapter.send_async(request_info, ediscovery_review_tag_collection_response.EdiscoveryReviewTagCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[ediscovery_review_tag.EdiscoveryReviewTag] = None, request_configuration: Optional[TagsRequestBuilderPostRequestConfiguration] = None) -> Optional[ediscovery_review_tag.EdiscoveryReviewTag]:
        """
        Create new navigation property to tags for security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_review_tag.EdiscoveryReviewTag]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.security import ediscovery_review_tag

        return await self.request_adapter.send_async(request_info, ediscovery_review_tag.EdiscoveryReviewTag, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TagsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of ediscoveryReviewTag objects associated to this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_post_request_information(self,body: Optional[ediscovery_review_tag.EdiscoveryReviewTag] = None, request_configuration: Optional[TagsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to tags for security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_as_hierarchy(self) -> microsoft_graph_security_as_hierarchy_request_builder.MicrosoftGraphSecurityAsHierarchyRequestBuilder:
        """
        Provides operations to call the asHierarchy method.
        """
        from .microsoft_graph_security_as_hierarchy import microsoft_graph_security_as_hierarchy_request_builder

        return microsoft_graph_security_as_hierarchy_request_builder.MicrosoftGraphSecurityAsHierarchyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TagsRequestBuilderGetQueryParameters():
        """
        Returns a list of ediscoveryReviewTag objects associated to this case.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class TagsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TagsRequestBuilder.TagsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TagsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

