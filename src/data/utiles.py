from pathlib import Path
from src.data import dir_path
import json


def read_json (json_name):

    with open(dir_path/json_name) as J:
            return json.load(J)