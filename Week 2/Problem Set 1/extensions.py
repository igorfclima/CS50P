def main():
    file_name = input("File name: ")
    mime_type = get_mime_type(file_name)
    print(mime_type)

def get_mime_type(file_name):
    normalized_name = file_name.strip().lower()

    parts = normalized_name.rsplit('.', 1)
    if len(parts) > 1:
        extension = parts[1]
    else:
        return "application/octet-stream"
    mime_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }
    return mime_types.get(extension, "application/octet-stream")

if __name__ == "__main__":
    main()
