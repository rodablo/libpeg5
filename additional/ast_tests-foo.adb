--
--
--
with AUnit.Assertions; use AUnit.Assertions;

with Ada.Text_IO;           use Ada.Text_IO;
--  with Ada.Integer_Text_IO;   use Ada.Integer_Text_IO;

with Libpeg5lang.Analysis;  -- use Libpeg5lang.Analysis;
with Libpeg5lang.Common;    use Libpeg5lang.Common;
with Libpeg5lang.Iterators; use Libpeg5lang.Iterators;

package body AST_Tests.Foo is

   --  function Name (P : Foo_Test) return Message_String is "tptp";

   --  procedure Register_Tests (P : in out Foo_Test) is
   --     package Register_Specific is
   --        new AUnit.Test_Cases.Specific_Test_Case_Registration (Foo_Test);
   --     use AST_Tests.Foo.Register_Specific;
   --  begin
   --     null;
   --  end Register_Tests;

   procedure Set_Up (T : in out AST_Test_Data) is
   begin
      T.Ctx := Create_Context (With_Trivia => True);
      T.Unit := Get_From_File (T.Ctx, "../../../../additional/test.peg");
   end Set_Up;

   procedure Tear_Down (T : in out AST_Test_Data) is
      package LAL renames Libpeg5lang.Analysis;
      pragma Unreferenced (LAL);
   begin
--  begin read only
--  LAL.  .Destroy(T.Ctx);
--  end read only
      null;
   end Tear_Down;

   --
   procedure Test_00 (T : in out AST_Test_Data) is

      --  Ctx       : constant Analysis_Context :=
      --  Create_Context(With_Trivia => True);
      --  T.Unit := Get_From_File (T.Ctx, "../../../../testsuite/000.peg");
      Type_Defs : constant P5_Node_Array :=
        Find (T.Unit.Root, Kind_Is (Peg5_Dot)).Consume;

   begin
      Assert (Type_Defs'Length > 0, "Empty");
      Put_Line (Type_Defs'Length'Image);
      Assert (Type_Defs'Length = 18, "Diff");
      for K of Type_Defs loop
         declare
         --  TD   : constant P5_Node_Kind_Type := T.As_Type_Decl;
         --  RTD  : constant Record_Type_Def :=
         --   TD.F_Type_Def.As_Record_Type_Def;
         --  Name : constant Text_Type := TD.F_Name.Text;

         begin
            --  Put (Child_Index (K));
            --  Put_Line ("-----");

            --  Print (K, True);
            --  Put_Line ("hola");
            Assert (True, "True");
            --(Image (Name) & " is abstract: ");
            --  & Boolean'Image (RTD.F_Has_Abstract));
            null;
         end;
      end loop;
      --  Put_Line ("Done.");
   end Test_00;

   procedure Test_01 (T : in out AST_Test_Data) is
   begin
     null;
   end Test_01;

end AST_Tests.Foo;
