"""Efficient Fibonacci number calculation using the fast-doubling method."""


def fibonacci(n: int) -> int:
	"""Return the nth Fibonacci number in O(log n) time."""
	if not isinstance(n, int) or isinstance(n, bool) or n < 0:
		raise ValueError("n must be a non-negative integer")

	def double(k: int) -> tuple[int, int]:
		if k == 0:
			return 0, 1

		a, b = double(k // 2)
		c = a * (2 * b - a)
		d = a * a + b * b
		return (d, c + d) if k & 1 else (c, d)

	return double(n)[0]


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Compute the nth Fibonacci number")
	parser.add_argument("n", type=int, help="a non-negative index")
	args = parser.parse_args()
	print(fibonacci(args.n))
