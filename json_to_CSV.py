import json
import csv
import os
import argparse
from collections import defaultdict

def process_json_files(folder_path, selected_stats):
    all_data = defaultdict(lambda: defaultdict(dict))
    all_benchmarks = set()

    # Process all JSON files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Determine if it's a Qiskit or tket benchmark
            if 'qiskit_info' in data:
                framework = 'Qiskit'
                version = data['qiskit_info']['qiskit']
            elif 'pytket_info' in data:
                framework = 'pytket'
                version = data['pytket_info']['pytket']
            else:
                print(f"Warning: {filename} does not contain version info for Qiskit or tket. Skipping...")
                continue

            framework_version = f"{framework} {version}"
            
            for benchmark in data['benchmarks']:
                all_benchmarks.add(benchmark['name'])
                for stat, value in benchmark['stats'].items():
                    if stat in selected_stats:  # Filter by selected statistics
                        all_data[framework_version][benchmark['name']][stat] = value

    return all_data, sorted(all_benchmarks)

def write_csv(output_file, all_data, all_benchmarks, selected_stats):
    temp_file = output_file.replace('.csv', '_temp.csv')
    
    # Write the original CSV
    with open(temp_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the header row
        header = ['Framework Version', 'Statistic'] + all_benchmarks
        csvwriter.writerow(header)

        # Write data rows
        for framework_version in sorted(all_data.keys()):
            for stat in selected_stats:
                row = [framework_version, stat]
                for benchmark in all_benchmarks:
                    row.append(all_data[framework_version][benchmark].get(stat, ''))
                csvwriter.writerow(row)

    # Transpose the CSV
    with open(temp_file, 'r') as infile:
        reader = list(csv.reader(infile))
        transposed_data = zip(*reader)  # Transpose the rows and columns

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(transposed_data)

    # Optionally, delete the temp file if not needed
    os.remove(temp_file)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process JSON files and output a transposed CSV with selected statistics.")
    parser.add_argument('folder_path', type=str, help="Path to the folder containing JSON files.")
    parser.add_argument('output_file', type=str, help="Name of the output CSV file.")
    parser.add_argument('--stats', nargs='+', default=['mean', 'median'], help="List of statistics to include in the CSV (e.g., --stats mean median).")
    
    args = parser.parse_args()

    # Process JSON files and write CSV
    all_data, all_benchmarks = process_json_files(args.folder_path, args.stats)
    write_csv(args.output_file, all_data, all_benchmarks, args.stats)

    print(f"Combined transposed CSV file '{args.output_file}' with selected statistics has been created successfully.")

if __name__ == "__main__":
    main()
