
from saw import normalisasi_saw, hitung_preferensi

print("=== HASIL NORMALISASI SAW ===")
normalisasi, ranking = hitung_preferensi()

print(normalisasi.round(3))

print("\n=== HASIL PERANGKINGAN ===")
print(ranking.to_string(index=False))
