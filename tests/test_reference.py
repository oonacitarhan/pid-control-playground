from controlbench.core import *

def self_test():
    history=simulate()
    assert abs(history[-1][1]-.7)<.01
    assert all(-1<=u<=1 for _,_,u in history)
    controller=PID(2,1,0)
    for _ in range(100): assert controller.step(100,0,.01)==1
    assert controller.integral==0
    controller.reset(); assert controller.previous is None
    try: controller.step(1,0,0)
    except ValueError: pass
    else: raise AssertionError('nonpositive dt accepted')
    return history[-1]

def test_original_reference_cases():
    self_test()
