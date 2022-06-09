def find_all_related_id(game, event_id: str):
    """Find all related id by given event id.

    It seems that StatsBomb already did a good job on marking related events.
    It is to be validated the result of this function could be the same for a group of related events.
    However, currently this function works well.  

    Args:
        game (DataFrame): the full events data
        event_id (str): the event uuid

    Returns:
        id_merged (set): A set all related event id
    """
    related_actions_df = game[~game["related_events"].isna()]
    is_in_related = related_actions_df["related_events"].apply(lambda x: event_id in x)
    filtered_action_df = related_actions_df[is_in_related]
    related_id = set(filtered_action_df["id"].unique())
    related_related_id = set(filtered_action_df["related_events"].explode().unique())
    id_merged = related_id.union(related_related_id)
    return id_merged