def build_search_query(city_name: str, query: str) -> str:
    SEARCH_QUERY_STRING: str = (
        f"https://2gis.ru/{city_name.lower()}/search/{query.title()}?m"
    )

    return SEARCH_QUERY_STRING
