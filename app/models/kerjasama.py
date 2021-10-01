from app import db


class Kerjasama(db.Model):
    __tablename__ = 'Kerjasama'

    ID_Surat = db.Column(db.Integer, primary_key=True)
    Lampiran = db.Column(db.String)
    Hal = db.Column(db.String)
    Sifat = db.Column(db.String)
    Nama_Perusahaan = db.Column(db.String)
    Besar_Dana = db.Column(db.Integer)
    Jenis_Kerjasama = db.Column(db.String)
    Penanggung_Jawab = db.Column(db.String)
    Nama_Manager = db.Column(db.String)
