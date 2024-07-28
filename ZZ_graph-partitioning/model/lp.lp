\* Source Pyomo model name=unknown *\

min 
z:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(1__3)_)
+2 epsilon(_Edge(1__4)_)
+1 epsilon(_Edge(2__3)_)
+1 epsilon(_Edge(4__5)_)
+6 kappa(_Sign(neg)_)
+6 kappa(_Sign(pos)_)

s.t.

c_u_node_can_represent_unique_partition(_Node(1)_)_:
+1 rho(_Node(1)_Partition(1)_)
+1 rho(_Node(1)_Partition(2)_)
<= 1

c_u_node_can_represent_unique_partition(_Node(2)_)_:
+1 rho(_Node(2)_Partition(1)_)
+1 rho(_Node(2)_Partition(2)_)
<= 1

c_u_node_can_represent_unique_partition(_Node(3)_)_:
+1 rho(_Node(3)_Partition(1)_)
+1 rho(_Node(3)_Partition(2)_)
<= 1

c_u_node_can_represent_unique_partition(_Node(4)_)_:
+1 rho(_Node(4)_Partition(1)_)
+1 rho(_Node(4)_Partition(2)_)
<= 1

c_u_node_can_represent_unique_partition(_Node(5)_)_:
+1 rho(_Node(5)_Partition(1)_)
+1 rho(_Node(5)_Partition(2)_)
<= 1

c_u_partition_can_have_unique_representant(_Partition(1)_)_:
+1 rho(_Node(1)_Partition(1)_)
+1 rho(_Node(2)_Partition(1)_)
+1 rho(_Node(3)_Partition(1)_)
+1 rho(_Node(4)_Partition(1)_)
+1 rho(_Node(5)_Partition(1)_)
<= 1

c_u_partition_can_have_unique_representant(_Partition(2)_)_:
+1 rho(_Node(1)_Partition(2)_)
+1 rho(_Node(2)_Partition(2)_)
+1 rho(_Node(3)_Partition(2)_)
+1 rho(_Node(4)_Partition(2)_)
+1 rho(_Node(5)_Partition(2)_)
<= 1

c_e_relaxation_of_number_of_partitions(Unique)_:
+1 kappa(_Sign(neg)_)
-1 kappa(_Sign(pos)_)
+1 rho(_Node(1)_Partition(1)_)
+1 rho(_Node(1)_Partition(2)_)
+1 rho(_Node(2)_Partition(1)_)
+1 rho(_Node(2)_Partition(2)_)
+1 rho(_Node(3)_Partition(1)_)
+1 rho(_Node(3)_Partition(2)_)
+1 rho(_Node(4)_Partition(1)_)
+1 rho(_Node(4)_Partition(2)_)
+1 rho(_Node(5)_Partition(1)_)
+1 rho(_Node(5)_Partition(2)_)
= 2

c_u_maximum_relaxation_of_partitions(Unique)_:
+1 kappa(_Sign(neg)_)
+1 kappa(_Sign(pos)_)
+1 rho(_Node(1)_Partition(1)_)
+1 rho(_Node(1)_Partition(2)_)
+1 rho(_Node(2)_Partition(1)_)
+1 rho(_Node(2)_Partition(2)_)
+1 rho(_Node(3)_Partition(1)_)
+1 rho(_Node(3)_Partition(2)_)
+1 rho(_Node(4)_Partition(1)_)
+1 rho(_Node(4)_Partition(2)_)
+1 rho(_Node(5)_Partition(1)_)
+1 rho(_Node(5)_Partition(2)_)
<= 2

c_e_representants_cannot_be_adjacent(_Node(1)_)_:
-1 rho(_Node(1)_Partition(1)_)
-1 rho(_Node(1)_Partition(2)_)
-1 xi(_Node(1)_Node(2)_Partition(1)_)
-1 xi(_Node(1)_Node(2)_Partition(2)_)
-1 xi(_Node(1)_Node(3)_Partition(1)_)
-1 xi(_Node(1)_Node(3)_Partition(2)_)
-1 xi(_Node(1)_Node(4)_Partition(1)_)
-1 xi(_Node(1)_Node(4)_Partition(2)_)
= -1

