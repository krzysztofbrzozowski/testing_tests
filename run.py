"""
@author:    Krzysztof Brzozowski
@file:      run
@time:      26/11/2022
@desc:      
"""
from argparse import ArgumentParser, Action


class Doctest(Action):
    def __call__(self, parser, namespace, paths, *args, **kwargs):
        print('elo')
        # run('clear && printf "\e[3J"')  # noqa
        # all_tests = 0
        # files = sorted(self.get_files(paths))
        # for file in files:
        #     if self.is_ignored(file): continue
        #     if self.is_venv(file): continue
        #     if self.is_skipped(file): continue
        #     if count := self.count_doctests(file):
        #         self.run_doctest(file)
        #         all_tests += count
        #     else:
        #         log.error(f'NOTESTS\t{file}')
        # logging.warning(f'\nAll tests {all_tests}')


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--doctest',
                        nargs='+', metavar='CHAPTER', action=Doctest,
                        help='doctest *.rst and *.py files')