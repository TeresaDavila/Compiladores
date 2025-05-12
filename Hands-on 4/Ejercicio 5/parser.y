%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ID 100

typedef struct {
    char *nombre;
    int es_funcion;
    int n_param;
} Simbolo;

Simbolo tabla[MAX_ID];
int ntabla = 0;

void agregar(char *id, int es_funcion, int n_param) {
  for (int i = 0; i < ntabla; i++)
    if (strcmp(tabla[i].nombre, id) == 0) return;
  tabla[ntabla].nombre = strdup(id);
  tabla[ntabla].es_funcion = es_funcion;
  tabla[ntabla].n_param = n_param;
  ntabla++;
}

int buscar(char *id) {
  for (int i = 0; i < ntabla; i++)
    if (strcmp(tabla[i].nombre, id) == 0) return 1;
  return 0;
}

int obtener_parametros(char *id) {
  for (int i = 0; i < ntabla; i++)
    if (strcmp(tabla[i].nombre, id) == 0)
      return tabla[i].n_param;
  return -1;
}

int yylex(void);
int yyerror(const char *s) {
  fprintf(stderr, "Error: %s\n", s);
  return 0;
}
%}

%union { char *str; int num; }

%token <str> ID
%token INT PUNTOYCOMA FUNC RETURN COMMA
%token ASSIGN LPAREN RPAREN LBRACE RBRACE
%type <num> args listaParam

%%
programa
  : declaraciones elementos
  ;

declaraciones
  : /* vacío */
  | declaraciones INT ID PUNTOYCOMA   { agregar($3, 0, 0); }
  ;

elementos
  : /* vacío */
  | elementos elemento
  ;

elemento
  : sentencia
  | funcion_def
  ;

sentencia
  : ID PUNTOYCOMA
      { if (!buscar($1)) printf("Error semántico: '%s' no está declarado\n", $1); }
  | ID ASSIGN ID PUNTOYCOMA
      { if (!buscar($1)) printf("Error semántico: '%s' no está declarado\n", $1);
        if (!buscar($3)) printf("Error semántico: '%s' no está declarado\n", $3); }
  | ID LPAREN args RPAREN PUNTOYCOMA
      {
        if (!buscar($1)) {
          printf("Error semántico: función '%s' no está declarada\n", $1);
        } else {
          int esperados = obtener_parametros($1);
          if (esperados != $3) {
            printf("Error semántico: función '%s' esperaba %d argumentos y recibió %d\n", $1, esperados, $3);
          }
        }
      }
  ;

args
  : /* vacío */             { $$ = 0; }
  | ID                      { if (!buscar($1)) printf("Error semántico: '%s' no está declarado\n", $1); $$ = 1; }
  | args COMMA ID           { if (!buscar($3)) printf("Error semántico: '%s' no está declarado\n", $3); $$ = $1 + 1; }
  ;

funcion_def
  : FUNC ID LPAREN listaParam RPAREN LBRACE declaraciones elementos RETURN ID PUNTOYCOMA RBRACE
      { agregar($2, 1, $4); }
  ;

listaParam
  : /* vacío */             { $$ = 0; }
  | ID                      { agregar($1, 0, 0); $$ = 1; }
  | listaParam COMMA ID     { agregar($3, 0, 0); $$ = $1 + 1; }
  ;

%%
int main() {
  return yyparse();
}