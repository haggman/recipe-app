import streamlit as st

#
# Template code to use Discovery Engine API to call the Search app
#

project_id = "YOUR_PROJECT_ID"
location = "global"
engine_id = "recipe-data-id" # Edit if your data store ID is different

from typing import List

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from typing import List
import ast


def search_sample(
    project_id: str,
    location: str,
    data_store_id: str,
    search_query: str,
) -> List[discoveryengine.SearchResponse]:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # The full resource name of the search engine serving config
    # e.g. projects/{project_id}/locations/{location}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}
    serving_config = client.serving_config_path(
        project=project_id,
        location=location,
        data_store=data_store_id,
        serving_config="default_config",
    )

    # Optional: Configuration options for search
    # Refer to the `ContentSearchSpec` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        # For information about snippets, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/snippets
        snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet=True
        ),
        # For information about search summaries, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=5,
            include_citations=True,
            ignore_adversarial_query=True,
            ignore_non_summary_seeking_query=True,
        ),
    )

    # Refer to the `SearchRequest` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=5,
        content_search_spec=content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    response = client.search(request)
    return response.results

#
# End template code to use Discovery Engine API to call the Search app
#

st.set_page_config(page_title="AI Recipe Haven - AI Recipe Search", page_icon="🍲")

st.title("Your AI Source for Recipes")

query = st.text_input("What recipes would you like me to search for?", value="")

if query:
    st.write(f"Processing '{query}'...")
    st.write("Here are the first 5 recipes I found:")

    # results = search_sample(project_id, location, engine_id, query)

    # for result in results:
    #     st.header(result.document.struct_data["title"])

    #     st.subheader("Ingredients")
    #     i_list = ast.literal_eval(result.document.struct_data["ingredients"])
    #     for ingredient in i_list:
    #         st.markdown("- " + ingredient)

    #     st.subheader("Directions")
    #     d_list = ast.literal_eval(result.document.struct_data["directions"])
    #     for direction in d_list:
    #         if direction:
    #             st.markdown("- " + direction)   

    #     st.write(result.document.struct_data["uri"])
 