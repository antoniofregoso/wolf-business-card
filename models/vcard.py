import qrcode
import os
class vcard:
    
    def get_qr(self,xcf_url):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(xcf_url)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(os.getcwd() + '/static/vcf/' + xcf_url + '.png')
        