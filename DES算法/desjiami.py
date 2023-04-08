import des, inandout
import base64


def des_jiami(miyao_list, mingwen_list):
    miwen = des.des(miyao_list, mingwen_list, 1)
    resultall = inandout.outcontent(miwen)
    resultall = resultall.encode("utf-8")
    bs64 = base64.b64encode(resultall)
    print("经过bs64加密后的密文:",end="")
    print(bs64)
