--
--
--
with AUnit.Assertions; use AUnit.Assertions;

package body Peg5_Tests is

   procedure Set_Up (T : in out SomeTestData) is
   begin
      null;
   end Set_Up;

   procedure Test_Dummy (T : in out SomeTestData) is
   begin
      --pragma Unreferenced (T);
      Assert (True, "Dummy message.");
   end Test_Dummy;

end Peg5_Tests;
