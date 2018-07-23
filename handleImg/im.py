from PIL import Image
n12090 = Image.new('RGB',(120,90),'black')
# n12090.show()
n12060 = Image.new('RGB',(120,70),'white')
# n12060.show()
n12090.paste(n12060,(0,10))
n12090.show()