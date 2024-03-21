import engine.ImageToImageDecryption as ImageToImageDecryption
import engine.TextToImageDecryption as TextToImageDecryption

text_file = './data/encrypted_text.txt'

def main(text_file):
    decrypted_text = TextToImageDecryption.main(text_file)
    ImageToImageDecryption.main(decrypted_text)
    
if __name__ == '__main__':
    main()