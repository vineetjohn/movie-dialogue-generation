"""
This file takes in a file in the style of the Cornell Movie-Dialog corpus and formats it
into a neural machine translation friendly format
"""
import sys
import logging


logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

METADATA_DELIMITER = "+++$+++"


def clean_dialog_line(dialogue_line):
    """
    Removed additional formatting from line
    parameters: metadata laden line
    returns: raw line
    """
    dialogue_segments = dialogue_line.split(METADATA_DELIMITER)
    return dialogue_segments[len(dialogue_segments) - 1].strip()


def format_dialogue_file(movie_lines_filepath):
    """
    Main formatter function that takes in a file, and writes to a new version of it
    parameters: Cornell Movie-Dialog corpus movie_lines.txt filepath
    returns: nothing
    """

    movie_lines = list()
    with open(movie_lines_filepath) as movie_lines_file:
        movie_lines = movie_lines_file.read().splitlines()

    formatted_movie_lines_path = movie_lines_filepath.replace(".txt", "_formatted.txt")

    with open(formatted_movie_lines_path, mode='w') as movie_lines_file:
        for i in range(len(movie_lines) - 1):
            dialogue_line = \
                "%s\t%s\n" % \
                (clean_dialog_line(movie_lines[i]), clean_dialog_line(movie_lines[i + 1]))
            movie_lines_file.write(dialogue_line)


if __name__ == "__main__":
    try:
        format_dialogue_file(sys.argv[1])
    except IndexError:
        LOG.error("No file provided")
        sys.exit(1)
