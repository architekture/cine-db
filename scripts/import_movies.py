"""Import movies using django-extensions runscript feature."""

from movies.models import(
    AspectRatio,
    Barcode,
    Cinematographer,
    CinematographerPosition,
    Composer,
    ComposerPosition,
    Director,
    DirectorPosition,
    Discs,
    Distributor,
    Editor,
    EditorPosition,
    GenreTag,
    Movie,
    MPAARating,
    ProdDesigner,
    ProdDesignerPosition,
    Publisher,
    RunTime,
    Writer,
    WriterPosition,
    Year,
)
from utils.data import add_crew, add_rating_reasons, get_crew_objects, get_rating_reason
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

        # Set MPAA info fields
        try:
            rating = details["data"]["mpaa"]["rating"]
            mpaa_cert = int(details["data"]["mpaa"]["certificate"])
            distributor = details["data"]["mpaa"]["distributor"]
            reasons = add_rating_reasons(reasons=details["data"]["mpaa"]["reason"])
            MPAARating.objects.get_or_create(rating=rating)
            rating = MPAARating.objects.get(rating=rating)
            Distributor.objects.get_or_create(distributor=distributor)
            distributor = Distributor.objects.get(distributor=distributor)
            movie["rating"] = rating
            movie["mpaa_cert"] = mpaa_cert
            movie["distributor"] = distributor
        except KeyError:
            pass

        # Set genre tags
        genres = details["data"]["genres"]
        genre_list = []
        for genre in genres:
            genre_list.append(genre)
            GenreTag.objects.get_or_create(genre=genre)
        genre_tags = []
        for genre in genre_list:
            genre = GenreTag.objects.get(genre=genre)
            genre_tags.append(genre)

        Movie.objects.get_or_create(**movie)
        try:
            movie = Movie.objects.get(slug=movie["slug"])

            seq = 0
            directors = get_crew_objects(model_name=Director, crew_members=directors)
            for director in directors:
                DirectorPosition.objects.get_or_create(movie=movie, director=director, sequence=seq)
                seq +=1
            if cinematographers is not None:
                seq = 0
                cinematographers = get_crew_objects(model_name=Cinematographer, crew_members=cinematographers)
                for dp in cinematographers:
                    CinematographerPosition.objects.get_or_create(movie=movie, dp=dp, sequence=seq)
                    seq += 1
            if composers is not None:
                seq = 0
                composers = get_crew_objects(model_name=Composer, crew_members=composers)
                for composer in composers:
                    ComposerPosition.objects.get_or_create(movie=movie, composer=composer, sequence=seq)
                    seq += 1
            if editors is not None:
                seq = 0
                editors = get_crew_objects(model_name=Editor, crew_members=editors)
                for editor in editors:
                    EditorPosition.objects.get_or_create(movie=movie, editor=editor, sequence=seq)
                    seq += 1
            if prod_designers is not None:
                seq = 0
                prod_designers = get_crew_objects(model_name=ProdDesigner, crew_members=prod_designers)
                for designer in prod_designers:
                    ProdDesignerPosition.objects.get_or_create(movie=movie, prod_designer=designer, sequence=seq)
                    seq += 1
            if writers is not None:
                seq = 0
                writers = get_crew_objects(model_name=Writer, crew_members=writers)
                for writer in writers:
                    WriterPosition.objects.get_or_create(movie=movie, writer=writer, sequence=seq)
                    seq += 1
            if reasons is not None:
                reasons = get_rating_reason(reasons=reasons)
                movie.rating_reason.set(reasons)
            movie.genre.set(genre_tags)
        except AttributeError:
            continue
