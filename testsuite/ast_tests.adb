--
--
--
with AUnit.Assertions; use AUnit.Assertions;

with Ada.Text_IO;           use Ada.Text_IO;
with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;

-- with Libpeg5lang.Analysis;  use Libpeg5lang.Analysis;
with Libpeg5lang.Common;    use Libpeg5lang.Common;
with Libpeg5lang.Iterators; use Libpeg5lang.Iterators;

package body AST_Tests is

   procedure Set_Up (T : in out AST_Test_Data) is
   begin
      T.Ctx := Create_Context(With_Trivia => True);
      T.Unit := Get_From_File (T.Ctx, "/home/rodablo/libpeg5lang/testsuite/test.peg");
   end Set_Up;

   --
   procedure Test_00 (T : in out AST_Test_Data) is

      --Ctx       : constant Analysis_Context :=
      --  Create_Context(With_Trivia => True);
      --T.Unit := Get_From_File (T.Ctx, "/home/rodablo/libpeg5lang/tests/000.peg");
      Type_Defs : constant P5_Node_Array :=
        Find (T.Unit.Root, Kind_Is (Peg5_Dot)).Consume;

   begin
      --  Print (Unit);
      for K of Type_Defs loop
         declare
         --  TD   : constant P5_Node_Kind_Type := T.As_Type_Decl;
         --  RTD  : constant Record_Type_Def :=
         --   TD.F_Type_Def.As_Record_Type_Def;
         --  Name : constant Text_Type := TD.F_Name.Text;

         begin
            Put (Child_Index (K));
            Put_Line ("-----");

            Print (K, True);
            --  Put_Line ("hola");
            -- Assert (T.I1 - T.I2 = 2, "Incorrect result after subtraction");
            -- Assert (True, "hola");
            --(Image (Name) & " is abstract: ");
            --  & Boolean'Image (RTD.F_Has_Abstract));
         end;
      end loop;
      Put_Line ("Done.");
   end Test_00;

end AST_Tests;