c_e_representants_cannot_be_adjacent(_Node(2)_)_:
-1 rho(_Node(2)_Partition(1)_)
-1 rho(_Node(2)_Partition(2)_)
-1 xi(_Node(2)_Node(1)_Partition(1)_)
-1 xi(_Node(2)_Node(1)_Partition(2)_)
-1 xi(_Node(2)_Node(3)_Partition(1)_)
-1 xi(_Node(2)_Node(3)_Partition(2)_)
= -1

c_e_representants_cannot_be_adjacent(_Node(3)_)_:
-1 rho(_Node(3)_Partition(1)_)
-1 rho(_Node(3)_Partition(2)_)
-1 xi(_Node(3)_Node(1)_Partition(1)_)
-1 xi(_Node(3)_Node(1)_Partition(2)_)
-1 xi(_Node(3)_Node(2)_Partition(1)_)
-1 xi(_Node(3)_Node(2)_Partition(2)_)
= -1

c_e_representants_cannot_be_adjacent(_Node(4)_)_:
-1 rho(_Node(4)_Partition(1)_)
-1 rho(_Node(4)_Partition(2)_)
-1 xi(_Node(4)_Node(1)_Partition(1)_)
-1 xi(_Node(4)_Node(1)_Partition(2)_)
-1 xi(_Node(4)_Node(5)_Partition(1)_)
-1 xi(_Node(4)_Node(5)_Partition(2)_)
= -1

c_e_representants_cannot_be_adjacent(_Node(5)_)_:
-1 rho(_Node(5)_Partition(1)_)
-1 rho(_Node(5)_Partition(2)_)
-1 xi(_Node(5)_Node(4)_Partition(1)_)
-1 xi(_Node(5)_Node(4)_Partition(2)_)
= -1

c_e_mutal_neighborhoods(_Edge(1__3)_)_:
+2 epsilon(_Edge(1__3)_)
-2 psi(_Node(1)_Node(3)_Node(3)_)
-1 psi(_Node(1)_Node(3)_Node(4)_)
= 0

c_e_mutal_neighborhoods(_Edge(1__2)_)_:
+2 epsilon(_Edge(1__2)_)
-2 psi(_Node(1)_Node(2)_Node(2)_)
-1 psi(_Node(1)_Node(2)_Node(4)_)
= 0

c_e_mutal_neighborhoods(_Edge(2__3)_)_:
+2 epsilon(_Edge(2__3)_)
-2 psi(_Node(2)_Node(3)_Node(3)_)
= 0

c_e_mutal_neighborhoods(_Edge(1__4)_)_:
-2 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(2)_)
+1 psi(_Node(1)_Node(4)_Node(3)_)
+2 psi(_Node(1)_Node(4)_Node(4)_)
+1 psi(_Node(4)_Node(1)_Node(5)_)
= 0

c_e_mutal_neighborhoods(_Edge(4__5)_)_:
-2 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(5)_Node(1)_)
+2 psi(_Node(4)_Node(5)_Node(5)_)
= 0

c_e_mutual_neighborhoods_integrity_lhs(_Edge(1__3)_)_:
+1 psi(_Node(1)_Node(3)_Node(2)_)
-1 psi(_Node(3)_Node(1)_Node(2)_)
= 0

c_e_mutual_neighborhoods_integrity_lhs(_Edge(1__2)_)_:
+1 psi(_Node(1)_Node(2)_Node(3)_)
-1 psi(_Node(2)_Node(1)_Node(3)_)
= 0

c_e_mutual_neighborhoods_integrity_lhs(_Edge(2__3)_)_:
+1 psi(_Node(2)_Node(3)_Node(1)_)
-1 psi(_Node(3)_Node(2)_Node(1)_)
= 0

c_e_mutual_neighborhoods_integrity_rhs(_Edge(1__3)_)_:
+1 psi(_Node(1)_Node(3)_Node(2)_)
+1 psi(_Node(1)_Node(3)_Node(4)_)
-1 psi(_Node(3)_Node(1)_Node(2)_)
= 0

