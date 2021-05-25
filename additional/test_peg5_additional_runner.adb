--
--
--
with AUnit.Reporter.Text;
--  with AUnit.Reporter.GNATtest;
--  with AUnit.Reporter.XML;
with AUnit.Run;
with test_peg5_additional;

procedure test_peg5_additional_runner is
   procedure Runner is new AUnit.Run.Test_Runner (test_peg5_additional.Suite);
   Reporter : AUnit.Reporter.Text.Text_Reporter;
   --  Reporter : AUnit.Reporter.GNATtest.GNATtest_Reporter;
   --  Reporter : AUnit.Reporter.XML.XML_Reporter;
begin
   Reporter.Set_Use_ANSI_Colors (Value => True);
   Runner (Reporter);
end test_peg5_additional_runner;
