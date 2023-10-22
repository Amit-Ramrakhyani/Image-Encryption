# Image Encryption

# Getting Started

## Dependencies

* Clone the repository using the command below:

```
git clone https://github.com/Amit-Ramrakhyani/Image-Encryption.git
```

* Move into the directory where we have the project files :
  
```
cd Image-Encryption
```

* Create a virtual environment :
  
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv venv

```

* Activate the virtual environment :
```bash
source venv\scripts\activate
```

* Install the requirements :
```bash
pip install -r requirements.txt

```

## Executing the program

- Use the following command in the command prompt to *input and resize the image*:

```
python3 resize_image.py
```

- Use the following command in the command prompt to *encrypt image to image*:

```
python3 ImageToImageEncryption.py
```

- Use the following command in the command prompt to *encrypt image to text*:

```
python3 ImageToTextEncryption.py
```

- Use the following command in the command prompt to *decrypt text to image*:

```
python3 TextToImageEncryption.py
```

- Use the following command in the command prompt to *decrypt image to image*:

```
python3 ImageToImageDecryption.py
```

# Basic Flow



# Future Scopes and updates

- Need to design frontend.
- Add new features like videos to text, text to audio, image to audio, text to image, etc
- Encrypting specific parts of the images/videos


# Current Issues

- Not getting the required output from Encryption and Decryption from image to image.