c_e_mutual_neighborhoods_integrity_rhs(_Edge(1__2)_)_:
+1 psi(_Node(1)_Node(2)_Node(3)_)
+1 psi(_Node(1)_Node(2)_Node(4)_)
-1 psi(_Node(2)_Node(1)_Node(3)_)
= 0

c_e_mutual_neighborhoods_integrity_rhs(_Edge(2__3)_)_:
+1 psi(_Node(2)_Node(3)_Node(1)_)
-1 psi(_Node(3)_Node(2)_Node(1)_)
= 0

c_e_mutual_neighborhoods_integrity_rhs(_Edge(1__4)_)_:
+1 psi(_Node(1)_Node(4)_Node(2)_)
+1 psi(_Node(1)_Node(4)_Node(3)_)
-1 psi(_Node(4)_Node(1)_Node(5)_)
= 0

c_e_mutual_neighborhoods_integrity_rhs(_Edge(4__5)_)_:
+1 psi(_Node(4)_Node(5)_Node(1)_)
= 0

c_u_xi_linearization_leq1(_xi_product(1__2__1)_)_:
-1 epsilon(_Edge(1__2)_)
+1 xi(_Node(1)_Node(2)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(1__2__2)_)_:
-1 epsilon(_Edge(1__2)_)
+1 xi(_Node(1)_Node(2)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(1__3__1)_)_:
-1 epsilon(_Edge(1__3)_)
+1 xi(_Node(1)_Node(3)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(1__3__2)_)_:
-1 epsilon(_Edge(1__3)_)
+1 xi(_Node(1)_Node(3)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(1__4__1)_)_:
-1 epsilon(_Edge(1__4)_)
+1 xi(_Node(1)_Node(4)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(1__4__2)_)_:
-1 epsilon(_Edge(1__4)_)
+1 xi(_Node(1)_Node(4)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(2__1__1)_)_:
-1 epsilon(_Edge(1__2)_)
+1 xi(_Node(2)_Node(1)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(2__1__2)_)_:
-1 epsilon(_Edge(1__2)_)
+1 xi(_Node(2)_Node(1)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(2__3__1)_)_:
-1 epsilon(_Edge(2__3)_)
+1 xi(_Node(2)_Node(3)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(2__3__2)_)_:
-1 epsilon(_Edge(2__3)_)
+1 xi(_Node(2)_Node(3)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(3__1__1)_)_:
-1 epsilon(_Edge(1__3)_)
+1 xi(_Node(3)_Node(1)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(3__1__2)_)_:
-1 epsilon(_Edge(1__3)_)
+1 xi(_Node(3)_Node(1)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(3__2__1)_)_:
-1 epsilon(_Edge(2__3)_)
+1 xi(_Node(3)_Node(2)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(3__2__2)_)_:
-1 epsilon(_Edge(2__3)_)
+1 xi(_Node(3)_Node(2)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(4__1__1)_)_:
-1 epsilon(_Edge(1__4)_)
+1 xi(_Node(4)_Node(1)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(4__1__2)_)_:
-1 epsilon(_Edge(1__4)_)
+1 xi(_Node(4)_Node(1)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(4__5__1)_)_:
-1 epsilon(_Edge(4__5)_)
+1 xi(_Node(4)_Node(5)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(4__5__2)_)_:
-1 epsilon(_Edge(4__5)_)
+1 xi(_Node(4)_Node(5)_Partition(2)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(5__4__1)_)_:
-1 epsilon(_Edge(4__5)_)
+1 xi(_Node(5)_Node(4)_Partition(1)_)
<= 0

