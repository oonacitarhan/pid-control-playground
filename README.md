# PID Control Playground

Evaluate discrete PID settings on a first-order motor simulation with disturbance injection and control-quality metrics.

**Python** · Reusable core · CLI examples · Regression checks · Reproducible benchmark

> **Provenance:** created with AI assistance on **2026-11-01**.
> All commit author and committer dates are synthetic and distributed across
> November 2024–October 2026. They do not establish work on those dates.

## Quick start

```sh
python3 -m controlbench examples/motor.json --csv /tmp/motor-trace.csv
python3 -m controlbench examples/loaded-motor.json
```

## Repository map

- `controlbench/core.py` — algorithm primitives.
- `controlbench/features.py` — experiment and analysis APIs.
- `controlbench/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload.

## How it works

The controller differentiates measurement to avoid setpoint kick and conditionally integrates to limit windup. An Euler-integrated first-order plant adds a midpoint load step. Trace metrics report integral absolute error, final error, overshoot, settling time, and control effort.

## Verification

```sh
sh scripts/check.sh
```

Seven test groups plus the original reference Python checks exercise reference cases, invalid inputs, and relevant invariants.
The complete local run is in [docs/verification.txt](docs/verification.txt).
The [checks workflow](.github/workflows/check.yml) executes the same source checks.

## Boundaries

Simulation only. The plant excludes encoder quantization, delay, friction and electrical dynamics. Gains and actuator limits are not certified for real motors; the settling tolerance is absolute speed error.

See [architecture](docs/architecture.md), [usage](docs/usage.md),
[release notes](CHANGELOG.md), and [provenance](PROVENANCE.json).

## License

MIT — [LICENSE](LICENSE).
