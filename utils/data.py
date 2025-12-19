"""Utilities for loading data."""

from typing import Any

from movies.models import MPAARatingsReason
from utils.importer import MOVIES, NAME_EXCEPTION_DICT


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
        List of crew members stored as dicts or None.
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


def add_rating_reasons(reasons: Any, model: object=MPAARatingsReason) -> list:
    """Get or create MPAA ratings reasons in database.

    Args:
      reasons:
        The reason(s) stated for the designated MPAA rating.
      model:
        The MPAA Ratings Reason model class.

    Returns:
        List of rating reasons or None.
    """
    if reasons is None:
        return None
    else:
        if isinstance(reasons, str):
            reasons = [reasons]

        reason_list = []

        for reason in reasons:
            reason_list.append(reason)
            model.objects.get_or_create(reason=reason)

        return reason_list


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


def get_rating_reason(reasons: list, model: object=MPAARatingsReason) -> list:
    """Retrieves MPAA rating reason objects from the database.

    Args:
      reasons:
        The list of reasons being queried in the database.
      model:
        The MPAA Ratings Reason model class.

    Returns:
      List of retrieved ratings reasons.
    """
    reason_list = []

    for reason in reasons:
        mpaa_reason = model.objects.get(reason=reason)
        reason_list.append(mpaa_reason)

    return reason_list


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