c_u_xi_linearization_leq1(_xi_product(5__4__2)_)_:
-1 epsilon(_Edge(4__5)_)
+1 xi(_Node(5)_Node(4)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(1__2__1)_)_:
-1 rho(_Node(2)_Partition(1)_)
+1 xi(_Node(1)_Node(2)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(1__2__2)_)_:
-1 rho(_Node(2)_Partition(2)_)
+1 xi(_Node(1)_Node(2)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(1__3__1)_)_:
-1 rho(_Node(3)_Partition(1)_)
+1 xi(_Node(1)_Node(3)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(1__3__2)_)_:
-1 rho(_Node(3)_Partition(2)_)
+1 xi(_Node(1)_Node(3)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(1__4__1)_)_:
-1 rho(_Node(4)_Partition(1)_)
+1 xi(_Node(1)_Node(4)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(1__4__2)_)_:
-1 rho(_Node(4)_Partition(2)_)
+1 xi(_Node(1)_Node(4)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(2__1__1)_)_:
-1 rho(_Node(1)_Partition(1)_)
+1 xi(_Node(2)_Node(1)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(2__1__2)_)_:
-1 rho(_Node(1)_Partition(2)_)
+1 xi(_Node(2)_Node(1)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(2__3__1)_)_:
-1 rho(_Node(3)_Partition(1)_)
+1 xi(_Node(2)_Node(3)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(2__3__2)_)_:
-1 rho(_Node(3)_Partition(2)_)
+1 xi(_Node(2)_Node(3)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(3__1__1)_)_:
-1 rho(_Node(1)_Partition(1)_)
+1 xi(_Node(3)_Node(1)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(3__1__2)_)_:
-1 rho(_Node(1)_Partition(2)_)
+1 xi(_Node(3)_Node(1)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(3__2__1)_)_:
-1 rho(_Node(2)_Partition(1)_)
+1 xi(_Node(3)_Node(2)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(3__2__2)_)_:
-1 rho(_Node(2)_Partition(2)_)
+1 xi(_Node(3)_Node(2)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(4__1__1)_)_:
-1 rho(_Node(1)_Partition(1)_)
+1 xi(_Node(4)_Node(1)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(4__1__2)_)_:
-1 rho(_Node(1)_Partition(2)_)
+1 xi(_Node(4)_Node(1)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(4__5__1)_)_:
-1 rho(_Node(5)_Partition(1)_)
+1 xi(_Node(4)_Node(5)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(4__5__2)_)_:
-1 rho(_Node(5)_Partition(2)_)
+1 xi(_Node(4)_Node(5)_Partition(2)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(5__4__1)_)_:
-1 rho(_Node(4)_Partition(1)_)
+1 xi(_Node(5)_Node(4)_Partition(1)_)
<= 0

c_u_xi_linearization_leq2(_xi_product(5__4__2)_)_:
-1 rho(_Node(4)_Partition(2)_)
+1 xi(_Node(5)_Node(4)_Partition(2)_)
<= 0

