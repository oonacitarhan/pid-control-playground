from .core import PID

def experiment(kp=2,ki=1,kd=.02,target=.7,dt=.01,duration=15,tau=.4,disturbance=0):
    if dt<=0 or duration<=0 or tau<=0 or dt>tau:raise ValueError('need 0<dt<=tau and positive duration')
    controller=PID(kp,ki,kd);speed=0;rows=[]
    for step in range(int(duration/dt)):
        t=step*dt;u=controller.step(target,speed,dt)
        load=disturbance if t>=duration/2 else 0
        speed+=dt*(u-speed-load)/tau
        rows.append({'time':t,'speed':speed,'control':u,'target':target})
    if not rows:raise ValueError('duration must include at least one step')
    return rows

def metrics(rows,dt,tolerance=.02):
    if not rows or dt<=0 or tolerance<0:raise ValueError('invalid trace or tolerance')
    errors=[abs(row['target']-row['speed']) for row in rows]
    violations=[i for i,e in enumerate(errors) if e>tolerance]
    settling=None if violations and violations[-1]==len(rows)-1 else (violations[-1]+1)*dt if violations else 0
    return {'integral_absolute_error':sum(errors)*dt,'final_error':errors[-1],
            'overshoot':max(0,max(row['speed']-row['target'] for row in rows)),
            'settling_time':settling,'control_effort':sum(row['control']**2 for row in rows)*dt}

def sweep(gains,**kwargs):
    return [{'kp':kp,**metrics(experiment(kp=kp,**kwargs),kwargs.get('dt',.01))} for kp in gains]
