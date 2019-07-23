from PIL import Image

# takes in a output screenshot and crops it to the qr
def crop_to_qr(full_image):
    # default QR code is @ (118, 293) and is 164x164
    return full_image.crop((118, 293, 118 + 164, 293 + 164))
    

# takes in an image and duplicates a horizontal line in it 
def fix_horizontal(qr_image, y_pos):
    # the qr code is squished in some places, we gotta fix the lines
    # get the original size
    orig_width, orig_height = qr_image.size

    # separate the image into 3 parts:
    #  above the line, on it, and below it
    above = qr_image.crop((0, 0, orig_width, y_pos-1))
    line = qr_image.crop((0, y_pos-1, orig_width, y_pos))
    below = qr_image.crop((0, y_pos, orig_width, orig_height))
    
    # resize the line to be two pixels tall
    line = line.resize((orig_width, 2))
    
    # create a new image that is 1px taller
    fixed_qr = Image.new('RGB', (orig_width, orig_height+1))
    
    # first, put back what was above.
    fixed_qr.paste(above, (0, 0))
    
    # put in the line
    fixed_qr.paste(line, (0, y_pos-1))
    
    # put in what was below
    fixed_qr.paste(below, (0, y_pos+1))

    return fixed_qr

# takes in an image and duplicates a vertical line in it
def fix_vertical(qr_image, x_pos):
    # the qr code is squished in some places, we gotta fix the lines
    # get the original size
    orig_width, orig_height = qr_image.size

    # first, separate the image into 3 parts:
    #  to the left of the line, on it, and to the right of it
    left = qr_image.crop((0, 0, x_pos-1, orig_height))
    line = qr_image.crop((x_pos-1, 0, x_pos, orig_height))
    right = qr_image.crop((x_pos, 0, orig_width, orig_height))

    # resize the line to be two pixels wide
    line = line.resize((2, orig_height))

    # create a new image that is 1px wider
    fixed_qr = Image.new('RGB', (orig_width+1, orig_height))

    # first put back the left side
    fixed_qr.paste(left, (0, 0))

    # put in the line
    fixed_qr.paste(line, (x_pos-1, 0))

    # put back what was on the right
    fixed_qr.paste(right, (x_pos+1, 0))
    
    return fixed_qr

# opens a guild card image file and fixes the lines
def fix_eo_qr(filepath):
    # should validate file here....
    im = Image.open(filepath)

    cropped = crop_to_qr(im)
    new_qr = cropped.copy()

    # the positions of the messed up lines
    verticals = [7, 38, 67, 98, 127, 158] # x position of vertical
    horizontals = [7, 38, 67, 98, 127, 158] # y position of horizontal

    # resize the horizontals 
    count = 0
    for y in horizontals:
        # fix the horizontal line.
        # gotta offset every time we do it, though.
        new_qr = fix_horizontal(new_qr, y+count)
        count = count + 1

    count = 0
    for x in verticals:
        # fix the horizontal lines.
        # gotta offset every time we do it, though
        new_qr = fix_vertical(new_qr, x+count)
        count = count + 1

    return new_qr
