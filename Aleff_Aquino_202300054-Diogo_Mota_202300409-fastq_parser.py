# Usage: python3 fastq.py in_file.fastq output_file.fastq -value x -len y  (use x or y or both as int)
import argparse

class Read:
    def __init__(self, file_path):
        """
        Initializes the Read class instance with the file path.
        """
        self.file_path = file_path
        self.file_content = None
    def file_reader(self):
        """
        Reads the file content and stores it in self.file_content.
        """
        with open(self.file_path) as file:
            self.file_content = file.readlines()
    def parse_fastq(self):
        """
        Parses the fastq file lines to extract relevant information.
        Returns fastq lines, average values, and sequence lengths.
        """
        fastq_lines = []
        for line in self.file_content:
            fastq_lines.append(line.strip())
        value_dict = {}
        for i in range(33, 84): # Creates a dictionary for quality values for ASCII characters
            char = chr(i)
            value_dict[char] = i - 33
        average_values = []
        length_sequences = []
        n = 0
        while n + 4 <= len(fastq_lines):
            values = []
            length_sequences.append(len(fastq_lines[n + 1]))
            for character in fastq_lines[n + 3]:
                if character in value_dict:
                    values.append(value_dict[character])
            n = n + 4
            average_values.append(sum(values) // len(fastq_lines[n - 1]))
        return fastq_lines, average_values, length_sequences

def parse_filter(in_fastq_file ,out_file_path, fastq_lines, average_values, length_sequences, cutoff_value=None, cutoff_length=None):
    """
    Filters sequences based on provided cutoff values.
    Writes filtered lines to the output file.
    Prints a filtering report.
    """
    discard_len = 0
    discard_qual = 0
    with open(out_file_path, 'w', newline='') as file:
        for indice in range(len(average_values)):
            if cutoff_value is not None:
                if cutoff_length is not None:
                    if  average_values[indice] >= cutoff_value:
                        if length_sequences[indice] >= cutoff_length:
                            file.write('\n'.join(fastq_lines[indice * 4:indice * 4 + 4]))
                            file.write('\n')
                        else:
                            discard_len = discard_len +1
                    else:
                        discard_qual = discard_qual +1
                elif average_values[indice] >= cutoff_value:
                    file.write('\n'.join(fastq_lines[indice * 4:indice * 4 + 4]))
                    file.write('\n')
                else:
                    discard_qual = discard_qual +1
            elif cutoff_length is not None:
                if length_sequences[indice] >= cutoff_length:
                    file.write('\n'.join(fastq_lines[indice * 4:indice * 4 + 4]))
                    file.write('\n')
                else:
                    discard_len = discard_len +1
        print(f"FilteringReport:")
        print(f"  Filename: {in_fastq_file[2:]}")
        print(f"  TotalReads: {len(length_sequences)}")
        print(f"  DiscardLowQual: {discard_qual}")
        print(f"  DiscardLen: {discard_len}")
        print(f"  ReadsAfterFilter: {len(length_sequences) - discard_len - discard_qual}")

def main():
    """
    Configures the command line argument parser.
    Processes the fastq file based on the provided arguments.
    """
    parser = argparse.ArgumentParser(description="fastq calculator")
    parser.add_argument("in_fastq_file", help="Path to the fastq file in")
    parser.add_argument("out_fastq_file", help="Path to fastq file out")
    parser.add_argument("-value", "--cutoff_value", type=int, help="Cutoff value for filtering")
    parser.add_argument("-len", "--cutoff_length", type=int, help="Cutoff length for filtering")
    args = parser.parse_args()
    if args.cutoff_value is None and args.cutoff_length is None: # Checks if at least one of the cutoff values was provided.
        parser.error('At least one of -value or -len must be provided.')
    fastq_reader = Read(args.in_fastq_file)
    fastq_reader.file_reader()
    fastq_lines, average_values, length_sequences = fastq_reader.parse_fastq()
    parse_filter(args.in_fastq_file ,args.out_fastq_file, fastq_lines, average_values, length_sequences, args.cutoff_value, args.cutoff_length) # Calls the filtering function with the provided arguments.

if __name__ == "__main__":
    main()
