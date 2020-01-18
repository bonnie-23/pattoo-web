#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(
        os.path.abspath(os.path.join(
            os.path.abspath(os.path.join(
                EXEC_DIR, os.pardir)), os.pardir)), os.pardir)), os.pardir))

if EXEC_DIR.endswith(
        '/pattoo-web/tests/test_pattoo_web/web/tables') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the "pattoo-web/tests/test_pattoo_web\
/tables/web" directory. Please fix.''')
    sys.exit(2)


from tests.libraries.configuration import UnittestConfig
from pattoo_web.web.query import agent as agent_query
from pattoo_web.web.tables import chart
from pattoo_web.web.query.datapoint import DataPoint
from pattoo_web.translate import KeyPair, datapoint_translations
from pattoo_web.web.query.pair_xlate import PairXlates


# Create a common dataset for testing
DATAPOINT = {'data': {'datapoint': {
    'agent': {'agentGroup': {'pairXlateGroup': {
        'id': 'UGFpclhsYXRlR3JvdXA6MQ==',
        'idxPairXlateGroup': '10'}},
              'agentPolledTarget': 'this_pc',
              'agentProgram': 'pattoo_test_snmpd'},
    'glueDatapoint': {'edges': [
        {'node': {'pair': {'key': 'pattoo_agent_snmpd_oid',
                           'value': '.1.3.6.1.2.1.2.2.1.10.345'}}},
        {'node': {'pair': {
            'key': 'pattoo_key',
            'value': '123'}}}]},
    'id': 'RGF0YVBvaW50OjM=',
    'idxDatapoint': '3'}}}

PAIRS = {'data': {'allPairXlateGroup': {'edges': [
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6Mg==',
              'idxPairXlateGroup': '10',
              'pairXlatePairXlateGroup': {'edges': [
                  {'node': {
                      'translation': (
                          'Interface Broadcast Packets (HC inbound)'),
                      'key': 'pattoo_agent_snmpd_oid',
                      'units': 'teddy_bear',
                      'language': {'code': 'en'}}},
                  {'node': {
                      'translation': (
                          'Interface Multicast Packets (HC inbound)'),
                      'key': 'pattoo_key',
                      'units': 'koala_bear',
                      'language': {'code': 'en'}}}]}}}]}}}


class TestRawCol(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass


class TestItemTable(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass


class TestItem(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass


class TestTable(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################
    point = DataPoint(DATAPOINT)
    translator = KeyPair(PairXlates(PAIRS).datapoints())
    dpt = datapoint_translations(point, translator)
    tester = chart.Table(dpt, 501)

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_html(self):
        """Testing method / function html."""
        # Test
        result = self.tester.html()
        expected = '''\
<table cellspacing="0" class="table table-bordered" id="dataTable" \
width="100%">
<thead><tr><th>Timeframe</th><th>Chart</th></tr></thead>
<tbody>
<tr><td>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=86400">Default</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago=\
604800">Week</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago=\
2592000">Month</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago=\
7776000">Quarter</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=31536000">Year</a></p>
</td><td><div id="pattoo_simple_line_chart"></div>
<script type="text/javascript">
  SimpleLineChart("/pattoo/web/chart/3/data?secondsago=501", "this_pc", "");
</script></td></tr>
</tbody>
</table>\
'''
        self.assertEqual(result, expected)

    def test__timeframe_links(self):
        """Testing method / function _timeframe_links."""
        # Test
        result = self.tester._timeframe_links()
        expected = '''
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=86400">Default</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=604800">Week</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=2592000">Month</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=7776000">Quarter</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=31536000">Year</a></p>
'''
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
