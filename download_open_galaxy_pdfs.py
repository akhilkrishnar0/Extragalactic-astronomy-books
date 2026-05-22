from pathlib import Path
from urllib.request import Request, urlopen
import shutil

items = [
    ("https://library.oapen.org/bitstream/handle/20.500.12657/25130/Fundamentals-of-Galaxy-Dynamics-Formation-and-Evolution.pdf?sequence=1", "Ferreras_2019_Fundamentals_of_Galaxy_Dynamics_Formation_Evolution.pdf"),
    ("https://arxiv.org/pdf/1912.06216", "Cimatti_Fraternali_Nipoti_2019_Intro_Galaxy_Formation_Evolution_arXiv.pdf"),
    ("https://kudzu.astr.ua.edu/psss/galaxy_morphology_v2.pdf", "Buta_2013_Galaxy_Morphology.pdf"),
    ("https://ned.ipac.caltech.edu/level5/Sept19/vanderKruit/paper.pdf", "vanderKruit_Galaxy_Disks_NED.pdf"),
    ("https://www.astro.rug.nl/~vdkruit/jea3/homepage/dynamics.pdf", "vanderKruit_Review_of_Galactic_Dynamics.pdf"),
    ("https://astroweb.case.edu/ssm/papers/SHPSv88p220.pdf", "McGaugh_2021_LSB_Galaxies_Dark_Matter_OpenAccess.pdf"),
    ("https://www.nasa.gov/wp-content/uploads/2019/08/hubblefocusgalaxies.pdf", "NASA_Hubble_Focus_Galaxies_Through_Space_and_Time.pdf"),
]

outdir = Path("pdfs")
outdir.mkdir(exist_ok=True)
for url, name in items:
    print(f"Downloading {name}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=90) as r, open(outdir / name, "wb") as f:
        shutil.copyfileobj(r, f)
print("Done. Online-only: https://galaxiesbook.org/")
print("OpenStax official page: https://openstax.org/details/books/astronomy-2e")
