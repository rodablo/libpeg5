--
--  Copyright (C) 2008, AdaCore
--
package Peg5 is

   type Int is new Integer;

   function "+" (I1, I2 : Int) return Int;

   function "-" (I1, I2 : Int) return Int;

   procedure Some_Procedure (A : in Int; B : in Boolean)
     with Pre => B = True,
     Test_Case => ("Condition 00", Nominal, Requires => A > 25);
   --  pagma Test_Case (Name => "Some_Op_Aux",
   --                    Mode => Nominal,
   --                    Requires => Op > 25
   --                   );
   --  --  pagma Test_Case (Name => "Some_Op_Aux_2"
   --  --                    , Mode => Nominal
   --  --                    , Requires => A > 20
   --  --                    -- , Ensures  => Sqrt'Result < 10.0
   --  --                   );

   function Some_Func return Boolean;
   pragma Test_Case (
                     Name => "Some_Func_Aux_2",
                     Mode => Nominal,
                     -- Requires => Op > 20,
                     Ensures  => Some_Func'Result
                    );

   function Some_Other_Func return Boolean
     with Post => Some_Other_Func'Result = True,
     Test_Case => ("Upper Bound", Robustness),
     Test_Case => ("Lower Bound", Robustness);

end Peg5;
