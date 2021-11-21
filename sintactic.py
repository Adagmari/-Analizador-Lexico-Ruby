import ply.yacc as yacc
from main import tokens

#INSTRUCCIÓN PRINCIPAL

def p_instrucciones(p):
    '''instrucciones : expression 
                        | cadena
                        | arreglo
                        | string
                        | hash
                        | boolean '''
    p[0] = p[1]


#BOOLEANOS

def p_boolean(p):
    '''boolean :  TRUE 
                | FALSE
                | NIL '''
    p[0] = p[1]
                


#NÚMEROS Y OPERACIONES 

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER
              | FLOAT'''
    p[0] = p[1]

def p_factor_numnegative(p):
    '''factor : MINUS NUMBER
              | MINUS FLOAT'''
    p[0] = p[1] + str(p[2])

#CADENAS

def p_string_str(p):
    'string : STRINGV'
    p[0] = p[1]

def p_cadena_forma1(p):
    'cadena : type POINT type'
    p[0] = p[1] + p[2] + p[3]  

def p_cadena_forma2(p):
    'cadena : type POINT type LPARENTHESIS string RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]  

def p_cadena_forma3(p):
    'cadena : type LPARENTHESIS string RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4]

'''def p_functionStr_empty(p):
    'functionStr : type POINT ' '''

#ARREGLOS

def p_arreglo_tipo1(p):
    'arreglo : type POINT type LPARENTHESIS factor RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6]

def p_arreglo_tipo2(p):
    'arreglo : type POINT type LPARENTHESIS factor COMMA arraycontent RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6] + p[7] + p[8]

def p_arreglo_tipo3(p):
    'arreglo : type LSQBRACKET arraycontent RSQBRACKET'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_arraycontent_var1(p):
    '''arraycontent : factor
                    | string'''
    p[0] = str(p[1])

def p_arraycontent_var2(p):
    '''arraycontent : factor COMMA arraycontent
                    | string COMMA arraycontent'''
    p[0] = str(p[1]) + p[2] + p[3]

#CADENAS MÉTODOS 

#def p_metodocadena_empty

#HASH

def p_hash_tipo1(p):
    'hash : LBRACKET hashcontent RBRACKET'
    p[0] = p[1] + p[2] + p[3] 

def p_hashcontent_var1(p):
    'hashcontent : string ASSIGN GREATER hashcontentvalue'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_hashcontent_var2(p):
    'hashcontent : string ASSIGN GREATER hashcontentvalue COMMA hashcontent'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_hashcontentvalue_var(p):
    '''hashcontentvalue : factor
                        | string'''
    p[0] = str(p[1])

#TIPOS - PALABRAS RESERVADAS

def p_type_String(p):
    'type : STRING'
    p[0] = p[1]

def p_type_Array(p):
    'type : ARRAY'
    p[0] = p[1]

def p_type_new(p):
    'type : NEW'
    p[0] = p[1]






parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)