c_u_xi_linearization_geq(_xi_product(1__2__1)_)_:
+1 epsilon(_Edge(1__2)_)
+1 rho(_Node(2)_Partition(1)_)
-1 xi(_Node(1)_Node(2)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(1__2__2)_)_:
+1 epsilon(_Edge(1__2)_)
+1 rho(_Node(2)_Partition(2)_)
-1 xi(_Node(1)_Node(2)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(1__3__1)_)_:
+1 epsilon(_Edge(1__3)_)
+1 rho(_Node(3)_Partition(1)_)
-1 xi(_Node(1)_Node(3)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(1__3__2)_)_:
+1 epsilon(_Edge(1__3)_)
+1 rho(_Node(3)_Partition(2)_)
-1 xi(_Node(1)_Node(3)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(1__4__1)_)_:
+1 epsilon(_Edge(1__4)_)
+1 rho(_Node(4)_Partition(1)_)
-1 xi(_Node(1)_Node(4)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(1__4__2)_)_:
+1 epsilon(_Edge(1__4)_)
+1 rho(_Node(4)_Partition(2)_)
-1 xi(_Node(1)_Node(4)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(2__1__1)_)_:
+1 epsilon(_Edge(1__2)_)
+1 rho(_Node(1)_Partition(1)_)
-1 xi(_Node(2)_Node(1)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(2__1__2)_)_:
+1 epsilon(_Edge(1__2)_)
+1 rho(_Node(1)_Partition(2)_)
-1 xi(_Node(2)_Node(1)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(2__3__1)_)_:
+1 epsilon(_Edge(2__3)_)
+1 rho(_Node(3)_Partition(1)_)
-1 xi(_Node(2)_Node(3)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(2__3__2)_)_:
+1 epsilon(_Edge(2__3)_)
+1 rho(_Node(3)_Partition(2)_)
-1 xi(_Node(2)_Node(3)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(3__1__1)_)_:
+1 epsilon(_Edge(1__3)_)
+1 rho(_Node(1)_Partition(1)_)
-1 xi(_Node(3)_Node(1)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(3__1__2)_)_:
+1 epsilon(_Edge(1__3)_)
+1 rho(_Node(1)_Partition(2)_)
-1 xi(_Node(3)_Node(1)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(3__2__1)_)_:
+1 epsilon(_Edge(2__3)_)
+1 rho(_Node(2)_Partition(1)_)
-1 xi(_Node(3)_Node(2)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(3__2__2)_)_:
+1 epsilon(_Edge(2__3)_)
+1 rho(_Node(2)_Partition(2)_)
-1 xi(_Node(3)_Node(2)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(4__1__1)_)_:
+1 epsilon(_Edge(1__4)_)
+1 rho(_Node(1)_Partition(1)_)
-1 xi(_Node(4)_Node(1)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(4__1__2)_)_:
+1 epsilon(_Edge(1__4)_)
+1 rho(_Node(1)_Partition(2)_)
-1 xi(_Node(4)_Node(1)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(4__5__1)_)_:
+1 epsilon(_Edge(4__5)_)
+1 rho(_Node(5)_Partition(1)_)
-1 xi(_Node(4)_Node(5)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(4__5__2)_)_:
+1 epsilon(_Edge(4__5)_)
+1 rho(_Node(5)_Partition(2)_)
-1 xi(_Node(4)_Node(5)_Partition(2)_)
<= 1

c_u_xi_linearization_geq(_xi_product(5__4__1)_)_:
+1 epsilon(_Edge(4__5)_)
+1 rho(_Node(4)_Partition(1)_)
-1 xi(_Node(5)_Node(4)_Partition(1)_)
<= 1

c_u_xi_linearization_geq(_xi_product(5__4__2)_)_:
+1 epsilon(_Edge(4__5)_)
+1 rho(_Node(4)_Partition(2)_)
-1 xi(_Node(5)_Node(4)_Partition(2)_)
<= 1

c_u_psi_linearization_leq1(_psi_product(1__3__2)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(3)_Node(2)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__3__3)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__3__4)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(3)_Node(4)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(3__1__1)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(3__1__2)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(3)_Node(1)_Node(2)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__2__2)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(2)_Node(2)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__2__3)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(2)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__2__4)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(2)_Node(4)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(2__1__1)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(2)_Node(2)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(2__1__3)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(2)_Node(1)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(2__3__1)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(2)_Node(3)_Node(1)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(2__3__3)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(2)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(3__2__1)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(3)_Node(2)_Node(1)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(3__2__2)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(2)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__4__2)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(2)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__4__3)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(3)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(1__4__4)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(4)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(4__1__1)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(4)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(4__1__5)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(4)_Node(1)_Node(5)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(4__5__1)_)_:
-1 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(5)_Node(1)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(4__5__5)_)_:
-1 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(5)_Node(5)_)
<= 0

c_u_psi_linearization_leq1(_psi_product(5__4__4)_)_:
-1 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(5)_Node(5)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__3__2)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(3)_Node(2)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__3__3)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__3__4)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(3)_Node(4)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(3__1__1)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(3__1__2)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(3)_Node(1)_Node(2)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__2__2)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(2)_Node(2)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__2__3)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(2)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__2__4)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(2)_Node(4)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(2__1__1)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(2)_Node(2)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(2__1__3)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(2)_Node(1)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(2__3__1)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(2)_Node(3)_Node(1)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(2__3__3)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(2)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(3__2__1)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(3)_Node(2)_Node(1)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(3__2__2)_)_:
-1 epsilon(_Edge(2__3)_)
+1 psi(_Node(2)_Node(3)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__4__2)_)_:
-1 epsilon(_Edge(1__2)_)
+1 psi(_Node(1)_Node(4)_Node(2)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__4__3)_)_:
-1 epsilon(_Edge(1__3)_)
+1 psi(_Node(1)_Node(4)_Node(3)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(1__4__4)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(4)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(4__1__1)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(1)_Node(4)_Node(4)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(4__1__5)_)_:
-1 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(1)_Node(5)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(4__5__1)_)_:
-1 epsilon(_Edge(1__4)_)
+1 psi(_Node(4)_Node(5)_Node(1)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(4__5__5)_)_:
-1 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(5)_Node(5)_)
<= 0

