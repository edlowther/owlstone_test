from owlstone_test.read_files import Text_Processor
from owlstone_test.json_exporter import json_exporter
from owlstone_test.simple_server import run

def main():
    """Reads text files and performs textual analysis on them, before exporting relevant data as json 
    and starting the server."""
    file_reader = Text_Processor()
    publishers = file_reader.read_files()
    json_exporter(publishers)
    run()

if __name__ == '__main__':
    main()