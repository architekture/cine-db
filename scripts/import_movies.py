"""Import movies using django-extensions runscript feature."""

from movies.models import(
    AspectRatio,
    Cinematographer,
    Composer,
    Director,
    Discs,
    Editor,
    Movie,
    ProdDesigner,
    Publisher,
    RunTime,
    Writer,
    Year,
)
from utils.data import add_crew, load_yaml, set_crew_field


def run():
    movies = load_yaml()

    for mv, details in movies.items():
        # Set primary fields
        title = details["data"]["title"]
        slug = details["sort_key"]
        directors = add_crew(model_name=Director, crew_members=details["data"]["director"])

        # Set crew fields
        cinematographers = add_crew(model_name=Cinematographer, crew_members=details["data"]["crew"]["cinematographer"])
        composers = add_crew(model_name=Composer, crew_members=details["data"]["crew"]["composer"])
        editors = add_crew(model_name=Editor, crew_members=details["data"]["crew"]["editor"])
        try:
            prod_designers = add_crew(model_name=ProdDesigner, crew_members=details["data"]["crew"]["prod_designer"])
        except KeyError:
            prod_designers = None
        writers = add_crew(model_name=Writer, crew_members=details["data"]["crew"]["writer"])

        # Set tech spec fields
        aspect_ratio = float(details["data"]["release"]["aspect_ratio"])
        run_time = int(details["data"]["runtime"])
        year = int(details["data"]["year"])

        # Set release info fields
        discs = int(details["data"]["release"]["discs"])
        publisher = details["data"]["release"]["publisher"]

        AspectRatio.objects.get_or_create(aspect_ratio=aspect_ratio)
        Discs.objects.get_or_create(discs=discs)
        Publisher.objects.get_or_create(publisher=publisher)
        RunTime.objects.get_or_create(run_time=run_time)
        Year.objects.get_or_create(year=year)

        aspect_ratio = AspectRatio.objects.get(aspect_ratio=aspect_ratio)
        discs = Discs.objects.get(discs=discs)
        publisher = Publisher.objects.get(publisher=publisher)
        run_time = RunTime.objects.get(run_time=run_time)
        year = Year.objects.get(year=year)

        movie = {
            "title": title,
            "slug": slug,
            "aspect_ratio": aspect_ratio,
            "discs": discs,
            "publisher": publisher,
            "run_time": run_time,
            "year": year,
        }

        Movie.objects.get_or_create(**movie)
        try:
            movie = Movie.objects.get(slug=movie["slug"])
            directors = set_crew_field(model_name=Director, crew_members=directors)
            movie.director.set(directors)
            if cinematographers is not None:
                cinematographers = set_crew_field(model_name=Cinematographer, crew_members=cinematographers)
                movie.dp.set(cinematographers)
            if composers is not None:
                composers = set_crew_field(model_name=Composer, crew_members=composers)
                movie.composer.set(composers)
            if editors is not None:
                editors = set_crew_field(model_name=Editor, crew_members=editors)
                movie.editor.set(editors)
            if prod_designers is not None:
                prod_designers = set_crew_field(model_name=ProdDesigner, crew_members=prod_designers)
                movie.prod_designer.set(prod_designers)
        except AttributeError:
            continue
