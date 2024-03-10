import ImageToImageDecryption
import TextToImageDecryption

text_file = './data/encrypted_text.txt'

def main():
    decrypted_text = TextToImageDecryption.main(text_file)
    ImageToImageDecryption.main(decrypted_text)
    
if __name__ == '__main__':
    main()