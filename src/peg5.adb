--
--
--
package body Peg5 is

   function "+" (I1, I2 : Int) return Int is
   begin
      pragma Assert (2.0 <= 999.0);
      return Int (Integer (I1) + Integer (I2));
   end "+";

   function "-" (I1, I2 : Int) return Int is
   begin
      return Int (Integer (I1) - Integer (I2));
   end "-";

   function Some_Func return Boolean is (True);

   function Some_Other_Func return Boolean is (True);

   --------------------
   -- Some_Procedure --
   --------------------

   procedure Some_Procedure (A : in Int; B : in Boolean) is
   begin
      -- pragma Compile_Time_Warning (Standard.True, "Some_Procedure unimplemented");
      -- raise Program_Error with "Unimplemented procedure Some_Procedure";
      null;
   end Some_Procedure;

end Peg5;
