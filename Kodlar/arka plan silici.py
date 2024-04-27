from rembg import remove
input_pat="image.jpg"
output_pat="output.png"
with open(input_pat,'rb')as i:
    with open(output_pat,'wb')as o:
        input_file=i.read()
        output_file=remove(input_file)
        o.write(output_file)