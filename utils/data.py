"""Utilities for loading data."""

from typing import Any

from utils.importer import MOVIES, NAME_EXCEPTION_DICT


SUBDIR = "file_imports/"


def add_crew(model_name: object, crew_members: Any) -> list:
    """Get or create new crew members in database.

    Args:
      model_name:
        The name of the crew member model class to get or
        create.
      crew_members:
        A string or list parsed from the imported YAML
        movies file.

    Returns:
        List of crew members stored as dicts.
    """
    if crew_members is None:
        return None
    else:
        if isinstance(crew_members, str):
            crew_members = [crew_members]

        crew_list = []

        for name in crew_members:
            if name in NAME_EXCEPTION_DICT.keys():
                crew_member = NAME_EXCEPTION_DICT[name]
            else:
                crew_member = parse_name(full_name=name)
            crew_list.append(crew_member)

            model_name.objects.get_or_create(**crew_member)

        return crew_list


def get_crew_objects(model_name: object, crew_members: list) -> list:
    """Retrieves crew member objects from the database.

    Args:
      model_name:
        The name of crew model class being queried in the database.
      crew_members:
        List of dicts containing the crew member(s) names returned by
        the add_crew function.

    Returns:
        List of retrieved crew member objects.
    """
    crew_list = []

    for member in crew_members:
        crew_member = model_name.objects.get(
            first_name=member["first_name"],
            middle_name=member["middle_name"],
            last_name=member["last_name"],
        )
        crew_list.append(crew_member)

    return crew_list


def parse_name(full_name: str) -> dict:
    """Parses full name and returns a dict.

    Args:
      full_name:
        String of the crew member's full name.

    Returns:
        The first, middle, and last names of the crew member as a dict.
    """
    name_list = full_name.split(" ")
    first_name = name_list[0]
    if len(name_list) == 1:
        middle_name = ""
        last_name = ""
    elif len(name_list) == 2:
        middle_name = ""
        last_name = name_list[1]
    elif len(name_list) == 3:
        middle_name = name_list[1]
        last_name = name_list[2]
    name = {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
    }

    return name
