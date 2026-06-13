import subprocess,sys
def test_help():
    result=subprocess.run([sys.executable,'-m','controlbench','--help'],text=True,capture_output=True)
    assert result.returncode==0 and 'usage:' in result.stdout
def test_cli_rejects_unknown_argument():
    result=subprocess.run([sys.executable,'-m','controlbench','--unknown-option'],text=True,capture_output=True)
    assert result.returncode!=0

def test_documented_workflow():
    import json
    result=subprocess.run([sys.executable,'-m','controlbench',*['examples/motor.json']],text=True,capture_output=True)
    assert result.returncode==0, result.stderr
    data=json.loads(result.stdout)
    assert data['final_error']<.01 and data['settling_time'] is not None
