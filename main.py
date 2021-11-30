import ply.lex as lex

#Jeremy Ramírez{
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
    'Hash':'HASH',
    'Array':'ARRAY',
    'String':'STRING',
    'new':'NEW',
    'empty':'EMPTY',
    'length':'LENGTH',
    'index':'INDEX',
}
#Jeremy Ramírez}

#Diana Ramírez{
tokens = [
    'NUMBER',
    'FLOAT',
    'STRINGV',
    'COMENTARIO',
    'IDLOCAL',
    'IDINSTANCE',
    'IDCLASS',
    'IDGLOBAL',
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
    'ASSIGN',
    'ASSIGNPLUS',
    'ASSIGNMIN',
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
    'COMID',
    'BSLASH',
    'NUML',
    'INTERROGATIVE'
    

    
] + list(reserved.values())

#Diana Ramírez}



#t_STRINGV = r'((\'[\w\W\s][^\']*\')|(\"[\w\W\s][^\"]*\"))'
#Jeremy Ramírez{
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
t_ASSIGN = r'\='
#Jeremy Ramírez}

#-SANDY{
t_ASSIGNPLUS = r'\+='
t_ASSIGNMIN = r'\-='
#-SANDY}

#Diana Ramírez{
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
t_BSLASH = r'\\'
t_COMIS = r'\''
t_COMID = r'\"'
t_INTERROGATIVE = r'\?'


def t_STRINGV(t):
    r'((\'[\w\W\s]?[^\']*\')|(\"[\w\W\s]?[^\"]*\"))'
    t.value= str(t.value)
    return t
#Diana Ramírez}

#SANDY{
def t_IDLOCAL(t):
    r'([a-z][a-zA-Z0-9_]*|[_][a-zA-Z0-9_]*)'
    t.type = reserved.get(t.value, 'IDLOCAL')
    return t
def t_IDINSTANCE(t):
    r'^[@][a-zA-Z0-9_]*$'
    t.type = reserved.get(t.value, 'IDINSTANCE')
    return t
def t_IDCLASS(t):
    r'([@]{2})[a-zA-Z0-9_]+'
    t.type = reserved.get(t.value, 'IDCLASS')
    return t
def t_IDGLOBAL(t):
    r'\s*[\$][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDGLOBAL')
    return t
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t
#-SANDY}

#Jeremy Ramírez{

def t_FLOAT(t):
     r'(\d+\.\d+)'
     t.value= float(t.value)
     return t

def t_NUML(t):
     r'[0-9]{3}_[0-9]{3}((_[0-9]{3})+)?'
     return t
       
def t_NUMBER(t):
     r'\d+'
     t.value= int(t.value)
     return t

     



#Jeremy Ramírez}

#Diana Ramírez{
def t_COMMENT(t):
    r'\#.*'
    pass
#Diana Ramírez}

#Jeremy Ramírez{
t_ignore = " \t" # Qué tipo de caracteres debe ignorar Ruby?

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
#Jeremy Ramírez}


#Diana Ramírez{
lexer = lex.lex()

"""def inputLex(s):
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

"""

def inputLex(s):
    lexer.input(s)
    resultado=""
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        resultado += str(tok) + "\n"
    return resultado


file = open("archivo.txt", encoding="utf8")  
for line in file:
    inputLex(line)
    
#Diana Ramírez}