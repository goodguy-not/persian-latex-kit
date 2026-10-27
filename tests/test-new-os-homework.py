#!/usr/bin/env python3
"""Check OS project generation without touching the actual GitHub remote."""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'new-os-homework.py'


class OSProjectGenerator(unittest.TestCase):
    def test_explicit_offline_single_question_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = pathlib.Path(tmp) / 'q2'
            cmd = [sys.executable, str(SCRIPT), '--destination', str(dest),
                   '--question-number', '۲', '--assignment-number', '۳', '--offline']
            p = subprocess.run(cmd, text=True, capture_output=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertTrue((dest / 'vendor/persian-latex-kit/tex/persian-os.sty').is_file())
            self.assertTrue((dest / 'questions/question02.tex').is_file())
            self.assertFalse((dest / 'questions/question01.tex').exists())
            self.assertIn(r'\input{questions/question02}',
                          (dest / 'main.tex').read_text(encoding='utf-8'))
            meta = (dest / 'config/metadata.tex').read_text(encoding='utf-8')
            self.assertIn(r'\OSQuestionNumber}{۲}', meta)
            self.assertIn('تمرین سری سوم', meta)
            self.assertTrue((dest / '.git').exists())
            self.assertFalse((dest / '.gitmodules').exists())

    def test_local_git_submodule_creation(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            remote = tmp / 'shared-repo'
            remote.mkdir()
            subprocess.run(['git', 'init', '-b', 'main'], cwd=remote, check=True,
                           capture_output=True)
            (remote / 'tex').mkdir()
            (remote / 'tex/persian-os.sty').write_bytes((ROOT / 'tex/persian-os.sty').read_bytes())
            subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.org',
                            'add', '.'], cwd=remote, check=True, capture_output=True)
            subprocess.run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.org',
                            'commit', '-m', 'fixture'], cwd=remote, check=True, capture_output=True)
            dest = tmp / 'project'
            cmd = [sys.executable, str(SCRIPT), '--destination', str(dest),
                   '--question-number', '۴', '--repository-url', str(remote)]
            env = dict(os.environ, GIT_ALLOW_PROTOCOL='file')
            p = subprocess.run(cmd, text=True, capture_output=True, env=env)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertTrue((dest / '.gitmodules').exists())
            self.assertTrue((dest / 'vendor/persian-latex-kit/tex/persian-os.sty').is_file())
            self.assertTrue((dest / 'questions/question04.tex').exists())

    def test_does_not_overwrite_existing_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = pathlib.Path(tmp) / 'q1'
            dest.mkdir()
            (dest / 'keep.txt').write_text('preserve', encoding='utf-8')
            p = subprocess.run([sys.executable, str(SCRIPT), '--destination', str(dest),
                                '--offline'], text=True, capture_output=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertEqual((dest / 'keep.txt').read_text(), 'preserve')

    def test_rejects_ambiguous_modes(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = pathlib.Path(tmp) / 'q1'
            p = subprocess.run([sys.executable, str(SCRIPT), '--destination', str(dest),
                                '--offline', '--repository-url', '/unused'],
                               text=True, capture_output=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertFalse(dest.exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
