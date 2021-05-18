--
--
--
with AUnit.Reporter.Text;
--  with AUnit.Reporter.GNATtest;
--  with AUnit.Reporter.XML;
with AUnit.Run;
with Peg5_Harness;

procedure Peg5_Harness_Runner is
   procedure Runner is new AUnit.Run.Test_Runner (Peg5_Harness.Suite);
   Reporter : AUnit.Reporter.Text.Text_Reporter;
   --  Reporter : AUnit.Reporter.GNATtest.GNATtest_Reporter;
   --  Reporter : AUnit.Reporter.XML.XML_Reporter;
begin
   Reporter.Set_Use_ANSI_Colors (Value => True);
   Runner (Reporter);
end Peg5_Harness_Runner;