c_u_psi_linearization_leq2(_psi_product(5__4__4)_)_:
-1 epsilon(_Edge(4__5)_)
+1 psi(_Node(4)_Node(5)_Node(5)_)
<= 0

c_u_psi_linearization_geq(_psi_product(1__3__2)_)_:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(1__3)_)
-1 psi(_Node(1)_Node(3)_Node(2)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__3__3)_)_:
+2 epsilon(_Edge(1__3)_)
-1 psi(_Node(1)_Node(3)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__3__4)_)_:
+1 epsilon(_Edge(1__3)_)
+1 epsilon(_Edge(1__4)_)
-1 psi(_Node(1)_Node(3)_Node(4)_)
<= 1

c_u_psi_linearization_geq(_psi_product(3__1__1)_)_:
+2 epsilon(_Edge(1__3)_)
-1 psi(_Node(1)_Node(3)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(3__1__2)_)_:
+1 epsilon(_Edge(1__3)_)
+1 epsilon(_Edge(2__3)_)
-1 psi(_Node(3)_Node(1)_Node(2)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__2__2)_)_:
+2 epsilon(_Edge(1__2)_)
-1 psi(_Node(1)_Node(2)_Node(2)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__2__3)_)_:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(1__3)_)
-1 psi(_Node(1)_Node(2)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__2__4)_)_:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(1__4)_)
-1 psi(_Node(1)_Node(2)_Node(4)_)
<= 1

c_u_psi_linearization_geq(_psi_product(2__1__1)_)_:
+2 epsilon(_Edge(1__2)_)
-1 psi(_Node(1)_Node(2)_Node(2)_)
<= 1

c_u_psi_linearization_geq(_psi_product(2__1__3)_)_:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(2__3)_)
-1 psi(_Node(2)_Node(1)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(2__3__1)_)_:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(2__3)_)
-1 psi(_Node(2)_Node(3)_Node(1)_)
<= 1

c_u_psi_linearization_geq(_psi_product(2__3__3)_)_:
+2 epsilon(_Edge(2__3)_)
-1 psi(_Node(2)_Node(3)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(3__2__1)_)_:
+1 epsilon(_Edge(1__3)_)
+1 epsilon(_Edge(2__3)_)
-1 psi(_Node(3)_Node(2)_Node(1)_)
<= 1

c_u_psi_linearization_geq(_psi_product(3__2__2)_)_:
+2 epsilon(_Edge(2__3)_)
-1 psi(_Node(2)_Node(3)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__4__2)_)_:
+1 epsilon(_Edge(1__2)_)
+1 epsilon(_Edge(1__4)_)
-1 psi(_Node(1)_Node(4)_Node(2)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__4__3)_)_:
+1 epsilon(_Edge(1__3)_)
+1 epsilon(_Edge(1__4)_)
-1 psi(_Node(1)_Node(4)_Node(3)_)
<= 1

c_u_psi_linearization_geq(_psi_product(1__4__4)_)_:
+2 epsilon(_Edge(1__4)_)
-1 psi(_Node(1)_Node(4)_Node(4)_)
<= 1

c_u_psi_linearization_geq(_psi_product(4__1__1)_)_:
+2 epsilon(_Edge(1__4)_)
-1 psi(_Node(1)_Node(4)_Node(4)_)
<= 1

c_u_psi_linearization_geq(_psi_product(4__1__5)_)_:
+1 epsilon(_Edge(1__4)_)
+1 epsilon(_Edge(4__5)_)
-1 psi(_Node(4)_Node(1)_Node(5)_)
<= 1

