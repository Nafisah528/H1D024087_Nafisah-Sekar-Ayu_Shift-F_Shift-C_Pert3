import numpy as np #import library numpy untuk operasi array
import skfuzzy as fuzz #import library skfuzzy untuk operasi fuzzy
from skfuzzy import control as ctrl #import library control dari skfuzzy untuk membuat sistem kontrol fuzzy
# Himpunan fuzzy untuk variabel input dan output
kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi') #
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')
# Fungsi keanggotaan untuk variabel kejelasan informasi
kejelasan_informasi["tidak_memuaskan"] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60, 75])
kejelasan_informasi["cukup_memuaskan"] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi["memuaskan"] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100, 100])
# fungsi keanggotaan untuk variabel kejelasan persyaratan
kejelasan_persyaratan["tidak_memuaskan"] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60, 75])
kejelasan_persyaratan["cukup_memuaskan"] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan["memuaskan"] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100, 100])
# fungsi keanggotaan untuk variabel kemampuan petugas
kemampuan_petugas["tidak_memuaskan"] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60, 75])
kemampuan_petugas["cukup_memuaskan"] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas["memuaskan"] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100, 100])
# fungsi keanggotaan untuk variabel ketersediaan sarpras
ketersediaan_sarpras["tidak_memuaskan"] = fuzz.trapmf(ketersediaan_sarpras.universe, [0, 0, 60, 75])
ketersediaan_sarpras["cukup_memuaskan"] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras["memuaskan"] = fuzz.trapmf(ketersediaan_sarpras.universe, [75, 90, 100, 100])
# fungsi keanggotaan untuk variabel kepuasan pelayanan
kepuasan_pelayanan["tidak_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan["kurang_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan["cukup_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan["memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan["sangat_memuaskan"] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])
# Aturan fuzzy untuk menentukan kepuasan pelayanan berdasarkan kejelasan informasi, kejelasan persyaratan, kemampuan petugas, dan ketersediaan sarpras
aturan1 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['kurang_memuaskan'])
aturan2 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan3 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan4 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan5 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan6 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan7 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan8 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan9 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan10 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan11 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan12 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan13 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan14 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan15 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan16 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan17 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan18 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan19 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan20 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan21 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan22 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan23 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan24 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan25 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan26 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan27 = ctrl.Rule(kejelasan_informasi['tidak_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan28 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan29 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan30 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan31 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan32 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan33 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan34 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan35 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan36 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan37 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan38 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan39 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan40 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan41 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan42 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan43 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan44 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan45 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan46 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan47 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan48 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan49 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan50 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan51 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan52 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan53 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan54 = ctrl.Rule(kejelasan_informasi['cukup_memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan55 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan56 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan57 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan58 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan59 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan60 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan61 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan62 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan63 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])

aturan64 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['cukup_memuaskan'])
aturan65 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan66 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan67 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan68 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan69 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan70 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan71 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan72 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup_memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan73 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan74 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan75 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan76 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan77 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan78 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup_memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan79 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan80 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup_memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
aturan81 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat_memuaskan'])
# list untuk menyimpan semua aturan fuzzy
rules_list = [
    aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9,
    aturan10, aturan11, aturan12, aturan13, aturan14, aturan15, aturan16, aturan17, aturan18,
    aturan19, aturan20, aturan21, aturan22, aturan23, aturan24, aturan25, aturan26, aturan27,
    aturan28, aturan29, aturan30, aturan31, aturan32, aturan33, aturan34, aturan35, aturan36,
    aturan37, aturan38, aturan39, aturan40, aturan41, aturan42, aturan43, aturan44, aturan45,
    aturan46, aturan47, aturan48, aturan49, aturan50, aturan51, aturan52, aturan53, aturan54,
    aturan55, aturan56, aturan57, aturan58, aturan59, aturan60, aturan61, aturan62, aturan63,
    aturan64, aturan65, aturan66, aturan67, aturan68, aturan69, aturan70, aturan71, aturan72,
    aturan73, aturan74, aturan75, aturan76, aturan77, aturan78, aturan79, aturan80, aturan81
]
# membuat sistem kontrol fuzzy dengan aturan yang telah dibuat
kepuasan_ctrl = ctrl.ControlSystem(rules_list)
#membuat simulasi untuk sistem kontrol fuzzy
kepuasan_sim = ctrl.ControlSystemSimulation(kepuasan_ctrl)
# input nilai untuk variabel kejelasan informasi, kejelasan persyaratan, kemampuan petugas, dan ketersediaan sarpras
kepuasan_sim.input["kejelasan_informasi"] = 80
kepuasan_sim.input["kejelasan_persyaratan"] = 60
kepuasan_sim.input["kemampuan_petugas"] = 50
kepuasan_sim.input["ketersediaan_sarpras"] = 90
# proses perhitungan dengan menggunakan sistem kontrol fuzzy
kepuasan_sim.compute()
# menampilkan hasil output dari sistem kontrol fuzzy
kepuasan_pelayanan.view(sim=kepuasan_sim)
hasil = kepuasan_sim.output["kepuasan_pelayanan"]
print("output:", hasil)
# visualisasi hasil output dengan menggunakan matplotlib
import matplotlib.pyplot as plt 
plt.show()

