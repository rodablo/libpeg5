--
--
--
with AUnit.Test_Caller;
with AUnit.Test_Suites;
with AST_Tests.Foo;

package body AST_Tests is
   use AUnit.Test_Suites;

   package Caller is new AUnit.Test_Caller (AST_Tests.Foo.AST_Test_Data);

   function Suite return Access_Test_Suite is
      Result : constant Access_Test_Suite := new Test_Suite;
   begin
      Result.Add_Test (Caller.Create ("Test 00", AST_Tests.Foo.Test_00'Access));
      --  Result.Add_Test (Caller.Create ("Test 01", AST_Tests.Foo.Test_01'Access));
      Add_Test (Result, Caller.Create ("Test 01", AST_Tests.Foo.Test_01'Access));
      return Result;
   end Suite;

end AST_Tests;
