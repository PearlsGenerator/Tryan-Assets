import os

def convert_png_extensions():
    # Mendapatkan direktori saat ini
    current_dir = os.getcwd()
    
    # Mencari semua file dalam direktori
    for filename in os.listdir(current_dir):
        # Cek apakah file berakhiran .PNG
        if filename.endswith('.PNG'):
            # Membuat nama file baru dengan ekstensi .png
            new_filename = filename[:-4] + '.png'
            
            # Melakukan rename file
            try:
                os.rename(filename, new_filename)
                print(f"Berhasil mengubah: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Gagal mengubah {filename}: {str(e)}")

if __name__ == "__main__":
    print("Memulai proses konversi ekstensi PNG ke png...")
    convert_png_extensions()
    print("Proses selesai!")