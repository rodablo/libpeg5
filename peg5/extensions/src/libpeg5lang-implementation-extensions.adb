with Langkit_Support.Adalog.Debug;
with Langkit_Support.Bump_Ptr;
with Langkit_Support.Text; use Langkit_Support.Text;

with LibPeg5lang.Sources;

--  Extension to store the code for external properties

package body LibPeg5lang.Implementation.Extensions is

   ----------------------------------
   -- Char_Node_P_Denoted_Value --
   ----------------------------------

   function Char_Node_P_Denoted_Value
     (Node : Bare_Char_Node) return Character_Type
   is
      N_Text : constant Text_Type := Text (Node);
   begin
      return Sources.Decode_Character_Literal (N_Text);
   end Char_Node_P_Denoted_Value;

end LibPeg5lang.Implementation.Extensions;