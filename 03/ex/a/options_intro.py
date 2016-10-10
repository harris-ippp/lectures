import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", help="A number!")
args = parser.parse_args()

print(args)
