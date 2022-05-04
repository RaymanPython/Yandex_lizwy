import argparse

params = argparse.ArgumentParser()
params.add_argument("arg", nargs='*', default=['no args'])
args = params.parse_args().arg
for i in args:
    print(i)
