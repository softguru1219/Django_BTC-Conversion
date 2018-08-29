from django import template

register = template.Library()

@register.filter
def multiply_operator(amount, rate):
	if not amount or rate:
		return 0.0

	return float(amount) * float(rate)
