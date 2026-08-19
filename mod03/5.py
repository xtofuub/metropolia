leiviskat = int(input('Anna leiviskät: '))
naulat = int(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat_yhteensa = luodit_yhteensa * 13.3
kilogrammat = int(grammat_yhteensa // 1000)
grammat = round(grammat_yhteensa - kilogrammat * 1000, 1)

print('Massa nykymittojen mukaan:', kilogrammat, 'kilogrammaa ja', grammat, 'grammaa.')
