estados = ["Acre","Alagoas","Amazonas","Bahia","Ceará","Distrito Federal","Espírito Santo","Goiás","Maranhão","Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná","Pernambuco","Piauí","Rio de Janeiro","Rio Grande do Norte","Rio Grande do Sul","Rondônia","Roraima","Santa Catarina","São Paulo","Sergipe","Tocantins","São Paulo"]

print(f"Quantidade de Nomes: {len(estados)}.\n")

for i in range(len(estados)):
    print(f"{i + 1}º nome: {estados[i]}.")

