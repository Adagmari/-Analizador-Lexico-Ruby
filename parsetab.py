
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDS ARRAY ASSIGN ASSIGNMIN ASSIGNPLUS BREAK BSLASH CASE CLASS COMENTARIO COMID COMIS COMMA COMPARE DEF DEFINED DIVISION DO ELSE ELSIF END ENSURE EXP FALSE FLOAT FOR GETS GREATER GREQUAL HASH IDCLASS IDENTIFIER IDGLOBAL IDINSTANCE IDLOCAL IF IN LBRACKET LESS LPARENTHESIS LSEQUAL LSQBRACKET MINUS MOD MODULE MULT NEW NEXT NIL NOT NOTEQUAL NOTS NUMBER NUML OR ORS PLUS POINT PRINT PUTC PUTS RBRACKET REDO RESCUE RETURN RPARENTHESIS RSQBRACKET SELF SEMICOLON STRING STRINGV TRUE UNDEF UNTIL WHEN WHILEinstrucciones : expression \n                        | cadena\n                        | arreglo\n                        | string\n                        | hash\n                        | boolean boolean :  TRUE \n                | FALSE expression : expression PLUS termexpression : expression MINUS termexpression : termterm : factorfactor : NUMBER\n              | FLOATfactor : MINUS NUMBER\n              | MINUS FLOATstring : STRINGVcadena : type POINT typecadena : type POINT type LPARENTHESIS string RPARENTHESIScadena : type LPARENTHESIS string RPARENTHESISarreglo : type POINT type LPARENTHESIS factor RPARENTHESISarreglo : type POINT type LPARENTHESIS factor COMMA arraycontent RPARENTHESISarreglo : type LSQBRACKET arraycontent RSQBRACKETarraycontent : factor\n                    | stringarraycontent : factor COMMA arraycontent\n                    | string COMMA arraycontenthash : LBRACKET hashcontent RBRACKEThashcontent : string ASSIGN GREATER hashcontentvaluehashcontent : string ASSIGN GREATER hashcontentvalue COMMA hashcontenthashcontentvalue : factor\n                        | stringtype : STRINGtype : ARRAYtype : NEW'
    
