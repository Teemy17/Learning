use assert_cmd::Command;
type TestResult = Result<(), Box<dyn std::error::Error>>;
#[test]
fn test_no_args() -> TestResult {
   let mut cmd = Command::cargo_bin("rusty")?;
   cmd.assert().failure();
    Ok(())

}
#[test]
fn test_area() -> TestResult {
    let mut cmd = Command::cargo_bin("rusty")?;
    cmd.arg("1").assert().success().stdout("Area: 3.1416\n");
    Ok(())


}