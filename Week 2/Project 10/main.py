import qrcode

from qrcode.constants import ERROR_CORRECT_L

def qr_generate(data, file_name="qrcode.png", error_correction=ERROR_CORRECT_L, box_size=10, border=4):
    
    try:
        
        qr = qrcode.QRCode(
            version=None,
            error_correction=error_correction,
            box_size=box_size,
            border=border
        )

        qr.add_data(data)
        qr.make(fit=True)


        img = qr.make_image(fill_color="black", back_color="white")

        img.save(file_name)
        
        print(f"QR Code Successfully generated and saved as {file_name}.")

    except Exception as e:
        print(f"An error occured: {e}")


def main():
    print("\n")
    print("Welcome to the QR Code Generator! \n")

    data = input("Enter the data to encode in the QR code: ")

    file_name = input("Enter the file name to save the QR code (Default: qrcode.png): ") or "qrcode.png"


    qr_generate(data, file_name=file_name)

if __name__ == "__main__":
    main()