import ui

def dvoika(k, sender):
	if k // 2 != 0:
		dvoika(k // 2, sender)
	csl = k % 2
	sender.superview['label1'].text += str(csl)

def perevesti(sender):
	m = 0
	m += 1
	k = sender.superview['textfield1'].text
	if m != 0:
		sender.superview['label1'].text = ' '
	dvoika(eval(k), sender)
	
v = ui.load_view()
v.present('sheet')
