import os
import shutil
import requests
import random
import gzip

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

def check_and_download_file(ftp_link):
    if not ftp_link.startswith("http://") and not ftp_link.startswith("https://"):
        ftp_link = "https://" + ftp_link

    response = requests.head(ftp_link)

    if response.status_code == 200:
        content_length = int(response.headers.get("Content-Length", 0))
        content_length_mb = content_length / (1024 * 1024)

        if content_length_mb <= MAX_FILE_SIZE:
            file_name = ftp_link.split('/')[-1]
            file_path = os.path.join(download_dir, file_name)

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

# Define your parameters
MAX_FILE_SIZE = 50  # Maximum file size to download in MB
DOWNLOAD_DIR = "/content/fastq_files"  # Directory to download files
NUM_OF_FILES_TO_DOWNLOAD = 50  # Number of files to download
SEED = 2  # Seed for random shuffling

# Call the function to download FASTQ files
download_reports(fastq_links, DOWNLOAD_DIR, num_files=NUM_OF_FILES_TO_DOWNLOAD, seed=SEED)

# Define the directory path containing .gz files
directory_path = DOWNLOAD_DIR

# Call the function to decompress .gz files
decompress_gz_files(directory_path)

# Define the source folder and its contents
source_folder = DOWNLOAD_DIR

# Zip the folder
shutil.make_archive(source_folder, 'zip', source_folder)

# Move the zip file to your desired location
timestamp = datetime.now().strftime("%Y%m%d")
new_filename = f'fastq_files_seed_{SEED}_{timestamp}.zip'
destination_folder = 'your_desired_folder_path'

shutil.move(source_folder + '.zip', os.path.join(destination_folder, new_filename))

print(f"Folder '{source_folder}' has been zipped and moved to '{destination_folder}' with seed {SEED}.")