
import pandas as pd
from data import df_alternatif, df_kriteria


def normalisasi_saw():
    """
    Menghitung normalisasi menggunakan metode SAW.
    """
    kolom_kriteria = df_kriteria["Kode"].tolist()
    hasil = df_alternatif.set_index("Alternatif")[kolom_kriteria].copy()

    normalisasi = pd.DataFrame(
        index=hasil.index,
        columns=hasil.columns,
        dtype=float
    )

    for kolom in kolom_kriteria:
        jenis = df_kriteria.loc[
            df_kriteria["Kode"] == kolom, "Jenis"
        ].iloc[0]

        if jenis == "Benefit":
            nilai_maks = hasil[kolom].max()
            normalisasi[kolom] = hasil[kolom] / nilai_maks

        elif jenis == "Cost":
            nilai_min = hasil[kolom].min()
            normalisasi[kolom] = nilai_min / hasil[kolom]

    return normalisasi


def hitung_preferensi():
    """
    Menghitung nilai preferensi setiap alternatif.
    """
    normalisasi = normalisasi_saw()

    bobot = df_kriteria.set_index("Kode")["Bobot"]

    nilai_preferensi = normalisasi.mul(bobot).sum(axis=1)

    hasil_ranking = pd.DataFrame({
        "Alternatif": nilai_preferensi.index,
        "Nilai Preferensi": nilai_preferensi.values
    })

    hasil_ranking = hasil_ranking.sort_values(
        by="Nilai Preferensi",
        ascending=False
    ).reset_index(drop=True)

    hasil_ranking.insert(
        0,
        "Peringkat",
        range(1, len(hasil_ranking) + 1)
    )

    return normalisasi, hasil_ranking
