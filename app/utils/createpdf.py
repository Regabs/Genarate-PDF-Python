import qrcode
import fpdf
import app
from fpdf import FPDF
from qrcode import image
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.image(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\app\utils\image\Logo_BA.png',10, 8, 55,)
        self.image(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\app\utils\image\TUV_Logo.jpeg', 130, 8, 20)
        self.image(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\app\utils\image\KAN_Logo.jpeg', 150, 8, 25)
        self.image(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\app\utils\image\SKB_Logo.jpeg', 175, 8, 20)
        self.ln(30)
        self.set_font('times', 'B', 30)
        self.cell(0, 10, 'Dokumen Persetujuan', border=False, ln=1, align='C' )
        self.ln(10)
        self.set_font('times', 'B', 12)
        self.cell(0, 5, 'Nomor Surat   : ', border=False, ln=1, align='C' )
        self.cell(0, 5, 'Lampiran        : ', border=False, ln=1, align='C' )
        self.cell(0, 5, 'Hal                   : ', border=False, ln=1, align='C' )
        self.cell(0, 5, 'Sifat                 : ', border=False, ln=1, align='C' )
        self.line(10, 85, 200, 85)
        self.ln(10)
    
    def footer(self):
        self.image(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\app\utils\image\alamat.jpeg', 3, 270, 210)

pdf = PDF('P', 'mm', format='A4')
pdf.add_page()
pdf.set_font('times', 'B', 12)
pdf.cell(0, 5, 'Dengan hormat,', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Dengan ini kami sampaikan bahwa Fakultas Teknik UGM telah menjalin kerjasama dengan PT PLN ', border=False, ln=1, align='L' )
pdf.cell(0, 5, '(Persero) Kantor Pusat dengan perjanjian nomor: 0443.PJ/DAN.02.07/010505/2019 ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Sehubungan dengan hal tersebut, mohon berkenan kebijaksanaan ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Bapak untuk dapat menerbitkan, E-Faktur, guna kelengkapan administrasi pembayaran,', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'dengan data sebagai berikut: ', border=False, ln=1, align='L' )
pdf.ln(10)
pdf.cell(0, 5, 'Nama Perusahan  : ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Besar dana            : ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Jenis Kejasama     : ', border=False, ln=1, align='L' )
pdf.ln(10)
pdf.cell(0, 5, 'Demikian dokumen Kerjasama, terimakasih atas perhatiannya.', border=False, ln=1, align='L' )

pdf.ln(30)
pdf.cell(0, 5, 'Manajer', border=False, ln=0, align='L' )
pdf.cell(0, 5, 'Penanggung Jawab', border=False, ln=1, align='R' )
pdf.ln(30)
img = qrcode.make('https://www.youtube.com/watch?v=-GmJLI122ZM')
type(img)
img.save(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\storage\some_file.png')
pdf.image(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\storage\some_file.png', 10,195,30)


pdf.cell(0, 5, 'Budi Budiman', border=False, ln=0, align='L' )
pdf.cell(0, 5, 'Sudriman', border=False, ln=0, align='R' )










pdf.output(r'C:\Users\hp\Pictures\Sem 7\Kerja Praktek\Genarate-PDF-Python\storage\Coba.pdf')
