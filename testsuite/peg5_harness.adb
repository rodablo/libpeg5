with Dummy_Tests;
with AST_Tests;

with AUnit.Test_Caller;

package body Peg5_Harness is

   package Caller is new AUnit.Test_Caller (Dummy_Tests.SomeTestData);

   function Suite return AUnit.Test_Suites.Access_Test_Suite is
      Result : constant AUnit.Test_Suites.Access_Test_Suite := new AUnit.Test_Suites.Test_Suite;
   begin
      Result.Add_Test (AST_Tests.Suite);
      Result.Add_Test (Caller.Create ("Test Dummy", Dummy_Tests.Test_00'Access));
      return Result;
   end Suite;

end Peg5_Harness;
