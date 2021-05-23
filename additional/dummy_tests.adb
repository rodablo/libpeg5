--
--
--
with AUnit.Assertions; use AUnit.Assertions;

package body Dummy_Tests is

   procedure Set_Up (T : in out SomeTestData) is
   begin
      null;
   end Set_Up;

   procedure Test_00 (T : in out SomeTestData) is
   begin
      --  pragma Unreferenced (T);
      Assert (False, "Dummy message.");
   end Test_00;

end Dummy_Tests;
