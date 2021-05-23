--
--
--
with AUnit.Test_Fixtures;
--  with AUnit.Test_Cases;

with Libpeg5lang.Analysis;

package AST_Tests.Foo is
   --
   use Libpeg5lang.Analysis;

   type AST_Test_Data is new AUnit.Test_Fixtures.Test_Fixture with record
      Ctx : Analysis_Context := Create_Context (With_Trivia => True);
      Unit : Analysis_Unit;
   end record;

   --  type Foo_Access is access all AST_Tests.Parent'Class;
   --  type Foo_Test is new AUnit.Test_Cases.Test_Case with record
   --    Fixture : Foo_Access;
   --  end record;
   --  function Name (P : Foo_Test) return AUnit.Message_String;
   --  procedure Register_Tests (P : in out Foo_Test);

   procedure Set_Up (T : in out AST_Test_Data);
   procedure Tear_Down (T : in out AST_Test_Data);

   procedure Test_00 (T : in out AST_Test_Data);
   procedure Test_01 (T : in out AST_Test_Data);

end AST_Tests.Foo;
