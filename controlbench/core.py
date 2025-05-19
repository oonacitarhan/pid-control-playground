"""Simulation only; gains and safety limits must be retuned for real hardware."""
class PID:
    def __init__(self,kp,ki,kd,lower=-1,upper=1):
        if lower>=upper: raise ValueError('invalid actuator limits')
        self.kp,self.ki,self.kd=kp,ki,kd
        self.lower,self.upper=lower,upper
        self.integral=0; self.previous=None
    def reset(self): self.integral=0; self.previous=None
    def step(self,target,measurement,dt):
        if dt<=0: raise ValueError('dt must be positive')
        error=target-measurement
        derivative=0 if self.previous is None else -(measurement-self.previous)/dt
        candidate=self.integral+error*dt
        raw=self.kp*error+self.ki*candidate+self.kd*derivative
        # Conditional integration prevents further windup in the saturation direction.
        if self.lower<=raw<=self.upper or (raw>self.upper and error<0) or (raw<self.lower and error>0):
            self.integral=candidate
        self.previous=measurement
        return max(self.lower,min(self.upper,raw))

def simulate(target=.7,steps=1500):
    controller=PID(2,1,.02)
    speed=0.; history=[]
    for i in range(steps):
        control=controller.step(target,speed,.01)
        speed += .01*(control-speed)/.4
        history.append((i*.01,speed,control))
    return history

