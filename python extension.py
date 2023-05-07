file = input("Input the Filename: ")
parts = file.split(".")
extension = parts[-1]
extension_of_language = {
    "py": "python",
}
language = extension_of_language.get(extension, "Unknown")
print("The extension of the file is : " + language)
