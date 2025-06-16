import os  
import pypandoc  
  
def md_to_pdf_pandoc(md_path, pdf_path):  
    output = pypandoc.convert_file(md_path, 'pdf', outputfile=pdf_path)  
    # output is '' if outputfile is given and file is successfully written  
  
def convert_all_md_to_pdf_in_folder(folder_path):  
    for filename in os.listdir(folder_path):  
        if filename.lower().endswith('.md'):  
            md_file = os.path.join(folder_path, filename)  
            pdf_file = os.path.splitext(md_file)[0] + '.pdf'  
            print(f"Converting: {md_file} -> {pdf_file}")  
            md_to_pdf_pandoc(md_file, pdf_file)  
    print("All conversions complete.")  
  
# Usage Example:  
# convert_all_md_to_pdf_in_folder('/path/to/your/folder')  
convert_all_md_to_pdf_in_folder('data')  