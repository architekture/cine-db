"""Import movies using django-extensions runscript feature."""

from movies.models import(
    AspectRatio,
    Barcode,
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
from utils.data import add_crew, get_crew_objects
from utils.importer import MOVIES


def run():
    movies = MOVIES

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
        barcode = int(details["data"]["release"]["upc"])
        discs = int(details["data"]["release"]["discs"])
        publisher = details["data"]["release"]["publisher"]

        AspectRatio.objects.get_or_create(aspect_ratio=aspect_ratio)
        Barcode.objects.get_or_create(barcode=barcode)
        Discs.objects.get_or_create(discs=discs)
        Publisher.objects.get_or_create(publisher=publisher)
        RunTime.objects.get_or_create(run_time=run_time)
        Year.objects.get_or_create(year=year)

        aspect_ratio = AspectRatio.objects.get(aspect_ratio=aspect_ratio)
        barcode = Barcode.objects.get(barcode=barcode)
        discs = Discs.objects.get(discs=discs)
        publisher = Publisher.objects.get(publisher=publisher)
        run_time = RunTime.objects.get(run_time=run_time)
        year = Year.objects.get(year=year)

        movie = {
            "title": title,
            "slug": slug,
            "aspect_ratio": aspect_ratio,
            "barcode": barcode,
            "discs": discs,
            "publisher": publisher,
            "run_time": run_time,
            "year": year,
        }

        Movie.objects.get_or_create(**movie)
        try:
            movie = Movie.objects.get(slug=movie["slug"])
            directors = get_crew_objects(model_name=Director, crew_members=directors)
            movie.director.set(directors)
            if cinematographers is not None:
                cinematographers = get_crew_objects(model_name=Cinematographer, crew_members=cinematographers)
                movie.dp.set(cinematographers)
            if composers is not None:
                composers = get_crew_objects(model_name=Composer, crew_members=composers)
                movie.composer.set(composers)
            if editors is not None:
                editors = get_crew_objects(model_name=Editor, crew_members=editors)
                movie.editor.set(editors)
            if prod_designers is not None:
                prod_designers = get_crew_objects(model_name=ProdDesigner, crew_members=prod_designers)
                movie.prod_designer.set(prod_designers)
        except AttributeError:
            continue
