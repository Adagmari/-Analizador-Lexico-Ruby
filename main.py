import ply.lex as lex



tokens = [
    'NUMBER',
    'BOOLEAN', 
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
    'defined?':'DEFINED?',
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
    'array':'ARRAY',
    'hash':'HASH'

   
}


tokens += list(reserved.values())