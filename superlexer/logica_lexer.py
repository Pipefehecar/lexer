import ply.lex as m
class Lexer():	
	
	def __init__(self):
		global resultado_lexema
		resultado_lexema = []
	def prueba(self,data):

	    analizador = m.lex()
	    analizador.input(data)
	    resultado_lexema.clear()
	    while True:
	        tok = analizador.token()
	        if not tok:
	            break
	        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
	        estado = "Linea {:4} Tipo {:13} Lexema {:13} Posicion {:2}".format(
	            str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
	        resultado_lexema.append(estado)
	    return resultado_lexema


tokens = (
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',
    'INICIO',
    'FIN',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'ESCRIBA',
    'LEER',
    'MINUSMINUS',
    'PLUSPLUS',

    # Condiones
    'SI',
    'SINO',
    # Ciclos
    'MIENTRAS',
    'PARA',
    # logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    # Symbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',

    # Otros
    'PUNTO',
    'PUNTOCOMA',
    'COMA',
    'COMIDOB'
)

# Reglas de Expresiones RegulAres para token de Un solo caracter

t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMIDOB = r'\"'





def t_ESCRIBA(t):
    r'P_'
    return t


def t_LEER(t):
    r'L_'
    return t


def t_ENDL(t):
    r'endl'
    return t


def t_SINO(t):
    r'SN_'
    return t


def t_SI(t):
    r'S_'
    return t


def t_RETURN(t):
    r'RETORNO'
    return t


def t_MIENTRAS(t):
    r'M_'
    return t


def t_PARA(t):
    r'P_'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t
def t_INICIO(t):
    r'\*(P)'
    return t
def t_FIN(t):
    r'\*(N)'
    return t

def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_NUMERAL(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUAL(t):
    r'=='
    return t


def t_MAYORDER(t):
    r'<<'
    return t


def t_MAYORIZQ(t):
    r'>>'
    return t


def t_DISTINTO(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")


def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

t_ignore = ' \t'
def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Lexema {:16} Posicion {:4}".format(str(t.lineno), str(t.value),str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)