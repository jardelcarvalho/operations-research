\* Source Pyomo model name=unknown *\

min 
z:
+12.0 ONE_VAR_CONSTANT
+1 epsilon(1_3)
+1 epsilon(1_2)
+1 epsilon(2_3)
+2.0 epsilon(1_4)
+1 epsilon(4_5)
-6.0 kappa(neg)
-6.0 kappa(pos)

s.t.

c_e_relaxation_total_components_:
+1 kappa(neg)
-1 kappa(pos)
+1 rho(1_0)
+1 rho(1_1)
+1 rho(2_0)
+1 rho(2_1)
+1 rho(3_0)
+1 rho(3_1)
+1 rho(4_0)
+1 rho(4_1)
+1 rho(5_0)
+1 rho(5_1)
= 0

bounds
   1 <= ONE_VAR_CONSTANT <= 1
   0 <= epsilon(1_3) <= 1
   0 <= epsilon(1_2) <= 1
   0 <= epsilon(2_3) <= 1
   0 <= epsilon(1_4) <= 1
   0 <= epsilon(4_5) <= 1
   0 <= kappa(neg) <= +inf
   0 <= kappa(pos) <= +inf
   0 <= rho(1_0) <= 1
   0 <= rho(1_1) <= 1
   0 <= rho(2_0) <= 1
   0 <= rho(2_1) <= 1
   0 <= rho(3_0) <= 1
   0 <= rho(3_1) <= 1
   0 <= rho(4_0) <= 1
   0 <= rho(4_1) <= 1
   0 <= rho(5_0) <= 1
   0 <= rho(5_1) <= 1
binary
  epsilon(1_3)
  epsilon(1_2)
  epsilon(2_3)
  epsilon(1_4)
  epsilon(4_5)
  rho(1_0)
  rho(1_1)
  rho(2_0)
  rho(2_1)
  rho(3_0)
  rho(3_1)
  rho(4_0)
  rho(4_1)
  rho(5_0)
  rho(5_1)
end