c_u_psi_linearization_geq(_psi_product(4__5__1)_)_:
+1 epsilon(_Edge(1__4)_)
+1 epsilon(_Edge(4__5)_)
-1 psi(_Node(4)_Node(5)_Node(1)_)
<= 1

c_u_psi_linearization_geq(_psi_product(4__5__5)_)_:
+2 epsilon(_Edge(4__5)_)
-1 psi(_Node(4)_Node(5)_Node(5)_)
<= 1

c_u_psi_linearization_geq(_psi_product(5__4__4)_)_:
+2 epsilon(_Edge(4__5)_)
-1 psi(_Node(4)_Node(5)_Node(5)_)
<= 1

bounds
   0 <= epsilon(_Edge(1__2)_) <= 1
   0 <= epsilon(_Edge(1__3)_) <= 1
   0 <= epsilon(_Edge(1__4)_) <= 1
   0 <= epsilon(_Edge(2__3)_) <= 1
   0 <= epsilon(_Edge(4__5)_) <= 1
   0 <= kappa(_Sign(neg)_) <= +inf
   0 <= kappa(_Sign(pos)_) <= +inf
   0 <= rho(_Node(1)_Partition(1)_) <= 1
   0 <= rho(_Node(1)_Partition(2)_) <= 1
   0 <= rho(_Node(2)_Partition(1)_) <= 1
   0 <= rho(_Node(2)_Partition(2)_) <= 1
   0 <= rho(_Node(3)_Partition(1)_) <= 1
   0 <= rho(_Node(3)_Partition(2)_) <= 1
   0 <= rho(_Node(4)_Partition(1)_) <= 1
   0 <= rho(_Node(4)_Partition(2)_) <= 1
   0 <= rho(_Node(5)_Partition(1)_) <= 1
   0 <= rho(_Node(5)_Partition(2)_) <= 1
   0 <= xi(_Node(1)_Node(2)_Partition(1)_) <= 1
   0 <= xi(_Node(1)_Node(2)_Partition(2)_) <= 1
   0 <= xi(_Node(1)_Node(3)_Partition(1)_) <= 1
   0 <= xi(_Node(1)_Node(3)_Partition(2)_) <= 1
   0 <= xi(_Node(1)_Node(4)_Partition(1)_) <= 1
   0 <= xi(_Node(1)_Node(4)_Partition(2)_) <= 1
   0 <= xi(_Node(2)_Node(1)_Partition(1)_) <= 1
   0 <= xi(_Node(2)_Node(1)_Partition(2)_) <= 1
   0 <= xi(_Node(2)_Node(3)_Partition(1)_) <= 1
   0 <= xi(_Node(2)_Node(3)_Partition(2)_) <= 1
   0 <= xi(_Node(3)_Node(1)_Partition(1)_) <= 1
   0 <= xi(_Node(3)_Node(1)_Partition(2)_) <= 1
   0 <= xi(_Node(3)_Node(2)_Partition(1)_) <= 1
   0 <= xi(_Node(3)_Node(2)_Partition(2)_) <= 1
   0 <= xi(_Node(4)_Node(1)_Partition(1)_) <= 1
   0 <= xi(_Node(4)_Node(1)_Partition(2)_) <= 1
   0 <= xi(_Node(4)_Node(5)_Partition(1)_) <= 1
   0 <= xi(_Node(4)_Node(5)_Partition(2)_) <= 1
   0 <= xi(_Node(5)_Node(4)_Partition(1)_) <= 1
   0 <= xi(_Node(5)_Node(4)_Partition(2)_) <= 1
   0 <= psi(_Node(1)_Node(2)_Node(2)_) <= 1
   0 <= psi(_Node(1)_Node(2)_Node(3)_) <= 1
   0 <= psi(_Node(1)_Node(2)_Node(4)_) <= 1
   0 <= psi(_Node(1)_Node(3)_Node(2)_) <= 1
   0 <= psi(_Node(1)_Node(3)_Node(3)_) <= 1
   0 <= psi(_Node(1)_Node(3)_Node(4)_) <= 1
   0 <= psi(_Node(1)_Node(4)_Node(2)_) <= 1
   0 <= psi(_Node(1)_Node(4)_Node(3)_) <= 1
   0 <= psi(_Node(1)_Node(4)_Node(4)_) <= 1
   0 <= psi(_Node(2)_Node(1)_Node(3)_) <= 1
   0 <= psi(_Node(2)_Node(3)_Node(1)_) <= 1
   0 <= psi(_Node(2)_Node(3)_Node(3)_) <= 1
   0 <= psi(_Node(3)_Node(1)_Node(2)_) <= 1
   0 <= psi(_Node(3)_Node(2)_Node(1)_) <= 1
   0 <= psi(_Node(4)_Node(1)_Node(5)_) <= 1
   0 <= psi(_Node(4)_Node(5)_Node(1)_) <= 1
   0 <= psi(_Node(4)_Node(5)_Node(5)_) <= 1
