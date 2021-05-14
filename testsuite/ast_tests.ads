--
--
--
with AUnit.Test_Fixtures;
with Libpeg5lang.Analysis;

package AST_Tests is
   --
   use Libpeg5lang.Analysis;

   type AST_Test_Data is new AUnit.Test_Fixtures.Test_Fixture with record
      Ctx : Analysis_Context := Create_Context (With_Trivia => True);
      Unit : Analysis_Unit;
   end record;

   procedure Set_Up (T : in out AST_Test_Data);
   -- procedure Tear_Down (T : in out AST_Test_Data);

   procedure Test_00 (T : in out AST_Test_Data);

end AST_Tests;
