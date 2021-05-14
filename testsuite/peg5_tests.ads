--
--
--
with AUnit;
with AUnit.Test_Fixtures;
-- with Peg5; use Peg5;

package Peg5_Tests is

   type SomeTestData is new AUnit.Test_Fixtures.Test_Fixture with null record;

   procedure Set_Up (T : in out SomeTestData);
   -- procedure Tear_Down (T : in out SomeTestData);
   procedure Test_Dummy (T : in out SomeTestData);

end Peg5_Tests;
