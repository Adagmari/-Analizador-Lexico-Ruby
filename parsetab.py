
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDS ARRAY ASSIGN ASSIGNMIN ASSIGNPLUS BREAK BSLASH CASE CLASS COMENTARIO COMID COMIS COMMA COMPARE DEF DEFINED DIVISION DO ELSE ELSIF EMPTY END ENSURE EXP FALSE FLOAT FOR GETS GREATER GREQUAL HASH IDCLASS IDENTIFIER IDGLOBAL IDINSTANCE IDLOCAL IF IN INDEX INTERROGATIVE LBRACKET LENGTH LESS LPARENTHESIS LSEQUAL LSQBRACKET MINUS MOD MODULE MULT NEW NEXT NIL NOT NOTEQUAL NOTS NUMBER NUML OR ORS PLUS POINT PRINT PUTC PUTS RBRACKET REDO RESCUE RETURN RPARENTHESIS RSQBRACKET SELF SEMICOLON STRING STRINGV TRUE UNDEF UNTIL WHEN WHILEinstrucciones : asignar\n                        | noasignar\n                         asignar : expression \n                | string\n                | cadena\n                | metodocadena\n                | arreglo\n                | metodosarreglo\n                | hash\n                | metodohash\n                | boolean \n                | variables\n                | assignsnoasignar : estructurasControl\n                    | oputs \n                    | putss\n                    | putsenx \n                    | sentenIF\n                    | sentenifp\n                    | sentenWHILEboolean :  TRUE \n                | FALSE\n                | NIL oputs : PUTS   putss : PUTS string\n              | PUTS cadena\n              | PRINT string\n              | PRINT cadena\n             putsenx : PUTS expression\n                | PRINT expression algoritmo : expression\n                | metodocadena\n                | arreglo\n                | metodosarreglo\n                | hash\n                | estructurasControl\n                | boolean\n                | assigns\n                | sentenIF\n                | sentenifp\n                | variables\n                | sentenWHILE  sentenWHILE : WHILE variables comparador  variables  algoritmo END\n                    | WHILE variables comparador  expression  algoritmo END\n                    | WHILE boolean  algoritmo END\n                    | WHILE variables algoritmo   END sentenIF : IF variables comparador term  sentenifp : IF variables comparador term algoritmo ENDvariables : IDLOCAL\n                | IDINSTANCE\n                | IDCLASS\n                | IDGLOBAL\n                assigns : variables ASSIGN expression\n                | variables ASSIGN variables\n                | variables ASSIGN boolean\n                | variables ASSIGN asignar\n                assigns : variables ASSIGNPLUS expression\n                    | variables ASSIGNPLUS variables\n\n                    assigns : variables ASSIGNMIN expression\n                    | variables ASSIGNMIN variables\n                    expression : expression PLUS termexpression : expression MINUS termexpression : termterm : factorfactor : NUMBER\n              | FLOATfactor : MINUS NUMBER\n              | MINUS FLOATexpression : expression DIVISION termexpression : expression MOD termexpression : expression MULT termexpression : expression EXP termstring : STRINGVcadena : STRING POINT NEWcadena : STRING POINT NEW LPARENTHESIS string RPARENTHESIScadena : STRING LPARENTHESIS string RPARENTHESISmetodocadena : cadena POINT EMPTY INTERROGATIVE\n                    | string POINT EMPTY INTERROGATIVEmetodocadena : cadena POINT LENGTH\n                    | string POINT LENGTHarreglo : ARRAY POINT NEWarreglo : ARRAY POINT NEW LPARENTHESIS factor RPARENTHESISarreglo : ARRAY POINT NEW LPARENTHESIS factor COMMA arraycontent RPARENTHESISarreglo : ARRAY LSQBRACKET arraycontent RSQBRACKETarreglo : LSQBRACKET arraycontent RSQBRACKETarraycontent : factor\n                    | stringarraycontent : factor COMMA arraycontent\n                    | string COMMA arraycontentmetodosarreglo : arreglo POINT INDEX LPARENTHESIS arraycontent RPARENTHESISmetodosarreglo : arreglo LSQBRACKET factor RSQBRACKEThash : LBRACKET hashcontent RBRACKEThash : HASH POINT NEWhashcontent : string ASSIGN GREATER hashcontentvaluehashcontent : string ASSIGN GREATER hashcontentvalue COMMA hashcontenthashcontentvalue : factor\n                        | stringmetodohash : variables ASSIGN hash POINT LENGTHmetodohash : variables POINT LENGTH comparador : COMPARE\n                   | GREQUAL \n                   | LSEQUAL\n                   | NOTEQUAL\n                   | LESS\n                   | GREATER estructurasControl : FOR IDLOCAL IN factor POINT POINT factor DO BREAK IF ENDestructurasControl : FOR IDLOCAL IN factor POINT POINT factor DO END'
    
