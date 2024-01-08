types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

try:
    file_name = input("File name: ").strip().lower()
    file_extension = file_name.split(".")[-1]

    # Check if the file extension is in the types dictionary
    file_type = types.get(file_extension, "application/octet-stream")

    print(f"{file_type}")

except IndexError:
    print("Invalid file name. Please include a file extension.")
