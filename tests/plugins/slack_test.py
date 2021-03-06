from __future__ import absolute_import
from __future__ import unicode_literals

import pytest

from detect_secrets.plugins.slack import SlackDetector
from testing.mocks import mock_file_object


class TestSlackDetector(object):

    @pytest.mark.parametrize(
        'file_content',
        [
            (
                'xoxp-523423-234243-234233-e039d02840a0b9379c'
            ),
            (
                'xoxo-523423-234243-234233-e039d02840a0b9379c'
            ),
            (
                'xoxs-523423-234243-234233-e039d02840a0b9379c'
            ),
            (
                'xoxa-511111111-31111111111-3111111111111-e039d02840a0b9379c'
            ),
            (
                'xoxa-2-511111111-31111111111-3111111111111-e039d02840a0b9379c'
            ),
            (
                'xoxr-523423-234243-234233-e039d02840a0b9379c'
            ),
            (
                'xoxb-34532454-e039d02840a0b9379c'
            ),
        ],
    )
    def test_analyze(self, file_content):
        logic = SlackDetector()

        f = mock_file_object(file_content)
        output = logic.analyze(f, 'mock_filename')
        assert len(output) == 1
        for potential_secret in output:
            assert 'mock_filename' == potential_secret.filename
