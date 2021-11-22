import ply.yacc as yacc
from main import tokens

#INSTRUCCIÓN PRINCIPAL
def p_instrucciones(p):
    '''instrucciones : asignar
                        | noasignar
                         '''
    p[0] = p[1]
                        
def p_asignar(p):
    '''asignar : expression 
                | string
                | cadena
                | metodocadena
                | arreglo
                | metodosarreglo
                | hash
                | metodohash
                | boolean 
                | variables
                | assigns'''
    p[0] = p[1]


def p_noasignar(p):
    '''noasignar : estructurasControl
                    | oputs 
                    | putss
                    | putsenx 
                    | sentenIF
                    | sentenWHILE'''
    p[0] = p[1]


#BOOLEANOS

def p_boolean(p):
    '''boolean :  TRUE 
                | FALSE
                | NIL '''
    p[0] = p[1]

#IMPRESION      
          
def p_oputs(p):
    '''oputs : PUTS  '''
    p[0] = ''

def p_puts_String(p):

    ''' putss : PUTS string
              | PUTS cadena
              | PRINT string
              | PRINT cadena
            '''

    p[0] = p[1] + '' + p[2]



def p_puts_expression(p):
    ''' putsenx : PUTS expression
                | PRINT expression '''
    p[0]= str(p[2])



#algoritmo
def p_algoritmo(p):
    '''algoritmo : expression
                | metodocadena
                | arreglo
                | metodosarreglo
                | hash
                | estructurasControl
                | boolean
                | assigns
                | sentenIF
                | sentenWHILE '''



#while
def p_sentenwhile(p):
    ''' sentenWHILE : WHILE variables comparador  variables  algoritmo END
                    | WHILE variables comparador  expression  algoritmo END
                    | WHILE boolean  algoritmo END
                    | WHILE variables algoritmo   END'''
    p[0] = p[1] + p[2] + str(p[3])

def p_comparador(p):
    ''' comparador : COMPARE
                   | GREQUAL 
                   | LSEQUAL
                   | NOTEQUAL
                   | LESS
                   | GREATER '''
    p[0]= p[1]

#OPERADORES


#VARIABLES
def p_variables(p):
   '''variables : IDLOCAL
                | IDINSTANCE
                | IDCLASS
                | IDGLOBAL
                '''
   p[0] = p[1]

#ASIGNACIONES

def p_assigns(p):
    '''assigns : variables ASSIGN expression
                | variables ASSIGN variables
                | variables ASSIGN boolean
                | variables ASSIGN asignar
                '''
    p[0] = p[1] + p[2] + str(p[3])

def p_assigns_plus(p):
    '''assigns : variables ASSIGNPLUS expression
                    | variables ASSIGNPLUS variables

                    '''
    p[0] = p[1] + p[2] + str(p[3])

def p_assigns_min(p):
    '''assigns : variables ASSIGNMIN expression
                    | variables ASSIGNMIN variables
                    '''
    p[0] = p[1] + p[2] + str(p[3])

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

def p_expression_division(p):
    'expression : expression DIVISION term'
    p[0] = p[1] / p[3]

def p_expression_mod(p):
    'expression : expression MOD term'
    p[0] = p[1] % p[3]

def p_expression_mult(p):
    'expression : expression MULT term'
    p[0] = p[1] * p[3]

def p_expression_exp(p):
    'expression : expression EXP term'
    p[0] = p[1] ** p[3]

#CADENAS

def p_string_str(p):
    'string : STRINGV'
    p[0] = p[1]

def p_cadena_forma1(p):
    'cadena : STRING POINT NEW'
    p[0] = p[1] + p[2] + p[3]  

def p_cadena_forma2(p):
    'cadena : STRING POINT NEW LPARENTHESIS string RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]  

def p_cadena_forma3(p):
    'cadena : STRING LPARENTHESIS string RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4]


#'''def p_functionStr_empty(p):
#   'functionStr : type POINT ' '''


#CADENAS MÉTODOS 

def p_metodocadena_empty(p):
    '''metodocadena : cadena POINT EMPTY INTERROGATIVE
                    | string POINT EMPTY INTERROGATIVE'''
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_metodocadena_length(p):
    '''metodocadena : cadena POINT LENGTH
                    | string POINT LENGTH'''
    p[0] = p[1] + p[2] + p[3]



#ARREGLOS

def p_arreglo_tipo4(p):
    'arreglo : ARRAY POINT NEW'
    p[0] = p[1] + p[2] + p[3]  

def p_arreglo_tipo1(p):
    'arreglo : ARRAY POINT NEW LPARENTHESIS factor RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6]

def p_arreglo_tipo2(p):
    'arreglo : ARRAY POINT NEW LPARENTHESIS factor COMMA arraycontent RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6] + p[7] + p[8]

def p_arreglo_tipo3(p):
    'arreglo : ARRAY LSQBRACKET arraycontent RSQBRACKET'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_arreglo_tipo5(p):
    'arreglo : LSQBRACKET arraycontent RSQBRACKET'
    p[0] = p[1] + p[2] + p[3]

def p_arraycontent_var1(p):
    '''arraycontent : factor
                    | string'''
    p[0] = str(p[1])

def p_arraycontent_var2(p):
    '''arraycontent : factor COMMA arraycontent
                    | string COMMA arraycontent'''
    p[0] = str(p[1]) + p[2] + p[3]

#METODOS ARREGLOS

def p_metodosarreglo_index(p):
    'metodosarreglo : arreglo POINT INDEX LPARENTHESIS arraycontent RPARENTHESIS'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] 

def p_metodosarreglo_num(p):
    'metodosarreglo : arreglo LSQBRACKET factor RSQBRACKET'
    p[0] = p[1] + p[2] + str(p[3]) + p[4]

#HASH

def p_hash_tipo1(p):
    'hash : LBRACKET hashcontent RBRACKET'
    p[0] = p[1] + p[2] + p[3] 

def p_hash_tipo2(p):
    'hash : HASH POINT NEW'
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

#METODOS HASH

def p_metodohash_length(p):
    '''metodohash : variables ASSIGN hash POINT LENGTH'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_metodohash_length2(p):
    '''metodohash : variables POINT LENGTH'''
    p[0] = p[1] + p[2] + p[3]


#ESTRUCTURAS DE CONTROL

# IF

def p_if(p):
    ''' sentenIF : IF comparador term '''
    p[0]= p[1] + p[2] + str(p[3])

def p_comparador(p):
    ''' comparador : COMPARE
                   | GREQUAL 
                   | LSEQUAL
                   | NOTEQUAL
                   | LESS
                   | GREATER '''
    p[0]= p[1]
    

#FOR
def p_estructurasControl_for1(p):
    '''estructurasControl : FOR IDLOCAL IN factor POINT POINT factor DO BREAK IF END'''
    p[0] = p[1] + str(p[2]) + p[3] + str(p[4]) + p[5] + p[6] + str(p[7]) + p[8] + p[9] + p[10] + p[11]

def p_estructurasControl_for2(p):
    '''estructurasControl : FOR IDLOCAL IN factor POINT POINT factor DO END'''
    p[0] = p[1] +str(p[2]) + p[3] + str(p[4]) + p[5] + p[6] + str(p[7]) + p[8] + p[9] 


parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)