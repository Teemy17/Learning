use assert_cmd::Command;
type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn test_no_args() -> TestResult {
   let mut cmd = Command::cargo_bin("q2")?;
   cmd.assert().failure();
    Ok(())

}
#[test]
fn test_temp() -> TestResult {
    let mut cmd = Command::cargo_bin("q2")?;
    cmd.arg("1").assert().success().stdout("1°F is -17.222223°C\n");
    Ok(())


}

#[test]
fn test_no_args_tempreverse() -> TestResult {
    let mut cmd = Command::cargo_bin("tempreverse")?;
    cmd.assert().failure();
     Ok(())
}

#[test]
fn test_tempreverse() -> TestResult {
    let mut cmd = Command::cargo_bin("tempreverse")?;
    cmd.arg("1").assert().success().stdout("1°C is 33.8°F\n");
     Ok(())
}