_lr_action_items = {'STRINGV':([0,13,26,27,39,42,43,44,54,55,],[12,12,12,12,12,12,12,12,12,12,]),'LBRACKET':([0,],[13,]),'TRUE':([0,],[14,]),'FALSE':([0,],[15,]),'STRING':([0,25,],[16,16,]),'ARRAY':([0,25,],[17,17,]),'NEW':([0,25,],[18,18,]),'NUMBER':([0,9,21,22,27,39,42,43,44,54,],[19,23,19,19,19,19,19,19,19,19,]),'FLOAT':([0,9,21,22,27,39,42,43,44,54,],[20,24,20,20,20,20,20,20,20,20,]),'MINUS':([0,2,8,11,19,20,21,22,23,24,27,30,31,39,42,43,44,54,],[9,22,-11,-12,-13,-14,9,9,-15,-16,9,-9,-10,9,9,9,9,9,]),'$end':([1,2,3,4,5,6,7,8,11,12,14,15,16,17,18,19,20,23,24,30,31,32,37,40,41,52,53,58,],[0,-1,-2,-3,-4,-5,-6,-11,-12,-17,-7,-8,-33,-34,-35,-13,-14,-15,-16,-9,-10,-18,-28,-20,-23,-19,-21,-22,]),'PLUS':([2,8,11,19,20,23,24,30,31,],[21,-11,-12,-13,-14,-15,-16,-9,-10,]),'POINT':([10,16,17,18,],[25,-33,-34,-35,]),'LPARENTHESIS':([10,16,17,18,32,],[26,-33,-34,-35,39,]),'LSQBRACKET':([10,16,17,18,],[27,-33,-34,-35,]),'ASSIGN':([12,29,],[-17,38,]),'RPARENTHESIS':([12,19,20,23,24,33,35,36,45,46,47,48,56,],[-17,-13,-14,-15,-16,40,-24,-25,52,53,-26,-27,58,]),'COMMA':([12,19,20,23,24,35,36,46,49,50,51,],[-17,-13,-14,-15,-16,42,43,54,-32,55,-31,]),'RSQBRACKET':([12,19,20,23,24,34,35,36,47,48,],[-17,-13,-14,-15,-16,41,-24,-25,-26,-27,]),'RBRACKET':([12,19,20,23,24,28,49,50,51,57,],[-17,-13,-14,-15,-16,37,-32,-29,-31,-30,]),'GREATER':([38,],[44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'expression':([0,],[2,]),'cadena':([0,],[3,]),'arreglo':([0,],[4,]),'string':([0,13,26,27,39,42,43,44,54,55,],[5,29,33,36,45,36,36,49,36,29,]),'hash':([0,],[6,]),'boolean':([0,],[7,]),'term':([0,21,22,],[8,30,31,]),'type':([0,25,],[10,32,]),'factor':([0,21,22,27,39,42,43,44,54,],[11,11,11,35,46,35,35,51,35,]),'hashcontent':([13,55,],[28,57,]),'arraycontent':([27,42,43,54,],[34,47,48,56,]),'hashcontentvalue':([44,],[50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> expression','instrucciones',1,'p_instrucciones','sintactic.py',7),
  ('instrucciones -> cadena','instrucciones',1,'p_instrucciones','sintactic.py',8),
  ('instrucciones -> arreglo','instrucciones',1,'p_instrucciones','sintactic.py',9),
  ('instrucciones -> string','instrucciones',1,'p_instrucciones','sintactic.py',10),
  ('instrucciones -> hash','instrucciones',1,'p_instrucciones','sintactic.py',11),
  ('instrucciones -> boolean','instrucciones',1,'p_instrucciones','sintactic.py',12),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactic.py',19),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactic.py',20),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintactic.py',28),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintactic.py',32),
  ('expression -> term','expression',1,'p_expression_term','sintactic.py',36),
  ('term -> factor','term',1,'p_term_factor','sintactic.py',40),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactic.py',44),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactic.py',45),
  ('factor -> MINUS NUMBER','factor',2,'p_factor_numnegative','sintactic.py',49),
  ('factor -> MINUS FLOAT','factor',2,'p_factor_numnegative','sintactic.py',50),
  ('string -> STRINGV','string',1,'p_string_str','sintactic.py',56),
  ('cadena -> type POINT type','cadena',3,'p_cadena_forma1','sintactic.py',60),
  ('cadena -> type POINT type LPARENTHESIS string RPARENTHESIS','cadena',6,'p_cadena_forma2','sintactic.py',64),
  ('cadena -> type LPARENTHESIS string RPARENTHESIS','cadena',4,'p_cadena_forma3','sintactic.py',68),
  ('arreglo -> type POINT type LPARENTHESIS factor RPARENTHESIS','arreglo',6,'p_arreglo_tipo1','sintactic.py',77),
  ('arreglo -> type POINT type LPARENTHESIS factor COMMA arraycontent RPARENTHESIS','arreglo',8,'p_arreglo_tipo2','sintactic.py',81),
  ('arreglo -> type LSQBRACKET arraycontent RSQBRACKET','arreglo',4,'p_arreglo_tipo3','sintactic.py',85),
  ('arraycontent -> factor','arraycontent',1,'p_arraycontent_var1','sintactic.py',89),
  ('arraycontent -> string','arraycontent',1,'p_arraycontent_var1','sintactic.py',90),
  ('arraycontent -> factor COMMA arraycontent','arraycontent',3,'p_arraycontent_var2','sintactic.py',94),
  ('arraycontent -> string COMMA arraycontent','arraycontent',3,'p_arraycontent_var2','sintactic.py',95),
  ('hash -> LBRACKET hashcontent RBRACKET','hash',3,'p_hash_tipo1','sintactic.py',105),
  ('hashcontent -> string ASSIGN GREATER hashcontentvalue','hashcontent',4,'p_hashcontent_var1','sintactic.py',109),
  ('hashcontent -> string ASSIGN GREATER hashcontentvalue COMMA hashcontent','hashcontent',6,'p_hashcontent_var2','sintactic.py',113),
  ('hashcontentvalue -> factor','hashcontentvalue',1,'p_hashcontentvalue_var','sintactic.py',117),
  ('hashcontentvalue -> string','hashcontentvalue',1,'p_hashcontentvalue_var','sintactic.py',118),
  ('type -> STRING','type',1,'p_type_String','sintactic.py',124),
  ('type -> ARRAY','type',1,'p_type_Array','sintactic.py',128),
  ('type -> NEW','type',1,'p_type_new','sintactic.py',132),
]
