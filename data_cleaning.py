import os
import pandas as pd
import json
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
OPEN_DATA_PATH = os.getenv("OPEN_DATA_PATH")

def load_game_df(data_type:str, game_id:int):
    """Load Statsbomb events or 360 data by given type and game game id. 

    Args:
        data_type (str): "events" or "three-sixty" 
        game_id (int): Specific game id. Available game id can be found in open-data/competion_info.csv

    Returns:
        game_df (DataFrame): normalised DataFrame of events / 360 data
    """
    try:
        path = OPEN_DATA_PATH + data_type +"/{}.json".format(game_id)
        with open(path) as f:
            game = json.load(f)
    except NameError:
        print("Cannot find the given data file. Check the game id and try again.")
    game_df = pd.json_normalize(game, sep="_")
    return game_df

def generate_location(game_df, location_col_name: str):
    """Expand Location column ([x, y]) into 2 columns of normalised events data

    Args:
        game_df (DataFrame): Normalised events DataFrame
        location_col_name (str): location, pass_end_location, or carry_end_location

    Returns:
        location (DataFrame): Events DataFrame with expanded location
    """
    location_list = game_df[location_col_name].to_list()
    location_list = location_list = [[None, None] if type(x)!=list  else x for x in location_list]
    location = pd.DataFrame(location_list, columns=[location_col_name + "_x", location_col_name + "_y"])
    location = pd.concat([game_df, location], axis = 1)
    #location = location.dropna(thresh=5)
    location = location.drop(location_col_name, axis= 1)
    return location

def expand_dict(game_df, col_name: str):
    values = [None if type(x) == float else x[0] for x in game_df[col_name].to_list()]
    values_df = pd.json_normalize(values, sep="_").add_prefix(col_name+"_").reset_index()
    return values_df


