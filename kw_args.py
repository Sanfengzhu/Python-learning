def f1(a, b, c=0, *, d, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
f1(1,2, d=99, ext=None)
