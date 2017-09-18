from django.db import models

class Pesquisador(models.Model):
    SEXO_CHOICES = (("feminino", "Feminino"), ("masculino", "Masculino"))
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome")
    cpf = models.CharField(max_length=50, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20, null=False)
    area_pesquisa = models.CharField(max_length=50, null=False, verbose_name="Área de Pesquisa")
    #foto?

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pesquisadores"

class Programa(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome")
    descricao = models.CharField(null = False, max_length=150, verbose_name="Descrição")
    #só?

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(null=False, max_length=50, verbose_name="Nome")
    endereco = models.CharField(null=False, max_length=50, verbose_name="Endereço")
    #so?

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Instituições"

class Bolsa(models.Model):
    PAISES_CHOICES = ( ("afeganistao", "Afeganistão"), ("africa_do_sul", "África do Sul"), ("albania", "Albânia"),
                      ("alemanha", "Alemanha"), ("andorra", "Andorra"), ("angola", "Angola"),
                      ("antiga_barbuda", "Antiga e Barbuda"), ("arabia", "Arábia Saudita"), ("argelia", "Argélia"),
                      ("argentina", "Argentina"), ("arménia", "Arménia"), ("australia", "Austrália"),
                      ("austria", "Áustria"), ("azer", "Azerbaijão"), ("angola", "Bahamas"),
                      ("bangladexe", "Bangladexe"), ("barbados", "Barbados"), ("barem", "Barém"),
                      ("belgica", "Bélgica"), ("belize", "Belize"), ("benim", "Benim"),
                      ("bielorrussia", "Bielorrússia"), ("bolivia", "Bolívia"), ("bosnia", "Bósnia e Herzegovina"),
                      ("botsuana", "Botsuana"), ("brasil", "Brasil"), ("brunei", "Brunei"),
                      ("bulgaria", "Bulgária"), ("burquina", "Burquina Faso"), ("burundi", "Burúndi"),
                      ("butao", "Butão"), ("cabo_verde", "Cabo Verde"), ("camaraes", "Camarões"),
                      ("camboja", "Camboja"), ("canada", "Canadá"), ("catar", "Catar"),
                      ("cazaquistao", "Cazaquistão"), ("chade", "Chade"), ("chile", "Chile"),
                      ("china", "China"), ("chipre", "Chipre"), ("colombia", "Colômbia"),
                      ("comores", "Comores"), ("congo", "Congo-Brazzaville"), ("coreia_norte", "Coreia do Norte"),
                      ("coreia_sul", "Coreia do Sul"), ("cosvo", "Cosovo"), ("costa_marfim", "Costa do Marfim"),
                      ("costa_rica", "Costa Rica"), ("croacia", "Croácia"), ("cuaite", "Cuaite"),
                      ("cuba", "Cuba"), ("dinamarca", "Dinamarca"), ("dominca", "Dominica"),
                      ("egito", "Egito"), ("emirados", "Emirados Árabes Unidos"), ("equador", "Equador"),
                      ("eritreia", "Eritreia"), ("eslovaquia", "Eslováquia"), ("eslovenia", "Eslovénia"),
                      ("espanha", "Espanha"), ("palestina", "Estado da Palestina"), ("eua", "Estados Unidos"),
                      ("estonia", "Estónia"), ("etiopia", "Etiópia"), ("fiji", "Fiji"),
                      ("filipinas", "Filipinas"), ("finlandia", "Finlândia"), ("franca", "França"),
                      ("gabao", "Gabão"), ("gambia", "Gâmbia"), ("gana", "Gana"),
                      ("georgia", "Geórgia"), ("granada", "Granada"), ("grecia", "Grécia"),
                      ("guine_e", "Guiné Equatorial"), ("guine_b", "Guiné-Bissau"), ("haiti", "Haiti"),
                      ("honduras", "Honduras"), ("hungria", "Hungria"), ("iemen", "Iémen"),
                      ("ilhas", "Ilhas Marechal"), ("india", "Índia"), ("indonésia", "Indonésia"),
                      ("irao", "Irão"), ("iraque", "Iraque"), ("irlanda", "Irlanda"),
                      ("islandia", "Islândia"), ("israel", "Israel"), ("italia", "Itália"),
                      ("jamaica", "Jamaica"), ("japao", "Japão"), ("jibuti", "Jibuti"),
                      ("jordania", "Jordânia"), ("laus", "Laus"), ("lesoto", "Lesoto"),
                      ("letonia", "Letónia"), ("libano", "Líbano"), ("liberia", "Libéria"),
                      ("libia", "Líbia"), ("listenstaine", "Listenstaine"), ("lituania", "Lituânia"),
                      ("luxemburgo", "Luxemburgo"), ("macedonia", "Macedónia"), ("madagascar", "Madagáscar"),
                      ("malasia", "Malásia"), ("malaui", "Maláui"), ("maldivas", "Maldivas"),
                      ("mali", "Mali"), ("malta", "Malta"), ("marrocos", "Marrocos"),
                      ("mauricia", "Maurícia"), ("mauritania", "Mauritânia"), ("mexico", "México"),
                      ("mianmar", "Mianmar"), ("micronesia", "Micronésia"), ("mocambique", "Moçambique"),
                      ("moldavia", "Moldávia"), ("monaco", "Mónaco"), ("mongolia", "Mongólia"),
                      ("montenegro", "Montenegro"), ("namibia", "Namíbia"), ("nauru", "Nauru"),
                      ("nepal", "Nepal"), ("nicaragua", "Nicarágua"), ("niger", "Níger"),
                      ("nigeria", "Nigéria"), ("noruega", "Noruega"), ("nova_zelandia", "Nova Zelândia"),
                      ("oma", "Omã"), ("paises_baixos", "Países Baixos"), ("palau", "Palau"),
                      ("panama", "Panamá"), ("nova_guine", "Papua Nova Guiné"), ("paquistao", "Paquistão"),
                      ("paraguai", "Paraguai"), ("peru", "Peru"), ("polonia", "Polónia"),
                      ("portugal", "Portugal"), ("quenia", "Quénia"), ("quirguistao", "Quirguistão"),
                      ("quiribati", "Quiribáti"), ("reino_unido", "Reino Unido"),
                      ("republica_ca", "República Centro-Africana"),
                      ("republica_checa", "República Checa"), ("republica_dc", "República Democrática do Congo"),
                      ("republica_d", "República Dominicana"),
                      ("romenia", "Roménia"), ("ruanda", "Ruanda"), ("russia", "Rússia"),
                      ("salomao", "Salomão"), ("salvador", "Salvador"), ("samoa", "Samoa"),
                      ("santa_lucia", "Santa Lúcia"), ("sao_cristovao", "São Cristóvão e Neves"),
                      ("sao_marinho", "São Marinho"),
                      ("sao_tome", "São Tomé e Príncipe"), ("sao_vicente", "São Vicente e Granadinas"),
                      ("seicheles", "Seicheles"),
                      ("senegal", "Senegal"), ("serra", "Serra Leoa"), ("servia", "Sérvia"), ("singapura", "Singapura"),
                      ("siria", "Síria"), ("angola", "Somália"), ("sri_Lanca", "Sri Lanca"),
                      ("suazilandia", "Suazilândia"),
                      ("sudao", "Sudão"), ("sudao_sul", "Sudão do Sul"), ("suecia", "Suécia"), ("suica", "Suíça"),
                      ("suriname", "Suriname"), ("tailandia", "Tailândia"), ("taiua", "Taiuã"),
                      ("tajiquistao", "Tajiquistão"), ("tanzania", "Tanzânia"), ("timor_leste", "Timor-Leste"),
                      ("togo", "Togo"), ("tonga", "Tonga"), ("trindade_tobago", "Trindade e Tobago"),
                      ("tunisia", "Tunísia"), ("turcomenistao", "Turcomenistão"), ("turquia", "Turquia"),
                      ("tuvalu", "Tuvalu"), ("ucrania", "Ucrânia"), ("uganda", "Uganda"),
                      ("uruguai", "Uruguai"), ("usbequistao", "Usbequistão"), ("vanuatu", "Vanuatu"),
                      ("vaticano", "Vaticano"), ("venezuela", "Venezuela"), ("vietname", "Vietname"),
                      ("zambia", "Zâmbia"), ("zimbabue", "Zimbábue"))

    pais = models.CharField(max_length=50, null=False, verbose_name="País", choices=PAISES_CHOICES)
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado")
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")
    modalidade = models.CharField(max_length=50, null=False, verbose_name="Modalidade")
    programa = models.ForeignKey(Programa, verbose_name="Programa")
    vigencia = models.DateField(null=False, verbose_name="Vigência")
    descricao = models.CharField(max_length=150, null=False, verbose_name="Descrição")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")

    def __str__(self):
        return self.descricao
