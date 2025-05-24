from src.utils import run_command

def test_run_command_success():
    out, err, code = run_command("echo hello")
    assert out.strip() == "hello"
    assert err == ""
    assert code == 0

def test_run_command_failure():
    out, err, code = run_command("nonexistentcommand1234")
    assert code != 0
    assert err != "" 