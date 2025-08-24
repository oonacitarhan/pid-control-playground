from controlbench.features import experiment,metrics,sweep
def test_tracking():
    result=metrics(experiment(),.01)
    assert result['final_error']<.01 and result['settling_time'] is not None
def test_disturbance_rejection():
    rows=experiment(disturbance=.1,duration=25)
    assert abs(rows[-1]['speed']-.7)<.01
def test_unsettled():
    rows=[{'speed':0,'target':1,'control':1,'time':0}]
    assert metrics(rows,.1)['settling_time'] is None
def test_bad_timestep():
    try:experiment(dt=1,tau=.4)
    except ValueError:return
    raise AssertionError('unstable timestep accepted')
