import numpy as np # untuk operasi matematika
import skfuzzy as fuzz # untuk logika fuzzy
from skfuzzy import control as ctrl # untuk sistem kontrol fuzzy
# himpunan fuzzy untuk variabel input dan output
barang_terjual = ctrl.Antecedent(np.arange(0, 100), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 300), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100000), 'harga')
profit = ctrl.Antecedent(np.arange(0, 4000000), 'profit')
stok_makanan = ctrl.Consequent(np.arange(0, 1000), 'stok_makanan')
# Fungsi keanggotaan untuk barang terjual
barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])
# Fungsi keanggotaan untuk permintaan
permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])
# Fungsi keanggotaan untuk harga
harga['murah'] = fuzz.trimf(harga.universe, [0, 0, 40000])
harga['sedang'] = fuzz.trimf(harga.universe, [30000, 50000, 80000])
harga['mahal'] = fuzz.trimf(harga.universe, [60000, 100000, 100000])
# Fungsi keanggotaan untuk profit
profit['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['tinggi'] = fuzz.trimf(profit.universe, [1500000, 2500000, 4000000])
# Fungsi keanggotaan untuk stok makanan
stok_makanan['sedang'] = fuzz.trimf(stok_makanan.universe, [300, 500, 700])
stok_makanan['banyak'] = fuzz.trimf(stok_makanan.universe, [600, 1000, 1000])
# Aturan fuzzy
rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok_makanan['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok_makanan['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], stok_makanan['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok_makanan['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok_makanan['banyak'])
rule6 = ctrl.Rule(barang_terjual['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], stok_makanan['sedang'])
#sistem kontrol fuzzy
stok_makanan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
stok_simulasi = ctrl.ControlSystemSimulation(stok_makanan_ctrl)
# Input
stok_simulasi.input['barang_terjual'] = 80
stok_simulasi.input['permintaan'] = 255
stok_simulasi.input['harga'] = 25000
stok_simulasi.input['profit'] = 3500000

# Proses 
stok_simulasi.compute()
# Output
print("Jumlah stok makanan:", stok_simulasi.output['stok_makanan'])
stok_makanan.view(sim=stok_simulasi)
input('Tekan ENTER untuk melanjutkan')