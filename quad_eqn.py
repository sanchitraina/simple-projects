import math
class quad_eqn(object):

	def __init__(self, coefx2, coefx, const):
		self.coefx2 = coefx2
		self.coefx = coefx
		self.const = const

	def calc_soln(self):
		if ((self.coefx * self.coefx) - (4 * self.coefx2 * self.const)) < 0:
			val = float(-((self.coefx * self.coefx) - (4 * self.coefx2 * self.const)))
			det = math.sqrt(val)
			# I couldn't figure out how to calculate the imaginary numbers :P
			sol1 = str(float(-self.coefx / (2 * self.coefx2))) + ' + ' + str(float(det / (2 * self.coefx2))) + 'i'
			sol2 = str(float(-self.coefx / (2 * self.coefx2))) + ' - ' + str(float(det / (2 * self.coefx2))) + 'i'
			return '\nThe solutions are imaginary numbers. %s and %s' % (sol1, sol2)
		elif ((self.coefx * self.coefx) - (4 * self.coefx2 * self.const)) == 0:
			return '\nBoth the solutions are equal and it\'s value is %f' % (float(-self.coefx / (2 * self.coefx2)))
		else:
			det = float(math.sqrt((self.coefx * self.coefx) - (4 * self.coefx2 * self.const)))
			sol1 = float(-(self.coefx + det) / (2 * self.coefx2))
			sol2 = float(-(self.coefx - det) / (2 * self.coefx2))
			return "\nThe solutions of this equation are: %d, %d" % (sol1, sol2)
ans = 'y'
ans_list = ['y', 'yes', 'YES', 'Yes']
while ans in ans_list:
	x2 = float(raw_input("\nEnter the coefficient of x squared: "))
	x = float(raw_input("\nEnter the coefficient of x: "))
	c = float(raw_input("\nEnter the constant: "))

	eqn = quad_eqn(x2, x, c)
	print eqn.calc_soln()

	ans = raw_input("\nDo you want to solve another equation?(y/n) ")