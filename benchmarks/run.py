import sys,time,statistics,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from controlbench.features import *
durations=[]
for _ in range(5):
    start=time.perf_counter()
    experiment(duration=3)
    durations.append(time.perf_counter()-start)
print(json.dumps({'workload':'experiment(duration=3)','repetitions':len(durations),'median_seconds':statistics.median(durations),'min_seconds':min(durations)}))