binary
  epsilon(_Edge(1__2)_)
  epsilon(_Edge(1__3)_)
  epsilon(_Edge(1__4)_)
  epsilon(_Edge(2__3)_)
  epsilon(_Edge(4__5)_)
  rho(_Node(1)_Partition(1)_)
  rho(_Node(1)_Partition(2)_)
  rho(_Node(2)_Partition(1)_)
  rho(_Node(2)_Partition(2)_)
  rho(_Node(3)_Partition(1)_)
  rho(_Node(3)_Partition(2)_)
  rho(_Node(4)_Partition(1)_)
  rho(_Node(4)_Partition(2)_)
  rho(_Node(5)_Partition(1)_)
  rho(_Node(5)_Partition(2)_)
  xi(_Node(1)_Node(2)_Partition(1)_)
  xi(_Node(1)_Node(2)_Partition(2)_)
  xi(_Node(1)_Node(3)_Partition(1)_)
  xi(_Node(1)_Node(3)_Partition(2)_)
  xi(_Node(1)_Node(4)_Partition(1)_)
  xi(_Node(1)_Node(4)_Partition(2)_)
  xi(_Node(2)_Node(1)_Partition(1)_)
  xi(_Node(2)_Node(1)_Partition(2)_)
  xi(_Node(2)_Node(3)_Partition(1)_)
  xi(_Node(2)_Node(3)_Partition(2)_)
  xi(_Node(3)_Node(1)_Partition(1)_)
  xi(_Node(3)_Node(1)_Partition(2)_)
  xi(_Node(3)_Node(2)_Partition(1)_)
  xi(_Node(3)_Node(2)_Partition(2)_)
  xi(_Node(4)_Node(1)_Partition(1)_)
  xi(_Node(4)_Node(1)_Partition(2)_)
  xi(_Node(4)_Node(5)_Partition(1)_)
  xi(_Node(4)_Node(5)_Partition(2)_)
  xi(_Node(5)_Node(4)_Partition(1)_)
  xi(_Node(5)_Node(4)_Partition(2)_)
  psi(_Node(1)_Node(2)_Node(2)_)
  psi(_Node(1)_Node(2)_Node(3)_)
  psi(_Node(1)_Node(2)_Node(4)_)
  psi(_Node(1)_Node(3)_Node(2)_)
  psi(_Node(1)_Node(3)_Node(3)_)
  psi(_Node(1)_Node(3)_Node(4)_)
  psi(_Node(1)_Node(4)_Node(2)_)
  psi(_Node(1)_Node(4)_Node(3)_)
  psi(_Node(1)_Node(4)_Node(4)_)
  psi(_Node(2)_Node(1)_Node(3)_)
  psi(_Node(2)_Node(3)_Node(1)_)
  psi(_Node(2)_Node(3)_Node(3)_)
  psi(_Node(3)_Node(1)_Node(2)_)
  psi(_Node(3)_Node(2)_Node(1)_)
  psi(_Node(4)_Node(1)_Node(5)_)
  psi(_Node(4)_Node(5)_Node(1)_)
  psi(_Node(4)_Node(5)_Node(5)_)
end
