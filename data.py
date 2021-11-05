memoria = {'x' : 0, 'y' : 0, 'z' : 0, 't' : 0, 'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}

juros_simples = {'J' : 'Juros', 'C' : 'Capital', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_js = 'C*i*n - J'
montante_simples = {'M' : 'Montante', 'C' : 'Capital', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_ms = 'C*(1 + i*n) - M'
desconto = {'D' : 'Desconto', 'N' : 'Valor nominal', 'VD' : 'Valor descontado'}
expr_d = 'N - VD - D'
drs = {'DRS' : 'DRS', 'VD' : 'Valor descontado', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_drs = 'VD*i*n - DRS'
drsN = {'DRS' : 'DRS', 'N' : 'Valor nominal', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_drsN = '(N*i*n)/(1 + i*n) - DRS'
dcs =  {'DCS' : 'DCS', 'N' : 'Valor nominal', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_dcs = 'N*i*n - DCS'
dbs =  {'DBS' : 'DBS', 'N' : 'Valor nominal', 'i' : 'Taxa', 'n' : 'Prazo', 'ib' : 'Taxa do banco'}
expr_dbs = 'N*(i*n + ib) - DBS'
difcsrs = {'Dif' : 'Diferença', 'DRS' : 'DRS', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_difcsrs = 'DRS*i*n - Dif'
ifs = {'ifs' : 'Taxa efetiva', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_ifs = 'i/(1 - i*n) - ifs'
juros_compostos = {'J' : 'Juros', 'C' : 'Capital', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_jc = 'C*((1 + i)**n - 1) - J'
montante_composto = {'M' : 'Montante', 'C' : 'Capital', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_mc = 'C*(1 + i)**(n) - M'
cl = {'MC' : 'Montante com convenção', 'M' : 'Montante', 'i' : 'Taxa', 'nf' : 'Prazo fracionário'}
expr_cl = 'M*(1 + i*nf) - MC'
ce = {'MC' : 'Montante com convenção', 'M' : 'Montante', 'i' : 'Taxa', 'nf' : 'Prazo fracionário'}
expr_ce = 'M*(1 + i)**nf - MC'
taxa_eq = {'ieq' : 'Taxa equivalente', 'i' : 'Taxa', 'nd' : 'Prazo da taxa desconhecida', 'nc' : 'Prazo da taxa conhecida'}
expr_teq = '(1 + i)**(nd/nc) - 1 - ieq'
drc =  {'DRC' : 'DRC', 'VD' : 'Valor descontado', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_drc = 'VD*((1 + i)**n - 1) - DRC'
drcN = {'DRC' : 'DRC', 'N' : 'Valor nominal', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_drcN = 'N*(1 - (1/((1 + i)**n))) - DRC'
dcc = {'DCC' : 'DCC', 'N' : 'Valor nominal', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_dcc = 'N*(1 - (1 - i)**n) - DCC'
difccrc = {'Dif' : 'Diferença', 'N' : 'Valor nominal', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_difccrc = '(N*(1 - (1 - i**2)**n))/(1 + i)**n - Dif'
ifc = {'ifc' : 'Taxa efetiva', 'i' : 'Taxa'}
expr_ifc = 'i/(1-i) - ifc'
vp_mode_padrao = {'PV' : 'Valor presente', 'PMT' : 'Pagamento', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_vp_mp = 'PMT*(1-(1+i)**(-n))/i-PV'
vf_mode_padrao = {'FV' : 'Valor futuro', 'PMT' : 'Pagamento', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_vf_mp = 'PMT*((1+i)**(n)-1)/i-FV'
vp_mode_ia = {'PV' : 'Valor presente', 'PMT' : 'Pagamento', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_vp_ia = 'PMT*(1+i)*(1-(1+i)**(-n))/i-PV'
vf_mode_ia = {'FV' : 'Valor futuro', 'PMT' : 'Pagamento', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_vf_ia = 'PMT*(1+i)*((1+i)**(n)-1)/i-FV'
vp_mode_d = {'PV' : 'Valor presente', 'PMT' : 'Pagamento', 'i' : 'Taxa', 'n' : 'Prazo', 'c' : 'Carência'}
expr_vp_d = 'PMT*(1-(1+i)**(-n))/(i*(1+i)**c)-PV'
vf_mode_d = {'FV' : 'Valor futuro', 'PMT' : 'Pagamento', 'i' : 'Taxa', 'n' : 'Prazo'}
expr_vf_d = 'PMT*((1+i)**(n)-1)/i-FV'
vp_mode_inf = {'PV' : 'Valor presente', 'PMT' : 'Pagamento', 'i' : 'Taxa'}
expr_vp_inf = 'PMT/i - PV'
vp_mode_infa = {'PV' : 'Valor presente', 'PMT' : 'Pagamento', 'i' : 'Taxa'}
expr_vp_infa = 'PMT*(1+i)/i - PV'


op_dict = {'1' : [juros_simples, expr_js], '2' : [montante_simples, expr_ms], '3' : [desconto, expr_d], '4' : [drs, expr_drs],
           '5' : [drsN, expr_drsN], '6' : [dcs, expr_dcs], '7' : [dbs, expr_dbs], '8' : [difcsrs, expr_difcsrs],
           '9' : [ifs, expr_ifs], '0' : [juros_compostos, expr_jc], 'A' : [montante_composto, expr_mc], 'B' : [cl, expr_cl],
           'C' : [ce, expr_ce], 'D' : [taxa_eq, expr_teq], 'E' : [drc, expr_drc], 'F' : [drcN, expr_drcN],
           'G' : [dcc, expr_dcc], 'H' : [difccrc, expr_difccrc], 'I' : [ifc, expr_ifc], 'J' : [vp_mode_padrao, expr_vp_mp],
           'K' : [vf_mode_padrao, expr_vf_mp], 'L' : [vp_mode_ia, expr_vp_ia], 'M' : [vf_mode_ia, expr_vf_ia], 'N' : [vp_mode_d, expr_vp_d],
           'O' : [vf_mode_d, expr_vf_d], 'P' :  [vp_mode_inf, expr_vp_inf], 'Q' :  [vp_mode_infa, expr_vp_infa]}
		   
ajuda = '''Digite 'list' para a lista de operações.
Digite 'esc' para sair.
Digite 'rcl' para ver o que está salvo na memória.
Digite 'clear' para limpar a memória.
Para usar uma operação, pressione seu caractere.
Para escolher uma incógnita, digite sua sigla.
Para usar ou salvar um valor, aperte x, y, z, t, a, b, c ou d.
Não esqueça de dar Enter!
Use pontos ao ínves de vírgulas.'''

listaop = '''1: Juros simples
2: Montante de juros simples
3: Desconto
4: Desconto racional simples
5: DRS em função de N
6: Desconto comercial simples
7: Deconto bancário simples
8: DCS - DRS
9: Taxa efetiva comercial simples
0: Juros compostos
A: Montante de juros compostos
B: MJC com convenção linear
C: MJC com convenção exponencial
D: Taxa equivalente
E: Desconto racional composto
F: DRC em função de N
G: Desconto comercial composto
H: DCC - DRC
I: Taxa efetiva comercial composta
J: Valor presente no modelo padrão
K: Valor futuro no modelo padrão
L: Valor presente no modelo IA
M: Valor futuro no modelo IA
N: Valor presente no modelo D
O: Valor futuro no modelo D
P: Valor presente no modelo Inf
Q: Valor presente no modelo Inf antecipado'''
