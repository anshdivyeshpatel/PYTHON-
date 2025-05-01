def convert():
    byte = float(input("Enter Bytes:   "))
    kb = byte*0.001
    mb =  byte*0.000001
    gb = byte*0.000000001
    print(f"{kb}KB {mb}MB {gb}GB")
convert()