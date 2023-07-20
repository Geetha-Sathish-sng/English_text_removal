# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



from langdetect import detect

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        # If langdetect fails to detect the language, assume it's not English.
        return False

def filter_non_english_lines(input_file, output_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as f_in:
        with open(output_file, 'w', encoding=encoding) as f_out:
            for line in f_in:
                if not is_english(line):
                    f_out.write(line)

if __name__ == "__main__":
    input_file_path = "C:\\Users\\drng\\EPS24_kan.docx"
    output_file_path = "C:\\Users\\drng\\output2.docx"
    filter_non_english_lines(input_file_path, output_file_path, encoding='latin-1')
