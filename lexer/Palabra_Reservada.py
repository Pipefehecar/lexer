class lenguaje():
    def__init__(self):
        global reservada, tokens
        reservada = (
            # Palabras Reservadas
            'NELSON',
            'NULL',
            'LUIS_FELIPE',
            'PI',
            'NUEVO',
        )
        tokens = reservada + (
            'IDENTIFICADOR',
            'ENTERO',
            'ASIGNAR',

            'SUMA',
            'RESTA',
            'MULT',
            'DIV',
            'POTENCIA',
            'MODULO',

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
            'PUNTOCOMA',
            'COMA',
            'COMDOB',
            'MAYORDER',  # >>
            'MAYORIZQ',  # <<
        )
