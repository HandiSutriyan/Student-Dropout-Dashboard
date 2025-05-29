# 👨🏻‍🎓 Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. 

### Permasalahan Bisnis
**Jaya Jaya Institut** memiliki masalah pada banyaknya juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Hal ini menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. 
Apabila dibiarkan, bisa saja angka dropout ini semakin meningkat dan membuat citra Jaya jaya Institut menjadi buruk di kalangan publik. Oleh karena itu, **Jaya Jaya Institut** ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Beberapa pertanyaan bisnis yang perlu dijawab yaitu:
1. Bagaimana persebaran siswa yang dropout dan tidak?
2. Bagaimana demografi siswa yang statusnya droput?
3. Faktor apa saja yang paling memengaruhi siswa untuk dropout?
4. Bagaimana profil akademik siswa yang dropout?

### Cakupan Proyek
Proyek ini bertujuan untuk membantu Jaya Jaya Institut untuk mengatasi masalah tinggi jumlah siswa yang Dropout mencapai lebih dari 30%. Pada proyek ini dilakukan serangkaian analisis data untuk membantu Jaya Jaya Institute memahami dan menangani permasalahan tingginya tingkat dropout. Pekerjaan utama dalam proyek ini meliputi:

1. Eksplorasi dan pembersihan data siswa yang mencakup data demografis, akademik, dan latar belakang keluarga & ekonomi siswa.

2. Analisis deskriptif untuk mengidentifikasi pola dan tren dropout berdasarkan faktor-faktor seperti latar belakang personal, kondisi keluarga, performa akademik, dll.

3. Pembangunan model prediksi dropout menggunakan algoritma *machine learning* untuk memprediksi kemungkinan seorang siswa akan dropout.

4. Evaluasi performa model untuk menentukan model terbaik berdasarkan akurasinya.

5. Pembuatan dashboard visualisasi interaktif sebagai alat bantu dalam memahami faktor risiko dropout dan memonitor kondisi siswa secara berkala.

6. Penyusunan rekomendasi berbasis data untuk strategi mencegah peningkatan jumlah siswa yang dropout.

**Output akhir dari proyek ini berupa**:

- Model prediksi dropout siswa.

- Dashboard visualisasi interaktif.

- Laporan analisis dan rekomendasi strategi yang bisa dilakukkan berdasarkan temuan data.

Batasan dalam proyek ini adalah **tidak mempertimbangkan** faktor penilaian siswa/wali siswa terhadap kualitas layanan institusi yang dapat memengaruhi keputusan siswa untuk keluar dari Jaya Jaya Institut.


### Persiapan

