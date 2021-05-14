with Peg5_Tests; --use Peg5_Tests;
with AST_Tests.Suite;

with AUnit.Test_Caller;

package body Peg5_Suite is
   --use AUnit.Test_Suites;
   --use AUnit.Test_Caller;

   package Caller is new AUnit.Test_Caller (Peg5_Tests.SomeTestData);

   function Suite return AUnit.Test_Suites.Access_Test_Suite is
      Result : constant AUnit.Test_Suites.Access_Test_Suite := new AUnit.Test_Suites.Test_Suite;
   begin
      -- Ret.Add_Test(Caller.Create("Test addition", Test_Addition'Access));
      -- Ret.Add_Test(Caller.Create("Test subtraction", Test_Subtraction'Access));
      Result.Add_Test (AST_Tests.Suite.Suite);
      Result.Add_Test (Caller.Create("Test Dummy", Peg5_Tests.Test_Dummy'Access));
      return Result;
   end Suite;

end Peg5_Suite;
