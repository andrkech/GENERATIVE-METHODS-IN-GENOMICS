import rarfile
import os
import requests
import random
import shutil
import gzip
from datetime import datetime
from lxml import etree

# Define the path to the XML file
xml_path = "/path/to/ena_sra-experiment_20231030-2024.xml"

# Define the path to save the FASTQ links
fastq_links_file = "/path/to/fastq_links.txt"

# Define the directory to download report files
report_files_dir = "/path/to/report_files/"

# Define the directory to download FASTQ files
fastq_files_dir = "/path/to/fastq_files/"

# Define the maximum file size to download (MB)
MAX_FILE_SIZE = 50

# Define the source folder to zip and upload
source_folder = '/path/to/fastq_files'

# Function to extract XML file from RAR archive
def extract_xml_from_rar(dataset_drive_path, xml_path):
    with rarfile.RarFile(dataset_drive_path) as rf:
        rf.extractall(os.path.dirname(xml_path))

# Function to parse XML file and extract FASTQ links
def parse_xml_and_extract_links(xml_path, fastq_links_file):
    parser = etree.XMLParser(recover=True)
    try:
        tree = etree.parse(xml_path, parser=parser)
        root = tree.getroot()
    except Exception as e:
        print("An error occurred while parsing the XML file:")
        print(e)
        root = None
    
    fastq_links = []
    if root is not None:
        for experiment in root.findall('.//EXPERIMENT'):
            experiment_links = experiment.findall('.//EXPERIMENT_LINKS/EXPERIMENT_LINK/XREF_LINK')
            for link in experiment_links:
                db = link.find('DB')
                if db is not None and db.text == 'ENA-FASTQ-FILES':
                    fastq_link = link.find('ID')
                    if fastq_link is not None:
                        fastq_links.append(fastq_link.text)
    
    with open(fastq_links_file, 'w') as file:
        file.write('\n'.join(fastq_links))

# Function to download report files
def download_reports(fastq_links, download_dir, num_files=None, seed=None):
    os.makedirs(download_dir, exist_ok=True)

    if seed is not None:
        random.seed(seed)
        random.shuffle(fastq_links)

    if num_files is not None:
        fastq_links = fastq_links[:num_files]

    for link in fastq_links:
        file_name = link.split('/')[-1]
        file_path = os.path.join(download_dir, file_name)

        response = requests.get(link, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

    print(f"Downloaded {len(fastq_links)} FASTQ files to {download_dir}.")

# Function to check file size and download from FTP links
def check_and_download_file(ftp_link):
    if not ftp_link.startswith("http://") and not ftp_link.startswith("https://"):
        ftp_link = "https://" + ftp_link

    response = requests.head(ftp_link)
    if response.status_code == 200:
        content_length = int(response.headers.get("Content-Length", 0))
        content_length_mb = content_length / (1024 * 1024)

        if content_length_mb <= MAX_FILE_SIZE:
            file_name = ftp_link.split('/')[-1]
            file_path = os.path.join(fastq_files_dir, file_name)

            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    file_response = requests.get(ftp_link, stream=True)
                    for chunk in file_response.iter_content(chunk_size=1024):
                        f.write(chunk)
                print(f"Downloaded: {file_name}")
            else:
                print(f"File already exists: {file_name}")
        else:
            print(f"Skipping file: {ftp_link} (Size exceeds maximum file size)")
    else:
        print(f"Failed to retrieve metadata for file: {ftp_link}")

# Function to decompress .gz files
def decompress_gz_files(directory_path):
    all_files = os.listdir(directory_path)
    gz_files = [file for file in all_files if file.endswith(".gz")]

    for gz_file in gz_files:
        gz_file_path = os.path.join(directory_path, gz_file)
        output_file_path = os.path.splitext(gz_file_path)[0]

        try:
            with gzip.open(gz_file_path, 'rb') as f_in, open(output_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(gz_file_path)
        except (OSError, gzip.BadGzipFile) as e:
            print(f"Error decompressing {gz_file}: {e}")

    print("Decompression complete.")

# Function to zip and upload folder to Google Drive
def zip_and_upload_to_drive(source_folder):
    shutil.make_archive(source_folder, 'zip', source_folder)
    timestamp = datetime.now().strftime("%Y%m%d")
    new_filename = f'fastq_files_seed_{SEED}_{timestamp}.zip'
    shutil.move(source_folder + '.zip', f'/path/to/destination/{new_filename}')
    print(f"Folder '{source_folder}' has been zipped and uploaded to destination folder.")

# Main execution
def main():
    dataset_drive_path = "/path/to/ena_sra-experiment_20231030-2024.rar"

    extract_xml_from_rar(dataset_drive_path, xml_path)
    parse_xml_and_extract_links(xml_path, fastq_links_file)

    with open(fastq_links_file, 'r') as file:
        fastq_links = file.read().splitlines()

    download_reports(fastq_links, report_files_dir)

    all_files = os.listdir(report_files_dir)
    info_files = [file for file in all_files if "filereport" in file]

    for info_file in info_files:
        file_path = os.path.join(report_files_dir, info_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
            data_line = lines[1]

            if data_line is not None:
                columns = data_line.strip().split('\t')
                if len(columns) >= 2:
                    ftp_link = columns[1].split(";")[0]
                    check_and_download_file(ftp_link)

    decompress_gz_files(fastq_files_dir)
    zip_and_upload_to_drive(source_folder)

if __name__ == "__main__":
    main()
