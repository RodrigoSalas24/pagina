from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    year = 2024
    general_photos = ["generales/img1.jpg", "generales/img2.jpg", "generales/img3.jpg",
                      "generales/img5.jpg", "generales/img6.jpg", "generales/img7.jpg", "generales/img8.jpg",
                      "generales/img9.jpg", "generales/img10.jpg", "generales/img11.jpg", "generales/img12.jpg",
                      "generales/img13.jpg", "generales/img14.jpg", "generales/img15.jpg", "generales/img16.jpg",
                      "generales/img17.jpg", "generales/img18.jpg", "generales/img19.jpg", "generales/img20.jpg",
                      "generales/img21.jpg", "generales/img22.jpg", "generales/img23.jpg"]
    return render_template("index.html", year=year, general_photos=general_photos)

@app.route("/albumes")
def albumes():
    album_covers = [("albumes/magbay.jpeg", "1. Imaginal Disk - Magdalena Bay"),
                    ("albumes/scrapyard.jpeg", "2. Scrapyard - Quadeca"),
                    ("albumes/jpegmafia.jpeg", "3. I lay down my life for you - jpegmafia"),
                    ("albumes/greep.jpeg", "4. The New Sound - Geordie Greep"),
                    ("albumes/dillom.jpeg", "5. Por cesárea - Dillom"),
                    ("albumes/chomakopia.jpeg", "6. Chromakopia - Tyler, the creator"),
                    ("albumes/brat.jpeg", "7. Brat - Charli xcx"), ("albumes/gnx.jpeg", "8.GNX - Kendrick Lamar"),
                    ("albumes/4ever.jpeg", "9. 4ever - T&K"), ("albumes/charm.jpeg", "10. Charm - Clairo"),
                    ("albumes/alligator.jpeg", "11. Alligator bites never heal - Doechii"),
                    ("albumes/tato.jpeg", "∞. 1312 - KDK")]

    stats = {
        "minutos": 107.638,
        "nuevos": 44,
    }
    return render_template("albumes.html", album_covers=album_covers, stats=stats)

@app.route("/peliculas")
def peliculas():
    movie_covers = [("peliculas/dune.jpg", "1. Dune: Part Two"), ("peliculas/challengers.jpg", "2. Challengers"),
                    ("peliculas/furiosa.jpg", "3. Furiosa",), ("peliculas/deadpool.jpg", "4. Deadpool y Wolverine"),
                    ("peliculas/juror.jpg", "5. Juror #2"), ("peliculas/jockey.jpg", "6. El Jockey - Luis Ortega")]
    return render_template("peliculas.html", movie_covers=movie_covers)

@app.route("/pelis")
def pelis():
    movie_posters = [("pelis/peli1.jpg", "1. The Father - 2020"), ("pelis/peli2.jpg", "2. Aftersun - 2022"),
                     ("pelis/peli3.jpg", "3. The Iron Claw - 2023"), ("pelis/peli4.jpg", "4. Ciudad de Dios - 2002"),
                     ("pelis/peli5.jpg", "5. Before Sunset - 2004"), ("pelis/peli6.jpg", "6. Everybody wants some - 2016")]
    return render_template("peliculas.html", movie_posters=movie_posters)

@app.route("/gimnasio")
def gimnasio():
    stats = {
        "entrenamientos": 120,
        "pierna": 36,
        "espalda": 44,
        "pecho": 40,
    }
    return render_template("gimnasio.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
