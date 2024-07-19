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

c_u_xi_linearization_constraint1(0)_:
-1 epsilon(1_2)
+1 xi(1_2_0)
<= 0

c_u_xi_linearization_constraint1(1)_:
-1 epsilon(1_2)
+1 xi(1_2_1)
<= 0

c_u_xi_linearization_constraint1(2)_:
-1 epsilon(1_3)
+1 xi(1_3_0)
<= 0

c_u_xi_linearization_constraint1(3)_:
-1 epsilon(1_3)
+1 xi(1_3_1)
<= 0

c_u_xi_linearization_constraint1(4)_:
-1 epsilon(1_4)
+1 xi(1_4_0)
<= 0

c_u_xi_linearization_constraint1(5)_:
-1 epsilon(1_4)
+1 xi(1_4_1)
<= 0

c_u_xi_linearization_constraint1(6)_:
-1 epsilon(2_3)
+1 xi(2_3_0)
<= 0

c_u_xi_linearization_constraint1(7)_:
-1 epsilon(2_3)
+1 xi(2_3_1)
<= 0

c_u_xi_linearization_constraint1(8)_:
-1 epsilon(4_5)
+1 xi(4_5_0)
<= 0

c_u_xi_linearization_constraint1(9)_:
-1 epsilon(4_5)
+1 xi(4_5_1)
<= 0

c_u_xi_linearization_constraint2(0)_:
+1 xi(1_2_0)
-1 rho(1_0)
<= 0

c_u_xi_linearization_constraint2(1)_:
+1 xi(1_2_1)
-1 rho(1_1)
<= 0

c_u_xi_linearization_constraint2(2)_:
+1 xi(1_3_0)
-1 rho(1_0)
<= 0

c_u_xi_linearization_constraint2(3)_:
+1 xi(1_3_1)
-1 rho(1_1)
<= 0

c_u_xi_linearization_constraint2(4)_:
+1 xi(1_4_0)
-1 rho(1_0)
<= 0

c_u_xi_linearization_constraint2(5)_:
+1 xi(1_4_1)
-1 rho(1_1)
<= 0

c_u_xi_linearization_constraint2(6)_:
+1 xi(2_3_0)
-1 rho(2_0)
<= 0

c_u_xi_linearization_constraint2(7)_:
+1 xi(2_3_1)
-1 rho(2_1)
<= 0

c_u_xi_linearization_constraint2(8)_:
+1 xi(4_5_0)
-1 rho(4_0)
<= 0

c_u_xi_linearization_constraint2(9)_:
+1 xi(4_5_1)
-1 rho(4_1)
<= 0

c_u_xi_linearization_constraint3(0)_:
+1 epsilon(1_2)
-1 xi(1_2_0)
+1 rho(1_0)
<= 1

c_u_xi_linearization_constraint3(1)_:
+1 epsilon(1_2)
-1 xi(1_2_1)
+1 rho(1_1)
<= 1

c_u_xi_linearization_constraint3(2)_:
+1 epsilon(1_3)
-1 xi(1_3_0)
+1 rho(1_0)
<= 1

c_u_xi_linearization_constraint3(3)_:
+1 epsilon(1_3)
-1 xi(1_3_1)
+1 rho(1_1)
<= 1

c_u_xi_linearization_constraint3(4)_:
+1 epsilon(1_4)
-1 xi(1_4_0)
+1 rho(1_0)
<= 1

c_u_xi_linearization_constraint3(5)_:
+1 epsilon(1_4)
-1 xi(1_4_1)
+1 rho(1_1)
<= 1

c_u_xi_linearization_constraint3(6)_:
+1 epsilon(2_3)
-1 xi(2_3_0)
+1 rho(2_0)
<= 1

c_u_xi_linearization_constraint3(7)_:
+1 epsilon(2_3)
-1 xi(2_3_1)
+1 rho(2_1)
<= 1

c_u_xi_linearization_constraint3(8)_:
+1 epsilon(4_5)
-1 xi(4_5_0)
+1 rho(4_0)
<= 1

c_u_xi_linearization_constraint3(9)_:
+1 epsilon(4_5)
-1 xi(4_5_1)
+1 rho(4_1)
<= 1

c_u_vertex_represents_unique_partition(1)_:
+1 rho(1_0)
+1 rho(1_1)
<= 1

c_u_vertex_represents_unique_partition(2)_:
+1 rho(2_0)
+1 rho(2_1)
<= 1

c_u_vertex_represents_unique_partition(3)_:
+1 rho(3_0)
+1 rho(3_1)
<= 1

c_u_vertex_represents_unique_partition(4)_:
+1 rho(4_0)
+1 rho(4_1)
<= 1

c_u_vertex_represents_unique_partition(5)_:
+1 rho(5_0)
+1 rho(5_1)
<= 1

c_u_partition_has_unique_representant(0)_:
+1 rho(1_0)
+1 rho(2_0)
+1 rho(3_0)
+1 rho(4_0)
+1 rho(5_0)
<= 1

c_u_partition_has_unique_representant(1)_:
+1 rho(1_1)
+1 rho(2_1)
+1 rho(3_1)
+1 rho(4_1)
+1 rho(5_1)
<= 1

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

c_u_max_kappa_:
+1 kappa(neg)
+1 kappa(pos)
<= 2

c_u_strongly_connected_components(0)_:
+4 epsilon(1_3)
+1 epsilon(1_2)
+1 epsilon(1_4)
<= 5

c_u_strongly_connected_components(1)_:
+5 epsilon(1_2)
+1 epsilon(1_4)
<= 6

c_u_strongly_connected_components(2)_:
+2 epsilon(2_3)
<= 3

c_u_strongly_connected_components(3)_:
+1 epsilon(1_3)
+1 epsilon(1_2)
+5 epsilon(1_4)
+1 epsilon(4_5)
<= 6

c_u_strongly_connected_components(4)_:
+2 epsilon(4_5)
<= 3

bounds
   1 <= ONE_VAR_CONSTANT <= 1
   0 <= epsilon(1_3) <= 1
   0 <= epsilon(1_2) <= 1
   0 <= epsilon(2_3) <= 1
   0 <= epsilon(1_4) <= 1
   0 <= epsilon(4_5) <= 1
   0 <= kappa(neg) <= +inf
   0 <= kappa(pos) <= +inf
   0 <= xi(1_2_0) <= 1
   0 <= xi(1_2_1) <= 1
   0 <= xi(1_3_0) <= 1
   0 <= xi(1_3_1) <= 1
   0 <= xi(1_4_0) <= 1
   0 <= xi(1_4_1) <= 1
   0 <= xi(2_3_0) <= 1
   0 <= xi(2_3_1) <= 1
   0 <= xi(4_5_0) <= 1
   0 <= xi(4_5_1) <= 1
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
  xi(1_2_0)
  xi(1_2_1)
  xi(1_3_0)
  xi(1_3_1)
  xi(1_4_0)
  xi(1_4_1)
  xi(2_3_0)
  xi(2_3_1)
  xi(4_5_0)
  xi(4_5_1)
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
