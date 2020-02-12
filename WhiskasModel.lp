\* El_problema_Whiskas *\
Minimize
OBJ: 0.013 %_Pollo + 0.008 %_Res
Subject To
Requerimiento_de_fibra: 0.001 %_Pollo + 0.005 %_Res <= 2
Requerimiento_de_grasa: 0.08 %_Pollo + 0.1 %_Res >= 6
Requerimiento_de_proteina: 0.1 %_Pollo + 0.2 %_Res >= 8
Requerimiento_de_sal: 0.002 %_Pollo + 0.005 %_Res <= 0.4
Suma_de_porcentajes: %_Pollo + %_Res = 100
Bounds
0 <= %_Pollo
Generals
%_Pollo
End
