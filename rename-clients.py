import os

#pfSense-UDP4-1194-Cidade-abv-usuario-02.ovpn

for i in os.listdir(): ##lista tudo
    if os.path.isfile(i): ##pega so arquivo
        if i.endswith(".ovpn"): ## separa por extensao
         cidade = i.split('-')[4]
         usuario = i.split('-')[5]
         ponto = i.split('-')[6]
         novo_nome = "{0}-{1}-{2}.conf".format(cidade, usuario, ponto)
         os.rename(i, novo_nome)
