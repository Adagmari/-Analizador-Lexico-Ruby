import ply.lex as lex



tokens = [
    'NUMBER',
    'STRINGV',
    'IDENTIFIER',
    'COMPARE',
    'MINUS',
    'PLUS',
    'DIVISION',
    'MOD',
    'MULT',
    'EXP',
    'LESS',
    'GREATER',
    'RPARENTHESIS',
    'LPARENTHESIS',
    'ASSING',
    'POINT',
    'COMMA',
    'SEMICOLON',
    'LSQBRACKET',
    'RSQBRACKET',
    'LBRACKET',
    'RBRACKET',
    'NOTS',
    'ANDS',
    'ORS',
    'GREQUAL',
    'LSEQUAL',
    'NOTEQUAL',
    'COMIS',
    'COMID'
]



reserved = {
    'class':'CLASS',
    'and':'AND',
    'break':'BREAK',
    'case': 'CASE',
    'def':'DEF',
    'defined':'DEFINED',
    'do':'DO',
    'else': 'ELSE',
    'elsif':'ELSIF',
    'end':'END',
    'ensure':'ENSURE',
    'false':'FALSE',
    'true':'TRUE',
    'for':'FOR',
    'if':'IF',
    'in':'IN',
    'module':'MODULE',
    'next':'NEXT',
    'nil':'NIL',
    'not':'NOT',
    'or':'OR',
    'redo':'REDO',
    'rescue':'RESCUE',
    'return':'RETURN',
    'self':'SELF',
    'until':'UNTIL',
    'when':'WHEN',
    'while':'WHILE',
    'undef':'UNDEF',
    'puts':'PUTS',
    'gets':'GETS',
    'print':'PRINT',
    'putc':'PUTC',
    'Array':'ARRAY',
    'Hash':'HASH',
    'String':'STRING',
    'new':'NEW'
}


tokens += list(reserved.values())


#t_STRINGV = r'((\'[\w\W\s][^\']*\')|(\"[\w\W\s][^\"]*\"))'
t_COMPARE = r'==='
t_MINUS = r'-'
t_PLUS = r'\+'
t_DIVISION = r'\/'
t_MOD = r'%'
t_MULT = r'\*'
t_EXP = r'\*\*'
t_LESS = r'<'
t_GREATER = r'>'
t_RPARENTHESIS = r'\)'
t_LPARENTHESIS = r'\('
t_ASSING = r'='
t_POINT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_NOTS = r'!'
t_ANDS = r'&&'
t_ORS = r'\|\|'
t_GREQUAL = r'>='
t_LSEQUAL = r'<='
t_NOTEQUAL = r'!='


def t_STRINGV(t):
    r'((\'[\w\W\s][^\']*\')|(\"[\w\W\s][^\"]*\"))'
    t.value= str(t.value)
    return t

#def t_NUMBER():

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t
    

def t_COMMENT(t):
    r'((?!.*\n)\#.*)|(\=begin(\n|.)*\=end)'
    pass

t_ignore = " \t" # Qué tipo de caracteres debe ignorar Ruby?

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")




lexer = lex.lex()


def inputLex(s):
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

file = open("archivo.txt", encoding="utf8")  

for line in file:
    inputLex(line)