Sumber data: [Data Siswa Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:


1. Jalankan perintah berikut di terminal/command prompt untuk membuat *virtual environment*:

```
python -m venv venv
```

2. Aktifkan *virtual environment*:
    - Windows:

    ```
    venv\Scripts\activate
    ```
    - MacOS/Linux:

    ```
    source venv/bin/activate
    ```
3. Install library dan dependensi yang diperlukan pada `requirements.txt`:

```
pip install -r requirements.txt
```

## Business Dashboard
Untuk memberikan gambaran hasil analisis yang telah dilakukan, terdapat dashboard visualisasi faktor-faktor terkait yang dapat diamati untuk mengatassi masalah *Dropout Rate* Jaya Jaya Institut. Dashboard visualisasi data dibuat dengan Google Looker Studio yang dapat diakses melalui [tautan ini](https://lookerstudio.google.com/reporting/f922294b-6255-4195-a572-889fecf4aba2/page/DmEMF)



## Menjalankan Sistem Machine Learning
Terdapat file `app.py` untuk menjalankan sistem Machine Learning yang sudah dibuat. Dengan sistem ini Anda bisa melakukan prediksi apakah seseorang berpotensi dropout atau tidak berdasarkan parameter-parameter yang diinputkan melalui form yang tersedia.

Sistem ini dibuat dengan Streamlit. Jika Anda menjalankan file `app.py` maka Anda akan menjalankan sistem ini di perangkat Anda secara lokal (localhost). Berikut ini cara untuk menjalankannya di perangkat Anda:

1. Pastikan Anda sudah mengaktifkan *virtual environtment* Pythhon seperti pada langkah [persiapan](#persiapan).

2. Jalankan perintah berikut:
```
streamlit run app.py
```

3. Jika berhasil, sistem akan langsung membuka jendela baru para peramban Anda dan menampilkan anatarmuka dari sistem. Atau Anda juga bisa mengakses melaui tautan yang tampil pada terminal/command promt saat perintah di atas berhasil dijalankan.

4. Untuk menghentikan/menutup sistem, buka terminal yang sebelumnya digunakan untuk menjalankan sistem, kemudian tekan `Ctrl`+`C`.

Sistem ini juga di deploy pada Streamlit Cloud Community, sehingga bisa diakses publik secara daring. Anda bisa mengaksesnya melalui [tautan ini](https://student-dropout-dashboard-jaya2institut.streamlit.app/).

## Conclusion
Berdasarkan hasil analisis yang telah dilakukan dapat diidentifikasi bahwa tingkat dropout paling kuat dipengaruhi oleh faktor akademik, ekonomi, dan demografi. Secara rinci dapat dijelaskan sebagai berikut:
1. **Performa akademik**: 
Siswa dengan performa akademik rendah cenderung berisiko untuk dropout, terutama performa pada semester 2. 

2. **Ekonomi**: 
Siswa yang dropout didominasi oleh siswa yang memilki latar belakang keluarga ekonomi menengah kebawah, karena didominasi oleh siswa yang orang tuanya bekerja sebagai buruh kasar (*Unskilled Worker*). Namun, siswa dengan beasiswa dan merupakan penerima kredit justru tidak mendominasi tingkat dropout. Ini berarti dari segi ekonomi, siswa dropout didominasi oleh ekonomi menengah yang tidak memenuhi syarat untuk mendapatkan beasiswa/kredit namun tidak memiliki kemampuan ekonomi yang kuat untuk melanjutkan pendidikan.

2. **Demografi**: 
Siswa yang dropout didominasi oleh siswa yang memilki latar belakang keluarga ekonomi menengah kebawah dengan tingkat pendidikan orang tua dasar hingga menengah. Selain kondisi ekonomi, siswa yang dropout juga didominasi oleh siswa yang saat mendaftar berumur lebih dari 23 tahun.

Maka kemudian, pertanyaan bisnisnya dapat dijawab:

1. **Bagaimana persebaran siswa yang dropout dan tidak?**

    - Siswa yang dropout berjumlah 1421 siswa (32.1%), siswa yang sudah lulus berjumlah 2209 siswa (49,9%), dan sisanya masih menempuh pendidikan dengan jumlah 794 siswa (17.9%).

2. **Faktor apa saja yang paling memengaruhi siswa untuk dropout?**

    - Berdasarkan analisis model dengan pembelajaran mesin, terdapat 10 faktor utama yang paling memengaruhi tingkat dropout yaitu: 
        - `Curricular_units_2nd_sem_approved`: 0.285729
        - `Tuition_fees_up_to_date`: 0.120368
        - `Curricular_units_1st_sem_enrolled`: 0.062965
        - `Scholarship_holder`: 0.042554
        - `Curricular_units_2nd_sem_grade`: 0.038359
        - `Curricular_units_1st_sem_approved`: 0.037573
        - `Age_at_enrollment`: 0.036161
        - `Debtor`: 0.026249
        - `Curricular_units_2nd_sem_credited`: 0.025350
        - `Curricular_units_2nd_sem_without_evaluations`: 0.025155

    - Berdasarkan analisi korelasi terhadap fitur numerik, terdapat 5 faktor utama yang memiliki nilai korelasi kuat lebih dari 0.2. Empat faktor memiliki korelasi positif terhadap tingkat dropout siswa, yang berarti semain kecil nilainya semaikin meningkatkan risiko siswa tersebut dropout yaitu : `Curricular_units_2nd_sem_approved`, `Curricular_units_2nd_sem_grade`,`Curricular_units_1st_sem_approved`, dan `Curricular_units_1st_sem_grade`. Sedangkan ada satu fitur yang memiliki nilai korelasi negatif yang cukup tinggi yaitu `Age_at_enrollment` yang berarti semakin tua usia siswa saat mendaftar, maka akan semakin tinggi risiko untuk dropout.

3. **Bagaimana profil siswa yang statusnya dropout?**

    - Berdasarkan analisis yang telah dilakukan, siswa yang berstatus dropout didominasi oleh siswa dengan:
        - Latar belakang pendidikan terakhir orang tua di level dasar hingga menengah (pendidikan 6-12 tahun)
        - Latar belakang pekerjaan orang tua yang merupakan pekerja kasar (*unskilled worker*)
        - Tidak mendapatkan beasiswa dan bukan merupakan penerima kredit
        - Berumur lebih dari 23 tahun saat mendaftar
        - Memiliki performa akademik yang kurang baik terutama pada semester 2.

4. **Bagaimana profil akademik siswa yang dropout?**

    - Secara akademik, siswa dropout didominasi oleh siswa yang memilki nilai akhir semester yang rendah dan jumlah mata kuliah yang dapat diluluskan cukup rendah dibandingkan dengan siswa yang lulus baik di semester 1 dan 2.

### Rekomendasi Action Items
Berikut ini beberapa rekomendasi aksi perbaikan dan evaluasi yang dapat dilakukan Jaya Jaya Institut:

1. **Tinjau kembali persyaratan insentif beasiswa dan kredit**

    - Perlu dibuatkan insentif dengan persyaratan yang lebih luas yang menyasar siswa dengan latar belakang keluarga dan ekonomi menengah.
    - Dapat dikembangkan insentif khusus untuk siswa ekonomi menengah selain beasiswa dan kredit, seperti keringanan biaya parsial dan relatif sesuai dengan tingkat pendapatan orang tua.

2. **Berikan pendampingan akademik dan psikologi**

    - Berikan pendampingan akademik pada siswa yang memilki performa kurang secara berkala, bisa diadakan evaluasi setiap pertengahan semester dan akhir semester agar dapat dimitigasi secara dini indikasi kendalan akademik dan psikis yang akan memengaruhi hasil evaluasi akademik siswa.
    - Berikan layanan pendampingan khusus untuk siswa di atas 23 tahun, fakta bahwa siswa dropout didominasi oleh siswa yang mendaftar di atas 23 tahun dan performa akademiknya juga kurang, menunjukkan bahwa siswa dengan rentang usia ini juga perlu bimbingan yang lebih intensif.

3. **Tinjau kembali jalur pendaftaran siswa di atas 23 tahun**

    - Pertimbangkan untuk meninjau kembali jumlah siswa yang diterima dari jalur ini jika ingin mengurangi jumlah siswa dropout, karena jalur ini mendominasi siswa yang dropout
    - Pastikan berikan fasilitas pendampingan khusus untuk siswa dengan golongan ini agar performa akademiknya dapat terjaga dengan baik.

4. **Evaluasi kurikulum dan sistem pembelajaran**

    - Lakukan asesmen pada kurikulum dan sistem pembelajaran terutama pada semester 2, karena secara keseluruhan, performa akademik menurun pada semester 2.
    - Sesuaikan metode pembelajaran/kurikulum yang lebih inklusif untuk semua usia terutama usia di atas 23 tahun dengan berbagai latar belakang yang mengikutinya agar materi lebih mudah diterima dan dapat meningkatkan perfroma akademik mereka.

5. **Lakukan survey kepuasan siswa**

    - Lakukan survey untuk memperluas wawasan tidak hanya dari sisi institusi tapi juga penilaian dari sisi siswa agar analisis lebih objektif dan dapat melihat masalah yang mungkin juga bisa datang dari sisi intitusi
    - Lakukan survey tambahan untuk siswa dengan usia di atas 23 tahun untuk menggali kebutuhan mereka terhadap fasilitas dan metode belajar institusi untuk dapat menangggulangi angka dropout yang tinggi dari golongan ini.
