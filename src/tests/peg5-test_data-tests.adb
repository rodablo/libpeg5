--  This package has been generated automatically by GNATtest.
--  You are allowed to add your code to the bodies of test routines.
--  Such changes will be kept during further regeneration of this file.
--  All code placed outside of test routine bodies will be lost. The
--  code intended to set up and tear down the test environment should be
--  placed into Peg5.Test_Data.

with AUnit.Assertions; use AUnit.Assertions;
with System.Assertions;

--  begin read only
--  id:2.2/00/
--
--  This section can be used to add with clauses if necessary.
--
--  end read only

--  begin read only
--  end read only
package body Peg5.Test_Data.Tests is

--  begin read only
--  id:2.2/01/
--
--  This section can be used to add global variables and other elements.
--
--  end read only

--  begin read only
--  end read only
--  begin read only
   procedure Wrap_Test_Some_Procedure_fbf12b_538bcf (A : in Int; B : in Boolean) 
   is
   begin
      begin
         pragma Assert
           ((B = True) and (A > 25));
         null;
      exception
         when System.Assertions.Assert_Failure =>
            AUnit.Assertions.Assert
              (False,
               "req_sloc(peg5.ads:14):Condition 00 test requirement violated");
      end;
      GNATtest_Generated.GNATtest_Standard.Peg5.Some_Procedure (A, B);
      begin
         pragma Assert
           (True);
         null;
      exception
         when System.Assertions.Assert_Failure =>
            AUnit.Assertions.Assert
              (False,
               "ens_sloc(peg5.ads:0:):Condition 00 test commitment violated");
      end;
   end Wrap_Test_Some_Procedure_fbf12b_538bcf;
--  end read only

--  begin read only
   procedure Test_Some_Procedure_condition_00 (Gnattest_T : in out Test);
   procedure Test_Some_Procedure_fbf12b_538bcf (Gnattest_T : in out Test) renames Test_Some_Procedure_condition_00;
--  id:2.2/fbf12b866d1bd8fe/Some_Procedure/1/0/condition_00/
   procedure Test_Some_Procedure_condition_00 (Gnattest_T : in out Test) is
   --  peg5.ads:12:4:Some_Procedure
   procedure Some_Procedure (A : in Int; B : in Boolean) renames Wrap_Test_Some_Procedure_fbf12b_538bcf;
--  end read only

      pragma Unreferenced (Gnattest_T);

   begin

      AUnit.Assertions.Assert
        (Gnattest_Generated.Default_Assert_Value,
         "Test not implemented.");

--  begin read only
   end Test_Some_Procedure_condition_00;
--  end read only

--  begin read only
   function Wrap_Test_Some_Func_87f90f_e2e554 return Boolean
   is
   begin
      begin
         pragma Assert
           (True);
         null;
      exception
            when System.Assertions.Assert_Failure =>
               AUnit.Assertions.Assert
                 (False,
                  "req_sloc(peg5.ads:0:):Some_Func_Aux_2 test requirement violated");
      end;
      declare
         Test_Some_Func_87f90f_e2e554_Result : constant Boolean := GNATtest_Generated.GNATtest_Standard.Peg5.Some_Func;
      begin
         begin
            pragma Assert
              (Test_Some_Func_87f90f_e2e554_Result);
            null;
         exception
            when System.Assertions.Assert_Failure =>
               AUnit.Assertions.Assert
                 (False,
                  "ens_sloc(peg5.ads:30:):Some_Func_Aux_2 test commitment violated");
         end;
         return Test_Some_Func_87f90f_e2e554_Result;
      end;
   end Wrap_Test_Some_Func_87f90f_e2e554;
--  end read only

--  begin read only
   procedure Test_Some_Func_some_func_aux_2 (Gnattest_T : in out Test);
   procedure Test_Some_Func_87f90f_e2e554 (Gnattest_T : in out Test) renames Test_Some_Func_some_func_aux_2;
--  id:2.2/87f90f7bc8891e19/Some_Func/1/0/some_func_aux_2/
   procedure Test_Some_Func_some_func_aux_2 (Gnattest_T : in out Test) is
   --  peg5.ads:25:4:Some_Func
      function Some_Func return Boolean renames Wrap_Test_Some_Func_87f90f_e2e554;
--  end read only

      pragma Unreferenced (Gnattest_T);

   begin

      AUnit.Assertions.Assert
        (Gnattest_Generated.Default_Assert_Value,
         "Test not implemented.");

--  begin read only
   end Test_Some_Func_some_func_aux_2;
--  end read only

--  begin read only
   function Wrap_Test_Some_Other_Func_b2fde4_311194 return Boolean
   is
   begin
      declare
         Test_Some_Other_Func_b2fde4_311194_Result : constant Boolean := GNATtest_Generated.GNATtest_Standard.Peg5.Some_Other_Func;
      begin
         return Test_Some_Other_Func_b2fde4_311194_Result;
      end;
   end Wrap_Test_Some_Other_Func_b2fde4_311194;
