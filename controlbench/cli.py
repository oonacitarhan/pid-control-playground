import argparse,json,csv
from .features import experiment,metrics
def main():
    parser=argparse.ArgumentParser(description='Simulate motor PID response from JSON configuration')
    parser.add_argument('config');parser.add_argument('--csv')
    args=parser.parse_args()
    try:
        with open(args.config) as f:config=json.load(f)
        rows=experiment(**config)
        if args.csv:
            with open(args.csv,'w',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
        print(json.dumps(metrics(rows,config.get('dt',.01)),indent=2))
    except (ValueError,KeyError,OSError,TypeError) as error:parser.error(str(error))
