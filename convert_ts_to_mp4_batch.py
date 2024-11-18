import os
import subprocess

def convert_ts_to_mp4_batch(input_files, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for input_file in input_files:
        # Derive output file name
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}.mp4")

        try:
            subprocess.run(
                ['ffmpeg', '-i', input_file, '-c:v', 'copy', '-c:a', 'copy', output_file],
                check=True
            )
            print(f"Converted: {input_file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_file}: {e}")
        except FileNotFoundError:
            print("ffmpeg is not installed or not found in PATH.")
            return

# Example usage:
input_ts_files = ["video1.ts", "video2.ts", "video3.ts"]  # List of .ts files
output_directory = "converted_videos"  # Directory to save .mp4 files

convert_ts_to_mp4_batch(input_ts_files, output_directory)
