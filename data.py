
import pandas as pd

# Data alternatif calon penerima beasiswa
data_alternatif = {
    "Alternatif": [
        "A1 - Davina Medusa",
        "A2 - Angga Agustina",
        "A3 - Wiwit Kurniawati",
        "A4 - Rizqi Prayoga",
        "A5 - Bima Tri Utama",
        "A6 - Riska Medisa",
        "A7 - Achmad Yani",
        "A8 - Rizqi Nurwahed"
    ],
    "C1": [2, 3, 4, 2, 4, 1, 2, 3],
    "C2": [1, 3, 2, 2, 3, 2, 2, 1],
    "C3": [1, 2, 1, 2, 2, 1, 1, 2],
    "C4": [3, 2, 4, 1, 2, 3, 4, 2],
    "C5": [4, 5, 6, 5, 5, 4, 6, 4]
}

df_alternatif = pd.DataFrame(data_alternatif)

# Data kriteria dan bobot
data_kriteria = {
    "Kode": ["C1", "C2", "C3", "C4", "C5"],
    "Kriteria": [
        "Penghasilan Orang Tua",
        "Potensi Akademik",
        "Pekerjaan Orang Tua",
        "Tanggungan Orang Tua",
        "Prestasi Non-Akademik"
    ],
    "Bobot": [0.30, 0.20, 0.20, 0.20, 0.10],
    "Jenis": ["Benefit", "Benefit", "Benefit", "Cost", "Benefit"]
}

df_kriteria = pd.DataFrame(data_kriteria)
