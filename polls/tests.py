from django.test import TestCase
# Create your tests here.
nama = [
  "rudi"
  "budi"
  "siti"
]
  
nama.append("jokowi")


def fungsi(nama):
    nama.append("joni")
fungsi(nama)

print(nama)

