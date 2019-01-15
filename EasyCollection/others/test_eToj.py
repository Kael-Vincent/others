from Setting.eToj import eToj


def test_eToj():
    file = 'D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/a.xlsx'
    debtor=eToj(file)[0]
    print(eToj(file))
    guarantor= eToj(file)
    urgents= [eToj(file)]

    data={'deptor':debtor,'guarantor':guarantor,'urgents':urgents,}
test_eToj()