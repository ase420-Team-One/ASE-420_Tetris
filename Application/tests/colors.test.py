import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.pardir,'Themes')))


# Basic python because pytest does not play well with adding system paths.


from colors import Colors
colors = Colors()
assert len(colors._colors)>0
assert colors.PRIMARY != None
assert colors.SECONDARY != None
assert colors.TERTIARY != None
assert type(colors.select(1)) == tuple
assert type(colors.select(1)) == tuple
print("Colors Exist")
assert type(colors.select(colors.random())) == tuple
for s in range(40):
    assert colors.random()<len(colors._colors)
color1=colors.random()
color2=colors.random()
color3=colors.random()
color4=colors.random()
assert color1 != color2 or color1 != color3 or color1 != color4
print("Color Randomizer not broken.")
assert colors.PRIMARY ==(255,255,255)
assert colors.SECONDARY ==(0,0,0)
assert colors.TERTIARY ==(128,128,128)
print("Default Correct")
colors.dark()
assert colors.PRIMARY ==(23,22,26)
assert colors.SECONDARY ==(70,70,82)
assert colors.TERTIARY ==(217,217,220)
print("Dark Correct")
colors.light()
assert colors.PRIMARY ==(255,255,255)
assert colors.SECONDARY ==(0,0,0)
assert colors.TERTIARY ==(128,128,128)
print("Light Correct")