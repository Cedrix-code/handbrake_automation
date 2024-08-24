import os
import subprocess
import time

def automate_handbrake(input_folder, output_folder):
    handbrake_path = r"C:\Users\Lance\OneDrive\Desktop\HandBrakeCLI-1.8.2-win-x86_64\HandBrakeCLI.exe"
    print("Available encoders:")
    print("1. SVT-AV1")
    print("2. SVT-AV1 (10-bit)")
    print("3. FFV1")
    print("4. H.264 (x264)")
    print("5. H.264 (x264, 10-bit)")
    print("6. H.264 (VCE)")
    print("7. H.265 (x265)")
    print("8. H.265 (x265, 10-bit)")
    print("9. H.265 (x265, 12-bit)")
    print("10. H.265 (VCE)")
    print("11. H.265 (VCE, 10-bit)")
    print("12. MPEG-4")
    print("13. MPEG-2")
    print("14. VP8")
    print("15. VP9")
    print("16. VP9 (10-bit)")
    print("17. Theora")
    encoder_choice = input("Choose an encoder (1-17): ")
    encoder_map = {
        "1": "svt_av1",
        "2": "svt_av1_10bit",
        "3": "ffv1",
        "4": "x264",
        "5": "x264_10bit",
        "6": "vce_h264",
        "7": "x265",
        "8": "x265_10bit",
        "9": "x265_12bit",
        "10": "vce_h265",
        "11": "vce_h265_10bit",
        "12": "mpeg4",
        "13": "mpeg2",
        "14": "VP8",
        "15": "VP9",
        "16": "VP9_10bit",
        "17": "theora"
    }
    encoder = encoder_map[encoder_choice]

    print("Quality options:")
    print("0: Very high quality, no compression")
    print("1-10: High quality, very low compression")
    print("11-20: Medium-high quality, low compression")
    print("21-30: Medium quality, medium compression")
    print("31-40: Medium-low quality, medium compression")
    print("41-51: Low quality, high compression")
    quality_choice = input("Choose a quality (0-51): ")

    start_time = time.time()

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + "-compressed.mp4")
            command = [
                handbrake_path,
                "-i", input_file,
                "-o", output_file,
                "--encoder", encoder,
                "--quality", quality_choice
            ]
            subprocess.run(command)

    end_time = time.time()
    total_time = end_time - start_time

print(f"Total time taken to encode all videos: {total_time // 3600:.0f} hours and {(total_time % 3600) // 60:.0f} minutes")

def main():
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    automate_handbrake(input_folder, output_folder)

if __name__ == "__main__":
    main()
