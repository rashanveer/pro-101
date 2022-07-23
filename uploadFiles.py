import dropbox
class TransferData:
    def __init__(self,rtoken):
        self.rtoken = rtoken
    def  uploadFile(self,ffrom,to):
        tbx = dropbox.Dropbox(self.rtoken)

def main():
    token = "sl.BLhgEtqgbbFgc3Vl37lnycTuZMuYpp3ZV6Xh1c4IFHae9r18cj9xt4CoWRXIu2sz3cUH9HnepTP6LGxiOG863L7HRNPfYYw5vyoK-FS8dwanPZYiN8KcGlixCEgpSpdNKt9yu-Y"
    td = TransferData(token)
    ffrom = "text.txt"
    f2 = "new.txt"
    td.uploadFile(ffrom,f2)
    print("file Transfeered")


main()