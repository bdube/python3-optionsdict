import pytest
import optionsdict

class TestParsing:

    def test_given_none_returns_empty_dict(self):
        assert optionsdict.parse(None) == {}

    def test_given_empty_list_returns_empty_dict(self):
        assert optionsdict.parse([]) == {}

    def test_one_list_member_with_int_arg(self):
        assert optionsdict.parse(['k=8']) == {'k': 8}

    def test_two_list_members_with_int_args(self):
        assert optionsdict.parse(['k=8', 'ntokens=64']) == {'k': 8, 'ntokens': 64}

    def test_one_list_member_with_string_arg(self):
        assert optionsdict.parse(['foo=bar']) == {'foo': 'bar'}

    def test_one_standalone_arg(self):
        assert optionsdict.parse(['filename.json']) == {'_arg': 'filename.json'}
        
    def test_multiple_standalone_args(self):
        args = ['file1.js', 'file2.txt', 'file3.xml']
        assert optionsdict.parse(args) == {'_arg': 'file3.xml'}
        
    def test_delete_default_arg(self):
        defaults = {'foo': 'bar'}
        assert optionsdict.parse(['foo='], defaults) == {}
        
    def test_deleting_nondefault_adds_nothing(self):
        assert optionsdict.parse(['foo=']) == {}
        
    def test_string_to_python_true(self):
        assert optionsdict.parse(['foo=true']) == {'foo': True}
        
    def test_string_to_python_false(self):
        assert optionsdict.parse(['foo=false']) == {'foo': False}
        
    def test_string_to_python_none(self):
        assert optionsdict.parse(['foo=none']) == {'foo': None}
        
    def test_last_setting_wins(self):
        args = ['foo=bar', 'one', 'bar=8', 'foo=nONE', 'two', 'bar=']
        assert optionsdict.parse(args) == {'foo': None, '_arg': 'two'}