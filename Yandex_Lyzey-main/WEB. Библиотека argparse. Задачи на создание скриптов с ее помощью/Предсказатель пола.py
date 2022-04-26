import argparse

parser = argparse.ArgumentParser(
    description="the analyzer")
parser.add_argument('--barbie', default=50, type=int,
                    help='barbie')
parser.add_argument('--cars', default=50, type=int,
                    help='cars')
parser.add_argument('--movie', default='other', type=str,
                    help='movie')
args = parser.parse_args()
barbie = args.barbie if 0 <= args.barbie <= 100 else 50
cars = args.cars if 0 <= args.cars <= 100 else 50
if args.movie == 'melodrama':
    movie = 0
elif args.movie == 'football':
    movie = 100
else:
    movie = 50
result = int((100 - barbie + cars + movie) / 3)
print(f'boy: {result}')
print(f'girl: {(100 - result)}')
