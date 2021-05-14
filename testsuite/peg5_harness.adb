--
--
--
--with AUnit.Reporter.Text;
with AUnit.Reporter.GNATtest;
with AUnit.Run;
with Peg5_Suite; --use Peg5.Suite;

procedure Peg5_Harness is
   procedure Runner is new AUnit.Run.Test_Runner (Peg5_Suite.Suite);
--   Reporter : AUnit.Reporter.Text.Text_Reporter;
   Reporter : AUnit.Reporter.GNATtest.GNATtest_Reporter;
begin

   Runner (Reporter);
end Peg5_Harness;
