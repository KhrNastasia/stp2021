import argparse
from glob import glob
import random


class Crawler:
    def __init__(self, name_of_directory):
        self.name_of_directory = name_of_directory

    def get_all_songs_list(self):
        files = [f for f in listdir(self.name_of_directory) if f.endswith(".txt")]
        print(files)
        return files


class Generator:
    def __init__(self, all_song_list):
        self.all_song_list = all_song_list

    def generate_random_row(self):
        random_row = randint(0, len(self.all_song_list) - 1)
        return self.all_song_list[random_row]

    def generate_couplet(self):
        couplets_rows = int(args['rows']) - 3 * int(args['chorus'])
        couplet = []
        for row in range(couplets_rows // 3):
            couplet.append(self.generate_random_row())
        yield couplet

        couplet = []
        for row in range(couplets_rows // 3):
            couplet.append(self.generate_random_row())
        yield couplet

        couplet = []
        for row in range(couplets_rows // 3):
            couplet.append(self.generate_random_row())
        yield couplet

    def generate_chorus(self):
        chorus = []
        chorus_len = int(args['chorus'])
        for row in range(chorus_len):
            chorus.append(self.generate_random_row())
        return chorus

    def generate_new_song(self):
        new_song_list = []
        couplets = self.generate_couplet()
        chorus = self.generate_chorus()
        for _ in range(3):
            new_song_list.extend(next(couplets))
            new_song_list.extend(['\n'])
            new_song_list.extend(chorus)
            new_song_list.extend(['\n'])
        return new_song_list


class Saver:
    def __init__(self, output_directory, new_song_list):
        self.output_directory = output_directory
        self.new_song_list = new_song_list

    def save_new_song(self):
        with open('new_song.txt', 'w+', encoding='utf-8') as output_file:
            output_file.writelines(self.new_song_list)


if __name__ == '__main__':

    args = {'directory': r'C:\Users\admin\PycharmProjects\pythonProject\lab1', 'rows': '40', 'chorus': '6'}

    if int(args['rows']) < int(args['chorus']) * 3:
        print('Your song is smaller than 3 choruses')
        exit()

    crawler = Crawler(name_of_directory=args['directory'])
    generator = Generator(all_song_list=crawler.get_all_songs_list())
    saver = Saver(output_directory=args['directory'], new_song_list=generator.generate_new_song())

    saver.save_new_song()