--  end read only

--  begin read only
   procedure Test_Some_Other_Func_upper_bound (Gnattest_T : in out Test);
   procedure Test_Some_Other_Func_b2fde4_311194 (Gnattest_T : in out Test) renames Test_Some_Other_Func_upper_bound;
--  id:2.2/b2fde4bf69985186/Some_Other_Func/1/0/upper_bound/
   procedure Test_Some_Other_Func_upper_bound (Gnattest_T : in out Test) is
   --  peg5.ads:33:4:Some_Other_Func
      function Some_Other_Func return Boolean renames Wrap_Test_Some_Other_Func_b2fde4_311194;
--  end read only

      pragma Unreferenced (Gnattest_T);

   begin

      AUnit.Assertions.Assert
        (Gnattest_Generated.Default_Assert_Value,
         "Test not implemented.");

--  begin read only
   end Test_Some_Other_Func_upper_bound;
--  end read only

--  begin read only
   function Wrap_Test_Some_Other_Func_b2fde4_db24d6 return Boolean
   is
   begin
      declare
         Test_Some_Other_Func_b2fde4_db24d6_Result : constant Boolean := GNATtest_Generated.GNATtest_Standard.Peg5.Some_Other_Func;
      begin
         return Test_Some_Other_Func_b2fde4_db24d6_Result;
      end;
   end Wrap_Test_Some_Other_Func_b2fde4_db24d6;
--  end read only

--  begin read only
   procedure Test_Some_Other_Func_lower_bound (Gnattest_T : in out Test);
   procedure Test_Some_Other_Func_b2fde4_db24d6 (Gnattest_T : in out Test) renames Test_Some_Other_Func_lower_bound;
--  id:2.2/b2fde4bf69985186/Some_Other_Func/1/0/lower_bound/
   procedure Test_Some_Other_Func_lower_bound (Gnattest_T : in out Test) is
   --  peg5.ads:33:4:Some_Other_Func
      function Some_Other_Func return Boolean renames Wrap_Test_Some_Other_Func_b2fde4_db24d6;
--  end read only

      pragma Unreferenced (Gnattest_T);

   begin

      AUnit.Assertions.Assert
        (Gnattest_Generated.Default_Assert_Value,
         "Test not implemented.");

--  begin read only
   end Test_Some_Other_Func_lower_bound;
--  end read only


--  begin read only
   --  procedure Test_Some_Op_some_op_aux (Gnattest_T : in out Test_);
   --  procedure Test_Some_Op_11c0d1_some_op_aux (Gnattest_T : in out Test_) renames Test_Some_Op_some_op_aux;
--  id:2.2/11c0d1f43b127c75/Some_Op/1/1/some_op_aux/
   --  procedure Test_Some_Op_some_op_aux (Gnattest_T : in out Test_) is
--  end read only
--  
--        pragma Unreferenced (Gnattest_T);
--  
--     begin
--  
--        AUnit.Assertions.Assert
--          (Gnattest_Generated.Default_Assert_Value,
--           "Test not implemented.");
--  
--  begin read only
   --  end Test_Some_Op_some_op_aux;
--  end read only


--  begin read only
   --  procedure Test_Some_Op_some_op_aux_2 (Gnattest_T : in out Test_);
   --  procedure Test_Some_Op_11c0d1_some_op_aux_2 (Gnattest_T : in out Test_) renames Test_Some_Op_some_op_aux_2;
--  id:2.2/11c0d1f43b127c75/Some_Op/1/1/some_op_aux_2/
   --  procedure Test_Some_Op_some_op_aux_2 (Gnattest_T : in out Test_) is
--  end read only
--  
--        pragma Unreferenced (Gnattest_T);
--  
--     begin
--  
--        AUnit.Assertions.Assert
--          (Gnattest_Generated.Default_Assert_Value,
--           "Test not implemented.");
--  
--  begin read only
   --  end Test_Some_Op_some_op_aux_2;
--  end read only


--  begin read only
   --  procedure Test_Some_Op_condition_00 (Gnattest_T : in out Test_);
   --  procedure Test_Some_Op_700a28_condition_00 (Gnattest_T : in out Test_) renames Test_Some_Op_condition_00;
--  id:2.2/700a280ad7177c86/Some_Op/1/1/condition_00/
   --  procedure Test_Some_Op_condition_00 (Gnattest_T : in out Test_) is
--  end read only
--  
--        pragma Unreferenced (Gnattest_T);
--  
--     begin
--  
--        AUnit.Assertions.Assert
--          (Gnattest_Generated.Default_Assert_Value,
--           "Test not implemented.");
--  
--  begin read only
   --  end Test_Some_Op_condition_00;
--  end read only

--  begin read only
--  id:2.2/02/
--
--  This section can be used to add elaboration code for the global state.
--
begin
--  end read only
   null;
--  begin read only
--  end read only
end Peg5.Test_Data.Tests;
