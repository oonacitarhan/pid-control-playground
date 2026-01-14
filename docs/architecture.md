# Architecture

The controller differentiates measurement to avoid setpoint kick and conditionally integrates to limit windup. An Euler-integrated first-order plant adds a midpoint load step. Trace metrics report integral absolute error, final error, overshoot, settling time, and control effort.

## Data flow

- `controlbench/core.py` — algorithm primitives.
- `controlbench/features.py` — experiment and analysis APIs.
- `controlbench/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload.

## Limits

Simulation only. The plant excludes encoder quantization, delay, friction and electrical dynamics. Gains and actuator limits are not certified for real motors; the settling tolerance is absolute speed error.