_lr_action_items = {'STRINGV':([0,22,27,28,29,31,32,33,34,35,36,37,40,41,43,44,55,59,60,62,64,79,80,81,82,83,84,85,86,108,109,140,143,149,151,152,153,154,172,173,178,179,],[24,-63,-64,24,24,-21,-22,-23,-49,-50,-51,-52,24,24,-65,-66,24,-67,-68,24,24,24,24,-61,-62,-69,-70,-71,-72,24,24,24,24,24,24,24,24,24,24,24,-65,-66,]),'STRING':([0,22,27,31,32,33,34,35,36,37,40,41,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[25,-63,-64,-21,-22,-23,-49,-50,-51,-52,25,25,-65,-66,25,-67,-68,25,25,-61,-62,-69,-70,-71,-72,25,25,25,25,-65,-66,]),'ARRAY':([0,22,27,31,32,33,34,35,36,37,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[26,-63,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,26,-67,-68,26,26,-61,-62,-69,-70,-71,-72,26,26,26,26,-65,-66,]),'LSQBRACKET':([0,8,22,26,27,31,32,33,34,35,36,37,43,44,55,59,60,79,80,81,82,83,84,85,86,105,107,126,146,151,152,153,154,171,178,179,183,],[28,54,-63,64,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,28,-67,-68,28,28,-61,-62,-69,-70,-71,-72,-81,-85,54,-84,28,28,28,28,-82,-65,-66,-83,]),'LBRACKET':([0,22,27,31,32,33,34,35,36,37,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[29,-63,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,29,-67,-68,29,29,-61,-62,-69,-70,-71,-72,29,29,29,29,-65,-66,]),'HASH':([0,22,27,31,32,33,34,35,36,37,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[30,-63,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,30,-67,-68,30,30,-61,-62,-69,-70,-71,-72,30,30,30,30,-65,-66,]),'TRUE':([0,22,27,31,32,33,34,35,36,37,42,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[31,-63,-64,-21,-22,-23,-49,-50,-51,-52,31,-65,-66,31,-67,-68,31,31,-61,-62,-69,-70,-71,-72,31,31,31,31,-65,-66,]),'FALSE':([0,22,27,31,32,33,34,35,36,37,42,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[32,-63,-64,-21,-22,-23,-49,-50,-51,-52,32,-65,-66,32,-67,-68,32,32,-61,-62,-69,-70,-71,-72,32,32,32,32,-65,-66,]),'NIL':([0,22,27,31,32,33,34,35,36,37,42,43,44,55,59,60,79,80,81,82,83,84,85,86,151,152,153,154,178,179,],[33,-63,-64,-21,-22,-23,-49,-50,-51,-52,33,-65,-66,33,-67,-68,33,33,-61,-62,-69,-70,-71,-72,33,33,33,33,-65,-66,]),'IDLOCAL':([0,22,27,31,32,33,34,35,36,37,38,39,42,43,44,55,57,58,59,60,79,80,81,82,83,84,85,86,115,116,117,118,119,120,122,151,152,153,154,178,179,],[34,-63,-64,-21,-22,-23,-49,-50,-51,-52,71,34,34,-65,-66,34,34,34,-67,-68,34,34,-61,-62,-69,-70,-71,-72,-100,-101,-102,-103,-104,-105,34,34,34,34,34,-65,-66,]),'IDINSTANCE':([0,22,27,31,32,33,34,35,36,37,39,42,43,44,55,57,58,59,60,79,80,81,82,83,84,85,86,115,116,117,118,119,120,122,151,152,153,154,178,179,],[35,-63,-64,-21,-22,-23,-49,-50,-51,-52,35,35,-65,-66,35,35,35,-67,-68,35,35,-61,-62,-69,-70,-71,-72,-100,-101,-102,-103,-104,-105,35,35,35,35,35,-65,-66,]),'IDCLASS':([0,22,27,31,32,33,34,35,36,37,39,42,43,44,55,57,58,59,60,79,80,81,82,83,84,85,86,115,116,117,118,119,120,122,151,152,153,154,178,179,],[36,-63,-64,-21,-22,-23,-49,-50,-51,-52,36,36,-65,-66,36,36,36,-67,-68,36,36,-61,-62,-69,-70,-71,-72,-100,-101,-102,-103,-104,-105,36,36,36,36,36,-65,-66,]),'IDGLOBAL':([0,22,27,31,32,33,34,35,36,37,39,42,43,44,55,57,58,59,60,79,80,81,82,83,84,85,86,115,116,117,118,119,120,122,151,152,153,154,178,179,],[37,-63,-64,-21,-22,-23,-49,-50,-51,-52,37,37,-65,-66,37,37,37,-67,-68,37,37,-61,-62,-69,-70,-71,-72,-100,-101,-102,-103,-104,-105,37,37,37,37,37,-65,-66,]),'FOR':([0,22,27,31,32,33,34,35,36,37,43,44,59,60,79,80,81,82,83,84,85,86,151,153,154,178,179,],[38,-63,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,-67,-68,38,38,-61,-62,-69,-70,-71,-72,38,38,38,-65,-66,]),'PUTS':([0,],[40,]),'PRINT':([0,],[41,]),'IF':([0,22,27,31,32,33,34,35,36,37,43,44,59,60,79,80,81,82,83,84,85,86,151,153,154,178,179,185,],[39,-63,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,-67,-68,39,39,-61,-62,-69,-70,-71,-72,39,39,39,-65,-66,187,]),'WHILE':([0,22,27,31,32,33,34,35,36,37,43,44,59,60,79,80,81,82,83,84,85,86,151,153,154,178,179,],[42,-63,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,-67,-68,42,42,-61,-62,-69,-70,-71,-72,42,42,42,-65,-66,]),'NUMBER':([0,22,23,27,28,31,32,33,34,35,36,37,40,41,43,44,45,46,47,48,49,50,54,55,57,58,59,60,64,79,80,81,82,83,84,85,86,108,109,113,114,115,116,117,118,119,120,122,140,145,149,151,152,153,154,168,172,174,178,179,],[43,-63,59,-64,43,-21,-22,-23,-49,-50,-51,-52,43,43,-65,-66,43,43,43,43,43,43,43,43,43,43,-67,-68,43,43,43,-61,-62,-69,-70,-71,-72,43,43,43,43,-100,-101,-102,-103,-104,-105,43,43,43,43,43,43,43,43,178,43,43,-65,-66,]),'FLOAT':([0,22,23,27,28,31,32,33,34,35,36,37,40,41,43,44,45,46,47,48,49,50,54,55,57,58,59,60,64,79,80,81,82,83,84,85,86,108,109,113,114,115,116,117,118,119,120,122,140,145,149,151,152,153,154,168,172,174,178,179,],[44,-63,60,-64,44,-21,-22,-23,-49,-50,-51,-52,44,44,-65,-66,44,44,44,44,44,44,44,44,44,44,-67,-68,44,44,44,-61,-62,-69,-70,-71,-72,44,44,44,44,-100,-101,-102,-103,-104,-105,44,44,44,44,44,44,44,44,179,44,44,-65,-66,]),'MINUS':([0,4,22,27,28,31,32,33,34,35,36,37,40,41,43,44,45,46,47,48,49,50,54,55,57,58,59,60,64,75,78,79,80,81,82,83,84,85,86,95,100,102,108,109,113,114,115,116,117,118,119,120,122,124,140,145,149,151,152,153,154,168,172,174,178,179,],[23,46,-63,-64,23,-21,-22,-23,-49,-50,-51,-52,23,23,-65,-66,23,23,23,23,23,23,23,23,23,23,-67,-68,23,46,46,23,23,-61,-62,-69,-70,-71,-72,46,46,46,23,23,23,23,-100,-101,-102,-103,-104,-105,23,46,23,23,23,23,23,23,168,23,23,23,-65,-66,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,27,31,32,33,34,35,36,37,40,43,44,59,60,73,74,75,76,77,78,81,82,83,84,85,86,88,90,93,94,95,96,97,98,99,100,101,102,103,105,107,110,112,138,139,141,144,146,151,155,156,158,169,170,171,175,176,177,183,186,188,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-63,-73,-64,-21,-22,-23,-49,-50,-51,-52,-24,-65,-66,-67,-68,-25,-26,-29,-27,-28,-30,-61,-62,-69,-70,-71,-72,-80,-79,-12,-9,-3,-11,-56,-99,-58,-57,-60,-59,-74,-81,-85,-92,-93,-78,-77,-91,-76,-84,-47,-46,-45,-98,-90,-75,-82,-48,-43,-44,-83,-107,-106,]),'PLUS':([4,22,27,43,44,59,60,75,78,81,82,83,84,85,86,95,100,102,124,154,178,179,],[45,-63,-64,-65,-66,-67,-68,45,45,-61,-62,-69,-70,-71,-72,45,45,45,45,45,-65,-66,]),'DIVISION':([4,22,27,43,44,59,60,75,78,81,82,83,84,85,86,95,100,102,124,154,178,179,],[47,-63,-64,-65,-66,-67,-68,47,47,-61,-62,-69,-70,-71,-72,47,47,47,47,47,-65,-66,]),'MOD':([4,22,27,43,44,59,60,75,78,81,82,83,84,85,86,95,100,102,124,154,178,179,],[48,-63,-64,-65,-66,-67,-68,48,48,-61,-62,-69,-70,-71,-72,48,48,48,48,48,-65,-66,]),'MULT':([4,22,27,43,44,59,60,75,78,81,82,83,84,85,86,95,100,102,124,154,178,179,],[49,-63,-64,-65,-66,-67,-68,49,49,-61,-62,-69,-70,-71,-72,49,49,49,49,49,-65,-66,]),'EXP':([4,22,27,43,44,59,60,75,78,81,82,83,84,85,86,95,100,102,124,154,178,179,],[50,-63,-64,-65,-66,-67,-68,50,50,-61,-62,-69,-70,-71,-72,50,50,50,50,50,-65,-66,]),'END':([5,6,7,8,9,10,11,14,22,24,27,31,32,33,34,35,36,37,43,44,59,60,81,82,83,84,85,86,88,90,93,94,95,96,97,98,99,100,101,102,103,105,107,110,112,121,123,124,125,126,127,128,129,130,131,132,133,134,137,138,139,141,144,146,151,155,156,158,165,166,167,169,170,171,175,176,177,178,179,183,184,186,187,188,],[-4,-5,-6,-7,-8,-9,-10,-13,-63,-73,-64,-21,-22,-23,-49,-50,-51,-52,-65,-66,-67,-68,-61,-62,-69,-70,-71,-72,-80,-79,-12,-9,-3,-11,-56,-99,-58,-57,-60,-59,-74,-81,-85,-92,-93,-41,155,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,156,-78,-77,-91,-76,-84,-47,-46,-45,-98,175,176,177,-90,-75,-82,-48,-43,-44,-65,-66,-83,186,-107,188,-106,]),'POINT':([5,6,8,13,24,25,26,30,34,35,36,37,43,44,59,60,93,94,103,105,107,110,112,126,135,136,144,146,150,164,170,171,183,],[51,52,53,56,-73,61,63,70,-49,-50,-51,-52,-65,-66,-67,-68,56,142,-74,-81,-85,-92,-93,53,52,51,-76,-84,164,174,-75,-82,-83,]),'ASSIGN':([13,24,34,35,36,37,69,93,121,],[55,-73,-49,-50,-51,-52,111,55,152,]),'ASSIGNPLUS':([13,34,35,36,37,93,121,],[57,-49,-50,-51,-52,57,57,]),'ASSIGNMIN':([13,34,35,36,37,93,121,],[58,-49,-50,-51,-52,58,58,]),'COMMA':([24,43,44,59,60,66,67,160,161,162,163,],[-73,-65,-66,-67,-68,108,109,172,-97,173,-96,]),'RSQBRACKET':([24,43,44,59,60,65,66,67,92,106,147,148,],[-73,-65,-66,-67,-68,107,-86,-87,141,146,-88,-89,]),'RPARENTHESIS':([24,43,44,59,60,66,67,104,147,148,157,159,160,180,],[-73,-65,-66,-67,-68,-86,-87,144,-88,-89,169,170,171,183,]),'RBRACKET':([24,43,44,59,60,68,161,162,163,181,],[-73,-65,-66,-67,-68,110,-97,-94,-96,-95,]),'LPARENTHESIS':([25,91,103,105,],[62,140,143,145,]),'COMPARE':([34,35,36,37,72,79,],[-49,-50,-51,-52,115,115,]),'GREQUAL':([34,35,36,37,72,79,],[-49,-50,-51,-52,116,116,]),'LSEQUAL':([34,35,36,37,72,79,],[-49,-50,-51,-52,117,117,]),'NOTEQUAL':([34,35,36,37,72,79,],[-49,-50,-51,-52,118,118,]),'LESS':([34,35,36,37,72,79,],[-49,-50,-51,-52,119,119,]),'GREATER':([34,35,36,37,72,79,111,],[-49,-50,-51,-52,120,120,149,]),'DO':([43,44,59,60,182,],[-65,-66,-67,-68,184,]),'EMPTY':([51,52,],[87,89,]),'LENGTH':([51,52,56,142,],[88,90,98,158,]),'INDEX':([53,],[91,]),'NEW':([61,63,70,],[103,105,112,]),'IN':([71,],[113,]),'INTERROGATIVE':([87,89,],[138,139,]),'BREAK':([184,],[185,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'asignar':([0,55,152,],[2,97,97,]),'noasignar':([0,],[3,]),'expression':([0,40,41,55,57,58,79,80,122,151,152,153,154,],[4,75,78,95,100,102,124,124,154,124,95,124,124,]),'string':([0,28,29,40,41,55,62,64,79,80,108,109,140,143,149,151,152,153,154,172,173,],[5,67,69,73,76,5,104,67,136,136,67,67,67,159,161,136,5,136,136,67,69,]),'cadena':([0,40,41,55,79,80,151,152,153,154,],[6,74,77,6,135,135,135,6,135,135,]),'metodocadena':([0,55,79,80,151,152,153,154,],[7,7,125,125,125,7,125,125,]),'arreglo':([0,55,79,80,151,152,153,154,],[8,8,126,126,126,8,126,126,]),'metodosarreglo':([0,55,79,80,151,152,153,154,],[9,9,127,127,127,9,127,127,]),'hash':([0,55,79,80,151,152,153,154,],[10,94,128,128,128,10,128,128,]),'metodohash':([0,55,152,],[11,11,11,]),'boolean':([0,42,55,79,80,151,152,153,154,],[12,80,96,130,130,130,96,130,130,]),'variables':([0,39,42,55,57,58,79,80,122,151,152,153,154,],[13,72,79,93,99,101,121,121,153,121,93,121,121,]),'assigns':([0,55,79,80,151,152,153,154,],[14,14,131,131,131,14,131,131,]),'estructurasControl':([0,79,80,151,153,154,],[15,129,129,129,129,129,]),'oputs':([0,],[16,]),'putss':([0,],[17,]),'putsenx':([0,],[18,]),'sentenIF':([0,79,80,151,153,154,],[19,132,132,132,132,132,]),'sentenifp':([0,79,80,151,153,154,],[20,133,133,133,133,133,]),'sentenWHILE':([0,79,80,151,153,154,],[21,134,134,134,134,134,]),'term':([0,40,41,45,46,47,48,49,50,55,57,58,79,80,114,122,151,152,153,154,168,],[22,22,22,81,82,83,84,85,86,22,22,22,22,22,151,22,22,22,22,22,82,]),'factor':([0,28,40,41,45,46,47,48,49,50,54,55,57,58,64,79,80,108,109,113,114,122,140,145,149,151,152,153,154,168,172,174,],[27,66,27,27,27,27,27,27,27,27,92,27,27,27,66,27,27,66,66,150,27,27,66,160,163,27,27,27,27,27,66,182,]),'arraycontent':([28,64,108,109,140,172,],[65,106,147,148,157,180,]),'hashcontent':([29,173,],[68,181,]),'comparador':([72,79,],[114,122,]),'algoritmo':([79,80,151,153,154,],[123,137,165,166,167,]),'hashcontentvalue':([149,],[162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> asignar','instrucciones',1,'p_instrucciones','sintactic.py',6),
  ('instrucciones -> noasignar','instrucciones',1,'p_instrucciones','sintactic.py',7),
  ('asignar -> expression','asignar',1,'p_asignar','sintactic.py',12),
  ('asignar -> string','asignar',1,'p_asignar','sintactic.py',13),
  ('asignar -> cadena','asignar',1,'p_asignar','sintactic.py',14),
  ('asignar -> metodocadena','asignar',1,'p_asignar','sintactic.py',15),
  ('asignar -> arreglo','asignar',1,'p_asignar','sintactic.py',16),
  ('asignar -> metodosarreglo','asignar',1,'p_asignar','sintactic.py',17),
  ('asignar -> hash','asignar',1,'p_asignar','sintactic.py',18),
  ('asignar -> metodohash','asignar',1,'p_asignar','sintactic.py',19),
  ('asignar -> boolean','asignar',1,'p_asignar','sintactic.py',20),
  ('asignar -> variables','asignar',1,'p_asignar','sintactic.py',21),
  ('asignar -> assigns','asignar',1,'p_asignar','sintactic.py',22),
  ('noasignar -> estructurasControl','noasignar',1,'p_noasignar','sintactic.py',27),
  ('noasignar -> oputs','noasignar',1,'p_noasignar','sintactic.py',28),
  ('noasignar -> putss','noasignar',1,'p_noasignar','sintactic.py',29),
  ('noasignar -> putsenx','noasignar',1,'p_noasignar','sintactic.py',30),
  ('noasignar -> sentenIF','noasignar',1,'p_noasignar','sintactic.py',31),
  ('noasignar -> sentenifp','noasignar',1,'p_noasignar','sintactic.py',32),
  ('noasignar -> sentenWHILE','noasignar',1,'p_noasignar','sintactic.py',33),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactic.py',40),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactic.py',41),
  ('boolean -> NIL','boolean',1,'p_boolean','sintactic.py',42),
  ('oputs -> PUTS','oputs',1,'p_oputs','sintactic.py',48),
  ('putss -> PUTS string','putss',2,'p_puts_String','sintactic.py',52),
  ('putss -> PUTS cadena','putss',2,'p_puts_String','sintactic.py',53),
  ('putss -> PRINT string','putss',2,'p_puts_String','sintactic.py',54),
  ('putss -> PRINT cadena','putss',2,'p_puts_String','sintactic.py',55),
  ('putsenx -> PUTS expression','putsenx',2,'p_puts_expression','sintactic.py',64),
  ('putsenx -> PRINT expression','putsenx',2,'p_puts_expression','sintactic.py',65),
  ('algoritmo -> expression','algoritmo',1,'p_algoritmo','sintactic.py',72),
  ('algoritmo -> metodocadena','algoritmo',1,'p_algoritmo','sintactic.py',73),
  ('algoritmo -> arreglo','algoritmo',1,'p_algoritmo','sintactic.py',74),
  ('algoritmo -> metodosarreglo','algoritmo',1,'p_algoritmo','sintactic.py',75),
  ('algoritmo -> hash','algoritmo',1,'p_algoritmo','sintactic.py',76),
  ('algoritmo -> estructurasControl','algoritmo',1,'p_algoritmo','sintactic.py',77),
  ('algoritmo -> boolean','algoritmo',1,'p_algoritmo','sintactic.py',78),
  ('algoritmo -> assigns','algoritmo',1,'p_algoritmo','sintactic.py',79),
  ('algoritmo -> sentenIF','algoritmo',1,'p_algoritmo','sintactic.py',80),
  ('algoritmo -> sentenifp','algoritmo',1,'p_algoritmo','sintactic.py',81),
  ('algoritmo -> variables','algoritmo',1,'p_algoritmo','sintactic.py',82),
  ('algoritmo -> sentenWHILE','algoritmo',1,'p_algoritmo','sintactic.py',83),
  ('sentenWHILE -> WHILE variables comparador variables algoritmo END','sentenWHILE',6,'p_sentenwhile','sintactic.py',89),
  ('sentenWHILE -> WHILE variables comparador expression algoritmo END','sentenWHILE',6,'p_sentenwhile','sintactic.py',90),
  ('sentenWHILE -> WHILE boolean algoritmo END','sentenWHILE',4,'p_sentenwhile','sintactic.py',91),
  ('sentenWHILE -> WHILE variables algoritmo END','sentenWHILE',4,'p_sentenwhile','sintactic.py',92),
  ('sentenIF -> IF variables comparador term','sentenIF',4,'p_if','sintactic.py',107),
  ('sentenifp -> IF variables comparador term algoritmo END','sentenifp',6,'p_vif','sintactic.py',112),
  ('variables -> IDLOCAL','variables',1,'p_variables','sintactic.py',118),
  ('variables -> IDINSTANCE','variables',1,'p_variables','sintactic.py',119),
  ('variables -> IDCLASS','variables',1,'p_variables','sintactic.py',120),
  ('variables -> IDGLOBAL','variables',1,'p_variables','sintactic.py',121),
  ('assigns -> variables ASSIGN expression','assigns',3,'p_assigns','sintactic.py',128),
  ('assigns -> variables ASSIGN variables','assigns',3,'p_assigns','sintactic.py',129),
  ('assigns -> variables ASSIGN boolean','assigns',3,'p_assigns','sintactic.py',130),
  ('assigns -> variables ASSIGN asignar','assigns',3,'p_assigns','sintactic.py',131),
  ('assigns -> variables ASSIGNPLUS expression','assigns',3,'p_assigns_plus','sintactic.py',136),
  ('assigns -> variables ASSIGNPLUS variables','assigns',3,'p_assigns_plus','sintactic.py',137),
  ('assigns -> variables ASSIGNMIN expression','assigns',3,'p_assigns_min','sintactic.py',143),
  ('assigns -> variables ASSIGNMIN variables','assigns',3,'p_assigns_min','sintactic.py',144),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintactic.py',151),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintactic.py',155),
  ('expression -> term','expression',1,'p_expression_term','sintactic.py',159),
  ('term -> factor','term',1,'p_term_factor','sintactic.py',163),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactic.py',167),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactic.py',168),
  ('factor -> MINUS NUMBER','factor',2,'p_factor_numnegative','sintactic.py',172),
  ('factor -> MINUS FLOAT','factor',2,'p_factor_numnegative','sintactic.py',173),
  ('expression -> expression DIVISION term','expression',3,'p_expression_division','sintactic.py',177),
  ('expression -> expression MOD term','expression',3,'p_expression_mod','sintactic.py',181),
  ('expression -> expression MULT term','expression',3,'p_expression_mult','sintactic.py',185),
  ('expression -> expression EXP term','expression',3,'p_expression_exp','sintactic.py',189),
  ('string -> STRINGV','string',1,'p_string_str','sintactic.py',195),
  ('cadena -> STRING POINT NEW','cadena',3,'p_cadena_forma1','sintactic.py',199),
  ('cadena -> STRING POINT NEW LPARENTHESIS string RPARENTHESIS','cadena',6,'p_cadena_forma2','sintactic.py',203),
  ('cadena -> STRING LPARENTHESIS string RPARENTHESIS','cadena',4,'p_cadena_forma3','sintactic.py',207),
  ('metodocadena -> cadena POINT EMPTY INTERROGATIVE','metodocadena',4,'p_metodocadena_empty','sintactic.py',218),
  ('metodocadena -> string POINT EMPTY INTERROGATIVE','metodocadena',4,'p_metodocadena_empty','sintactic.py',219),
  ('metodocadena -> cadena POINT LENGTH','metodocadena',3,'p_metodocadena_length','sintactic.py',223),
  ('metodocadena -> string POINT LENGTH','metodocadena',3,'p_metodocadena_length','sintactic.py',224),
  ('arreglo -> ARRAY POINT NEW','arreglo',3,'p_arreglo_tipo4','sintactic.py',232),
  ('arreglo -> ARRAY POINT NEW LPARENTHESIS factor RPARENTHESIS','arreglo',6,'p_arreglo_tipo1','sintactic.py',236),
  ('arreglo -> ARRAY POINT NEW LPARENTHESIS factor COMMA arraycontent RPARENTHESIS','arreglo',8,'p_arreglo_tipo2','sintactic.py',240),
  ('arreglo -> ARRAY LSQBRACKET arraycontent RSQBRACKET','arreglo',4,'p_arreglo_tipo3','sintactic.py',244),
  ('arreglo -> LSQBRACKET arraycontent RSQBRACKET','arreglo',3,'p_arreglo_tipo5','sintactic.py',248),
  ('arraycontent -> factor','arraycontent',1,'p_arraycontent_var1','sintactic.py',252),
  ('arraycontent -> string','arraycontent',1,'p_arraycontent_var1','sintactic.py',253),
  ('arraycontent -> factor COMMA arraycontent','arraycontent',3,'p_arraycontent_var2','sintactic.py',257),
  ('arraycontent -> string COMMA arraycontent','arraycontent',3,'p_arraycontent_var2','sintactic.py',258),
  ('metodosarreglo -> arreglo POINT INDEX LPARENTHESIS arraycontent RPARENTHESIS','metodosarreglo',6,'p_metodosarreglo_index','sintactic.py',264),
  ('metodosarreglo -> arreglo LSQBRACKET factor RSQBRACKET','metodosarreglo',4,'p_metodosarreglo_num','sintactic.py',268),
  ('hash -> LBRACKET hashcontent RBRACKET','hash',3,'p_hash_tipo1','sintactic.py',274),
  ('hash -> HASH POINT NEW','hash',3,'p_hash_tipo2','sintactic.py',278),
  ('hashcontent -> string ASSIGN GREATER hashcontentvalue','hashcontent',4,'p_hashcontent_var1','sintactic.py',282),
  ('hashcontent -> string ASSIGN GREATER hashcontentvalue COMMA hashcontent','hashcontent',6,'p_hashcontent_var2','sintactic.py',286),
  ('hashcontentvalue -> factor','hashcontentvalue',1,'p_hashcontentvalue_var','sintactic.py',290),
  ('hashcontentvalue -> string','hashcontentvalue',1,'p_hashcontentvalue_var','sintactic.py',291),
  ('metodohash -> variables ASSIGN hash POINT LENGTH','metodohash',5,'p_metodohash_length','sintactic.py',297),
  ('metodohash -> variables POINT LENGTH','metodohash',3,'p_metodohash_length2','sintactic.py',302),
  ('comparador -> COMPARE','comparador',1,'p_comparador','sintactic.py',313),
  ('comparador -> GREQUAL','comparador',1,'p_comparador','sintactic.py',314),
  ('comparador -> LSEQUAL','comparador',1,'p_comparador','sintactic.py',315),
  ('comparador -> NOTEQUAL','comparador',1,'p_comparador','sintactic.py',316),
  ('comparador -> LESS','comparador',1,'p_comparador','sintactic.py',317),
  ('comparador -> GREATER','comparador',1,'p_comparador','sintactic.py',318),
  ('estructurasControl -> FOR IDLOCAL IN factor POINT POINT factor DO BREAK IF END','estructurasControl',11,'p_estructurasControl_for1','sintactic.py',324),
  ('estructurasControl -> FOR IDLOCAL IN factor POINT POINT factor DO END','estructurasControl',9,'p_estructurasControl_for2','sintactic.py',328),
]
