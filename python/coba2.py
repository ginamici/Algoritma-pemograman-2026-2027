# Menginput Nilai Tugas, UUTS dan UAS 
tugas = float(input("Input Nilai Tugas:"))
uts = float(input("Input Nilai UTS:"))
uas = float(input("Input Nilai UAS:"))

#Menghitung Nilai Akhir sesuai dengan Bobot
nilai = (0.15*tugas) + (0.35 * uts) + (0.50 * uas)

#Menetukan Grade Berdasarkan Nilai Akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'

#Menetukan Status Kelulusan Berdasarkan Nilai Akhir
if nilai>60:
    status = 'LULUS'
else:
    status = 'TIDAK LULUS'

#Menampilkan Nilai Akhir, Grade, dan Status Kelulusan
print('Nilai Akhir:%0.2f' % nilai)
print('Grade: {}'.format(grade))
print('status:{}'.format(status))